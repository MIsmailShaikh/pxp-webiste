import os
import re

base_file = r"d:\project pxp\website\privacy-policy.html"
with open(base_file, 'r', encoding='utf-8') as f:
    base_html = f.read()

# Extract header (up to HERO SECTION) and footer (from FOOTER to end)
header_match = re.search(r'(.*?)<!-- HERO SECTION -->', base_html, re.DOTALL)
footer_match = re.search(r'<!-- FOOTER -->(.*)', base_html, re.DOTALL)

if not header_match or not footer_match:
    print("Could not find header or footer in base file")
    exit(1)

header_html = header_match.group(1)
footer_html = "<!-- FOOTER -->" + footer_match.group(1)

# Fix title in header
header_html = header_html.replace("<title>Privacy Policy - PeopleXplus</title>", "<title>{page_title} - PeopleXplus</title>")

# 1. Documentation Page
doc_content = """
    <!-- HERO SECTION -->
    <div class="pt-32 pb-16 md:pt-40 md:pb-24 bg-gradient-to-br from-gray-900 to-black text-white relative overflow-hidden">
        <div class="absolute top-[-20%] left-[-10%] w-[50%] h-[50%] bg-blue-600 rounded-full blur-[120px] opacity-30"></div>
        <div class="absolute bottom-[-10%] right-[-10%] w-[50%] h-[50%] bg-purple-600 rounded-full blur-[120px] opacity-30"></div>
        <div class="max-w-7xl mx-auto px-4 relative z-10 text-center">
            <h1 class="text-4xl md:text-5xl font-bold mb-4">Documentation</h1>
            <p class="text-gray-400 max-w-2xl mx-auto text-lg">Everything you need to set up, integrate, and master PeopleXplus.</p>
            
            <div class="max-w-xl mx-auto mt-8 relative">
                <i data-lucide="search" class="absolute left-4 top-1/2 -translate-y-1/2 text-gray-400 w-5 h-5"></i>
                <input type="text" placeholder="Search documentation..." class="w-full bg-white/10 border border-white/20 rounded-xl py-3 pl-12 pr-4 text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-blue-500 backdrop-blur-sm transition-all">
            </div>
        </div>
    </div>

    <!-- MAIN CONTENT AREA -->
    <div class="max-w-7xl mx-auto px-4 py-12 flex flex-col md:flex-row gap-8 lg:gap-16 w-full flex-grow">
        <!-- SIDEBAR NAVIGATION -->
        <div class="w-full md:w-64 flex-shrink-0">
            <div class="sticky top-32 flex flex-col gap-6">
                
                <div>
                    <h4 class="text-xs font-bold text-gray-400 uppercase tracking-wider mb-3 px-2">Getting Started</h4>
                    <div class="flex flex-col gap-1">
                        <a href="#" class="px-3 py-2 rounded-lg text-sm font-semibold transition-colors bg-blue-50 text-blue-700">Introduction</a>
                        <a href="#" class="px-3 py-2 rounded-lg text-sm font-medium transition-colors text-gray-600 hover:bg-gray-50">Quick Start Guide</a>
                        <a href="#" class="px-3 py-2 rounded-lg text-sm font-medium transition-colors text-gray-600 hover:bg-gray-50">System Requirements</a>
                    </div>
                </div>

                <div>
                    <h4 class="text-xs font-bold text-gray-400 uppercase tracking-wider mb-3 px-2">Workforce OS</h4>
                    <div class="flex flex-col gap-1">
                        <a href="#" class="px-3 py-2 rounded-lg text-sm font-medium transition-colors text-gray-600 hover:bg-gray-50">Employee Onboarding</a>
                        <a href="#" class="px-3 py-2 rounded-lg text-sm font-medium transition-colors text-gray-600 hover:bg-gray-50">Shift Management</a>
                        <a href="#" class="px-3 py-2 rounded-lg text-sm font-medium transition-colors text-gray-600 hover:bg-gray-50">Leave Policies</a>
                    </div>
                </div>

                <div>
                    <h4 class="text-xs font-bold text-gray-400 uppercase tracking-wider mb-3 px-2">Payroll Engine</h4>
                    <div class="flex flex-col gap-1">
                        <a href="#" class="px-3 py-2 rounded-lg text-sm font-medium transition-colors text-gray-600 hover:bg-gray-50">Tax Configuration</a>
                        <a href="#" class="px-3 py-2 rounded-lg text-sm font-medium transition-colors text-gray-600 hover:bg-gray-50">Running Payroll</a>
                        <a href="#" class="px-3 py-2 rounded-lg text-sm font-medium transition-colors text-gray-600 hover:bg-gray-50">Payslip Generation</a>
                    </div>
                </div>

                <div>
                    <h4 class="text-xs font-bold text-gray-400 uppercase tracking-wider mb-3 px-2">Developers</h4>
                    <div class="flex flex-col gap-1">
                        <a href="#" class="px-3 py-2 rounded-lg text-sm font-medium transition-colors text-gray-600 hover:bg-gray-50">API Authentication</a>
                        <a href="#" class="px-3 py-2 rounded-lg text-sm font-medium transition-colors text-gray-600 hover:bg-gray-50">Webhooks</a>
                        <a href="#" class="px-3 py-2 rounded-lg text-sm font-medium transition-colors text-gray-600 hover:bg-gray-50">Rate Limits</a>
                    </div>
                </div>
            </div>
        </div>

        <!-- DOC CONTENT -->
        <div class="w-full max-w-3xl">
            <h2 class="text-3xl font-bold text-gray-900 mb-6">Introduction to PeopleXplus</h2>
            
            <div class="prose prose-blue max-w-none text-gray-600 space-y-6">
                <p class="text-lg leading-relaxed">
                    Welcome to the official PeopleXplus documentation. Our platform is designed to streamline your entire HR, workforce, and payroll operations into one unified ecosystem.
                </p>

                <div class="bg-blue-50 border border-blue-100 rounded-2xl p-6 my-8">
                    <h4 class="text-blue-900 font-semibold mb-2 flex items-center gap-2">
                        <i data-lucide="info" class="w-5 h-5 text-blue-600"></i> Note for Developers
                    </h4>
                    <p class="text-sm text-blue-800 leading-relaxed m-0">
                        If you are looking to integrate your existing systems with PeopleXplus, please jump straight to the <a href="#" class="underline font-semibold hover:text-blue-600">API Documentation</a> section. Our RESTful API allows you to programmatically manage employees, payroll, and access logs.
                    </p>
                </div>

                <h3 class="text-xl font-bold text-gray-900 mt-10 mb-4">Core Components</h3>
                
                <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mt-6">
                    <div class="border border-gray-200 rounded-2xl p-6 hover:shadow-lg transition-shadow cursor-pointer group">
                        <div class="w-10 h-10 rounded-lg bg-emerald-100 text-emerald-600 flex items-center justify-center mb-4 group-hover:scale-110 transition-transform">
                            <i data-lucide="users" class="w-5 h-5"></i>
                        </div>
                        <h4 class="font-bold text-gray-900 mb-2">Workforce OS</h4>
                        <p class="text-sm text-gray-500">Manage employee lifecycles, shifts, and leave tracking.</p>
                    </div>
                    
                    <div class="border border-gray-200 rounded-2xl p-6 hover:shadow-lg transition-shadow cursor-pointer group">
                        <div class="w-10 h-10 rounded-lg bg-indigo-100 text-indigo-600 flex items-center justify-center mb-4 group-hover:scale-110 transition-transform">
                            <i data-lucide="calculator" class="w-5 h-5"></i>
                        </div>
                        <h4 class="font-bold text-gray-900 mb-2">Payroll Engine</h4>
                        <p class="text-sm text-gray-500">Automate salary processing, tax deductions, and compliance.</p>
                    </div>
                </div>

                <h3 class="text-xl font-bold text-gray-900 mt-10 mb-4">Next Steps</h3>
                <p>
                    Ready to dive in? Head over to the <a href="#" class="text-blue-600 hover:underline">Quick Start Guide</a> to learn how to set up your first organization and add your first employee.
                </p>
            </div>
            
            <!-- Pagination / Next Prev -->
            <div class="border-t border-gray-200 mt-12 pt-8 flex justify-between items-center">
                <div></div> <!-- Empty for flex spacing if no previous -->
                <a href="#" class="flex flex-col items-end text-right group">
                    <span class="text-sm text-gray-500 mb-1">Next up</span>
                    <span class="text-blue-600 font-semibold flex items-center gap-2 group-hover:text-blue-700">
                        Quick Start Guide <i data-lucide="arrow-right" class="w-4 h-4 group-hover:translate-x-1 transition-transform"></i>
                    </span>
                </a>
            </div>
        </div>
    </div>
"""

