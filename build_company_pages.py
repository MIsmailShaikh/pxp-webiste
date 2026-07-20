import os
import re

base_file = r"d:\project pxp\website\privacy-policy.html"
with open(base_file, 'r', encoding='utf-8') as f:
    base_html = f.read()

header_match = re.search(r'(.*?)<!-- HERO SECTION -->', base_html, re.DOTALL)
footer_match = re.search(r'<!-- FOOTER -->(.*)', base_html, re.DOTALL)

if not header_match or not footer_match:
    print("Could not find header or footer in base file")
    exit(1)

header_html = header_match.group(1)
footer_html = "<!-- FOOTER -->" + footer_match.group(1)

# Fix title in header
header_html = header_html.replace("<title>Privacy Policy - PeopleXplus</title>", "<title>{page_title} - PeopleXplus</title>")


# 1. About Us Page
about_content = """
    <!-- HERO SECTION -->
    <div class="pt-32 pb-16 md:pt-40 md:pb-24 bg-gradient-to-br from-gray-900 to-black text-white relative overflow-hidden">
        <div class="absolute top-[-20%] left-[-10%] w-[50%] h-[50%] bg-blue-600 rounded-full blur-[120px] opacity-30"></div>
        <div class="absolute bottom-[-10%] right-[-10%] w-[50%] h-[50%] bg-purple-600 rounded-full blur-[120px] opacity-30"></div>
        <div class="max-w-7xl mx-auto px-4 relative z-10 text-center">
            <h1 class="text-4xl md:text-5xl font-bold mb-4">About PeopleXplus</h1>
            <p class="text-gray-400 max-w-2xl mx-auto text-lg">We are on a mission to completely redefine how businesses manage their workforce.</p>
        </div>
    </div>

    <!-- MAIN CONTENT AREA -->
    <div class="max-w-7xl mx-auto px-4 py-16 flex-grow">
        <!-- Our Story -->
        <div class="max-w-3xl mx-auto text-center mb-24">
            <h2 class="text-3xl font-bold text-gray-900 mb-6">Our Story</h2>
            <p class="text-lg text-gray-600 leading-relaxed mb-6">
                PeopleXplus started with a simple observation: modern businesses were using half a dozen disjointed tools to manage their most valuable asset—their people. Payroll lived in one system, shift scheduling in another, and physical access control was completely siloed.
            </p>
            <p class="text-lg text-gray-600 leading-relaxed">
                We built Workforce OS to bridge those gaps. By bringing HR, payroll, benefits, and hardware into a single ecosystem, we help companies save hundreds of administrative hours so they can focus on what they do best: building great products and serving their customers.
            </p>
        </div>

        <!-- Core Values Grid -->
        <div class="mb-16">
            <h2 class="text-3xl font-bold text-center text-gray-900 mb-12">Our Core Values</h2>
            
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
                <!-- Value 1 -->
                <div class="bg-white p-8 rounded-3xl shadow-sm border border-gray-100 hover:shadow-xl transition-all group">
                    <div class="w-12 h-12 rounded-xl bg-blue-50 text-blue-600 flex items-center justify-center mb-6 group-hover:scale-110 group-hover:bg-blue-600 group-hover:text-white transition-all">
                        <i data-lucide="zap" class="w-6 h-6"></i>
                    </div>
                    <h3 class="text-xl font-bold text-gray-900 mb-3">Relentless Innovation</h3>
                    <p class="text-gray-500 leading-relaxed text-sm">We never settle for "industry standard". We are constantly pushing the boundaries of what enterprise software can and should do.</p>
                </div>
                
                <!-- Value 2 -->
                <div class="bg-white p-8 rounded-3xl shadow-sm border border-gray-100 hover:shadow-xl transition-all group">
                    <div class="w-12 h-12 rounded-xl bg-emerald-50 text-emerald-600 flex items-center justify-center mb-6 group-hover:scale-110 group-hover:bg-emerald-600 group-hover:text-white transition-all">
                        <i data-lucide="shield-check" class="w-6 h-6"></i>
                    </div>
                    <h3 class="text-xl font-bold text-gray-900 mb-3">Absolute Security</h3>
                    <p class="text-gray-500 leading-relaxed text-sm">We are entrusted with highly sensitive financial and personal data. We engineer security into the very foundation of our platform.</p>
                </div>

                <!-- Value 3 -->
                <div class="bg-white p-8 rounded-3xl shadow-sm border border-gray-100 hover:shadow-xl transition-all group">
                    <div class="w-12 h-12 rounded-xl bg-purple-50 text-purple-600 flex items-center justify-center mb-6 group-hover:scale-110 group-hover:bg-purple-600 group-hover:text-white transition-all">
                        <i data-lucide="heart" class="w-6 h-6"></i>
                    </div>
                    <h3 class="text-xl font-bold text-gray-900 mb-3">People First</h3>
                    <p class="text-gray-500 leading-relaxed text-sm">Our tools are built for humans. We prioritize intuitive design and zero-friction experiences for the end-user.</p>
                </div>
            </div>
        </div>
    </div>
"""

