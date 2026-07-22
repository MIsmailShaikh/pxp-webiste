require('dotenv').config();
const express = require('express');
const compression = require('compression');
const cors = require('cors');
const mysql = require('mysql2/promise');
const bcrypt = require('bcrypt');
const jwt = require('jsonwebtoken');
const { OAuth2Client } = require('google-auth-library');
const stripe = require('stripe')(process.env.STRIPE_SECRET_KEY);
const path = require('path');

const googleClient = new OAuth2Client(process.env.GOOGLE_CLIENT_ID || 'YOUR_GOOGLE_CLIENT_ID');

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(compression()); // Gzip compress all responses for faster load times
app.use(cors());
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Serve static frontend files with aggressive browser caching
app.use(express.static(path.join(__dirname, '.'), {
    maxAge: '1d', // Cache files in browser for 1 day
    setHeaders: (res, path) => {
        if (path.endsWith('.html')) {
            // HTML files shouldn't be cached as aggressively to ensure updates are seen
            res.setHeader('Cache-Control', 'public, max-age=0, must-revalidate');
        }
    }
}));

// Default route to index.html (since we don't have an index.html)
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'index.html'));
});

// Database Connection Pool
const pool = mysql.createPool({
    host: process.env.DB_HOST || 'localhost',
    user: process.env.DB_USER || 'root',
    password: process.env.DB_PASSWORD || '',
    database: process.env.DB_NAME || 'pxp_database',
    waitForConnections: true,
    connectionLimit: 10,
    queueLimit: 0
});

// ==========================================
// 1. AUTHENTICATION ENDPOINTS
// ==========================================

// Register a new user
app.post('/api/auth/register', async (req, res) => {
    try {
        const { email, password, fullName } = req.body;
        
        // Check if user exists
        const [existingUsers] = await pool.execute('SELECT * FROM users WHERE email = ?', [email]);
        if (existingUsers.length > 0) {
            return res.status(400).json({ error: 'Email already registered' });
        }

        // Hash password
        const hashedPassword = await bcrypt.hash(password, 10);

        // Insert new user
        const [result] = await pool.execute(
            'INSERT INTO users (email, password_hash, full_name) VALUES (?, ?, ?)',
            [email, hashedPassword, fullName]
        );

        res.status(201).json({ message: 'Registration successful', userId: result.insertId });
    } catch (error) {
        console.error(error);
        res.status(500).json({ error: 'Internal server error' });
    }
});

// Login
app.post('/api/auth/login', async (req, res) => {
    try {
        const { email, password } = req.body;

        // Find user
        const [users] = await pool.execute('SELECT * FROM users WHERE email = ?', [email]);
        if (users.length === 0) {
            return res.status(401).json({ error: 'Invalid credentials' });
        }

        const user = users[0];

        // Check password
        const validPassword = await bcrypt.compare(password, user.password_hash);
        if (!validPassword) {
            return res.status(401).json({ error: 'Invalid credentials' });
        }

        // Generate token
        const token = jwt.sign(
            { userId: user.id, email: user.email },
            process.env.JWT_SECRET || 'your-fallback-secret',
            { expiresIn: '24h' }
        );

        res.json({ message: 'Login successful', token, user: { id: user.id, email: user.email, name: user.full_name } });
    } catch (error) {
        console.error(error);
        res.status(500).json({ error: 'Internal server error' });
    }
});

// Google Sign-In
app.post('/api/auth/google', async (req, res) => {
    try {
        const { credential } = req.body;
        
        // Verify Google token
        const ticket = await googleClient.verifyIdToken({
            idToken: credential,
            audience: process.env.GOOGLE_CLIENT_ID || 'YOUR_GOOGLE_CLIENT_ID',
        });
        const payload = ticket.getPayload();
        
        const googleId = payload['sub'];
        const email = payload['email'];
        const fullName = payload['name'];

        // Check if user exists
        const [users] = await pool.execute('SELECT * FROM users WHERE email = ?', [email]);
        let user;

        if (users.length === 0) {
            // Register new user
            const [result] = await pool.execute(
                'INSERT INTO users (email, full_name, google_id) VALUES (?, ?, ?)',
                [email, fullName, googleId]
            );
            user = { id: result.insertId, email, full_name: fullName };
        } else {
            user = users[0];
            // Update google_id if missing
            if (!user.google_id) {
                await pool.execute('UPDATE users SET google_id = ? WHERE id = ?', [googleId, user.id]);
            }
        }

        // Generate token
        const token = jwt.sign(
            { userId: user.id, email: user.email },
            process.env.JWT_SECRET || 'your-fallback-secret',
            { expiresIn: '24h' }
        );

        res.json({ message: 'Google Login successful', token, user: { id: user.id, email: user.email, name: user.full_name } });
    } catch (error) {
        console.error(error);
        res.status(401).json({ error: 'Invalid Google token' });
    }
});


// ==========================================
// 2. PAYMENT & SUBSCRIPTION ENDPOINTS (STRIPE)
// ==========================================

app.post('/api/checkout/create-session', async (req, res) => {
    try {
        const { planId, userId } = req.body;
        
        // Define your plan prices here
        const planPrices = {
            'business': 'price_12345', // Replace with real Stripe Price ID
            'enterprise': 'price_67890'
        };

        const session = await stripe.checkout.sessions.create({
            payment_method_types: ['card'],
            line_items: [
                {
                    price: planPrices[planId] || 'price_default',
                    quantity: 1,
                },
            ],
            mode: 'subscription',
            success_url: `${req.headers.origin}/checkout-success.html?session_id={CHECKOUT_SESSION_ID}`,
            cancel_url: `${req.headers.origin}/checkout.html`,
            metadata: {
                userId: userId,
                planId: planId
            }
        });

        res.json({ url: session.url });
    } catch (error) {
        console.error(error);
        res.status(500).json({ error: error.message });
    }
});


// ==========================================
// START SERVER
// ==========================================
app.listen(PORT, () => {
    console.log(`PXP Backend server is running on port ${PORT}`);
});
