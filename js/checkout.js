lucide.createIcons();

        
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
        lucide.createIcons();
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