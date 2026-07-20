import os
import re
import glob

base_dir = r"d:\project pxp\website"
index_path = os.path.join(base_dir, 'index11.html')

with open(index_path, 'r', encoding='utf-8') as f:
    index_content = f.read()

nav_match = re.search(r'(<nav.*?</nav>)', index_content, re.DOTALL)
footer_match = re.search(r'(<footer.*?</footer>)', index_content, re.DOTALL)

nav_html = nav_match.group(1) if nav_match else ""
# Remove the fixed class so it doesn't overlap everything in standard flow, or keep it and add padding
# The nav is fixed at the top, so we will need padding at the top of the hero section.
# Actually, nav in index11.html is `fixed top-1`.

footer_html = footer_match.group(1) if footer_match else ""

# Clean up the footer html to point to right files and remove Affiliate / GDPR
def clean_footer(footer_content):
    # Update links
    footer_content = footer_content.replace('href="#" class="hover:text-white transition-colors">Terms & Conditions', 'href="terms-and-conditions.html" class="hover:text-white transition-colors">Terms & Conditions')
    footer_content = footer_content.replace('href="#" class="hover:text-white transition-colors">Privacy Policy', 'href="privacy-policy.html" class="hover:text-white transition-colors">Privacy Policy')
    footer_content = footer_content.replace('href="#" class="hover:text-white transition-colors">Refund Policy', 'href="refund-policy.html" class="hover:text-white transition-colors">Refund Policy')
    
    # Remove Affiliate Policy
    footer_content = re.sub(r'<li><a href="#" class="hover:text-white transition-colors">Affiliate Policy</a></li>\s*', '', footer_content)
    
    # Remove GDPR Compliance if it exists
    footer_content = re.sub(r'<li><a href="#" class="hover:text-white transition-colors">GDPR Compliance</a></li>\s*', '', footer_content)
    return footer_content

footer_html_cleaned = clean_footer(footer_html)

# Template for Legal Pages
template = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{{{TITLE}}}} - PeopleXplus (PXP)</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://unpkg.com/lucide@latest"></script>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Outfit:wght@400;500;600;700&display=swap" rel="stylesheet">
    <script src="js/auth-guard.js"></script>
    <style>
        body {{ font-family: 'Inter', sans-serif; }}
        h1, h2, h3, h4, h5, h6 {{ font-family: 'Outfit', sans-serif; }}
        
        /* Custom scrollbar for active tab */
        .glass-nav {{
            background: rgba(255, 255, 255, 0.7);
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
        }}
    </style>
</head>
<body class="bg-gray-50 text-gray-900 antialiased selection:bg-black selection:text-white min-h-screen flex flex-col">

    <!-- NAVBAR -->
    {nav_html}

    <!-- HERO SECTION -->
    <div class="pt-32 pb-16 md:pt-40 md:pb-24 bg-gradient-to-br from-gray-900 to-black text-white relative overflow-hidden">
        <div class="absolute top-[-20%] left-[-10%] w-[50%] h-[50%] bg-blue-600 rounded-full blur-[120px] opacity-30"></div>
        <div class="absolute bottom-[-10%] right-[-10%] w-[50%] h-[50%] bg-purple-600 rounded-full blur-[120px] opacity-30"></div>
        <div class="max-w-7xl mx-auto px-4 relative z-10 text-center">
            <h1 class="text-4xl md:text-5xl font-bold mb-4">{{{{TITLE}}}}</h1>
            <p class="text-gray-400 max-w-2xl mx-auto text-lg">{{{{SUBTITLE}}}}</p>
        </div>
    </div>

    <!-- MAIN CONTENT AREA -->
    <div class="max-w-7xl mx-auto px-4 py-12 flex flex-col md:flex-row gap-8 lg:gap-16 w-full flex-grow">
        
        <!-- SIDEBAR NAVIGATION -->
        <div class="w-full md:w-64 flex-shrink-0">
            <div class="sticky top-32 flex flex-col gap-1 bg-white p-2 rounded-2xl shadow-sm border border-gray-100">
                <a href="terms-and-conditions.html" class="px-4 py-3 rounded-xl text-sm font-semibold transition-colors {{{{ACTIVE_TERMS}}}}">Terms & Conditions</a>
                <a href="privacy-policy.html" class="px-4 py-3 rounded-xl text-sm font-semibold transition-colors {{{{ACTIVE_PRIVACY}}}}">Privacy Policy</a>
                <a href="refund-policy.html" class="px-4 py-3 rounded-xl text-sm font-semibold transition-colors {{{{ACTIVE_REFUND}}}}">Refund Policy</a>
            </div>
        </div>

        <!-- POLICY CONTENT -->
        <div class="w-full max-w-3xl">
            <!-- Binding Notification Box -->
            <div class="bg-blue-50 border border-blue-100 rounded-2xl p-6 mb-10">
                <p class="text-sm text-blue-900 leading-relaxed">
                    The English version of legal agreements and policies is considered as the only current and valid version of this document. Any translated version is provided for your convenience only, to facilitate reading and understanding of the English version. Any translated versions are not legally binding and cannot replace the English versions. In the event of disagreement or conflict, the English language legal agreements and policies shall prevail.
                </p>
            </div>
            
            <p class="text-sm text-gray-500 mb-8 pb-8 border-b border-gray-200">Last revised: {{{{DATE}}}}</p>

            <div class="prose prose-gray max-w-none text-gray-700 space-y-6">
                {{{{CONTENT}}}}
            </div>
        </div>
    </div>

    <!-- FOOTER -->
    {footer_html_cleaned}
    
    <script>
        lucide.createIcons();
    </script>
