window.addEventListener('load', () => {
    if (window.lucide) {
        if (window.requestIdleCallback) {
            requestIdleCallback(() => window.lucide.createIcons());
        } else {
            setTimeout(() => window.lucide.createIcons(), 100);
        }
    }
});

        
        const urlParams = new URLSearchParams(window.location.search);
        const planParam = urlParams.get('plan') || 'email-standard';

        const planConfig = {
            'email-starter': {
                name: 'Starter Plan', category: 'Corporate Email', icon: 'mail',
                baseMonthly: 80, taxRate: 0.18, periods: [48, 24, 12, 1], defaultPeriod: '48',
                discounts: { '48': 20, '24': 50, '12': 65, '1': 80 },
                label: 'Mailbox', labelPlural: 'Mailboxes'
            },
            'email-standard': {
                name: 'Standard Business Plan', category: 'Corporate Email', icon: 'mail',
                baseMonthly: 150, taxRate: 0.18, periods: [48, 24, 12, 1], defaultPeriod: '48',
                discounts: { '48': 45, '24': 90, '12': 120, '1': 150 },
                label: 'Mailbox', labelPlural: 'Mailboxes'
            },
            'email-pro': {
                name: 'Pro Business Plan', category: 'Corporate Email', icon: 'mail',
                baseMonthly: 599, taxRate: 0.18, periods: [48, 24, 12, 1], defaultPeriod: '48',
                discounts: { '48': 299, '24': 399, '12': 499, '1': 599 },
                label: 'Mailbox', labelPlural: 'Mailboxes'
            },
            'workforce-essential': {
                name: 'Essential Plan', category: 'Workforce OS', icon: 'layers',
                baseMonthly: 140, taxRate: 0.18, periods: [12, 1], defaultPeriod: '12',
                discounts: { '12': 112, '1': 140 },
                label: 'Employee', labelPlural: 'Employees'
            },
            'workforce-growth': {
                name: 'Growth Plan', category: 'Workforce OS', icon: 'layers',
                baseMonthly: 220, taxRate: 0.18, periods: [12, 1], defaultPeriod: '12',
                discounts: { '12': 176, '1': 220 },
                label: 'Employee', labelPlural: 'Employees'
            },
            'assessment-pro': {
                name: 'Pro Plan', category: 'Assessment Portal', icon: 'code',
                baseMonthly: 12000, taxRate: 0.18, periods: [24, 12, 1], defaultPeriod: '1',
                discounts: { '24': 8400, '12': 9600, '1': 12000 },
                label: 'Assessment', labelPlural: 'Assessments'
            },
            'interview-pro': {
                name: 'Pro Plan', category: 'Interview Portal', icon: 'video',
                baseMonthly: 4999, taxRate: 0.18, periods: [1], defaultPeriod: '1',
                discounts: { '1': 4999 },
                label: 'License', labelPlural: 'Licenses'
            },
            'all-in-one': {
                name: 'The PXP Business Suite', category: 'All-in-One Plan', icon: 'sparkles',
                baseMonthly: 12000, taxRate: 0.18, periods: [1], defaultPeriod: '1',
                discounts: { '1': 12000 },
                label: 'Suite', labelPlural: 'Suites'
            }
        };

        const config = planConfig[planParam] || planConfig['email-standard'];

        // Populate DOM elements based on config
        document.getElementById('plan-name-display').textContent = config.name;
        document.getElementById('summary-plan-name').textContent = config.name;
        document.getElementById('plan-category-display').textContent = config.category;
        document.getElementById('quantity-label').textContent = config.labelPlural;
        
        const iconEl = document.getElementById('plan-icon-display');
        iconEl.setAttribute('data-lucide', config.icon);



        const periodSelector = document.getElementById('period-selector');
        periodSelector.innerHTML = '';
        config.periods.forEach(p => {
            const opt = document.createElement('option');
            opt.value = p;
            opt.textContent = p + (p === 1 ? ' month' : ' months');
            periodSelector.appendChild(opt);
        });

        // Initialize variables
        const baseMonthly = config.baseMonthly;
        const discountRates = config.discounts;
        const taxRate = config.taxRate;
        
        let currentQty = 1;
        let currentPeriod = config.defaultPeriod;
        periodSelector.value = currentPeriod;

        const qtyDisplay = document.getElementById('qty-display');
        const btnMinus = document.getElementById('btn-minus');
        const btnPlus = document.getElementById('btn-plus');

        const basePriceDisplay = document.getElementById('base-price-display');
        const discountPriceDisplay = document.getElementById('discount-price-display');
        const renewPrice = document.getElementById('renew-price');

        const sumPeriod = document.getElementById('summary-period');
        const sumQty = document.getElementById('summary-qty');
        const sumBaseTotal = document.getElementById('summary-base-total');
        const sumDiscountTotal = document.getElementById('summary-discount-total');
        const sumTaxes = document.getElementById('summary-taxes');
        const sumFinalBase = document.getElementById('summary-final-base');
        const sumFinalTotal = document.getElementById('summary-final-total');

        function formatCurrency(num) {
            return new Intl.NumberFormat('en-IN', { maximumFractionDigits: 2 }).format(num);
        }

        function updateCart() {
            const months = parseInt(currentPeriod);
            const discountedMonthly = discountRates[currentPeriod];

            // Left panel updates
            basePriceDisplay.textContent = '₹' + formatCurrency(baseMonthly);
            discountPriceDisplay.textContent = '₹' + formatCurrency(discountedMonthly);
            renewPrice.textContent = '₹' + formatCurrency(baseMonthly);

            // Summary text updates
            sumPeriod.textContent = `${months}-month period`;
            sumQty.textContent = `${currentQty} ${currentQty > 1 ? config.labelPlural : config.label}`;

            // Math
            const totalBase = baseMonthly * months * currentQty;
            const totalDiscount = discountedMonthly * months * currentQty;
            const taxes = totalDiscount * taxRate;
            const finalTotal = totalDiscount + taxes;

            sumBaseTotal.textContent = '₹' + formatCurrency(totalBase);
            sumDiscountTotal.textContent = '₹' + formatCurrency(totalDiscount);
            sumTaxes.textContent = '₹' + formatCurrency(taxes);
            
            sumFinalBase.textContent = '₹' + formatCurrency(totalBase) + (totalBase % 1 === 0 ? '.00' : '');
            sumFinalTotal.textContent = '₹' + formatCurrency(finalTotal);

            // Hide strikethroughs if no discount
            if (months === 1 || baseMonthly === discountedMonthly) {
                basePriceDisplay.parentElement.classList.add('hidden');
                sumBaseTotal.parentElement.classList.add('hidden');
                sumFinalBase.parentElement.classList.add('hidden');
            } else {
                basePriceDisplay.parentElement.classList.remove('hidden');
                sumBaseTotal.parentElement.classList.remove('hidden');
                sumFinalBase.parentElement.classList.remove('hidden');
            }
        }

        periodSelector.addEventListener('change', (e) => {
            currentPeriod = e.target.value;
            updateCart();
        });

        btnMinus.addEventListener('click', () => {
            if (currentQty > 1) {
                currentQty--;
                qtyDisplay.value = currentQty;
                updateCart();
            }
        });

        qtyDisplay.addEventListener('input', (e) => {
            let val = parseInt(e.target.value);
            if (val >= 1 && val <= 1000) {
                currentQty = val;
                updateCart();
            }
        });
        
        btnPlus.addEventListener('click', () => {
            if (currentQty < 1000) {
                currentQty++;
                qtyDisplay.value = currentQty;
                updateCart();
            }
        });

        // Initialize
        window.addEventListener('load', () => {
    if (window.lucide) {
        if (window.requestIdleCallback) {
            requestIdleCallback(() => window.lucide.createIcons());
        } else {
            setTimeout(() => window.lucide.createIcons(), 100);
        }
    }
});
        updateCart();

    
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

        // ==========================================
        // CHECKOUT LOGIC (AUTH & PAYMENT)
        // ==========================================
        
        let paymentMethod = null;
        let isLoggedIn = localStorage.getItem('pxp_logged_in') === 'true';

        // UI Elements
        const authUnlogged = document.getElementById('auth-unlogged');
        const authLogged = document.getElementById('auth-logged');
        const authUserName = document.getElementById('auth-user-name');
        const authUserEmail = document.getElementById('auth-user-email');
        const authAvatar = document.getElementById('auth-avatar');
        const paymentOverlay = document.getElementById('payment-overlay');
        const authModal = document.getElementById('auth-modal');
        const authModalContent = document.getElementById('auth-modal-content');
        
        function updateAuthState() {
            if (isLoggedIn) {
                authUnlogged.classList.add('hidden');
                authUnlogged.classList.remove('flex', 'md:flex');
                
                authLogged.classList.remove('hidden');
                authLogged.classList.add('flex');
                
                paymentOverlay.classList.add('opacity-0', 'pointer-events-none');
                
                // Populate mock user data
                const email = localStorage.getItem('pxp_email') || 'user@example.com';
                const name = email.split('@')[0];
                authUserName.textContent = name.charAt(0).toUpperCase() + name.slice(1);
                authUserEmail.textContent = email;
                authAvatar.textContent = name.substring(0,2).toUpperCase();
            } else {
                authUnlogged.classList.remove('hidden');
                authUnlogged.classList.add('flex', 'md:flex');
                
                authLogged.classList.add('hidden');
                authLogged.classList.remove('flex');
                
                paymentOverlay.classList.remove('opacity-0', 'pointer-events-none');
            }
        }
        
        // Initial state
        updateAuthState();

        // Payment Toggle Logic
        window.togglePayment = function(method) {
            if (!isLoggedIn) return; // Prevent selection if not logged in
            
            paymentMethod = method;
            
            // Elements
            const cardAcc = document.getElementById('acc-card');
            const cardBody = document.getElementById('body-card');
            const cardRadio = document.getElementById('radio-card');
            const cardIcon = document.getElementById('icon-card');
            
            const upiAcc = document.getElementById('acc-upi');
            const upiBody = document.getElementById('body-upi');
            const upiRadio = document.getElementById('radio-upi');
            const upiIcon = document.getElementById('icon-upi');

            // Reset both
            cardAcc.classList.remove('border-blue-600', 'shadow-[0_0_0_1px_rgba(37,99,235,1)]');
            cardAcc.classList.add('border-gray-200');
            cardBody.classList.remove('h-[280px]', 'md:h-[220px]');
            cardBody.classList.add('h-0');
            cardRadio.classList.remove('border-[5px]', 'border-blue-600');
            cardRadio.classList.add('border-gray-300', 'border');
            if (cardIcon) cardIcon.classList.remove('rotate-180');
            
            upiAcc.classList.remove('border-blue-600', 'shadow-[0_0_0_1px_rgba(37,99,235,1)]');
            upiAcc.classList.add('border-gray-200');
            upiBody.classList.remove('h-[100px]');
            upiBody.classList.add('h-0');
            upiRadio.classList.remove('border-[5px]', 'border-blue-600');
            upiRadio.classList.add('border-gray-300', 'border');
            if (upiIcon) upiIcon.classList.remove('rotate-180');

            // Activate selected
            if (method === 'card') {
                cardAcc.classList.add('border-blue-600', 'shadow-[0_0_0_1px_rgba(37,99,235,1)]');
                cardAcc.classList.remove('border-gray-200');
                cardBody.classList.add('h-[280px]', 'md:h-[220px]');
                cardBody.classList.remove('h-0');
                cardRadio.classList.add('border-[5px]', 'border-blue-600');
                cardRadio.classList.remove('border-gray-300', 'border');
                if (cardIcon) cardIcon.classList.add('rotate-180');
            } else if (method === 'upi') {
                upiAcc.classList.add('border-blue-600', 'shadow-[0_0_0_1px_rgba(37,99,235,1)]');
                upiAcc.classList.remove('border-gray-200');
                upiBody.classList.add('h-[100px]');
                upiBody.classList.remove('h-0');
                upiRadio.classList.add('border-[5px]', 'border-blue-600');
                upiRadio.classList.remove('border-gray-300', 'border');
                if (upiIcon) upiIcon.classList.add('rotate-180');
            }
        };

        // Modal Logic
        function openAuthModal() {
            authModal.classList.remove('hidden');
            setTimeout(() => {
                authModal.classList.remove('opacity-0');
                authModalContent.classList.remove('scale-95');
                authModalContent.classList.add('scale-100');
            }, 10);
        }
        
        function closeAuthModal() {
            authModal.classList.add('opacity-0');
            authModalContent.classList.add('scale-95');
            authModalContent.classList.remove('scale-100');
            setTimeout(() => {
                authModal.classList.add('hidden');
            }, 300);
        }

        document.getElementById('btn-open-login').addEventListener('click', openAuthModal);
        document.getElementById('btn-close-modal').addEventListener('click', closeAuthModal);
        
        document.getElementById('btn-logout').addEventListener('click', () => {
            isLoggedIn = false;
            paymentMethod = null; // reset payment
            localStorage.removeItem('pxp_logged_in');
            localStorage.removeItem('pxp_email');
            
            // reset accordion styles
            document.getElementById('body-card').classList.add('h-0');
            document.getElementById('body-card').classList.remove('h-[280px]', 'md:h-[220px]');
            document.getElementById('acc-card').classList.remove('border-blue-600', 'shadow-[0_0_0_1px_rgba(37,99,235,1)]');
            document.getElementById('acc-card').classList.add('border-gray-200');
            document.getElementById('radio-card').classList.remove('border-[5px]', 'border-blue-600');
            document.getElementById('radio-card').classList.add('border-gray-300', 'border');

            document.getElementById('body-upi').classList.add('h-0');
            document.getElementById('body-upi').classList.remove('h-[100px]');
            document.getElementById('acc-upi').classList.remove('border-blue-600', 'shadow-[0_0_0_1px_rgba(37,99,235,1)]');
            document.getElementById('acc-upi').classList.add('border-gray-200');
            document.getElementById('radio-upi').classList.remove('border-[5px]', 'border-blue-600');
            document.getElementById('radio-upi').classList.add('border-gray-300', 'border');

            updateAuthState();
        });

        document.getElementById('btn-submit-auth').addEventListener('click', () => {
            const email = document.getElementById('auth-email').value;
            const pass = document.getElementById('auth-password').value;
            
            if (!email || !pass) {
                alert("Please enter both email and password.");
                return;
            }
            
            // Mock login
            isLoggedIn = true;
            localStorage.setItem('pxp_logged_in', 'true');
            localStorage.setItem('pxp_email', email);
            updateAuthState();
            closeAuthModal();
            
            // Auto-select card if none selected
            if (!paymentMethod) {
                setTimeout(() => { togglePayment('card'); }, 300);
            }
        });

        // Checkout Button Logic
        document.getElementById('btn-checkout-continue').addEventListener('click', () => {
            if (!isLoggedIn) {
                openAuthModal();
                return;
            }
            
            if (!paymentMethod) {
                alert("Please select a payment method.");
                return;
            }
            
            if (paymentMethod === 'card') {
                const num = document.getElementById('cc-number').value;
                if(num.length < 15) {
                    alert("Please enter a valid card number.");
                    return;
                }
            } else if (paymentMethod === 'upi') {
                const upi = document.getElementById('upi-id').value;
                if(!upi.includes('@')) {
                    alert("Please enter a valid UPI ID.");
                    return;
                }
            }
            
            // Proceed to Razorpay Mock
            const loader = document.getElementById('razorpay-loader');
            loader.classList.remove('hidden');
            
            setTimeout(() => {
                alert("This is a frontend demo. The integration would now open Razorpay securely using the tokenized card details.");
                loader.classList.add('hidden');
            }, 2500);
        });