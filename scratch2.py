import re

with open('d:/project pxp/website/pricing.html', 'r', encoding='utf-8') as f:
    content = f.read()

# We need to replace the Pricing Cards Grid and the Javascript Logic, and the Detailed Comparison table.
# Actually, since I generated the whole `new_body` in scratch.py, I can just replace `new_body` and `footer_and_scripts` again from scratch, using the original `pricing.html` logic.
# Wait, let's just use regex to replace specific parts of `pricing.html`.

# 1. Replace Pricing Cards
cards_start = content.find('<!-- Pricing Cards Grid -->')
cards_end = content.find('<!-- Feature Comparison Table -->')

new_cards = """<!-- Pricing Cards Grid -->
            <div class="grid grid-cols-1 lg:grid-cols-3 gap-8 relative z-20 mb-16">
                
                <!-- Essential Card -->
                <div class="bg-white rounded-3xl p-8 border border-gray-100 shadow-sm hover:shadow-xl hover:-translate-y-2 transition-all duration-300 flex flex-col">
                    <h3 class="text-2xl font-bold text-gray-900 mb-2">Essential</h3>
                    <p class="text-sm text-gray-500 mb-6 h-10">Perfect for small teams needing core HR and leave management.</p>
                    
                    <div class="mb-8">
                        <div class="flex items-end gap-1 mb-2">
                            <span class="text-5xl font-black text-gray-900 tracking-tight">₹<span id="price-essential" class="tabular-nums">0</span></span>
                            <span class="text-gray-500 mb-2 font-medium">/mo</span>
                        </div>
                        <div class="text-sm text-blue-600 font-medium bg-blue-50 inline-block px-3 py-1 rounded-full">₹140 per employee</div>
                    </div>

                    <ul class="space-y-4 mb-8 text-sm text-gray-600 font-medium flex-grow">
                        <li class="flex items-start gap-3"><i data-lucide="check-circle-2" class="w-5 h-5 text-blue-500 shrink-0"></i> HRM Software</li>
                        <li class="flex items-start gap-3"><i data-lucide="check-circle-2" class="w-5 h-5 text-blue-500 shrink-0"></i> Leave Engine</li>
                        <li class="flex items-start gap-3"><i data-lucide="check-circle-2" class="w-5 h-5 text-blue-500 shrink-0"></i> 2 Dashboards (HR & Manager)</li>
                        <li class="flex items-start gap-3"><i data-lucide="check-circle-2" class="w-5 h-5 text-blue-500 shrink-0"></i> Data Integrity</li>
                    </ul>
                    
                    <button class="w-full py-4 rounded-xl border border-gray-200 text-gray-900 font-bold hover:bg-gray-50 transition-colors mt-auto">Start Free Trial</button>
                </div>

                <!-- Growth Card (Recommended) -->
                <div class="animated-border-box p-8 shadow-2xl relative transform lg:-translate-y-8 flex flex-col z-30">
                    <div class="absolute -top-4 left-1/2 -translate-x-1/2 bg-gradient-to-r from-blue-600 to-purple-600 text-white px-6 py-1.5 rounded-full text-sm font-bold uppercase tracking-widest shadow-md whitespace-nowrap">
                        Most Popular
                    </div>
                    
                    <h3 class="text-2xl font-bold text-gray-900 mb-2">Growth</h3>
                    <p class="text-sm text-gray-500 mb-6 h-10">Everything you need to automate payroll and operations.</p>
                    
                    <div class="mb-8">
                        <div class="flex items-end gap-1 mb-2">
                            <span class="text-5xl font-black text-gray-900 tracking-tight">₹<span id="price-growth" class="tabular-nums">0</span></span>
                            <span class="text-gray-500 mb-2 font-medium">/mo</span>
                        </div>
                        <div class="text-sm text-purple-600 font-medium bg-purple-50 inline-block px-3 py-1 rounded-full">₹220 per employee</div>
                    </div>

                    <ul class="space-y-4 mb-8 text-sm text-gray-700 font-medium flex-grow">
                        <li class="flex items-start gap-3"><i data-lucide="check-circle-2" class="w-5 h-5 text-purple-600 shrink-0"></i> Everything in Essential</li>
                        <li class="flex items-start gap-3"><i data-lucide="check-circle-2" class="w-5 h-5 text-purple-600 shrink-0"></i> 6 Dashboards (Emp, Mgr, HR, IT, Dir)</li>
                        <li class="flex items-start gap-3"><i data-lucide="check-circle-2" class="w-5 h-5 text-purple-600 shrink-0"></i> Automatic Payroll Processing</li>
                        <li class="flex items-start gap-3"><i data-lucide="check-circle-2" class="w-5 h-5 text-purple-600 shrink-0"></i> Automation Emails (Leave & More)</li>
                        <li class="flex items-start gap-3"><i data-lucide="check-circle-2" class="w-5 h-5 text-purple-600 shrink-0"></i> Change on demand (5 Free)</li>
                        <li class="flex items-start gap-3"><i data-lucide="check-circle-2" class="w-5 h-5 text-purple-600 shrink-0"></i> Automatic Biometric Sync</li>
                    </ul>
                    
                    <button class="w-full py-4 rounded-xl bg-gray-900 text-white font-bold hover:bg-gray-800 transition-colors shadow-lg mt-auto">Get Started Now</button>
                </div>

                <!-- Premium Card -->
                <div class="bg-[#131313] rounded-3xl p-8 shadow-xl text-white flex flex-col relative overflow-hidden border border-white/10 hover:-translate-y-2 transition-transform duration-300">
                    <!-- Subtle Glow -->
                    <div class="absolute -top-24 -right-24 w-48 h-48 bg-purple-500/30 rounded-full blur-[60px]"></div>

                    <h3 class="text-2xl font-bold mb-2">Enterprise</h3>
                    <p class="text-sm text-gray-400 mb-6 h-10">Bespoke features and your brand's identity across the app.</p>
                    
                    <div class="mb-8 h-[76px] flex items-end">
                        <span class="text-5xl font-black tracking-tight bg-gradient-to-r from-white to-gray-400 bg-clip-text text-transparent">Custom</span>
                    </div>

                    <ul class="space-y-4 mb-8 text-sm text-gray-300 font-medium flex-grow">
                        <li class="flex items-start gap-3"><i data-lucide="check-circle-2" class="w-5 h-5 text-white/50 shrink-0"></i> Everything from Growth</li>
                        <li class="flex items-start gap-3"><i data-lucide="check-circle-2" class="w-5 h-5 text-white/50 shrink-0"></i> White-labeling (Your Logo & Name)</li>
                        <li class="flex items-start gap-3"><i data-lucide="check-circle-2" class="w-5 h-5 text-white/50 shrink-0"></i> Custom Workflows & Workspaces</li>
                        <li class="flex items-start gap-3"><i data-lucide="check-circle-2" class="w-5 h-5 text-white/50 shrink-0"></i> Dedicated Support & Rep</li>
                    </ul>
                    
                    <button class="w-full py-4 rounded-xl bg-white text-black font-bold hover:bg-gray-200 transition-colors mt-auto">Contact Sales</button>
                </div>

            </div>
            
            <!-- Add-ons Section -->
            <div class="max-w-4xl mx-auto bg-white rounded-3xl p-8 shadow-xl border border-gray-100 relative z-20 reveal-text mt-8">
                <h3 class="text-2xl font-bold text-gray-900 mb-6 text-center">Customize your plan with Add-ons</h3>
                <div class="flex flex-col gap-4">
                    
                    <label class="flex items-center justify-between p-4 border border-gray-200 rounded-2xl cursor-pointer hover:bg-blue-50/50 transition-colors group">
                        <div class="flex items-center gap-4">
                            <input type="checkbox" id="addon-interview" value="40" class="addon-checkbox w-6 h-6 text-blue-600 rounded-md focus:ring-blue-500">
                            <div>
                                <h4 class="font-bold text-gray-900 group-hover:text-blue-600 transition-colors">Interview Portal</h4>
                                <p class="text-sm text-gray-500">Streamline your hiring and scheduling process.</p>
                            </div>
                        </div>
                        <div class="text-right">
                            <span class="block font-bold text-gray-900">+₹40</span>
                            <span class="text-xs text-gray-500">/emp/mo</span>
                        </div>
                    </label>

                    <label class="flex items-center justify-between p-4 border border-gray-200 rounded-2xl cursor-pointer hover:bg-blue-50/50 transition-colors group">
                        <div class="flex items-center gap-4">
                            <input type="checkbox" id="addon-messaging" value="30" class="addon-checkbox w-6 h-6 text-blue-600 rounded-md focus:ring-blue-500">
                            <div>
                                <h4 class="font-bold text-gray-900 group-hover:text-blue-600 transition-colors">Messaging Tool</h4>
                                <p class="text-sm text-gray-500">Internal chat and secure communication module.</p>
                            </div>
                        </div>
                        <div class="text-right">
                            <span class="block font-bold text-gray-900">+₹30</span>
                            <span class="text-xs text-gray-500">/emp/mo</span>
                        </div>
                    </label>

                    <label class="flex items-center justify-between p-4 border border-gray-200 rounded-2xl cursor-pointer hover:bg-blue-50/50 transition-colors group">
                        <div class="flex items-center gap-4">
                            <input type="checkbox" id="addon-inventory" value="50" class="addon-checkbox w-6 h-6 text-blue-600 rounded-md focus:ring-blue-500">
                            <div>
                                <h4 class="font-bold text-gray-900 group-hover:text-blue-600 transition-colors">IT Inventory Management Tool</h4>
                                <p class="text-sm text-gray-500">Track laptops, assets, and software licenses.</p>
                            </div>
                        </div>
                        <div class="text-right">
                            <span class="block font-bold text-gray-900">+₹50</span>
                            <span class="text-xs text-gray-500">/emp/mo</span>
                        </div>
                    </label>

                </div>
            </div>
            
        </div>
    </section>

    <!-- Feature Comparison Table -->"""

