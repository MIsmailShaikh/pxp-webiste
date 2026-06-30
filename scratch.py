import re

with open('d:/project pxp/website/pricing.html', 'r', encoding='utf-8') as f:
    content = f.read()

nav_end_idx = content.find('</nav>') + len('</nav>')
footer_start_idx = content.find('<!-- Footer -->')

head_and_nav = content[:nav_end_idx]
footer_and_scripts = content[footer_start_idx:]

# Let's inject new styles in the head.
new_styles = """
        /* Pricing Animations */
        @keyframes gradientPulse {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }
        .animate-gradient-pulse {
            background-size: 200% 200%;
            animation: gradientPulse 6s ease infinite;
        }
        
        .modern-slider {
            -webkit-appearance: none;
            width: 100%;
            height: 12px;
            background: #e2e8f0;
            border-radius: 9999px;
            outline: none;
            cursor: pointer;
            box-shadow: inset 0 2px 4px rgba(0,0,0,0.05);
        }
        .modern-slider::-webkit-slider-thumb {
            -webkit-appearance: none;
            appearance: none;
            width: 32px;
            height: 32px;
            border-radius: 50%;
            background: white;
            cursor: pointer;
            box-shadow: 0 4px 10px rgba(0,0,0,0.1), 0 0 0 5px #3b82f6;
            transition: transform 0.2s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        }
        .modern-slider::-webkit-slider-thumb:hover {
            transform: scale(1.15);
        }
        
        /* Glassmorphism for Pricing Cards */
        .glass-card {
            background: rgba(255, 255, 255, 0.7);
            backdrop-filter: blur(20px);
            border: 1px solid rgba(255, 255, 255, 0.5);
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.05);
        }
        
        /* Animated Border for Recommended Card */
        .animated-border-box {
            position: relative;
            background: #fff;
            background-clip: padding-box;
            border: 2px solid transparent;
            border-radius: 24px;
        }
        .animated-border-box::before {
            content: '';
            position: absolute;
            top: 0; right: 0; bottom: 0; left: 0;
            z-index: -1;
            margin: -2px;
            border-radius: inherit;
            background: linear-gradient(45deg, #3b82f6, #8b5cf6, #3b82f6);
            background-size: 200% 200%;
            animation: gradientPulse 3s linear infinite;
        }
"""
head_and_nav = head_and_nav.replace('</style>', new_styles + '\n    </style>')

