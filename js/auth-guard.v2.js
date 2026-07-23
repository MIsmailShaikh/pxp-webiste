// js/auth-guard.js

window.requireAuth = function(intendedUrl) {
    const isLoggedIn = localStorage.getItem('pxp_logged_in') === 'true';
    
    if (!isLoggedIn) {
        // Not logged in, save destination and go to login
        localStorage.setItem('pxp_intended_url', intendedUrl);
        window.location.replace('login.html');
    }
    // If logged in, do nothing (let the protected page load)
};

/**
 * Helper to update Navbar state based on login status.
 * Run this on DOMContentLoaded if the page includes a standard Navbar.
 */
window.updateNavbarAuthUI = function() {
    const isLoggedIn = localStorage.getItem('pxp_logged_in') === 'true';
    const email = localStorage.getItem('pxp_email');
    
    const navUnauth = document.getElementById('nav-unauth');
    const navAuth = document.getElementById('nav-auth');
    
    if (isLoggedIn) {
        // Toggle desktop navbar elements
        if (navUnauth) navUnauth.classList.add('hidden');
        if (navAuth) {
            navAuth.classList.remove('hidden');
            navAuth.classList.add('flex');
            
            const nameEl = document.getElementById('nav-user-name');
            if (nameEl && email) {
                // Try to show first part of email, or just 'Account'
                nameEl.textContent = email.split('@')[0];
            }
        }
        
        // Handle mobile menu links
        const mobileLoginLinks = document.querySelectorAll('#mobile-menu a[href="login.html"]');
        mobileLoginLinks.forEach(link => {
            if (link.textContent.toLowerCase().includes('log in') || link.textContent.toLowerCase().includes('login')) {
                link.textContent = 'Dashboard';
                link.href = 'dashboard.html';
            }
        });
        
        // Hide "Get started" button in mobile menu
        const getStartedLinks = document.querySelectorAll('#mobile-menu a[href="pricing.html"]');
        getStartedLinks.forEach(link => {
            if (link.textContent.toLowerCase().includes('get started')) {
                link.style.display = 'none';
            }
        });
    }
};

window.logout = function() {
    localStorage.removeItem('pxp_logged_in');
    localStorage.removeItem('pxp_token');
    localStorage.removeItem('pxp_email');
    window.location.href = 'login.html';
};

document.addEventListener('DOMContentLoaded', () => {
    if (typeof updateNavbarAuthUI === 'function') {
        updateNavbarAuthUI();
    }
});
