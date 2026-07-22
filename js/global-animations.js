document.addEventListener('DOMContentLoaded', () => {
    // Scroll Reveal Logic
    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.15
    };

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('revealed');
                observer.unobserve(entry.target); // Only reveal once
            }
        });
    }, observerOptions);

    // Apply reveal-text class to sections we want to animate on scroll
    document.querySelectorAll('section > div > div:first-child, .grid > div, .tab-content, .prose > *, .max-w-3xl > *, .max-w-7xl > *').forEach(el => {
        // Skip elements that explicitly opt out or already have it
        if(!el.classList.contains('reveal-text') && !el.classList.contains('tab-content') && !el.classList.contains('no-reveal')) {
            el.classList.add('reveal-text');
        }
    });

    // Observe all reveal elements
    document.querySelectorAll('.reveal-text, .scroll-reveal').forEach((el) => {
        observer.observe(el);
    });

    // Custom Back Logic for Main Page Navigation
    document.querySelectorAll('a[href="index.html"], a[href="./index.html"]').forEach(link => {
        link.addEventListener('click', (e) => {
            e.preventDefault();
            window.location.replace(link.href);
        });
    });
});