new_body = """
    <!-- Pricing Hero Section -->
    <div class="relative pt-40 pb-24 overflow-hidden bg-white">
        <!-- Abstract Background Shapes -->
        <div class="absolute top-[-10%] left-[-10%] w-[50%] h-[50%] bg-blue-500/10 rounded-full blur-[120px] pointer-events-none"></div>
        <div class="absolute bottom-[-10%] right-[-10%] w-[50%] h-[50%] bg-purple-500/10 rounded-full blur-[120px] pointer-events-none"></div>

        <div class="max-w-[1400px] mx-auto px-4 md:px-8 text-center relative z-10">
            <div class="inline-flex items-center justify-center p-[1.5px] rounded-full mb-8 overflow-hidden group cursor-default shadow-sm reveal-text">
                <span class="absolute inset-[-1000%] animate-[spinSlow_3s_linear_infinite] bg-[conic-gradient(from_90deg_at_50%_50%,#c084fc_0%,#3b82f6_50%,#c084fc_100%)]"></span>
                <span class="relative bg-white px-4 py-1.5 rounded-full text-xs font-bold uppercase tracking-widest text-gray-800 w-full h-full flex items-center justify-center">
                    Simple & Transparent
                </span>
            </div>
            
            <h1 class="text-5xl md:text-7xl font-bold tracking-tight text-gray-900 mb-6 reveal-text reveal-delay-1 leading-tight">
                Pricing that scales <br class="hidden md:block"> with your ambition.
            </h1>
            <p class="text-xl text-gray-500 max-w-2xl mx-auto reveal-text reveal-delay-2">
                No hidden fees. No surprise charges. Just powerful software designed to help your workforce thrive.
            </p>
        </div>
    </div>

    <!-- Pricing Interactive Section -->
    <section class="px-2 md:px-4 lg:px-6 pb-24 bg-white relative z-20">
        <div class="max-w-[1400px] mx-auto bg-[#F3F5F7] rounded-[40px] md:rounded-[60px] p-4 md:p-8 lg:p-16 relative overflow-hidden shadow-sm">
            
            <!-- Dynamic Slider Box -->
            <div class="max-w-4xl mx-auto bg-white rounded-[32px] p-8 md:p-12 shadow-xl border border-gray-100/50 mb-16 reveal-text reveal-delay-3 relative overflow-visible z-30">
                
                <div class="flex flex-col md:flex-row items-center justify-center gap-6 mb-12">
                    <span class="text-xl md:text-2xl font-medium text-gray-600">Estimate pricing for</span>
                    <div class="relative group">
                        <div class="absolute inset-0 bg-blue-500/20 rounded-2xl blur-lg group-hover:bg-blue-500/30 transition-all duration-300"></div>
                        <input type="number" id="emp-input" value="50" min="10" max="3000" class="relative w-36 text-center text-4xl font-bold text-blue-600 bg-white border-2 border-blue-100 rounded-2xl py-2 focus:outline-none focus:border-blue-500 transition-colors shadow-sm">
                    </div>
                    <span class="text-xl md:text-2xl font-medium text-gray-600">employees</span>
                </div>

                <!-- Slider -->
                <div class="relative max-w-3xl mx-auto pb-4">
                    <!-- The Slide Tag -->
                    <div class="absolute left-[-1rem] top-[-1rem] hidden md:flex animate-float-x z-20">
                        <div class="bg-gray-900 text-white px-4 py-1.5 rounded-full text-sm font-bold shadow-lg flex items-center gap-2">
                            Slide to calculate <i data-lucide="arrow-right" class="w-4 h-4"></i>
                        </div>
                    </div>

                    <div class="w-full relative px-2 md:px-6">
                        <input type="range" id="emp-slider" min="10" max="3000" value="50" step="1" class="modern-slider" style="background: linear-gradient(to right, #3b82f6 1.3%, #e2e8f0 1.3%);">
                        <div class="flex justify-between text-xs font-bold text-gray-400 mt-6 absolute w-full left-0 px-4 md:px-8">
                            <span>10</span>
                            <span>500</span>
                            <span>1,000</span>
                            <span>2,000</span>
                            <span>3,000+</span>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Pricing Cards Grid -->
            <div class="grid grid-cols-1 lg:grid-cols-3 gap-8 relative z-20">
                
                <!-- Essential Card -->
                <div class="bg-white rounded-3xl p-8 border border-gray-100 shadow-sm hover:shadow-xl hover:-translate-y-2 transition-all duration-300 flex flex-col">
                    <h3 class="text-2xl font-bold text-gray-900 mb-2">Essential</h3>
                    <p class="text-sm text-gray-500 mb-6 h-10">Perfect for small teams needing core HR and payroll automation.</p>
                    
                    <div class="mb-8">
                        <div class="flex items-end gap-1 mb-2">
                            <span class="text-5xl font-black text-gray-900 tracking-tight">₹<span id="price-essential" class="tabular-nums">2,495</span></span>
                            <span class="text-gray-500 mb-2 font-medium">/mo</span>
                        </div>
                        <div class="text-sm text-blue-600 font-medium bg-blue-50 inline-block px-3 py-1 rounded-full">₹45/employee above 50</div>
                    </div>

                    <ul class="space-y-4 mb-8 text-sm text-gray-600 font-medium flex-grow">
                        <li class="flex items-start gap-3"><i data-lucide="check-circle-2" class="w-5 h-5 text-blue-500 shrink-0"></i> Complete payroll processing</li>
                        <li class="flex items-start gap-3"><i data-lucide="check-circle-2" class="w-5 h-5 text-blue-500 shrink-0"></i> Basic leave management</li>
                        <li class="flex items-start gap-3"><i data-lucide="check-circle-2" class="w-5 h-5 text-blue-500 shrink-0"></i> Employee self-service portal</li>
                        <li class="flex items-start gap-3"><i data-lucide="minus" class="w-5 h-5 text-gray-300 shrink-0"></i> Advanced attendance tracking</li>
                        <li class="flex items-start gap-3"><i data-lucide="minus" class="w-5 h-5 text-gray-300 shrink-0"></i> Performance management</li>
                    </ul>
                    
                    <button class="w-full py-4 rounded-xl border border-gray-200 text-gray-900 font-bold hover:bg-gray-50 transition-colors mt-auto">Start Free Trial</button>
                </div>

                <!-- Growth Card (Recommended) -->
                <div class="animated-border-box p-8 shadow-2xl relative transform lg:-translate-y-8 flex flex-col z-30">
                    <div class="absolute -top-4 left-1/2 -translate-x-1/2 bg-gradient-to-r from-blue-600 to-purple-600 text-white px-6 py-1.5 rounded-full text-sm font-bold uppercase tracking-widest shadow-md whitespace-nowrap">
                        Most Popular
                    </div>
                    
                    <h3 class="text-2xl font-bold text-gray-900 mb-2">Growth</h3>
                    <p class="text-sm text-gray-500 mb-6 h-10">Everything you need to scale your operations securely and efficiently.</p>
                    
                    <div class="mb-8">
                        <div class="flex items-end gap-1 mb-2">
                            <span class="text-5xl font-black text-gray-900 tracking-tight">₹<span id="price-growth" class="tabular-nums">4,495</span></span>
                            <span class="text-gray-500 mb-2 font-medium">/mo</span>
                        </div>
                        <div class="text-sm text-purple-600 font-medium bg-purple-50 inline-block px-3 py-1 rounded-full">₹85/employee above 50</div>
                    </div>

                    <ul class="space-y-4 mb-8 text-sm text-gray-700 font-medium flex-grow">
                        <li class="flex items-start gap-3"><i data-lucide="check-circle-2" class="w-5 h-5 text-purple-600 shrink-0"></i> Everything in Essential</li>
                        <li class="flex items-start gap-3"><i data-lucide="check-circle-2" class="w-5 h-5 text-purple-600 shrink-0"></i> Advanced attendance & shifts</li>
                        <li class="flex items-start gap-3"><i data-lucide="check-circle-2" class="w-5 h-5 text-purple-600 shrink-0"></i> Geo-fencing & live tracking</li>
                        <li class="flex items-start gap-3"><i data-lucide="check-circle-2" class="w-5 h-5 text-purple-600 shrink-0"></i> Multi-level approval workflows</li>
                        <li class="flex items-start gap-3"><i data-lucide="sparkles" class="w-5 h-5 text-blue-500 shrink-0"></i> Priority email & chat support</li>
                    </ul>
                    
                    <button class="w-full py-4 rounded-xl bg-gray-900 text-white font-bold hover:bg-gray-800 transition-colors shadow-lg mt-auto">Get Started Now</button>
                </div>

                <!-- Premium Card -->
                <div class="bg-[#131313] rounded-3xl p-8 shadow-xl text-white flex flex-col relative overflow-hidden border border-white/10 hover:-translate-y-2 transition-transform duration-300">
                    <!-- Subtle Glow -->
                    <div class="absolute -top-24 -right-24 w-48 h-48 bg-purple-500/30 rounded-full blur-[60px]"></div>

                    <h3 class="text-2xl font-bold mb-2">Enterprise</h3>
                    <p class="text-sm text-gray-400 mb-6 h-10">Bespoke features, dedicated support, and enterprise-grade security.</p>
                    
                    <div class="mb-8 h-[76px] flex items-end">
                        <span class="text-5xl font-black tracking-tight bg-gradient-to-r from-white to-gray-400 bg-clip-text text-transparent">Custom</span>
                    </div>

                    <ul class="space-y-4 mb-8 text-sm text-gray-300 font-medium flex-grow">
                        <li class="flex items-start gap-3"><i data-lucide="check-circle-2" class="w-5 h-5 text-white/50 shrink-0"></i> Everything in Growth</li>
                        <li class="flex items-start gap-3"><i data-lucide="check-circle-2" class="w-5 h-5 text-white/50 shrink-0"></i> Custom API Integrations</li>
                        <li class="flex items-start gap-3"><i data-lucide="check-circle-2" class="w-5 h-5 text-white/50 shrink-0"></i> Single Sign-On (SSO)</li>
                        <li class="flex items-start gap-3"><i data-lucide="check-circle-2" class="w-5 h-5 text-white/50 shrink-0"></i> Dedicated Account Manager</li>
                        <li class="flex items-start gap-3"><i data-lucide="check-circle-2" class="w-5 h-5 text-white/50 shrink-0"></i> On-premise deployment option</li>
                    </ul>
                    
                    <button class="w-full py-4 rounded-xl bg-white text-black font-bold hover:bg-gray-200 transition-colors mt-auto">Contact Sales</button>
                </div>

            </div>
        </div>
    </section>

    <!-- Feature Comparison Table -->
    <section class="px-4 py-24 bg-white relative z-10">
        <div class="max-w-[1200px] mx-auto">
            <div class="text-center mb-16">
                <h2 class="text-3xl md:text-5xl font-bold tracking-tight text-gray-900 mb-4">Compare all features</h2>
                <p class="text-lg text-gray-500">Find the perfect plan for your organizational needs.</p>
            </div>

            <div class="overflow-x-auto pb-8">
                <table class="w-full text-left border-collapse min-w-[800px]">
                    <thead>
                        <tr>
                            <th class="p-4 border-b-2 border-gray-200 text-lg font-bold text-gray-900 w-1/3">Features</th>
                            <th class="p-4 border-b-2 border-gray-200 text-lg font-bold text-gray-900 w-2/9">Essential</th>
                            <th class="p-4 border-b-2 border-gray-200 text-lg font-bold text-blue-600 w-2/9">Growth</th>
                            <th class="p-4 border-b-2 border-gray-200 text-lg font-bold text-gray-900 w-2/9">Enterprise</th>
                        </tr>
                    </thead>
                    <tbody class="text-sm">
                        <!-- Category 1 -->
                        <tr>
                            <td colspan="4" class="p-4 pt-8 pb-2 text-xs font-bold uppercase tracking-wider text-gray-400 bg-white">Core HR & Payroll</td>
                        </tr>
                        <tr class="hover:bg-gray-50 transition-colors border-b border-gray-100">
                            <td class="p-4 text-gray-700 font-medium">Automated Payroll Processing</td>
                            <td class="p-4"><i data-lucide="check" class="w-5 h-5 text-gray-400"></i></td>
                            <td class="p-4"><i data-lucide="check" class="w-5 h-5 text-blue-600"></i></td>
                            <td class="p-4"><i data-lucide="check" class="w-5 h-5 text-gray-900"></i></td>
                        </tr>
                        <tr class="hover:bg-gray-50 transition-colors border-b border-gray-100">
                            <td class="p-4 text-gray-700 font-medium">Statutory Compliance (PF, PT, TDS)</td>
                            <td class="p-4"><i data-lucide="check" class="w-5 h-5 text-gray-400"></i></td>
                            <td class="p-4"><i data-lucide="check" class="w-5 h-5 text-blue-600"></i></td>
                            <td class="p-4"><i data-lucide="check" class="w-5 h-5 text-gray-900"></i></td>
                        </tr>
                        <tr class="hover:bg-gray-50 transition-colors border-b border-gray-100">
                            <td class="p-4 text-gray-700 font-medium">Employee Self Service Portal</td>
                            <td class="p-4"><i data-lucide="check" class="w-5 h-5 text-gray-400"></i></td>
                            <td class="p-4"><i data-lucide="check" class="w-5 h-5 text-blue-600"></i></td>
                            <td class="p-4"><i data-lucide="check" class="w-5 h-5 text-gray-900"></i></td>
                        </tr>
                        
                        <!-- Category 2 -->
                        <tr>
                            <td colspan="4" class="p-4 pt-8 pb-2 text-xs font-bold uppercase tracking-wider text-gray-400 bg-white">Time & Attendance</td>
                        </tr>
                        <tr class="hover:bg-gray-50 transition-colors border-b border-gray-100">
                            <td class="p-4 text-gray-700 font-medium">Leave Management</td>
                            <td class="p-4"><i data-lucide="check" class="w-5 h-5 text-gray-400"></i></td>
                            <td class="p-4"><i data-lucide="check" class="w-5 h-5 text-blue-600"></i></td>
                            <td class="p-4"><i data-lucide="check" class="w-5 h-5 text-gray-900"></i></td>
                        </tr>
                        <tr class="hover:bg-gray-50 transition-colors border-b border-gray-100">
                            <td class="p-4 text-gray-700 font-medium">Biometric Integration</td>
                            <td class="p-4"><i data-lucide="minus" class="w-5 h-5 text-gray-300"></i></td>
                            <td class="p-4"><i data-lucide="check" class="w-5 h-5 text-blue-600"></i></td>
                            <td class="p-4"><i data-lucide="check" class="w-5 h-5 text-gray-900"></i></td>
                        </tr>
                        <tr class="hover:bg-gray-50 transition-colors border-b border-gray-100">
                            <td class="p-4 text-gray-700 font-medium">Geo-fencing & Mobile Tracking</td>
                            <td class="p-4"><i data-lucide="minus" class="w-5 h-5 text-gray-300"></i></td>
                            <td class="p-4"><i data-lucide="check" class="w-5 h-5 text-blue-600"></i></td>
                            <td class="p-4"><i data-lucide="check" class="w-5 h-5 text-gray-900"></i></td>
                        </tr>

                        <!-- Category 3 -->
                        <tr>
                            <td colspan="4" class="p-4 pt-8 pb-2 text-xs font-bold uppercase tracking-wider text-gray-400 bg-white">Security & Support</td>
                        </tr>
                        <tr class="hover:bg-gray-50 transition-colors border-b border-gray-100">
                            <td class="p-4 text-gray-700 font-medium">Data Encryption</td>
                            <td class="p-4">Standard</td>
                            <td class="p-4 text-blue-600 font-bold">Bank-Grade</td>
                            <td class="p-4 font-bold text-gray-900">Bank-Grade + Isolated DB</td>
                        </tr>
                        <tr class="hover:bg-gray-50 transition-colors border-b border-gray-100">
                            <td class="p-4 text-gray-700 font-medium">Support Channel</td>
                            <td class="p-4">Email</td>
                            <td class="p-4 font-bold text-blue-600">Email & Priority Chat</td>
                            <td class="p-4 font-bold text-gray-900">Dedicated 24/7 Rep</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </section>

    <!-- FAQ Section -->
    <section class="px-4 py-24 bg-[#F3F5F7] border-y border-gray-200">
        <div class="max-w-[800px] mx-auto">
            <div class="text-center mb-16">
                <h2 class="text-3xl md:text-5xl font-bold tracking-tight text-gray-900 mb-4">Frequently Asked Questions</h2>
            </div>
            
            <div class="space-y-4">
                <!-- FAQ Item 1 -->
                <div class="bg-white border border-gray-200 rounded-2xl p-6 shadow-sm hover:shadow-md transition-shadow">
                    <h3 class="text-lg font-bold text-gray-900 mb-2">Can I switch plans later?</h3>
                    <p class="text-gray-600 leading-relaxed text-sm">Absolutely. You can upgrade or downgrade your plan at any time. Prorated charges will automatically be applied to your next billing cycle.</p>
                </div>
                <!-- FAQ Item 2 -->
                <div class="bg-white border border-gray-200 rounded-2xl p-6 shadow-sm hover:shadow-md transition-shadow">
                    <h3 class="text-lg font-bold text-gray-900 mb-2">How do you count 'employees'?</h3>
                    <p class="text-gray-600 leading-relaxed text-sm">We only charge for active employees enrolled in the system for that billing month. Suspended or past employees kept for record-keeping are totally free.</p>
                </div>
                <!-- FAQ Item 3 -->
                <div class="bg-white border border-gray-200 rounded-2xl p-6 shadow-sm hover:shadow-md transition-shadow">
                    <h3 class="text-lg font-bold text-gray-900 mb-2">Do you offer on-premise deployment?</h3>
                    <p class="text-gray-600 leading-relaxed text-sm">Yes, on-premise and dedicated cloud deployments are available under our Enterprise custom plan. Contact our sales team to arrange a technical consultation.</p>
                </div>
            </div>
        </div>
    </section>
"""

# Let's replace the JS script color logic for the slider as well.
# It used #0d9488 (teal) before. We want to use #3b82f6 (blue).
footer_and_scripts = footer_and_scripts.replace('#0d9488', '#3b82f6')

final_content = head_and_nav + new_body + footer_and_scripts

with open('d:/project pxp/website/pricing.html', 'w', encoding='utf-8') as f:
    f.write(final_content)
print("Pricing page redesigned successfully!")
