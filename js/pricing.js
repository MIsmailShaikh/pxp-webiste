const hash = window.location.hash.substring(1);
        const validHashes = ['workforce', 'email', 'assessment', 'interview', 'allinone'];
        if (hash && validHashes.includes(hash) && hash !== 'workforce') {
            document.documentElement.classList.add('hide-default-tab');
            document.documentElement.classList.add('show-' + hash);
        }

if (window.requestIdleCallback) {
    requestIdleCallback(() => { if (window.lucide) lucide.createIcons(); });
} else {
    setTimeout(() => { if (window.lucide) lucide.createIcons(); }, 0);
}

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

        // Toggle Logic
        const toggleBtn = document.getElementById('billing-toggle');
        const toggleCircle = document.getElementById('toggle-circle');
        const priceEssential = document.getElementById('price-essential');
        const priceGrowth = document.getElementById('price-growth');
        const textEssential = document.getElementById('billing-text-essential');
        const textGrowth = document.getElementById('billing-text-growth');

        let isYearly = true; // default as requested by UI position

        function updatePrices() {
            if (isYearly) {
                toggleBtn.classList.remove('bg-gray-300');
                toggleBtn.classList.add('bg-orange-500');
                toggleCircle.classList.remove('translate-x-1');
                toggleCircle.classList.add('translate-x-7');
                
                priceEssential.textContent = '₹112';
                priceGrowth.textContent = '₹176';
                textEssential.textContent = 'per month, billed yearly';
                textGrowth.textContent = 'per month, billed yearly';
            } else {
                toggleBtn.classList.add('bg-gray-300');
                toggleBtn.classList.remove('bg-orange-500');
                toggleCircle.classList.add('translate-x-1');
                toggleCircle.classList.remove('translate-x-7');
                
                priceEssential.textContent = '₹140';
                priceGrowth.textContent = '₹220';
                textEssential.textContent = 'per month, billed monthly';
                textGrowth.textContent = 'per month, billed monthly';
            }
        }

        if(toggleBtn) {
            toggleBtn.addEventListener('click', () => {
                isYearly = !isYearly;
                updatePrices();
            });
            // Init
            updatePrices();
        }

        // Service Tabs Logic
        const serviceTabs = document.querySelectorAll('.service-tab');
        const serviceContents = document.querySelectorAll('.service-content');
        const serviceTitle = document.getElementById('service-title');
        
        const serviceNames = {
            'workforce': 'Workforce OS',
            'email': 'Corporate Email',
            'assessment': 'Assessment Portal',
            'interview': 'Interview Portal',
            'allinone': 'All-in-One Business Plan'
        };

        function switchService(targetId) {
            // Clean up anti-FOUC classes
            document.documentElement.classList.remove('hide-default-tab', 'show-email', 'show-assessment', 'show-interview', 'show-allinone');
            // Update tabs UI
            serviceTabs.forEach(tab => {
                const isAllInOne = tab.dataset.target === 'allinone';
                
                if (tab.dataset.target === targetId) {
                    tab.classList.add('active');
                    if (isAllInOne) {
                        tab.classList.add('scale-105', 'ring-2', 'ring-white', 'ring-offset-2', 'ring-offset-[#0a0a0a]');
                    } else {
                        tab.classList.remove('bg-white/10', 'text-white', 'border-white/10', 'hover:bg-white/20');
                        tab.classList.add('bg-white', 'text-black', 'shadow-md');
                    }
                } else {
                    tab.classList.remove('active');
                    if (isAllInOne) {
                        tab.classList.remove('scale-105', 'ring-2', 'ring-white', 'ring-offset-2', 'ring-offset-[#0a0a0a]');
                    } else {
                        tab.classList.add('bg-white/10', 'text-white', 'border-white/10', 'hover:bg-white/20');
                        tab.classList.remove('bg-white', 'text-black', 'shadow-md');
                    }
                }
            });

            // Update Title
            if (serviceTitle) {
                serviceTitle.textContent = serviceNames[targetId];
            }

            // Update Billing Toggle Visibility
            const billingContainer = document.getElementById('billing-toggle-container');
            if (billingContainer) {
                if (targetId === 'workforce') {
                    billingContainer.style.display = 'flex';
                } else {
                    billingContainer.style.display = 'none';
                }
            }

            // Update Compare Features Section Visibility
            const compareSection = document.getElementById('compare-features');
            const tableWorkforce = document.getElementById('table-workforce');
            const tableEmail = document.getElementById('table-email');
            
            if (compareSection) {
                if (targetId === 'workforce' || targetId === 'email') {
                    compareSection.style.display = 'block';
                    if (targetId === 'workforce') {
                        if (tableWorkforce) tableWorkforce.classList.remove('hidden');
                        if (tableEmail) tableEmail.classList.add('hidden');
                    } else if (targetId === 'email') {
                        if (tableWorkforce) tableWorkforce.classList.add('hidden');
                        if (tableEmail) tableEmail.classList.remove('hidden');
                    }
                } else {
                    compareSection.style.display = 'none';
                }
            }

            // Update Content Visibility
            serviceContents.forEach(content => {
                if (content.id === `content-${targetId}`) {
                    content.classList.remove('hidden');
                    // simple animation
                    content.style.opacity = '0';
                    content.style.transform = 'translateY(10px)';
                    setTimeout(() => {
                        content.style.transition = 'all 0.4s ease';
                        content.style.opacity = '1';
                        content.style.transform = 'translateY(0)';
                    }, 50);
                } else {
                    content.classList.add('hidden');
                }
            });
            
            // Re-render icons for new content
            if (window.lucide) {
                if (window.requestIdleCallback) {
    requestIdleCallback(() => { if (window.lucide) lucide.createIcons(); });
} else {
    setTimeout(() => { if (window.lucide) lucide.createIcons(); }, 0);
}
            }
            
            // Update URL hash without scrolling
            if(history.pushState) {
                history.pushState(null, null, '#' + targetId);
            }
        }
        
        window.addEventListener('DOMContentLoaded', () => {
            const hash = window.location.hash.substring(1);
            if (hash && serviceNames[hash]) {
                switchService(hash);
            }
        });


        // Corporate Email Term Logic
        const emailTermBtns = document.querySelectorAll('.email-term-btn');
        const starterPrice = document.getElementById('starter-price');
        const starterBase = document.getElementById('starter-base');
        const starterDiscount = document.getElementById('starter-discount');
        const starterTermText = document.getElementById('starter-term-text');
        
        const standardPrice = document.getElementById('standard-price');
        const standardBase = document.getElementById('standard-base');
        const standardDiscount = document.getElementById('standard-discount');
        const standardTermText = document.getElementById('standard-term-text');
        
        const proPrice = document.getElementById('pro-price');
        const proBase = document.getElementById('pro-base');
        const proDiscount = document.getElementById('pro-discount');
        const proTermText = document.getElementById('pro-term-text');
        
        // Removed enterprise dynamic logic as it is now custom pricing

        const emailPricing = {
            '48': {
                starter: { price: 20, base: 80, discount: '75% off' },
                standard: { price: 45, base: 150, discount: '70% off' },
                pro: { price: 299, base: 599, discount: '50% off' },
                enterprise: { price: '45,000', base: '60,000', discount: '25% off' }
            },
            '24': {
                starter: { price: 50, base: 80, discount: '37% off' },
                standard: { price: 90, base: 150, discount: '40% off' },
                pro: { price: 399, base: 599, discount: '33% off' },
                enterprise: { price: '50,000', base: '60,000', discount: '16% off' }
            },
            '12': {
                starter: { price: 65, base: 80, discount: '18% off' },
                standard: { price: 120, base: 150, discount: '20% off' },
                pro: { price: 499, base: 599, discount: '17% off' },
                enterprise: { price: '55,000', base: '60,000', discount: '8% off' }
            },
            '1': {
                starter: { price: 80, base: 80, discount: '' },
                standard: { price: 150, base: 150, discount: '' },
                pro: { price: 599, base: 599, discount: '' },
                enterprise: { price: '60,000', base: '60,000', discount: '' }
            }
        };

        if(emailTermBtns.length > 0) {
            emailTermBtns.forEach(btn => {
                btn.addEventListener('click', (e) => {
                    // UI update
                    emailTermBtns.forEach(b => {
                        b.classList.remove('bg-orange-500', 'text-white', 'active');
                        b.classList.add('text-gray-600', 'hover:text-gray-900');
                    });
                    e.target.classList.remove('text-gray-600', 'hover:text-gray-900');
                    e.target.classList.add('bg-orange-500', 'text-white', 'active');

                    const term = e.target.dataset.term;
                    const data = emailPricing[term];

                    // Update Starter
                    starterPrice.textContent = '₹' + data.starter.price;
                    if(term === '1') {
                        starterBase.classList.add('hidden');
                        starterDiscount.classList.add('hidden');
                        starterTermText.textContent = 'Price per mailbox. For 1-month term.';
                    } else {
                        starterBase.classList.remove('hidden');
                        starterDiscount.classList.remove('hidden');
                        starterDiscount.textContent = data.starter.discount;
                        starterTermText.textContent = `Price per mailbox. For ${term}-month term.`;
                    }

                    // Update Standard
                    standardPrice.textContent = '₹' + data.standard.price;
                    if(term === '1') {
                        standardBase.classList.add('hidden');
                        standardDiscount.classList.add('hidden');
                        standardTermText.textContent = 'Price per mailbox. For 1-month term.';
                    } else {
                        standardBase.classList.remove('hidden');
                        standardDiscount.classList.remove('hidden');
                        standardDiscount.textContent = data.standard.discount;
                        standardTermText.textContent = `Price per mailbox. For ${term}-month term.`;
                    }

                    // Update Pro
                    proPrice.textContent = '₹' + data.pro.price;
                    if(term === '1') {
                        proBase.classList.add('hidden');
                        proDiscount.classList.add('hidden');
                        proTermText.textContent = 'Price per mailbox. For 1-month term.';
                    } else {
                        proBase.classList.remove('hidden');
                        proDiscount.classList.remove('hidden');
                        proDiscount.textContent = data.pro.discount;
                        proTermText.textContent = `Price per mailbox. For ${term}-month term.`;
                    }

                    // Enterprise is static 'Custom' pricing
                });
            });
        }

        // Assessment Portal Term Logic
        const assessmentTermBtns = document.querySelectorAll('.assessment-term-btn');
        const assessmentPrice = document.getElementById('assessment-price');
        const assessmentBase = document.getElementById('assessment-base');
        const assessmentTermText = document.getElementById('assessment-term-text');

        const assessmentPricing = {
            '24': { price: '8,400', discountText: 'For 24-month term.' },
            '12': { price: '9,600', discountText: 'For 12-month term.' },
            '1': { price: '12,000', discountText: 'For 1-month term.' }
        };

        if(assessmentTermBtns.length > 0) {
            assessmentTermBtns.forEach(btn => {
                btn.addEventListener('click', (e) => {
                    assessmentTermBtns.forEach(b => {
                        b.classList.remove('bg-orange-500', 'text-white', 'active');
                        b.classList.add('text-gray-600', 'hover:text-gray-900');
                    });
                    e.target.classList.remove('text-gray-600', 'hover:text-gray-900');
                    e.target.classList.add('bg-orange-500', 'text-white', 'active');

                    const term = e.target.dataset.term;
                    const data = assessmentPricing[term];

                    assessmentPrice.textContent = '₹' + data.price;
                    assessmentTermText.textContent = data.discountText;
                    
                    if(term === '1') {
                        assessmentBase.classList.add('hidden');
                    } else {
                        assessmentBase.classList.remove('hidden');
                    }
                });
            });
        }

    
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
                    if (window.lucide) window.if (window.requestIdleCallback) {
    requestIdleCallback(() => { if (window.lucide) lucide.createIcons(); });
} else {
    setTimeout(() => { if (window.lucide) lucide.createIcons(); }, 0);
}
                } else {
                    mobileMenu.classList.remove('opacity-100', 'scale-y-100');
                    mobileMenu.classList.add('opacity-0', 'scale-y-95');
                    setTimeout(() => {
                        mobileMenu.classList.add('hidden');
                    }, 300); // Wait for transition
                    // Change icon back to menu
                    mobileMenuBtn.innerHTML = '<i data-lucide="menu" class="w-6 h-6 text-gray-900"></i>';
                    if (window.lucide) window.if (window.requestIdleCallback) {
    requestIdleCallback(() => { if (window.lucide) lucide.createIcons(); });
} else {
    setTimeout(() => { if (window.lucide) lucide.createIcons(); }, 0);
}
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