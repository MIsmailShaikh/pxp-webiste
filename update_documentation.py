import os
import re

base_file = r"d:\project pxp\website\documentation.html"
with open(base_file, 'r', encoding='utf-8') as f:
    base_html = f.read()

# I want to replace everything from <!-- MAIN CONTENT AREA --> up to the script/footer part
main_content = """
    <!-- MAIN CONTENT AREA -->
    <div class="max-w-7xl mx-auto px-4 py-12 flex flex-col md:flex-row gap-8 lg:gap-16 w-full flex-grow">
        <!-- SIDEBAR NAVIGATION -->
        <div class="w-full md:w-64 flex-shrink-0">
            <div class="flex flex-col gap-6">
                
                <div>
                    <h4 class="text-xs font-bold text-gray-400 uppercase tracking-wider mb-3 px-2">Getting Started</h4>
                    <div class="flex flex-col gap-1">
                        <a href="#" data-target="intro" class="doc-nav-link px-3 py-2 rounded-lg text-sm font-semibold transition-colors bg-blue-50 text-blue-700">Introduction</a>
                        <a href="#" data-target="quick-start" class="doc-nav-link px-3 py-2 rounded-lg text-sm font-medium transition-colors text-gray-600 hover:bg-gray-50">Quick Start Guide</a>
                        <a href="#" data-target="sys-req" class="doc-nav-link px-3 py-2 rounded-lg text-sm font-medium transition-colors text-gray-600 hover:bg-gray-50">System Requirements</a>
                    </div>
                </div>

                <div>
                    <h4 class="text-xs font-bold text-gray-400 uppercase tracking-wider mb-3 px-2">Workforce OS</h4>
                    <div class="flex flex-col gap-1">
                        <a href="#" data-target="onboarding" class="doc-nav-link px-3 py-2 rounded-lg text-sm font-medium transition-colors text-gray-600 hover:bg-gray-50">Employee Onboarding</a>
                        <a href="#" data-target="shifts" class="doc-nav-link px-3 py-2 rounded-lg text-sm font-medium transition-colors text-gray-600 hover:bg-gray-50">Shift Management</a>
                        <a href="#" data-target="leave" class="doc-nav-link px-3 py-2 rounded-lg text-sm font-medium transition-colors text-gray-600 hover:bg-gray-50">Leave Policies</a>
                    </div>
                </div>

                <div>
                    <h4 class="text-xs font-bold text-gray-400 uppercase tracking-wider mb-3 px-2">Payroll Engine</h4>
                    <div class="flex flex-col gap-1">
                        <a href="#" data-target="tax" class="doc-nav-link px-3 py-2 rounded-lg text-sm font-medium transition-colors text-gray-600 hover:bg-gray-50">Tax Configuration</a>
                        <a href="#" data-target="payroll" class="doc-nav-link px-3 py-2 rounded-lg text-sm font-medium transition-colors text-gray-600 hover:bg-gray-50">Running Payroll</a>
                        <a href="#" data-target="payslips" class="doc-nav-link px-3 py-2 rounded-lg text-sm font-medium transition-colors text-gray-600 hover:bg-gray-50">Payslip Generation</a>
                    </div>
                </div>

                <div>
                    <h4 class="text-xs font-bold text-gray-400 uppercase tracking-wider mb-3 px-2">Developers</h4>
                    <div class="flex flex-col gap-1">
                        <a href="#" data-target="api-auth" class="doc-nav-link px-3 py-2 rounded-lg text-sm font-medium transition-colors text-gray-600 hover:bg-gray-50">API Authentication</a>
                        <a href="#" data-target="webhooks" class="doc-nav-link px-3 py-2 rounded-lg text-sm font-medium transition-colors text-gray-600 hover:bg-gray-50">Webhooks</a>
                        <a href="#" data-target="rate-limits" class="doc-nav-link px-3 py-2 rounded-lg text-sm font-medium transition-colors text-gray-600 hover:bg-gray-50">Rate Limits</a>
                    </div>
                </div>
            </div>
        </div>

        <!-- DOC CONTENT CONTAINER -->
        <div class="w-full max-w-3xl min-h-[600px] relative">
            
            <!-- SECTIONS -->
            
            <!-- 1. Intro -->
            <div id="intro" class="doc-section animate-[fadeIn_0.3s_ease-out]">
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
                            If you are looking to integrate your existing systems with PeopleXplus, please jump straight to the <a href="#" onclick="switchSection('api-auth')" class="underline font-semibold hover:text-blue-600">API Documentation</a> section. Our RESTful API allows you to programmatically manage employees, payroll, and access logs.
                        </p>
                    </div>
                    <h3 class="text-xl font-bold text-gray-900 mt-10 mb-4">Core Components</h3>
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mt-6">
                        <div class="border border-gray-200 rounded-2xl p-6">
                            <div class="w-10 h-10 rounded-lg bg-emerald-100 text-emerald-600 flex items-center justify-center mb-4"><i data-lucide="users" class="w-5 h-5"></i></div>
                            <h4 class="font-bold text-gray-900 mb-2">Workforce OS</h4>
                            <p class="text-sm text-gray-500">Manage employee lifecycles, shifts, and leave tracking.</p>
                        </div>
                        <div class="border border-gray-200 rounded-2xl p-6">
                            <div class="w-10 h-10 rounded-lg bg-indigo-100 text-indigo-600 flex items-center justify-center mb-4"><i data-lucide="calculator" class="w-5 h-5"></i></div>
                            <h4 class="font-bold text-gray-900 mb-2">Payroll Engine</h4>
                            <p class="text-sm text-gray-500">Automate salary processing, tax deductions, and compliance.</p>
                        </div>
                    </div>
                </div>
                <div class="border-t border-gray-200 mt-12 pt-8 flex justify-between items-center">
                    <div></div>
                    <a href="#" data-target="quick-start" class="next-section-btn flex flex-col items-end text-right group">
                        <span class="text-sm text-gray-500 mb-1">Next up</span>
                        <span class="text-blue-600 font-semibold flex items-center gap-2 group-hover:text-blue-700">Quick Start Guide <i data-lucide="arrow-right" class="w-4 h-4 group-hover:translate-x-1 transition-transform"></i></span>
                    </a>
                </div>
            </div>

            <!-- 2. Quick Start -->
            <div id="quick-start" class="doc-section hidden animate-[fadeIn_0.3s_ease-out]">
                <h2 class="text-3xl font-bold text-gray-900 mb-6">Quick Start Guide</h2>
                <div class="prose prose-blue max-w-none text-gray-600 space-y-6">
                    <p class="text-lg leading-relaxed">
                        Get up and running with PeopleXplus in under 10 minutes. Follow these simple steps to configure your first organization.
                    </p>
                    <h3 class="text-xl font-bold text-gray-900 mt-8 mb-4">1. Create your Organization</h3>
                    <p>Navigate to <strong>Settings &gt; Organization</strong>. Enter your legal company name, registration number, and primary currency.</p>
                    <h3 class="text-xl font-bold text-gray-900 mt-8 mb-4">2. Add your first Employee</h3>
                    <p>Go to the <strong>Workforce</strong> tab and click <strong>+ Add Employee</strong>. You can manually enter their details or invite them via email to self-onboard.</p>
                    <h3 class="text-xl font-bold text-gray-900 mt-8 mb-4">3. Setup a Payroll Schedule</h3>
                    <p>Under <strong>Payroll &gt; Schedules</strong>, define whether you pay your employees weekly, bi-weekly, or monthly. Assign your new employee to this schedule.</p>
                    <div class="bg-gray-900 text-gray-300 p-6 rounded-2xl font-mono text-sm mt-6">
                        <p class="text-gray-500 mb-2">// Pro-tip: You can also bulk import employees via CSV</p>
                        <span class="text-purple-400">Settings</span> &gt; <span class="text-blue-400">Data Import</span> &gt; Upload <span class="text-emerald-400">employees.csv</span>
                    </div>
                </div>
                <div class="border-t border-gray-200 mt-12 pt-8 flex justify-between items-center">
                    <a href="#" data-target="intro" class="next-section-btn flex flex-col items-start text-left group">
                        <span class="text-sm text-gray-500 mb-1">Previous</span>
                        <span class="text-gray-600 font-semibold flex items-center gap-2 group-hover:text-gray-900"><i data-lucide="arrow-left" class="w-4 h-4 group-hover:-translate-x-1 transition-transform"></i> Introduction</span>
                    </a>
                    <a href="#" data-target="sys-req" class="next-section-btn flex flex-col items-end text-right group">
                        <span class="text-sm text-gray-500 mb-1">Next up</span>
                        <span class="text-blue-600 font-semibold flex items-center gap-2 group-hover:text-blue-700">System Requirements <i data-lucide="arrow-right" class="w-4 h-4 group-hover:translate-x-1 transition-transform"></i></span>
                    </a>
                </div>
            </div>

            <!-- 3. System Requirements -->
            <div id="sys-req" class="doc-section hidden animate-[fadeIn_0.3s_ease-out]">
                <h2 class="text-3xl font-bold text-gray-900 mb-6">System Requirements</h2>
                <div class="prose prose-blue max-w-none text-gray-600 space-y-6">
                    <p class="text-lg leading-relaxed">
                        PeopleXplus is a cloud-based SaaS platform. You do not need to install any local servers to run our core software. However, certain hardware integrations do have requirements.
                    </p>
                    <h3 class="text-xl font-bold text-gray-900 mt-8 mb-4">Supported Browsers</h3>
                    <ul class="list-disc pl-5 space-y-2">
                        <li>Google Chrome (latest 2 versions)</li>
                        <li>Mozilla Firefox (latest 2 versions)</li>
                        <li>Apple Safari (latest 2 versions)</li>
                        <li>Microsoft Edge (Chromium-based)</li>
                    </ul>
                    <h3 class="text-xl font-bold text-gray-900 mt-8 mb-4">Biometric Scanner Requirements</h3>
                    <p>If you are integrating physical time-clocks, they must support our <code>WSS (WebSocket Secure)</code> streaming protocol. Contact our support team for a list of pre-approved hardware vendors.</p>
                </div>
                <div class="border-t border-gray-200 mt-12 pt-8 flex justify-between items-center">
                    <a href="#" data-target="quick-start" class="next-section-btn flex flex-col items-start text-left group">
                        <span class="text-sm text-gray-500 mb-1">Previous</span>
                        <span class="text-gray-600 font-semibold flex items-center gap-2 group-hover:text-gray-900"><i data-lucide="arrow-left" class="w-4 h-4 group-hover:-translate-x-1 transition-transform"></i> Quick Start Guide</span>
                    </a>
                    <a href="#" data-target="onboarding" class="next-section-btn flex flex-col items-end text-right group">
                        <span class="text-sm text-gray-500 mb-1">Next up</span>
                        <span class="text-blue-600 font-semibold flex items-center gap-2 group-hover:text-blue-700">Employee Onboarding <i data-lucide="arrow-right" class="w-4 h-4 group-hover:translate-x-1 transition-transform"></i></span>
                    </a>
                </div>
            </div>

            <!-- 4. Employee Onboarding -->
            <div id="onboarding" class="doc-section hidden animate-[fadeIn_0.3s_ease-out]">
                <h2 class="text-3xl font-bold text-gray-900 mb-6">Employee Onboarding</h2>
                <div class="prose prose-blue max-w-none text-gray-600 space-y-6">
                    <p class="text-lg leading-relaxed">
                        Automate the collection of tax documents, bank details, and compliance forms using our self-serve onboarding portal.
                    </p>
                    <h3 class="text-xl font-bold text-gray-900 mt-8 mb-4">Onboarding Workflows</h3>
                    <p>You can create custom onboarding checklists based on the employee's role. For example, a Developer might require GitHub access, while a Sales Rep requires CRM access.</p>
                    <img src="https://placehold.co/800x400/111827/FFF?text=Custom+Onboarding+Flow" class="w-full rounded-2xl shadow-sm border border-gray-200 mt-6" alt="Onboarding Flow">
                </div>
                <div class="border-t border-gray-200 mt-12 pt-8 flex justify-between items-center">
                    <a href="#" data-target="sys-req" class="next-section-btn flex flex-col items-start text-left group">
                        <span class="text-sm text-gray-500 mb-1">Previous</span>
                        <span class="text-gray-600 font-semibold flex items-center gap-2 group-hover:text-gray-900"><i data-lucide="arrow-left" class="w-4 h-4 group-hover:-translate-x-1 transition-transform"></i> System Requirements</span>
                    </a>
                    <a href="#" data-target="shifts" class="next-section-btn flex flex-col items-end text-right group">
                        <span class="text-sm text-gray-500 mb-1">Next up</span>
                        <span class="text-blue-600 font-semibold flex items-center gap-2 group-hover:text-blue-700">Shift Management <i data-lucide="arrow-right" class="w-4 h-4 group-hover:translate-x-1 transition-transform"></i></span>
                    </a>
                </div>
            </div>

            <!-- 5. Shift Management -->
            <div id="shifts" class="doc-section hidden animate-[fadeIn_0.3s_ease-out]">
                <h2 class="text-3xl font-bold text-gray-900 mb-6">Shift Management</h2>
                <div class="prose prose-blue max-w-none text-gray-600 space-y-6">
                    <p class="text-lg leading-relaxed">
                        Create complex, rotating shift patterns and automatically assign them to groups of employees.
                    </p>
                    <h3 class="text-xl font-bold text-gray-900 mt-8 mb-4">Creating a Shift Pattern</h3>
                    <p>Go to <strong>Workforce &gt; Shifts</strong>. Click Create Pattern. You can define a 4-on, 4-off pattern, or a standard Monday-Friday 9-5.</p>
                </div>
                <div class="border-t border-gray-200 mt-12 pt-8 flex justify-between items-center">
                    <a href="#" data-target="onboarding" class="next-section-btn flex flex-col items-start text-left group">
                        <span class="text-sm text-gray-500 mb-1">Previous</span>
                        <span class="text-gray-600 font-semibold flex items-center gap-2 group-hover:text-gray-900"><i data-lucide="arrow-left" class="w-4 h-4 group-hover:-translate-x-1 transition-transform"></i> Onboarding</span>
                    </a>
                    <a href="#" data-target="leave" class="next-section-btn flex flex-col items-end text-right group">
                        <span class="text-sm text-gray-500 mb-1">Next up</span>
                        <span class="text-blue-600 font-semibold flex items-center gap-2 group-hover:text-blue-700">Leave Policies <i data-lucide="arrow-right" class="w-4 h-4 group-hover:translate-x-1 transition-transform"></i></span>
                    </a>
                </div>
            </div>

            <!-- 6. Leave Policies -->
            <div id="leave" class="doc-section hidden animate-[fadeIn_0.3s_ease-out]">
                <h2 class="text-3xl font-bold text-gray-900 mb-6">Leave Policies</h2>
                <div class="prose prose-blue max-w-none text-gray-600 space-y-6">
                    <p class="text-lg leading-relaxed">
                        Configure how time-off is accrued, requested, and approved within your organization.
                    </p>
                </div>
                <div class="border-t border-gray-200 mt-12 pt-8 flex justify-between items-center">
                    <a href="#" data-target="shifts" class="next-section-btn flex flex-col items-start text-left group">
                        <span class="text-sm text-gray-500 mb-1">Previous</span>
                        <span class="text-gray-600 font-semibold flex items-center gap-2 group-hover:text-gray-900"><i data-lucide="arrow-left" class="w-4 h-4 group-hover:-translate-x-1 transition-transform"></i> Shifts</span>
                    </a>
                    <a href="#" data-target="tax" class="next-section-btn flex flex-col items-end text-right group">
                        <span class="text-sm text-gray-500 mb-1">Next up</span>
                        <span class="text-blue-600 font-semibold flex items-center gap-2 group-hover:text-blue-700">Tax Configuration <i data-lucide="arrow-right" class="w-4 h-4 group-hover:translate-x-1 transition-transform"></i></span>
                    </a>
                </div>
            </div>

            <!-- 7. Tax Configuration -->
            <div id="tax" class="doc-section hidden animate-[fadeIn_0.3s_ease-out]">
                <h2 class="text-3xl font-bold text-gray-900 mb-6">Tax Configuration</h2>
                <div class="prose prose-blue max-w-none text-gray-600 space-y-6">
                    <p class="text-lg leading-relaxed">
                        PXP automatically updates tax brackets for over 140 jurisdictions.
                    </p>
                </div>
                <div class="border-t border-gray-200 mt-12 pt-8 flex justify-between items-center">
                    <a href="#" data-target="leave" class="next-section-btn flex flex-col items-start text-left group">
                        <span class="text-sm text-gray-500 mb-1">Previous</span>
                        <span class="text-gray-600 font-semibold flex items-center gap-2 group-hover:text-gray-900"><i data-lucide="arrow-left" class="w-4 h-4 group-hover:-translate-x-1 transition-transform"></i> Leave</span>
                    </a>
                    <a href="#" data-target="payroll" class="next-section-btn flex flex-col items-end text-right group">
                        <span class="text-sm text-gray-500 mb-1">Next up</span>
                        <span class="text-blue-600 font-semibold flex items-center gap-2 group-hover:text-blue-700">Running Payroll <i data-lucide="arrow-right" class="w-4 h-4 group-hover:translate-x-1 transition-transform"></i></span>
                    </a>
                </div>
            </div>

            <!-- 8. Running Payroll -->
            <div id="payroll" class="doc-section hidden animate-[fadeIn_0.3s_ease-out]">
                <h2 class="text-3xl font-bold text-gray-900 mb-6">Running Payroll</h2>
                <div class="prose prose-blue max-w-none text-gray-600 space-y-6">
                    <p class="text-lg leading-relaxed">
                        Execute a payroll run with a single click. Our engine calculates gross, net, taxes, and deductions instantly.
                    </p>
                </div>
                <div class="border-t border-gray-200 mt-12 pt-8 flex justify-between items-center">
                    <a href="#" data-target="tax" class="next-section-btn flex flex-col items-start text-left group">
                        <span class="text-sm text-gray-500 mb-1">Previous</span>
                        <span class="text-gray-600 font-semibold flex items-center gap-2 group-hover:text-gray-900"><i data-lucide="arrow-left" class="w-4 h-4 group-hover:-translate-x-1 transition-transform"></i> Taxes</span>
                    </a>
                    <a href="#" data-target="payslips" class="next-section-btn flex flex-col items-end text-right group">
                        <span class="text-sm text-gray-500 mb-1">Next up</span>
                        <span class="text-blue-600 font-semibold flex items-center gap-2 group-hover:text-blue-700">Payslip Generation <i data-lucide="arrow-right" class="w-4 h-4 group-hover:translate-x-1 transition-transform"></i></span>
                    </a>
                </div>
            </div>

            <!-- 9. Payslips -->
            <div id="payslips" class="doc-section hidden animate-[fadeIn_0.3s_ease-out]">
                <h2 class="text-3xl font-bold text-gray-900 mb-6">Payslip Generation</h2>
                <div class="prose prose-blue max-w-none text-gray-600 space-y-6">
                    <p class="text-lg leading-relaxed">
                        Automatically generate and distribute secure, encrypted payslips to your employees' portals via email or SMS.
                    </p>
                </div>
                <div class="border-t border-gray-200 mt-12 pt-8 flex justify-between items-center">
                    <a href="#" data-target="payroll" class="next-section-btn flex flex-col items-start text-left group">
                        <span class="text-sm text-gray-500 mb-1">Previous</span>
                        <span class="text-gray-600 font-semibold flex items-center gap-2 group-hover:text-gray-900"><i data-lucide="arrow-left" class="w-4 h-4 group-hover:-translate-x-1 transition-transform"></i> Payroll</span>
                    </a>
                    <a href="#" data-target="api-auth" class="next-section-btn flex flex-col items-end text-right group">
                        <span class="text-sm text-gray-500 mb-1">Next up</span>
                        <span class="text-blue-600 font-semibold flex items-center gap-2 group-hover:text-blue-700">API Authentication <i data-lucide="arrow-right" class="w-4 h-4 group-hover:translate-x-1 transition-transform"></i></span>
                    </a>
                </div>
            </div>

            <!-- 10. API Auth -->
            <div id="api-auth" class="doc-section hidden animate-[fadeIn_0.3s_ease-out]">
                <h2 class="text-3xl font-bold text-gray-900 mb-6">API Authentication</h2>
                <div class="prose prose-blue max-w-none text-gray-600 space-y-6">
                    <p class="text-lg leading-relaxed">
                        Secure your API requests using Bearer tokens. Generate your API keys in the developer console.
                    </p>
                    <div class="bg-gray-900 text-gray-300 p-6 rounded-2xl font-mono text-sm mt-6">
                        <p class="text-gray-500 mb-2">// Example Request</p>
                        <p>curl -X GET "https://api.peoplexplus.com/v1/employees" \</p>
                        <p class="ml-4">-H "Authorization: Bearer pxp_live_abc123..."</p>
                    </div>
                </div>
                <div class="border-t border-gray-200 mt-12 pt-8 flex justify-between items-center">
                    <a href="#" data-target="payslips" class="next-section-btn flex flex-col items-start text-left group">
                        <span class="text-sm text-gray-500 mb-1">Previous</span>
                        <span class="text-gray-600 font-semibold flex items-center gap-2 group-hover:text-gray-900"><i data-lucide="arrow-left" class="w-4 h-4 group-hover:-translate-x-1 transition-transform"></i> Payslips</span>
                    </a>
                    <a href="#" data-target="webhooks" class="next-section-btn flex flex-col items-end text-right group">
                        <span class="text-sm text-gray-500 mb-1">Next up</span>
                        <span class="text-blue-600 font-semibold flex items-center gap-2 group-hover:text-blue-700">Webhooks <i data-lucide="arrow-right" class="w-4 h-4 group-hover:translate-x-1 transition-transform"></i></span>
                    </a>
                </div>
            </div>

            <!-- 11. Webhooks -->
            <div id="webhooks" class="doc-section hidden animate-[fadeIn_0.3s_ease-out]">
                <h2 class="text-3xl font-bold text-gray-900 mb-6">Webhooks</h2>
                <div class="prose prose-blue max-w-none text-gray-600 space-y-6">
                    <p class="text-lg leading-relaxed">
                        Subscribe to real-time events on your account, such as <code>employee.created</code> or <code>payroll.completed</code>.
                    </p>
                </div>
                <div class="border-t border-gray-200 mt-12 pt-8 flex justify-between items-center">
                    <a href="#" data-target="api-auth" class="next-section-btn flex flex-col items-start text-left group">
                        <span class="text-sm text-gray-500 mb-1">Previous</span>
                        <span class="text-gray-600 font-semibold flex items-center gap-2 group-hover:text-gray-900"><i data-lucide="arrow-left" class="w-4 h-4 group-hover:-translate-x-1 transition-transform"></i> API Auth</span>
                    </a>
                    <a href="#" data-target="rate-limits" class="next-section-btn flex flex-col items-end text-right group">
                        <span class="text-sm text-gray-500 mb-1">Next up</span>
                        <span class="text-blue-600 font-semibold flex items-center gap-2 group-hover:text-blue-700">Rate Limits <i data-lucide="arrow-right" class="w-4 h-4 group-hover:translate-x-1 transition-transform"></i></span>
                    </a>
                </div>
            </div>

            <!-- 12. Rate Limits -->
            <div id="rate-limits" class="doc-section hidden animate-[fadeIn_0.3s_ease-out]">
                <h2 class="text-3xl font-bold text-gray-900 mb-6">Rate Limits</h2>
                <div class="prose prose-blue max-w-none text-gray-600 space-y-6">
                    <p class="text-lg leading-relaxed">
                        To ensure system stability, our APIs are rate-limited to 1,000 requests per minute per organization.
                    </p>
                </div>
                <div class="border-t border-gray-200 mt-12 pt-8 flex justify-between items-center">
                    <a href="#" data-target="webhooks" class="next-section-btn flex flex-col items-start text-left group">
                        <span class="text-sm text-gray-500 mb-1">Previous</span>
                        <span class="text-gray-600 font-semibold flex items-center gap-2 group-hover:text-gray-900"><i data-lucide="arrow-left" class="w-4 h-4 group-hover:-translate-x-1 transition-transform"></i> Webhooks</span>
                    </a>
                    <div></div>
                </div>
            </div>

        </div>
    </div>
"""