# 2. Career Page
career_content = """
    <!-- HERO SECTION -->
    <div class="pt-32 pb-16 md:pt-40 md:pb-24 bg-gradient-to-br from-gray-900 to-black text-white relative overflow-hidden">
        <div class="absolute top-[-20%] left-[-10%] w-[50%] h-[50%] bg-blue-600 rounded-full blur-[120px] opacity-30"></div>
        <div class="absolute bottom-[-10%] right-[-10%] w-[50%] h-[50%] bg-purple-600 rounded-full blur-[120px] opacity-30"></div>
        <div class="max-w-7xl mx-auto px-4 relative z-10 text-center">
            <h1 class="text-4xl md:text-5xl font-bold mb-4">Join Our Team</h1>
            <p class="text-gray-400 max-w-2xl mx-auto text-lg mb-8">Build the future of work alongside passionate, driven, and kind people.</p>
            <a href="#open-roles" class="inline-flex items-center gap-2 bg-white text-black px-6 py-3 rounded-xl font-bold hover:bg-gray-100 transition-colors">
                View Open Roles <i data-lucide="arrow-down" class="w-4 h-4"></i>
            </a>
        </div>
    </div>

    <!-- MAIN CONTENT AREA -->
    <div class="max-w-7xl mx-auto px-4 py-16 flex-grow">
        
        <!-- Perks & Benefits -->
        <div class="mb-24">
            <h2 class="text-3xl font-bold text-center text-gray-900 mb-12">Why work with us?</h2>
            
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 text-center">
                <div class="p-6">
                    <div class="w-12 h-12 mx-auto bg-gray-100 rounded-full flex items-center justify-center mb-4 text-gray-900">
                        <i data-lucide="globe" class="w-6 h-6"></i>
                    </div>
                    <h4 class="font-bold text-gray-900 mb-2">Remote First</h4>
                    <p class="text-sm text-gray-500">Work from anywhere. We provide a generous home-office stipend.</p>
                </div>
                
                <div class="p-6">
                    <div class="w-12 h-12 mx-auto bg-gray-100 rounded-full flex items-center justify-center mb-4 text-gray-900">
                        <i data-lucide="stethoscope" class="w-6 h-6"></i>
                    </div>
                    <h4 class="font-bold text-gray-900 mb-2">Top Healthcare</h4>
                    <p class="text-sm text-gray-500">100% premium coverage for you and your dependents.</p>
                </div>

                <div class="p-6">
                    <div class="w-12 h-12 mx-auto bg-gray-100 rounded-full flex items-center justify-center mb-4 text-gray-900">
                        <i data-lucide="book-open" class="w-6 h-6"></i>
                    </div>
                    <h4 class="font-bold text-gray-900 mb-2">Learning Budget</h4>
                    <p class="text-sm text-gray-500">$2,000 annual budget for courses, books, and conferences.</p>
                </div>

                <div class="p-6">
                    <div class="w-12 h-12 mx-auto bg-gray-100 rounded-full flex items-center justify-center mb-4 text-gray-900">
                        <i data-lucide="coffee" class="w-6 h-6"></i>
                    </div>
                    <h4 class="font-bold text-gray-900 mb-2">Flexible PTO</h4>
                    <p class="text-sm text-gray-500">Take the time you need to recharge and avoid burnout.</p>
                </div>
            </div>
        </div>

        <!-- Open Roles List -->
        <div id="open-roles" class="max-w-4xl mx-auto">
            <h2 class="text-3xl font-bold text-gray-900 mb-8">Open Positions</h2>
            
            <div class="space-y-4">
                <!-- Job 1 -->
                <a href="#" class="block bg-white border border-gray-200 rounded-2xl p-6 hover:border-blue-500 hover:shadow-md transition-all group">
                    <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
                        <div>
                            <h3 class="text-xl font-bold text-gray-900 group-hover:text-blue-600 transition-colors">Senior Full Stack Engineer</h3>
                            <div class="flex items-center gap-4 mt-2 text-sm text-gray-500">
                                <span class="flex items-center gap-1"><i data-lucide="briefcase" class="w-4 h-4"></i> Engineering</span>
                                <span class="flex items-center gap-1"><i data-lucide="map-pin" class="w-4 h-4"></i> Remote (US)</span>
                            </div>
                        </div>
                        <div class="text-blue-600 font-semibold flex items-center gap-2">
                            Apply Now <i data-lucide="arrow-right" class="w-4 h-4 group-hover:translate-x-1 transition-transform"></i>
                        </div>
                    </div>
                </a>

                <!-- Job 2 -->
                <a href="#" class="block bg-white border border-gray-200 rounded-2xl p-6 hover:border-blue-500 hover:shadow-md transition-all group">
                    <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
                        <div>
                            <h3 class="text-xl font-bold text-gray-900 group-hover:text-blue-600 transition-colors">Enterprise Account Executive</h3>
                            <div class="flex items-center gap-4 mt-2 text-sm text-gray-500">
                                <span class="flex items-center gap-1"><i data-lucide="briefcase" class="w-4 h-4"></i> Sales</span>
                                <span class="flex items-center gap-1"><i data-lucide="map-pin" class="w-4 h-4"></i> Remote (EMEA)</span>
                            </div>
                        </div>
                        <div class="text-blue-600 font-semibold flex items-center gap-2">
                            Apply Now <i data-lucide="arrow-right" class="w-4 h-4 group-hover:translate-x-1 transition-transform"></i>
                        </div>
                    </div>
                </a>

                <!-- Job 3 -->
                <a href="#" class="block bg-white border border-gray-200 rounded-2xl p-6 hover:border-blue-500 hover:shadow-md transition-all group">
                    <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
                        <div>
                            <h3 class="text-xl font-bold text-gray-900 group-hover:text-blue-600 transition-colors">Product Designer</h3>
                            <div class="flex items-center gap-4 mt-2 text-sm text-gray-500">
                                <span class="flex items-center gap-1"><i data-lucide="briefcase" class="w-4 h-4"></i> Design</span>
                                <span class="flex items-center gap-1"><i data-lucide="map-pin" class="w-4 h-4"></i> San Francisco, CA (Hybrid)</span>
                            </div>
                        </div>
                        <div class="text-blue-600 font-semibold flex items-center gap-2">
                            Apply Now <i data-lucide="arrow-right" class="w-4 h-4 group-hover:translate-x-1 transition-transform"></i>
                        </div>
                    </div>
                </a>
            </div>
        </div>
    </div>
"""