</body>
</html>
"""

policies = [
    {
        "filename": "privacy-policy.html",
        "title": "Privacy Policy",
        "subtitle": "Please read this agreement carefully, as it contains important information regarding your privacy and our data practices.",
        "active_terms": "text-gray-600 hover:bg-gray-50",
        "active_privacy": "bg-blue-50 text-blue-700",
        "active_refund": "text-gray-600 hover:bg-gray-50",
        "content": """
        <h3 class="text-xl font-bold text-black uppercase tracking-wider mb-4">1. Introduction</h3>
        <p>At PeopleXplus ("PXP"), the privacy and security of our Users is of paramount importance. PXP is committed to protecting the data you share with us. This Privacy Policy ("Policy") explains how PXP processes information that can be used to directly or indirectly identify an individual ("Personal Data") collected through use of our website and services.</p>
        
        <h3 class="text-xl font-bold text-black uppercase tracking-wider mt-10 mb-4">2. Data We Collect</h3>
        <p>We may collect the following types of Personal Data:</p>
        <ul class="list-disc pl-5 space-y-2">
            <li><strong>Contact Information:</strong> Name, email address, phone number, and company details.</li>
            <li><strong>Account Information:</strong> Passwords and security credentials.</li>
            <li><strong>Usage Data:</strong> Information on how you interact with our Services, including IP addresses, browser types, and access times.</li>
        </ul>
        
        <h3 class="text-xl font-bold text-black uppercase tracking-wider mt-10 mb-4">3. How We Use Your Data</h3>
        <p>Your Personal Data is used to:</p>
        <ul class="list-disc pl-5 space-y-2">
            <li>Provide and maintain our Services.</li>
            <li>Process payments and manage billing.</li>
            <li>Communicate with you regarding updates, offers, and support.</li>
            <li>Improve the functionality and security of our platform.</li>
        </ul>
        """
    },
    {
        "filename": "terms-and-conditions.html",
        "title": "Terms & Conditions",
        "subtitle": "Please read this agreement carefully, as it governs your use of the PeopleXplus platform and services.",
        "active_terms": "bg-blue-50 text-blue-700",
        "active_privacy": "text-gray-600 hover:bg-gray-50",
        "active_refund": "text-gray-600 hover:bg-gray-50",
        "content": """
        <h3 class="text-xl font-bold text-black uppercase tracking-wider mb-4">1. Acceptance of Terms</h3>
        <p>By accessing or using the PeopleXplus website, platform, and services (collectively, the "Services"), you agree to be bound by these Terms & Conditions. If you do not agree to these terms, please do not use the Services.</p>
        
        <h3 class="text-xl font-bold text-black uppercase tracking-wider mt-10 mb-4">2. Use of Services</h3>
        <p>You agree to use the Services only for lawful purposes and in accordance with these Terms. You are responsible for maintaining the confidentiality of your account credentials and for all activities that occur under your account.</p>
        
        <h3 class="text-xl font-bold text-black uppercase tracking-wider mt-10 mb-4">3. Intellectual Property</h3>
        <p>All content, features, and functionality of the Services, including but not limited to text, graphics, logos, and software, are the exclusive property of PeopleXplus and are protected by international copyright, trademark, and other intellectual property laws.</p>
        """
    },
    {
        "filename": "refund-policy.html",
        "title": "Refund Policy",
        "subtitle": "Our commitment to customer satisfaction and the terms under which refunds may be issued.",
        "active_terms": "text-gray-600 hover:bg-gray-50",
        "active_privacy": "text-gray-600 hover:bg-gray-50",
        "active_refund": "bg-blue-50 text-blue-700",
        "content": """
        <h3 class="text-xl font-bold text-black uppercase tracking-wider mb-4">1. General Refund Terms</h3>
        <p>At PeopleXplus, we strive to provide exceptional value. If you are not satisfied with our Services, you may request a refund within 14 days of your initial purchase, subject to the conditions outlined below.</p>
        
        <h3 class="text-xl font-bold text-black uppercase tracking-wider mt-10 mb-4">2. Eligibility</h3>
        <p>Refunds are applicable only for annual subscriptions and first-time purchases. Monthly subscriptions, custom development fees, and one-time setup fees are non-refundable.</p>
        
        <h3 class="text-xl font-bold text-black uppercase tracking-wider mt-10 mb-4">3. Process</h3>
        <p>To request a refund, please contact our support team at support@peoplexplus.com with your account details and reason for cancellation. Refunds will be processed to the original payment method within 5-10 business days.</p>
        """
    }
]

import datetime
current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

for policy in policies:
    html = template.replace('{{TITLE}}', policy['title'])
    html = html.replace('{{SUBTITLE}}', policy['subtitle'])
    html = html.replace('{{ACTIVE_TERMS}}', policy['active_terms'])
    html = html.replace('{{ACTIVE_PRIVACY}}', policy['active_privacy'])
    html = html.replace('{{ACTIVE_REFUND}}', policy['active_refund'])
    html = html.replace('{{CONTENT}}', policy['content'])
    html = html.replace('{{DATE}}', current_date)
    
    with open(os.path.join(base_dir, policy['filename']), 'w', encoding='utf-8') as f:
        f.write(html)

print("Legal pages created.")

# Now update all footers in existing HTML files
html_files = glob.glob(os.path.join(base_dir, "*.html"))
for filepath in html_files:
    if os.path.basename(filepath) in [p['filename'] for p in policies]:
        continue # Already updated
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    old_footer_match = re.search(r'(<footer.*?</footer>)', content, re.DOTALL)
    if old_footer_match:
        old_footer = old_footer_match.group(1)
        new_footer = clean_footer(old_footer)
        content = content.replace(old_footer, new_footer)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
            
print("Global footers updated.")