# 2. Tutorial Page
tutorial_content = """
    <!-- HERO SECTION -->
    <div class="pt-32 pb-16 md:pt-40 md:pb-24 bg-gradient-to-br from-gray-900 to-black text-white relative overflow-hidden">
        <div class="absolute top-[-20%] left-[-10%] w-[50%] h-[50%] bg-blue-600 rounded-full blur-[120px] opacity-30"></div>
        <div class="absolute bottom-[-10%] right-[-10%] w-[50%] h-[50%] bg-purple-600 rounded-full blur-[120px] opacity-30"></div>
        <div class="max-w-7xl mx-auto px-4 relative z-10 text-center">
            <h1 class="text-4xl md:text-5xl font-bold mb-4">Video Tutorials</h1>
            <p class="text-gray-400 max-w-2xl mx-auto text-lg">Learn how to maximize your efficiency with step-by-step video guides.</p>
        </div>
    </div>

    <!-- MAIN CONTENT AREA -->
    <div class="max-w-7xl mx-auto px-4 py-16 flex-grow">
        
        <!-- Filter/Tabs -->
        <div class="flex flex-wrap justify-center gap-2 mb-12">
            <button class="px-6 py-2.5 rounded-full bg-black text-white text-sm font-semibold shadow-md">All Videos</button>
            <button class="px-6 py-2.5 rounded-full bg-gray-100 text-gray-600 text-sm font-medium hover:bg-gray-200 transition-colors">Getting Started</button>
            <button class="px-6 py-2.5 rounded-full bg-gray-100 text-gray-600 text-sm font-medium hover:bg-gray-200 transition-colors">Payroll</button>
            <button class="px-6 py-2.5 rounded-full bg-gray-100 text-gray-600 text-sm font-medium hover:bg-gray-200 transition-colors">Admin Tools</button>
        </div>

        <!-- Video Grid -->
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
            
            <!-- Card 1 -->
            <div class="group cursor-pointer">
                <div class="relative w-full aspect-video bg-gray-900 rounded-2xl overflow-hidden mb-4 shadow-lg shadow-black/5">
                    <!-- Placeholder Image -->
                    <div class="absolute inset-0 bg-gradient-to-tr from-blue-900 to-indigo-800 opacity-80 group-hover:scale-105 transition-transform duration-500"></div>
                    <!-- Play Button Overlay -->
                    <div class="absolute inset-0 flex items-center justify-center">
                        <div class="w-14 h-14 rounded-full bg-white/20 backdrop-blur-md flex items-center justify-center border border-white/30 group-hover:bg-white group-hover:text-black transition-all">
                            <i data-lucide="play" class="w-6 h-6 ml-1 text-white group-hover:text-blue-600"></i>
                        </div>
                    </div>
                    <span class="absolute bottom-3 right-3 bg-black/70 backdrop-blur-sm text-white text-xs font-medium px-2 py-1 rounded">04:20</span>
                </div>
                <h3 class="text-lg font-bold text-gray-900 mb-1 group-hover:text-blue-600 transition-colors">Platform Overview</h3>
                <p class="text-sm text-gray-500">A quick 4-minute tour of the main dashboard and features.</p>
            </div>

            <!-- Card 2 -->
            <div class="group cursor-pointer">
                <div class="relative w-full aspect-video bg-gray-900 rounded-2xl overflow-hidden mb-4 shadow-lg shadow-black/5">
                    <div class="absolute inset-0 bg-gradient-to-tr from-emerald-900 to-teal-800 opacity-80 group-hover:scale-105 transition-transform duration-500"></div>
                    <div class="absolute inset-0 flex items-center justify-center">
                        <div class="w-14 h-14 rounded-full bg-white/20 backdrop-blur-md flex items-center justify-center border border-white/30 group-hover:bg-white group-hover:text-black transition-all">
                            <i data-lucide="play" class="w-6 h-6 ml-1 text-white group-hover:text-blue-600"></i>
                        </div>
                    </div>
                    <span class="absolute bottom-3 right-3 bg-black/70 backdrop-blur-sm text-white text-xs font-medium px-2 py-1 rounded">12:15</span>
                </div>
                <h3 class="text-lg font-bold text-gray-900 mb-1 group-hover:text-blue-600 transition-colors">Running Your First Payroll</h3>
                <p class="text-sm text-gray-500">Step-by-step guide to processing salary and generating slips.</p>
            </div>

            <!-- Card 3 -->
            <div class="group cursor-pointer">
                <div class="relative w-full aspect-video bg-gray-900 rounded-2xl overflow-hidden mb-4 shadow-lg shadow-black/5">
                    <div class="absolute inset-0 bg-gradient-to-tr from-purple-900 to-fuchsia-800 opacity-80 group-hover:scale-105 transition-transform duration-500"></div>
                    <div class="absolute inset-0 flex items-center justify-center">
                        <div class="w-14 h-14 rounded-full bg-white/20 backdrop-blur-md flex items-center justify-center border border-white/30 group-hover:bg-white group-hover:text-black transition-all">
                            <i data-lucide="play" class="w-6 h-6 ml-1 text-white group-hover:text-blue-600"></i>
                        </div>
                    </div>
                    <span class="absolute bottom-3 right-3 bg-black/70 backdrop-blur-sm text-white text-xs font-medium px-2 py-1 rounded">08:45</span>
                </div>
                <h3 class="text-lg font-bold text-gray-900 mb-1 group-hover:text-blue-600 transition-colors">Setting up Shift Policies</h3>
                <p class="text-sm text-gray-500">Learn how to configure complex shift timings and rotations.</p>
            </div>

        </div>
    </div>
"""