# 3. Case Studies Page
case_studies_content = """
    <!-- HERO SECTION -->
    <div class="pt-32 pb-16 md:pt-40 md:pb-24 bg-gradient-to-br from-gray-900 to-black text-white relative overflow-hidden">
        <div class="absolute top-[-20%] left-[-10%] w-[50%] h-[50%] bg-blue-600 rounded-full blur-[120px] opacity-30"></div>
        <div class="absolute bottom-[-10%] right-[-10%] w-[50%] h-[50%] bg-purple-600 rounded-full blur-[120px] opacity-30"></div>
        <div class="max-w-7xl mx-auto px-4 relative z-10 text-center">
            <h1 class="text-4xl md:text-5xl font-bold mb-4">Customer Success Stories</h1>
            <p class="text-gray-400 max-w-2xl mx-auto text-lg">See how modern companies are using PeopleXplus to scale their operations.</p>
        </div>
    </div>

    <!-- MAIN CONTENT AREA -->
    <div class="max-w-7xl mx-auto px-4 py-16 flex-grow">
        
        <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
            
            <!-- Story 1 -->
            <div class="bg-white rounded-3xl border border-gray-100 overflow-hidden shadow-sm hover:shadow-lg transition-all group">
                <div class="h-48 bg-gradient-to-br from-blue-900 to-indigo-900 relative overflow-hidden p-8 flex items-end">
                    <!-- Abstract geometric pattern placeholder -->
                    <div class="absolute inset-0 opacity-20 bg-[radial-gradient(circle_at_center,_var(--tw-gradient-stops))] from-white to-transparent"></div>
                    <h3 class="relative z-10 text-3xl font-bold text-white tracking-widest">TECHCORP</h3>
                </div>
                <div class="p-8">
                    <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-emerald-50 text-emerald-700 text-xs font-bold uppercase tracking-wider mb-4">
                        <i data-lucide="trending-up" class="w-3 h-3"></i> 40% time saved
                    </div>
                    <h3 class="text-2xl font-bold text-gray-900 mb-3">How TechCorp automated global payroll for 500+ employees</h3>
                    <p class="text-gray-500 mb-6 line-clamp-3">TechCorp was struggling with disjointed local providers. By switching to PeopleXplus, they consolidated their entire payroll system and saved over 40 hours of manual data entry every month.</p>
                    <a href="#" class="inline-flex items-center gap-2 text-blue-600 font-bold hover:text-blue-700">
                        Read full story <i data-lucide="arrow-right" class="w-4 h-4 group-hover:translate-x-1 transition-transform"></i>
                    </a>
                </div>
            </div>

            <!-- Story 2 -->
            <div class="bg-white rounded-3xl border border-gray-100 overflow-hidden shadow-sm hover:shadow-lg transition-all group">
                <div class="h-48 bg-gradient-to-br from-purple-900 to-fuchsia-900 relative overflow-hidden p-8 flex items-end">
                    <div class="absolute inset-0 opacity-20 bg-[radial-gradient(circle_at_center,_var(--tw-gradient-stops))] from-white to-transparent"></div>
                    <h3 class="relative z-10 text-3xl font-bold text-white tracking-widest">NEXUS<span class="text-purple-300">HEALTH</span></h3>
                </div>
                <div class="p-8">
                    <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-blue-50 text-blue-700 text-xs font-bold uppercase tracking-wider mb-4">
                        <i data-lucide="shield-check" class="w-3 h-3"></i> HIPAA Compliant
                    </div>
                    <h3 class="text-2xl font-bold text-gray-900 mb-3">Scaling shift management across 12 hospitals securely</h3>
                    <p class="text-gray-500 mb-6 line-clamp-3">NexusHealth needed a robust, compliant way to manage dynamic shift rotations. Our Workforce OS deployed physical scanners and real-time rostering to eliminate staffing gaps.</p>
                    <a href="#" class="inline-flex items-center gap-2 text-blue-600 font-bold hover:text-blue-700">
                        Read full story <i data-lucide="arrow-right" class="w-4 h-4 group-hover:translate-x-1 transition-transform"></i>
                    </a>
                </div>
            </div>

            <!-- Story 3 -->
            <div class="bg-white rounded-3xl border border-gray-100 overflow-hidden shadow-sm hover:shadow-lg transition-all group">
                <div class="h-48 bg-gradient-to-br from-emerald-900 to-teal-900 relative overflow-hidden p-8 flex items-end">
                    <div class="absolute inset-0 opacity-20 bg-[radial-gradient(circle_at_center,_var(--tw-gradient-stops))] from-white to-transparent"></div>
                    <h3 class="relative z-10 text-3xl font-bold text-white tracking-widest text-serif italic">Velvet & Co.</h3>
                </div>
                <div class="p-8">
                    <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-orange-50 text-orange-700 text-xs font-bold uppercase tracking-wider mb-4">
                        <i data-lucide="zap" class="w-3 h-3"></i> 3x Faster Onboarding
                    </div>
                    <h3 class="text-2xl font-bold text-gray-900 mb-3">Velvet & Co. transforms retail employee onboarding</h3>
                    <p class="text-gray-500 mb-6 line-clamp-3">With high turnover in the retail space, Velvet & Co. required a frictionless onboarding process. They utilized our custom portals to create a deeply branded, automated experience.</p>
                    <a href="#" class="inline-flex items-center gap-2 text-blue-600 font-bold hover:text-blue-700">
                        Read full story <i data-lucide="arrow-right" class="w-4 h-4 group-hover:translate-x-1 transition-transform"></i>
                    </a>
                </div>
            </div>

        </div>
    </div>
"""

pages = {
    "about-us.html": about_content,
    "career.html": career_content,
    "case-studies.html": case_studies_content
}

out_dir = r"d:\project pxp\website"

for filename, content in pages.items():
    page_title = filename.replace('-', ' ').split('.')[0].title()
    
    full_html = header_html.replace("{page_title}", page_title) + content + footer_html
    
    path = os.path.join(out_dir, filename)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(full_html)
    print(f"Created {filename}")
