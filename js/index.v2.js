document.addEventListener("DOMContentLoaded", () => {
                    const serviceCards = document.querySelectorAll('.service-card-reveal');
                    let currentCardIndex = 0;
                    
                    // Continuously cycle the hover effect on mobile
                    setInterval(() => {
                        if (window.innerWidth <= 768 && serviceCards.length > 0) {
                            // Remove from all
                            serviceCards.forEach(card => card.classList.remove('simulated-hover'));
                            
                            // Add to current card
                            serviceCards[currentCardIndex].classList.add('simulated-hover');
                            
                            // Move to next card
                            currentCardIndex = (currentCardIndex + 1) % serviceCards.length;
                        } else {
                            // Clean up if resized back to PC
                            serviceCards.forEach(card => card.classList.remove('simulated-hover'));
                        }
                    }, 1000); // Triggers the next card every 1 second
                });

document.addEventListener("DOMContentLoaded", () => {
                    const buildCards = document.querySelectorAll('.what-we-build-card');
                    let currentBuildCard = 0;
                    setInterval(() => {
                        if (buildCards.length > 0) {
                            buildCards.forEach(card => card.classList.remove('auto-play'));
                            buildCards[currentBuildCard].classList.add('auto-play');
                            currentBuildCard = (currentBuildCard + 1) % buildCards.length;
                        }
                    }, 2000); // 2 seconds per card
                });

// Initialize Lucide Icons
        window.addEventListener('load', () => {
    if (window.lucide) window.lucide.createIcons();
});

        // Initialize Lenis Smooth Scroll
        const lenis = new Lenis({
            duration: 1.2,
            easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)),
            direction: 'vertical',
            gestureDirection: 'vertical',
            smooth: true,
            mouseMultiplier: 1,
            smoothTouch: false,
            touchMultiplier: 2,
        })

        // SCROLL REVEAL TEXT LOGIC
        const textElement = document.getElementById('scroll-reveal-text');
        const textContent = textElement.innerText;
        textElement.innerHTML = textContent.split(' ').map(word => `<span class="reveal-word">${word}</span>`).join(' ');
        const words = document.querySelectorAll('.reveal-word');

        function animateScrollText() {
            const triggerPoint = window.innerHeight * 0.75;
            words.forEach((word) => {
                const rect = word.getBoundingClientRect();
                if (rect.top < triggerPoint) {
                    const distance = triggerPoint - rect.top;
                    let opacity = 0.2 + (distance / 150);
                    if (opacity > 1) opacity = 1;
                    if (opacity < 0.2) opacity = 0.2;
                    word.style.opacity = opacity;
                } else {
                    word.style.opacity = 0.2;
                }
            });
        }


        function raf(time) {
            lenis.raf(time)
            animateScrollText();
            requestAnimationFrame(raf)
        }
        requestAnimationFrame(raf)

        // Handle Anchor Links for Lenis Smooth Scroll
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                const targetId = this.getAttribute('href');
                if (targetId && targetId !== '#') {
                    const targetElement = document.querySelector(targetId);
                    if (targetElement) {
                        e.preventDefault();
                        lenis.scrollTo(targetElement, {
                            offset: -80, // Accounts for the floating navbar
                            duration: 1.2
                        });
                    }
                }
            });
        });

        // General Fade Up Observer
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('active');
                }
            });
        }, { threshold: 0.1 });

        document.querySelectorAll('.scroll-reveal').forEach((el) => observer.observe(el));

        // FAQ ACCORDION LOGIC
        const faqItems = document.querySelectorAll('.faq-item');

        faqItems.forEach(item => {
            const trigger = item.querySelector('.faq-trigger');
            const content = item.querySelector('.faq-content');

            trigger.addEventListener('click', () => {
                // IMPORTANT: Select the icon *inside* the click handler because Lucide replaces <i> with <svg>
                // This ensures we get the SVG that currently exists in the DOM
                const icon = trigger.querySelector('svg');
                const isOpen = item.classList.contains('active');

                // Close all other items
                faqItems.forEach(otherItem => {
                    if (otherItem !== item) {
                        otherItem.classList.remove('active');
                        otherItem.querySelector('.faq-content').style.height = '0';
                        otherItem.querySelector('.faq-content').style.opacity = '0';
                        // Also reset other icons
                        const otherIcon = otherItem.querySelector('.faq-trigger svg');
                        if (otherIcon) otherIcon.style.transform = 'rotate(0deg)';
                    }
                });

                // Toggle current item
                if (!isOpen) {
                    item.classList.add('active');
                    content.style.height = content.scrollHeight + 'px';
                    content.style.opacity = '1';
                    if (icon) icon.style.transform = 'rotate(180deg)';
                } else {
                    item.classList.remove('active');
                    content.style.height = '0';
                    content.style.opacity = '0';
                    if (icon) icon.style.transform = 'rotate(0deg)';
                }
            });
        });

        // Open the last FAQ item by default (optional, matches screenshot style)
        // setTimeout(() => { faqItems[3].querySelector('.faq-trigger').click(); }, 500);