content = content[:cards_start] + new_cards + content[cards_end + len('<!-- Feature Comparison Table -->'):]

# 2. Fix JS logic 
js_start = content.find('// Pricing Logic')
js_end = content.find('// Interactive Spotlight Logic')

new_js = """// Pricing Logic
        const empInput = document.getElementById('emp-input');
        const empSlider = document.getElementById('emp-slider');
        const priceEssential = document.getElementById('price-essential');
        const priceGrowth = document.getElementById('price-growth');
        const addonCheckboxes = document.querySelectorAll('.addon-checkbox');

        if(empInput && empSlider) {
            // New Plan Base Prices per Employee
            const ESSENTIAL_RATE = 140;
            const GROWTH_RATE = 220;

            function calculateAddons() {
                let addonTotalPerEmp = 0;
                addonCheckboxes.forEach(cb => {
                    if(cb.checked) {
                        addonTotalPerEmp += parseInt(cb.value);
                    }
                });
                return addonTotalPerEmp;
            }

            function updatePrices(empCount) {
                const addonsPerEmp = calculateAddons();
                
                let essentialTotal = empCount * (ESSENTIAL_RATE + addonsPerEmp);
                let growthTotal = empCount * (GROWTH_RATE + addonsPerEmp);

                // Format with commas (Indian numbering system)
                priceEssential.textContent = essentialTotal.toLocaleString('en-IN');
                priceGrowth.textContent = growthTotal.toLocaleString('en-IN');
            }

            function syncValues(value) {
                // Ensure bounds
                let val = parseInt(value);
                if(isNaN(val)) val = 10;
                if(val > 3000) val = 3000; 
                
                empInput.value = val;
                empSlider.value = val;

                // Update slider background gradient dynamically
                const percentage = ((val - 10) / (3000 - 10)) * 100;
                empSlider.style.background = `linear-gradient(to right, #3b82f6 ${percentage}%, #e2e8f0 ${percentage}%)`;
                
                updatePrices(val);
            }

            empSlider.addEventListener('input', (e) => {
                syncValues(e.target.value);
            });

            empInput.addEventListener('change', (e) => {
                let val = parseInt(e.target.value);
                if(val < 10) val = 10;
                syncValues(val);
            });

            addonCheckboxes.forEach(cb => {
                cb.addEventListener('change', () => {
                    syncValues(empSlider.value);
                });
            });

            // Initial setup
            syncValues(50);
        }

        """