# 3. Support Page
support_content = """
    <!-- HERO SECTION -->
    <div class="pt-32 pb-16 md:pt-40 md:pb-24 bg-gradient-to-br from-gray-900 to-black text-white relative overflow-hidden">
        <div class="absolute top-[-20%] left-[-10%] w-[50%] h-[50%] bg-blue-600 rounded-full blur-[120px] opacity-30"></div>
        <div class="absolute bottom-[-10%] right-[-10%] w-[50%] h-[50%] bg-purple-600 rounded-full blur-[120px] opacity-30"></div>
        <div class="max-w-7xl mx-auto px-4 relative z-10 text-center">
            <h1 class="text-4xl md:text-5xl font-bold mb-4">How can we help?</h1>
            <p class="text-gray-400 max-w-2xl mx-auto text-lg">Our expert team is here to assist you 24/7 with any technical or billing inquiries.</p>
        </div>
    </div>

    <!-- MAIN CONTENT AREA -->
    <div class="max-w-7xl mx-auto px-4 py-16 flex-grow relative z-20">
        
        <div class="bg-white rounded-3xl shadow-xl shadow-black/5 border border-gray-100 overflow-hidden flex flex-col md:flex-row max-w-5xl mx-auto -mt-32 animate-[slideUp_0.5s_ease-out_forwards]">
            
            <!-- Contact Info Sidebar -->
            <div class="w-full md:w-1/3 bg-gray-50 p-8 md:p-12 border-r border-gray-100 flex flex-col justify-between">
                <div>
                    <h3 class="text-2xl font-bold text-gray-900 mb-2">Contact Info</h3>
                    <p class="text-gray-500 text-sm mb-8">Reach out to us directly through any of these channels.</p>

                    <div class="space-y-6">
                        <div class="flex items-start gap-4">
                            <div class="w-10 h-10 rounded-full bg-blue-100 text-blue-600 flex items-center justify-center shrink-0">
                                <i data-lucide="mail" class="w-5 h-5"></i>
                            </div>
                            <div>
                                <h4 class="text-sm font-semibold text-gray-900">Email Support</h4>
                                <a href="mailto:support@peoplexplus.com" class="text-sm text-gray-500 hover:text-blue-600 transition-colors">support@peoplexplus.com</a>
                            </div>
                        </div>

                        <div class="flex items-start gap-4">
                            <div class="w-10 h-10 rounded-full bg-emerald-100 text-emerald-600 flex items-center justify-center shrink-0">
                                <i data-lucide="phone" class="w-5 h-5"></i>
                            </div>
                            <div>
                                <h4 class="text-sm font-semibold text-gray-900">Phone Support</h4>
                                <a href="tel:+18001234567" class="text-sm text-gray-500 hover:text-emerald-600 transition-colors">+1 (800) 123-4567</a>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="mt-12 p-6 bg-white rounded-2xl border border-gray-200">
                    <div class="flex items-center gap-3 mb-2">
                        <div class="w-2 h-2 rounded-full bg-emerald-500 animate-pulse"></div>
                        <span class="text-sm font-bold text-gray-900">Live Status</span>
                    </div>
                    <p class="text-xs text-gray-500">All systems operational. Average response time is currently <span class="font-bold text-gray-900">under 10 minutes</span>.</p>
                </div>
            </div>

            <!-- Contact Form -->
            <div class="w-full md:w-2/3 p-8 md:p-12">
                <h3 class="text-2xl font-bold text-gray-900 mb-6">Send us a message</h3>
                
                <form class="space-y-6">
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                        <div class="space-y-2">
                            <label class="text-sm font-semibold text-gray-700">Full Name</label>
                            <input type="text" placeholder="John Doe" class="w-full bg-gray-50 border border-gray-200 rounded-xl px-4 py-3 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:bg-white transition-all">
                        </div>
                        <div class="space-y-2">
                            <label class="text-sm font-semibold text-gray-700">Email Address</label>
                            <input type="email" placeholder="john@company.com" class="w-full bg-gray-50 border border-gray-200 rounded-xl px-4 py-3 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:bg-white transition-all">
                        </div>
                    </div>

                    <div class="space-y-2">
                        <label class="text-sm font-semibold text-gray-700">Issue Type</label>
                        <select class="w-full bg-gray-50 border border-gray-200 rounded-xl px-4 py-3 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:bg-white transition-all text-gray-700 appearance-none">
                            <option>Technical Support</option>
                            <option>Billing Inquiry</option>
                            <option>Feature Request</option>
                            <option>Other</option>
                        </select>
                    </div>

                    <div class="space-y-2">
                        <label class="text-sm font-semibold text-gray-700">Message</label>
                        <textarea rows="5" placeholder="Please describe your issue in detail..." class="w-full bg-gray-50 border border-gray-200 rounded-xl px-4 py-3 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:bg-white transition-all resize-none"></textarea>
                    </div>

                    <button type="button" class="w-full bg-black text-white rounded-xl py-4 font-semibold hover:bg-gray-800 transition-colors flex items-center justify-center gap-2">
                        Send Message <i data-lucide="send" class="w-4 h-4"></i>
                    </button>
                </form>
            </div>
        </div>
    </div>
"""

pages = {
    "documentation.html": doc_content,
    "tutorial.html": tutorial_content,
    "support.html": support_content
}

out_dir = r"d:\project pxp\website"

for filename, content in pages.items():
    page_title = filename.split('.')[0].capitalize()
    
    # Generate full HTML
    full_html = header_html.replace("{page_title}", page_title) + content + footer_html
    
    # Save file
    path = os.path.join(out_dir, filename)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(full_html)
    print(f"Created {filename}")
