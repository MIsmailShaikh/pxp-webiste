// js/auth-guard.js

/**
 * Checks if the user is logged in. 
 * If not, redirects to login.html and saves the intended destination.
 * If yes, redirects immediately to the intended destination.
 * 
 * @param {string} intendedUrl - The URL to go to after successful login (or immediately if already logged in).
 */
window.requireAuth = function(intendedUrl) {
    const isLoggedIn = localStorage.getItem('pxp_logged_in') === 'true';
    
    if (isLoggedIn) {
        // Already logged in, go straight to the destination
        window.location.replace(intendedUrl);
    } else {
        // Not logged in, save destination and go to login
        localStorage.setItem('pxp_intended_url', intendedUrl);
        window.location.replace('login.html');
    }
};

/**
 * Helper to update Navbar state based on login status.
 * Run this on DOMContentLoaded if the page includes a standard Navbar.
 */
window.updateNavbarAuthUI = function() {
    const isLoggedIn = localStorage.getItem('pxp_logged_in') === 'true';
    
    // Find generic "Log in" and "Get started" buttons in the nav
    // This requires specific IDs or classes, which we can adapt based on the HTML
    const loginLinks = document.querySelectorAll('a[href="login.html"], button[onclick*="login.html"]');
    
    if (isLoggedIn) {
        // If logged in, change "Log in" to "Dashboard"
        loginLinks.forEach(link => {
            if (link.textContent.toLowerCase().includes('log in') || link.textContent.toLowerCase().includes('login')) {
                link.textContent = 'Dashboard';
                link.href = 'dashboard.html';
                if(link.tagName === 'BUTTON') link.onclick = null;
            }
        });
    }
};

document.addEventListener('DOMContentLoaded', () => {
    if (typeof updateNavbarAuthUI === 'function') {
        updateNavbarAuthUI();
    }
});
