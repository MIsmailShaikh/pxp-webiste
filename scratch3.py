import re

with open('d:/project pxp/website/pricing.html', 'r', encoding='utf-8') as f:
    content = f.read()

nav_end_idx = content.find('</nav>') + len('</nav>')
footer_start_idx = content.find('<!-- Footer -->')

head_and_nav = content[:nav_end_idx]
footer_and_scripts = content[footer_start_idx:]

new_body = """
    <!-- Pricing Hero & Toggle -->
    <div class="pt-32 pb-16 bg-[#FAFAFA] text-center">
        <h1 class="text-5xl font-bold tracking-tight text-gray-900 mb-8 font-inter">Pricing</h1>
        
        <!-- Toggle Switch -->
        <div class="flex items-center justify-center gap-4">
            <span class="text-sm font-medium text-gray-600">Pay monthly</span>
            <button id="billing-toggle" class="relative inline-flex h-8 w-14 items-center rounded-full bg-orange-500 transition-colors focus:outline-none">
                <span class="sr-only">Toggle billing</span>
                <span id="toggle-circle" class="inline-block h-6 w-6 translate-x-7 rounded-full bg-white transition-transform shadow-sm"></span>
            </button>
            <div class="flex flex-col text-left">
                <span class="text-sm font-medium text-gray-900">Pay yearly</span>
                <span class="text-xs font-bold text-orange-500">Save 20%</span>
            </div>
        </div>
    </div>

    <!-- Pricing Cards Section -->
    <section class="px-4 py-8 bg-[#FAFAFA]">
        <div class="max-w-[1000px] mx-auto">
            
            <div class="grid grid-cols-1 md:grid-cols-2 gap-0 relative">
                
                <!-- Essential Card -->
                <div class="bg-white border border-gray-200 p-10 flex flex-col hover:shadow-xl transition-shadow duration-300 relative z-10 md:border-r-0">
                    <h3 class="text-3xl font-semibold text-gray-900 mb-3 tracking-tight">Essential</h3>
                    <p class="text-gray-500 mb-8 text-sm h-10">For businesses needing core HR features and leave management.</p>
                    
                    <div class="flex items-start gap-1 mb-8">
                        <span class="text-5xl font-bold text-gray-900 tracking-tighter" id="price-essential">₹140</span>
                        <div class="flex flex-col text-xs text-gray-500 font-medium ml-1 mt-1">
                            <span>per employee</span>
                            <span id="billing-text-essential">per month</span>
                        </div>
                    </div>

                    <div class="mb-4 text-sm font-medium text-gray-900">Includes</div>
                    <ul class="space-y-4 text-sm text-gray-600 flex-grow">
                        <li class="flex items-start gap-3"><i data-lucide="check-circle-2" class="w-5 h-5 text-gray-900 shrink-0"></i> HRM software</li>
                        <li class="flex items-start gap-3"><i data-lucide="check-circle-2" class="w-5 h-5 text-gray-900 shrink-0"></i> Leave Engine</li>
                        <li class="flex items-start gap-3"><i data-lucide="check-circle-2" class="w-5 h-5 text-gray-900 shrink-0"></i> 2 Dashboards (HR & Manager)</li>
                        <li class="flex items-start gap-3"><i data-lucide="check-circle-2" class="w-5 h-5 text-gray-900 shrink-0"></i> Data Integrity</li>
                    </ul>
                    
                    <button class="w-full bg-gray-900 text-white rounded-full py-4 mt-10 font-medium hover:bg-gray-800 transition-colors">Get started</button>
                </div>

                <!-- Growth Card -->
                <div class="bg-white border border-gray-200 p-10 flex flex-col hover:shadow-xl transition-shadow duration-300 relative z-20">
                    <div class="absolute -top-[1px] -left-[1px] -right-[1px] border-t-4 border-blue-500"></div>
                    <div class="absolute top-4 right-4 text-xs font-bold text-blue-600 flex items-center gap-1">
                        Most popular <i data-lucide="star" class="w-3 h-3 fill-blue-600"></i>
                    </div>

                    <h3 class="text-3xl font-semibold text-gray-900 mb-3 tracking-tight">Growth</h3>
                    <p class="text-gray-500 mb-8 text-sm h-10">Everything you need to automate payroll and scale operations.</p>
                    
                    <div class="flex items-start gap-1 mb-8">
                        <span class="text-5xl font-bold text-gray-900 tracking-tighter" id="price-growth">₹220</span>
                        <div class="flex flex-col text-xs text-gray-500 font-medium ml-1 mt-1">
                            <span>per employee</span>
                            <span id="billing-text-growth">per month</span>
                        </div>
                    </div>

                    <div class="mb-4 text-sm font-medium text-gray-900">Everything in Essential, plus...</div>
                    <ul class="space-y-4 text-sm text-gray-600 flex-grow">
                        <li class="flex items-start gap-3"><i data-lucide="check-circle-2" class="w-5 h-5 text-gray-900 shrink-0"></i> 6 Dashboards (Emp, Mgr, HR, IT, Dir)</li>
                        <li class="flex items-start gap-3"><i data-lucide="check-circle-2" class="w-5 h-5 text-gray-900 shrink-0"></i> Automatic Payroll Processing</li>
                        <li class="flex items-start gap-3"><i data-lucide="check-circle-2" class="w-5 h-5 text-gray-900 shrink-0"></i> Automation Emails</li>
                        <li class="flex items-start gap-3"><i data-lucide="check-circle-2" class="w-5 h-5 text-gray-900 shrink-0"></i> Change on demand (5 Free)</li>
                        <li class="flex items-start gap-3"><i data-lucide="check-circle-2" class="w-5 h-5 text-gray-900 shrink-0"></i> Automatic Biometric Sync</li>
                    </ul>
                    
                    <button class="w-full bg-gray-900 text-white rounded-full py-4 mt-10 font-medium hover:bg-gray-800 transition-colors">Get started</button>
                </div>
            </div>

            <!-- Enterprise Wide Box -->
            <div class="bg-[#F3F4F6] border border-gray-200 mt-6 p-8 md:p-10 flex flex-col md:flex-row items-center justify-between gap-6 hover:shadow-lg transition-shadow">
                <div>
                    <h3 class="text-2xl font-semibold text-gray-900 mb-2">Enterprise</h3>
                    <p class="text-gray-600 text-sm">Transform your business with a custom-tailored solution built for scale. Includes full white-labeling.</p>
                </div>
                <button class="bg-gray-900 text-white rounded-full px-8 py-4 font-medium hover:bg-gray-800 transition-colors whitespace-nowrap">Get in touch</button>
            </div>

            <!-- Add-ons Minimal Rows -->
            <div class="mt-16 mb-8">
                <h3 class="text-2xl font-bold text-gray-900 mb-6 text-center">Customize with Add-ons</h3>
                <div class="max-w-2xl mx-auto space-y-0 border border-gray-200 bg-white">
                    
                    <div class="flex items-center justify-between p-5 border-b border-gray-200 hover:bg-gray-50 transition-colors">
                        <div class="flex items-center gap-4">
                            <i data-lucide="video" class="w-5 h-5 text-gray-400"></i>
                            <div>
                                <h4 class="font-medium text-gray-900">Interview Portal</h4>
                                <p class="text-xs text-gray-500 mt-0.5">Streamline your hiring and scheduling process.</p>
                            </div>
                        </div>
                        <div class="text-right">
                            <span class="block font-medium text-gray-900">+₹40</span>
                            <span class="text-[10px] text-gray-500">/emp/mo</span>
                        </div>
                    </div>

                    <div class="flex items-center justify-between p-5 border-b border-gray-200 hover:bg-gray-50 transition-colors">
                        <div class="flex items-center gap-4">
                            <i data-lucide="message-square" class="w-5 h-5 text-gray-400"></i>
                            <div>
                                <h4 class="font-medium text-gray-900">Messaging Tool</h4>
                                <p class="text-xs text-gray-500 mt-0.5">Internal chat and secure communication module.</p>
                            </div>
                        </div>
                        <div class="text-right">
                            <span class="block font-medium text-gray-900">+₹30</span>
                            <span class="text-[10px] text-gray-500">/emp/mo</span>
                        </div>
                    </div>

                    <div class="flex items-center justify-between p-5 hover:bg-gray-50 transition-colors">
                        <div class="flex items-center gap-4">
                            <i data-lucide="hard-drive" class="w-5 h-5 text-gray-400"></i>
                            <div>
                                <h4 class="font-medium text-gray-900">IT Inventory Management Tool</h4>
                                <p class="text-xs text-gray-500 mt-0.5">Track laptops, assets, and software licenses.</p>
                            </div>
                        </div>
                        <div class="text-right">
                            <span class="block font-medium text-gray-900">+₹50</span>
                            <span class="text-[10px] text-gray-500">/emp/mo</span>
                        </div>
                    </div>

                </div>
            </div>

        </div>
    </section>

    <!-- Expanded Comparison Table -->
    <section class="px-4 py-24 bg-white border-t border-gray-100">
        <div class="max-w-[1000px] mx-auto">
            <div class="text-center mb-16">
                <h2 class="text-4xl font-bold tracking-tight text-gray-900 mb-4">Compare features</h2>
            </div>

            <div class="overflow-x-auto">
                <table class="w-full text-left border-collapse min-w-[800px]">
                    <thead>
                        <tr>
                            <th class="p-4 border-b border-gray-200 text-sm font-medium text-transparent w-[40%]">Features</th>
                            <th class="p-4 border-b border-gray-200 text-sm font-bold text-gray-900 text-center w-[20%]">Essential</th>
                            <th class="p-4 border-b border-gray-200 text-sm font-bold text-gray-900 text-center w-[20%]">Growth</th>
                            <th class="p-4 border-b border-gray-200 text-sm font-bold text-gray-900 text-center w-[20%]">Enterprise</th>
                        </tr>
                    </thead>
                    <tbody class="text-[13px] text-gray-800">
                        <!-- Category: Overview -->
                        <tr class="bg-[#F3F4F6]">
                            <td colspan="4" class="px-4 py-3 font-semibold text-gray-900">Overview</td>
                        </tr>
                        <tr class="border-b border-gray-100 hover:bg-gray-50">
                            <td class="px-4 py-4 font-medium flex items-center gap-1">Dashboards <i data-lucide="info" class="w-3 h-3 text-gray-400"></i></td>
                            <td class="px-4 py-4 text-center">2</td>
                            <td class="px-4 py-4 text-center">6</td>
                            <td class="px-4 py-4 text-center">Unlimited</td>
                        </tr>
                        <tr class="border-b border-gray-100 hover:bg-gray-50">
                            <td class="px-4 py-4 font-medium">Core HRM Software</td>
                            <td class="px-4 py-4 text-center"><i data-lucide="check" class="w-4 h-4 mx-auto text-gray-900"></i></td>
                            <td class="px-4 py-4 text-center"><i data-lucide="check" class="w-4 h-4 mx-auto text-gray-900"></i></td>
                            <td class="px-4 py-4 text-center"><i data-lucide="check" class="w-4 h-4 mx-auto text-gray-900"></i></td>
                        </tr>
                        <tr class="border-b border-gray-100 hover:bg-gray-50">
                            <td class="px-4 py-4 font-medium">Leave Engine</td>
                            <td class="px-4 py-4 text-center"><i data-lucide="check" class="w-4 h-4 mx-auto text-gray-900"></i></td>
                            <td class="px-4 py-4 text-center"><i data-lucide="check" class="w-4 h-4 mx-auto text-gray-900"></i></td>
                            <td class="px-4 py-4 text-center"><i data-lucide="check" class="w-4 h-4 mx-auto text-gray-900"></i></td>
                        </tr>

                        <!-- Category: Standard Components -->
                        <tr class="bg-[#F3F4F6]">
                            <td colspan="4" class="px-4 py-3 font-semibold text-gray-900">Standard Components</td>
                        </tr>
                        <tr class="border-b border-gray-100 hover:bg-gray-50">
                            <td class="px-4 py-4 font-medium">Data Integrity</td>
                            <td class="px-4 py-4 text-center"><i data-lucide="check" class="w-4 h-4 mx-auto text-gray-900"></i></td>
                            <td class="px-4 py-4 text-center"><i data-lucide="check" class="w-4 h-4 mx-auto text-gray-900"></i></td>
                            <td class="px-4 py-4 text-center"><i data-lucide="check" class="w-4 h-4 mx-auto text-gray-900"></i></td>
                        </tr>
                        <tr class="border-b border-gray-100 hover:bg-gray-50">
                            <td class="px-4 py-4 font-medium">Employee Directory</td>
                            <td class="px-4 py-4 text-center"><i data-lucide="check" class="w-4 h-4 mx-auto text-gray-900"></i></td>
                            <td class="px-4 py-4 text-center"><i data-lucide="check" class="w-4 h-4 mx-auto text-gray-900"></i></td>
                            <td class="px-4 py-4 text-center"><i data-lucide="check" class="w-4 h-4 mx-auto text-gray-900"></i></td>
                        </tr>
                        <tr class="border-b border-gray-100 hover:bg-gray-50">
                            <td class="px-4 py-4 font-medium">Document Storage</td>
                            <td class="px-4 py-4 text-center"><i data-lucide="check" class="w-4 h-4 mx-auto text-gray-900"></i></td>
                            <td class="px-4 py-4 text-center"><i data-lucide="check" class="w-4 h-4 mx-auto text-gray-900"></i></td>
                            <td class="px-4 py-4 text-center"><i data-lucide="check" class="w-4 h-4 mx-auto text-gray-900"></i></td>
                        </tr>
                        <tr class="border-b border-gray-100 hover:bg-gray-50">
                            <td class="px-4 py-4 font-medium">Basic Reporting</td>
                            <td class="px-4 py-4 text-center"><i data-lucide="check" class="w-4 h-4 mx-auto text-gray-900"></i></td>
                            <td class="px-4 py-4 text-center"><i data-lucide="check" class="w-4 h-4 mx-auto text-gray-900"></i></td>
                            <td class="px-4 py-4 text-center"><i data-lucide="check" class="w-4 h-4 mx-auto text-gray-900"></i></td>
                        </tr>
                        <tr class="border-b border-gray-100 hover:bg-gray-50">
                            <td class="px-4 py-4 font-medium flex items-center gap-1">Expense Tracking <i data-lucide="info" class="w-3 h-3 text-gray-400"></i></td>
                            <td class="px-4 py-4 text-center"><span class="text-gray-300">—</span></td>
                            <td class="px-4 py-4 text-center"><i data-lucide="check" class="w-4 h-4 mx-auto text-gray-900"></i></td>
                            <td class="px-4 py-4 text-center"><i data-lucide="check" class="w-4 h-4 mx-auto text-gray-900"></i></td>
                        </tr>

                        <!-- Category: Premium Components -->
                        <tr class="bg-[#F3F4F6]">
                            <td colspan="4" class="px-4 py-3 font-semibold text-gray-900">Premium Components</td>
                        </tr>
                        <tr class="border-b border-gray-100 hover:bg-gray-50">
                            <td class="px-4 py-4 font-medium">Automatic Payroll Processing</td>
                            <td class="px-4 py-4 text-center"><span class="text-gray-300">—</span></td>
                            <td class="px-4 py-4 text-center"><i data-lucide="check" class="w-4 h-4 mx-auto text-gray-900"></i></td>
                            <td class="px-4 py-4 text-center"><i data-lucide="check" class="w-4 h-4 mx-auto text-gray-900"></i></td>
                        </tr>
                        <tr class="border-b border-gray-100 hover:bg-gray-50">
                            <td class="px-4 py-4 font-medium">Automation Emails</td>
                            <td class="px-4 py-4 text-center"><span class="text-gray-300">—</span></td>
                            <td class="px-4 py-4 text-center"><i data-lucide="check" class="w-4 h-4 mx-auto text-gray-900"></i></td>
                            <td class="px-4 py-4 text-center"><i data-lucide="check" class="w-4 h-4 mx-auto text-gray-900"></i></td>
                        </tr>
                        <tr class="border-b border-gray-100 hover:bg-gray-50">
                            <td class="px-4 py-4 font-medium">Automatic Biometric Sync</td>
                            <td class="px-4 py-4 text-center"><span class="text-gray-300">—</span></td>
                            <td class="px-4 py-4 text-center"><i data-lucide="check" class="w-4 h-4 mx-auto text-gray-900"></i></td>
                            <td class="px-4 py-4 text-center"><i data-lucide="check" class="w-4 h-4 mx-auto text-gray-900"></i></td>
                        </tr>
                        <tr class="border-b border-gray-100 hover:bg-gray-50">
                            <td class="px-4 py-4 font-medium">Shift Scheduling</td>
                            <td class="px-4 py-4 text-center"><span class="text-gray-300">—</span></td>
                            <td class="px-4 py-4 text-center"><i data-lucide="check" class="w-4 h-4 mx-auto text-gray-900"></i></td>
                            <td class="px-4 py-4 text-center"><i data-lucide="check" class="w-4 h-4 mx-auto text-gray-900"></i></td>
                        </tr>

                        <!-- Category: Customization & Branding -->
                        <tr class="bg-[#F3F4F6]">
                            <td colspan="4" class="px-4 py-3 font-semibold text-gray-900">Customization & Branding</td>
                        </tr>
                        <tr class="border-b border-gray-100 hover:bg-gray-50">
                            <td class="px-4 py-4 font-medium flex items-center gap-1">Change on Demand <i data-lucide="info" class="w-3 h-3 text-gray-400"></i></td>
                            <td class="px-4 py-4 text-center text-gray-500">Paid</td>
                            <td class="px-4 py-4 text-center">5 Free</td>
                            <td class="px-4 py-4 text-center">Unlimited</td>
                        </tr>
                        <tr class="border-b border-gray-100 hover:bg-gray-50">
                            <td class="px-4 py-4 font-medium">White-labeling (Your Logo & Name)</td>
                            <td class="px-4 py-4 text-center"><span class="text-gray-300">—</span></td>
                            <td class="px-4 py-4 text-center"><span class="text-gray-300">—</span></td>
                            <td class="px-4 py-4 text-center"><i data-lucide="check" class="w-4 h-4 mx-auto text-gray-900"></i></td>
                        </tr>
                        <tr class="border-b border-gray-100 hover:bg-gray-50">
                            <td class="px-4 py-4 font-medium">Custom Workflows</td>
                            <td class="px-4 py-4 text-center"><span class="text-gray-300">—</span></td>
                            <td class="px-4 py-4 text-center"><span class="text-gray-300">—</span></td>
                            <td class="px-4 py-4 text-center"><i data-lucide="check" class="w-4 h-4 mx-auto text-gray-900"></i></td>
                        </tr>

                        <!-- Category: Community & Support -->
                        <tr class="bg-[#F3F4F6]">
                            <td colspan="4" class="px-4 py-3 font-semibold text-gray-900">Community & Support</td>
                        </tr>
                        <tr class="border-b border-gray-100 hover:bg-gray-50">
                            <td class="px-4 py-4 font-medium">Email Support</td>
                            <td class="px-4 py-4 text-center"><i data-lucide="check" class="w-4 h-4 mx-auto text-gray-900"></i></td>
                            <td class="px-4 py-4 text-center"><i data-lucide="check" class="w-4 h-4 mx-auto text-gray-900"></i></td>
                            <td class="px-4 py-4 text-center"><i data-lucide="check" class="w-4 h-4 mx-auto text-gray-900"></i></td>
                        </tr>
                        <tr class="border-b border-gray-100 hover:bg-gray-50">
                            <td class="px-4 py-4 font-medium">Priority Chat Support</td>
                            <td class="px-4 py-4 text-center"><span class="text-gray-300">—</span></td>
                            <td class="px-4 py-4 text-center"><i data-lucide="check" class="w-4 h-4 mx-auto text-gray-900"></i></td>
                            <td class="px-4 py-4 text-center"><i data-lucide="check" class="w-4 h-4 mx-auto text-gray-900"></i></td>
                        </tr>
                        <tr class="border-b border-gray-100 hover:bg-gray-50">
                            <td class="px-4 py-4 font-medium">Dedicated Account Manager</td>
                            <td class="px-4 py-4 text-center"><span class="text-gray-300">—</span></td>
                            <td class="px-4 py-4 text-center"><span class="text-gray-300">—</span></td>
                            <td class="px-4 py-4 text-center"><i data-lucide="check" class="w-4 h-4 mx-auto text-gray-900"></i></td>
                        </tr>
                        
                    </tbody>
                </table>
            </div>
        </div>
    </section>
"""

# Now write the JS part for the toggle. I'll replace all script block.
# Wait, I can just replace the whole `<script>` block.
script_start = footer_and_scripts.find('<script>')
script_end = footer_and_scripts.find('</script>') + len('</script>')

new_scripts = """<script>
        lucide.createIcons();

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

    </script>"""

footer_and_scripts = footer_and_scripts[:script_start] + new_scripts + footer_and_scripts[script_end:]

final_content = head_and_nav + new_body + footer_and_scripts

with open('d:/project pxp/website/pricing.html', 'w', encoding='utf-8') as f:
    f.write(final_content)
print("Minimalist pricing page redesigned successfully!")