script_content = """
    <script>
        function switchSection(targetId) {
            // hide all sections
            document.querySelectorAll('.doc-section').forEach(s => s.classList.add('hidden'));
            
            // reset all links
            document.querySelectorAll('.doc-nav-link').forEach(l => {
                l.classList.remove('bg-blue-50', 'text-blue-700');
                l.classList.add('text-gray-600', 'hover:bg-gray-50');
            });

            // show target section
            const targetSection = document.getElementById(targetId);
            if(targetSection) targetSection.classList.remove('hidden');

            // highlight active link
            const targetLink = document.querySelector(`.doc-nav-link[data-target="${targetId}"]`);
            if(targetLink) {
                targetLink.classList.remove('text-gray-600', 'hover:bg-gray-50');
                targetLink.classList.add('bg-blue-50', 'text-blue-700');
            }

            // Scroll to the top of the content area
            window.scrollTo({ top: 350, behavior: 'smooth' });
        }

        document.addEventListener('DOMContentLoaded', () => {
            const links = document.querySelectorAll('.doc-nav-link');
            const nextButtons = document.querySelectorAll('.next-section-btn');

            links.forEach(link => {
                link.addEventListener('click', (e) => {
                    e.preventDefault();
                    switchSection(link.getAttribute('data-target'));
                });
            });

            nextButtons.forEach(btn => {
                btn.addEventListener('click', (e) => {
                    e.preventDefault();
                    switchSection(btn.getAttribute('data-target'));
                });
            });
        });
    </script>
"""

# Replace in documentation.html
start_marker = "<!-- MAIN CONTENT AREA -->"
end_marker = "<!-- FOOTER -->"

start_idx = base_html.find(start_marker)
end_idx = base_html.find(end_marker)

if start_idx != -1 and end_idx != -1:
    new_html = base_html[:start_idx] + main_content + "\n" + script_content + "\n" + base_html[end_idx:]
    with open(base_file, 'w', encoding='utf-8') as f:
        f.write(new_html)
    print("Successfully updated documentation.html with SPA logic.")
else:
    print("Failed to find markers")