content = content[:js_start] + new_js + content[js_end:]

# 3. Fix the Comparison table to match the new features exactly
table_start = content.find('<tbody class="text-sm">')
table_end = content.find('</tbody>')

new_table = """<tbody class="text-sm">
                        <!-- Category 1: HR & Core -->
                        <tr>
                            <td colspan="4" class="p-4 pt-8 pb-2 text-xs font-bold uppercase tracking-wider text-gray-400 bg-white">Core Modules</td>
                        </tr>
                        <tr class="hover:bg-gray-50 transition-colors border-b border-gray-100">
                            <td class="p-4 text-gray-700 font-medium">HRM Software</td>
                            <td class="p-4"><i data-lucide="check" class="w-5 h-5 text-blue-600"></i></td>
                            <td class="p-4"><i data-lucide="check" class="w-5 h-5 text-purple-600"></i></td>
                            <td class="p-4"><i data-lucide="check" class="w-5 h-5 text-gray-900"></i></td>
                        </tr>
                        <tr class="hover:bg-gray-50 transition-colors border-b border-gray-100">
                            <td class="p-4 text-gray-700 font-medium">Leave Engine</td>
                            <td class="p-4"><i data-lucide="check" class="w-5 h-5 text-blue-600"></i></td>
                            <td class="p-4"><i data-lucide="check" class="w-5 h-5 text-purple-600"></i></td>
                            <td class="p-4"><i data-lucide="check" class="w-5 h-5 text-gray-900"></i></td>
                        </tr>
                        <tr class="hover:bg-gray-50 transition-colors border-b border-gray-100">
                            <td class="p-4 text-gray-700 font-medium">Dashboards Included</td>
                            <td class="p-4 text-blue-600 font-bold">2 (HR, Manager)</td>
                            <td class="p-4 text-purple-600 font-bold">6 (Emp, Mgr, HR, IT, Dir)</td>
                            <td class="p-4 text-gray-900 font-bold">Unlimited Custom</td>
                        </tr>
                        <tr class="hover:bg-gray-50 transition-colors border-b border-gray-100">
                            <td class="p-4 text-gray-700 font-medium">Automatic Payroll Processing</td>
                            <td class="p-4"><i data-lucide="minus" class="w-5 h-5 text-gray-300"></i></td>
                            <td class="p-4"><i data-lucide="check" class="w-5 h-5 text-purple-600"></i></td>
                            <td class="p-4"><i data-lucide="check" class="w-5 h-5 text-gray-900"></i></td>
                        </tr>

                        <!-- Category 2: Automation -->
                        <tr>
                            <td colspan="4" class="p-4 pt-8 pb-2 text-xs font-bold uppercase tracking-wider text-gray-400 bg-white">Automation & Integrations</td>
                        </tr>
                        <tr class="hover:bg-gray-50 transition-colors border-b border-gray-100">
                            <td class="p-4 text-gray-700 font-medium">Automation Emails (Leave, Alerts)</td>
                            <td class="p-4"><i data-lucide="minus" class="w-5 h-5 text-gray-300"></i></td>
                            <td class="p-4"><i data-lucide="check" class="w-5 h-5 text-purple-600"></i></td>
                            <td class="p-4"><i data-lucide="check" class="w-5 h-5 text-gray-900"></i></td>
                        </tr>
                        <tr class="hover:bg-gray-50 transition-colors border-b border-gray-100">
                            <td class="p-4 text-gray-700 font-medium">Automatic Biometric Sync</td>
                            <td class="p-4"><i data-lucide="minus" class="w-5 h-5 text-gray-300"></i></td>
                            <td class="p-4"><i data-lucide="check" class="w-5 h-5 text-purple-600"></i></td>
                            <td class="p-4"><i data-lucide="check" class="w-5 h-5 text-gray-900"></i></td>
                        </tr>
                        <tr class="hover:bg-gray-50 transition-colors border-b border-gray-100">
                            <td class="p-4 text-gray-700 font-medium">Change on demand (Extra app changes)</td>
                            <td class="p-4 text-gray-500">Paid</td>
                            <td class="p-4 text-purple-600 font-bold">5 Free, then Paid</td>
                            <td class="p-4 text-gray-900 font-bold">Unlimited Customizations</td>
                        </tr>

                        <!-- Category 3: Branding & Security -->
                        <tr>
                            <td colspan="4" class="p-4 pt-8 pb-2 text-xs font-bold uppercase tracking-wider text-gray-400 bg-white">Branding & Data</td>
                        </tr>
                        <tr class="hover:bg-gray-50 transition-colors border-b border-gray-100">
                            <td class="p-4 text-gray-700 font-medium">Data Integrity</td>
                            <td class="p-4"><i data-lucide="check" class="w-5 h-5 text-blue-600"></i></td>
                            <td class="p-4"><i data-lucide="check" class="w-5 h-5 text-purple-600"></i></td>
                            <td class="p-4"><i data-lucide="check" class="w-5 h-5 text-gray-900"></i></td>
                        </tr>
                        <tr class="hover:bg-gray-50 transition-colors border-b border-gray-100">
                            <td class="p-4 text-gray-700 font-medium">White-labeling (Your Logo & Name)</td>
                            <td class="p-4"><i data-lucide="minus" class="w-5 h-5 text-gray-300"></i></td>
                            <td class="p-4"><i data-lucide="minus" class="w-5 h-5 text-gray-300"></i></td>
                            <td class="p-4"><i data-lucide="check" class="w-5 h-5 text-gray-900"></i></td>
                        </tr>
                    """

content = content[:table_start] + new_table + content[table_end:]

with open('d:/project pxp/website/pricing.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated cards, table, and pricing logic successfully!")