// Hero Dashboard Tab Switcher
        function switchHeroTab(tabId) {
            // Reset tabs
            const tabs = document.querySelectorAll('.hero-sidebar-tab');
            tabs.forEach(t => {
                t.classList.remove('bg-white', 'shadow-sm', 'text-gray-700');
                t.classList.add('hover:bg-gray-100', 'text-gray-500');
            });

            // Set active tab
            const activeTab = document.getElementById('tab-' + tabId);
            if (activeTab) {
                activeTab.classList.add('bg-white', 'shadow-sm', 'text-gray-700');
                activeTab.classList.remove('hover:bg-gray-100', 'text-gray-500');
            }

            // Reset views
            const views = document.querySelectorAll('.hero-tab-view');
            views.forEach(v => {
                v.classList.remove('opacity-100', 'z-10', 'active');
                v.classList.add('opacity-0', 'z-0', 'pointer-events-none');
            });

            // Set active view
            const activeView = document.getElementById('view-' + tabId);
            if (activeView) {
                activeView.classList.remove('opacity-0', 'z-0', 'pointer-events-none');
                activeView.classList.add('opacity-100', 'z-10');

                // Trigger animation state after short delay
                setTimeout(() => {
                    activeView.classList.add('active');
                }, 50);
            }

            // Handle floating cursor specifically
            const cursor = document.getElementById('hero-cursor');
            if (cursor) {
                if (tabId === 'dashboard') {
                    cursor.style.display = '';
                } else {
                    cursor.style.display = 'none';
                }
            }
        }

        // --- Auto-cycle Hero Tabs (MOBILE ONLY) ---
        const heroTabsList = ['dashboard', 'hr', 'mail'];
        let currentHeroTabIndex = 0;
        let heroTabInterval;

        function startHeroTabCycle() {
            stopHeroTabCycle(); // Prevent multiple intervals
            
            // STRICTLY FOR MOBILE VIEW ONLY
            if (window.innerWidth > 768) return; 

            heroTabInterval = setInterval(() => {
                // Double check it's still mobile in case they resized the window
                if (window.innerWidth > 768) {
                    stopHeroTabCycle();
                    return;
                }
                
                currentHeroTabIndex = (currentHeroTabIndex + 1) % heroTabsList.length;
                
                // Call original logic without triggering a manual override loop
                const nextTabId = heroTabsList[currentHeroTabIndex];
                const activeTab = document.getElementById('tab-' + nextTabId);
                if(activeTab) {
                    activeTab.click(); // Trigger the onclick defined in HTML
                }
            }, 4000); // 4 seconds per tab
        }

        function stopHeroTabCycle() {
            if (heroTabInterval) clearInterval(heroTabInterval);
        }

        // Intercept manual clicks to update index and reset the timer
        const originalSwitchHeroTab = switchHeroTab;
        switchHeroTab = function(tabId) {
            currentHeroTabIndex = Math.max(0, heroTabsList.indexOf(tabId));
            originalSwitchHeroTab(tabId);
            startHeroTabCycle(); // Reset timer so it doesn't switch instantly after a click
        };

        // Start cycling (only kicks in if mobile)
        startHeroTabCycle();
        
        // Handle window resize to start/stop the cycle dynamically
        window.addEventListener('resize', () => {
            if (window.innerWidth > 768) {
                stopHeroTabCycle();
                // Optionally reset to dashboard on PC when resizing up
                if (currentHeroTabIndex !== 0) {
                    currentHeroTabIndex = 0;
                    originalSwitchHeroTab('dashboard');
                }
            } else if (!heroTabInterval) {
                startHeroTabCycle();
            }
        });
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

        // Continuous animations for mobile (simulating group-hover)
        if (window.innerWidth <= 768) {
            // Wait for Tailwind CDN to finish generating styles
            setTimeout(() => {
                let rulesAdded = false;
                for (let i = 0; i < document.styleSheets.length; i++) {
                    try {
                        const sheet = document.styleSheets[i];
                        const rules = sheet.cssRules || sheet.rules;
                        const newRules = [];
                        
                        for (let j = 0; j < rules.length; j++) {
                            const rule = rules[j];
                            if (rule.type === CSSRule.STYLE_RULE && rule.selectorText && rule.selectorText.includes('.group:hover')) {
                                const newRuleText = rule.cssText.replace(/\.group:hover/g, '.group.mobile-anim-active');
                                newRules.push(newRuleText);
                            }
                        }
                        
                        if (newRules.length > 0) {
                            newRules.forEach(r => sheet.insertRule(r, sheet.cssRules.length));
                            rulesAdded = true;
                        }
                    } catch (e) {
                        // Skip cross-origin stylesheets if any
                    }
                }

                if (rulesAdded) {
                    const groups = document.querySelectorAll('.service-card-reveal, .group');
                    let isActive = false;
                    setInterval(() => {
                        isActive = !isActive;
                        groups.forEach(g => {
                            if (isActive) {
                                g.classList.add('mobile-anim-active');
                            } else {
                                g.classList.remove('mobile-anim-active');
                            }
                        });
                    }, 2500); // Toggle every 2.5 seconds
                }
            }, 1000);
        }