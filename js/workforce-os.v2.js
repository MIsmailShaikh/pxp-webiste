window.addEventListener('load', () => {
    if (window.lucide) {
        if (window.requestIdleCallback) {
            requestIdleCallback(() => window.lucide.createIcons());
        } else {
            setTimeout(() => window.lucide.createIcons(), 100);
        }
    }
});

        const lenis = new Lenis({
            duration: 1.2,
            easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)),
            direction: 'vertical',
            gestureDirection: 'vertical',
            smooth: true,
        })

        function raf(time) {
            lenis.raf(time)
            requestAnimationFrame(raf)
        }
        requestAnimationFrame(raf)

        // Interactive Spotlight Logic
        const heroSection = document.getElementById('hero-section');
        const spotlight = document.getElementById('spotlight');
        if (heroSection && spotlight) {
            heroSection.addEventListener('mousemove', (e) => {
                const rect = heroSection.getBoundingClientRect();
                const x = e.clientX - rect.left;
                const y = e.clientY - rect.top;
                spotlight.style.setProperty('--x', `${x}px`);
                spotlight.style.setProperty('--y', `${y}px`);
            });
            // Default center position on load
            spotlight.style.setProperty('--x', `50%`);
            spotlight.style.setProperty('--y', `50%`);
        }

        // Tab Switching Logic
        const tabBtns = document.querySelectorAll('.tab-btn');
        const tabContents = document.querySelectorAll('.tab-content');

        tabBtns.forEach(btn => {
            btn.addEventListener('click', () => {
                // Remove active styling from all buttons
                tabBtns.forEach(b => {
                    b.classList.remove('active', 'text-gray-900', 'font-semibold');
                    b.classList.add('text-gray-500', 'font-medium');
                });
                
                // Add active styling to clicked button
                btn.classList.add('active', 'text-gray-900', 'font-semibold');
                btn.classList.remove('text-gray-500', 'font-medium');

                // Move the sliding background pill
                const slider = document.getElementById('tab-slider');
                if (slider) {
                    slider.style.width = btn.offsetWidth + 'px';
                    slider.style.height = btn.offsetHeight + 'px';
                    slider.style.left = btn.offsetLeft + 'px';
                    slider.style.top = btn.offsetTop + 'px';
                }

                // Hide all contents
                tabContents.forEach(content => {
                    content.classList.remove('block');
                    content.classList.add('hidden', 'pointer-events-none', 'absolute');
                    content.style.opacity = '0';
                });

                // Show target content
                const targetId = btn.getAttribute('data-target');
                const targetContent = document.getElementById(targetId);
                targetContent.classList.remove('hidden', 'pointer-events-none', 'absolute');
                targetContent.classList.add('block');
                
                // Small delay for fade in effect
                setTimeout(() => {
                    targetContent.style.opacity = '1';
                }, 50);
            });
        });

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

        // First apply reveal-text class to sections we want to animate on scroll
        document.querySelectorAll('section > div > div:first-child, .grid > div, .tab-content').forEach(el => {
            if(!el.classList.contains('reveal-text') && !el.classList.contains('tab-content')) {
                el.classList.add('reveal-text');
            }
        });

        document.querySelectorAll('.reveal-text').forEach((el) => {
            observer.observe(el);
        });

        // Initialize tab slider position
        function initTabSlider() {
            const activeBtn = document.querySelector('.tab-btn.active');
            const slider = document.getElementById('tab-slider');
            if (activeBtn && slider) {
                slider.style.width = activeBtn.offsetWidth + 'px';
                slider.style.height = activeBtn.offsetHeight + 'px';
                slider.style.left = activeBtn.offsetLeft + 'px';
                slider.style.top = activeBtn.offsetTop + 'px';
            }
        }
        window.addEventListener('load', initTabSlider);
        window.addEventListener('resize', initTabSlider);
        // Run once immediately in case elements are already parsed
        initTabSlider();
    
        // Mobile Menu Toggle Logic
        const mobileMenuBtn = document.getElementById('mobile-menu-btn');
        const mobileMenu = document.getElementById('mobile-menu');
        let isMobileMenuOpen = false;

        if (mobileMenuBtn && mobileMenu) {
            mobileMenuBtn.addEventListener('click', (event) => {
                event.stopPropagation();
                isMobileMenuOpen = !isMobileMenuOpen;
                if (isMobileMenuOpen) {
                    mobileMenu.classList.remove('hidden');
                    // Small delay to allow display block to apply before animating
                    setTimeout(() => {
                        mobileMenu.classList.remove('opacity-0', 'scale-y-95');
                        mobileMenu.classList.add('opacity-100', 'scale-y-100');
                    }, 10);
                    // Change icon to close (X)
                    mobileMenuBtn.innerHTML = '<i data-lucide="x" class="w-6 h-6 text-gray-900"></i>';
                    if (window.lucide) window.lucide.createIcons();
                } else {
                    mobileMenu.classList.remove('opacity-100', 'scale-y-100');
                    mobileMenu.classList.add('opacity-0', 'scale-y-95');
                    setTimeout(() => {
                        mobileMenu.classList.add('hidden');
                    }, 300); // Wait for transition
                    // Change icon back to menu
                    mobileMenuBtn.innerHTML = '<i data-lucide="menu" class="w-6 h-6 text-gray-900"></i>';
                    if (window.lucide) window.lucide.createIcons();
                }
            });

            // Close mobile menu when clicking outside
            document.addEventListener('click', (event) => {
                // Ensure we only close if the click is outside the menu
                if (isMobileMenuOpen && !mobileMenu.contains(event.target)) {
                    mobileMenuBtn.click();
                }
            });
        }