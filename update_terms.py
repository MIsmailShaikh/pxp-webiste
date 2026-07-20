import os
import re

text = """
1. OVERVIEW
These Terms of Service (“Terms of Service”) set forth the general terms and conditions of your use of this website (“Site”) and the workforce management, payroll, and access control products and services purchased or accessed through this Site (individually and collectively, the “Services”).

Terms of Service and the documents to which they refer, form an agreement (“Agreement”) between PeopleXplus and you. The Agreement is made effective as of the date of your use of the Site or the date of electronic acceptance thereof, whichever occurs earlier. The terms “we”, “us” or “our” shall refer to PeopleXplus. The terms “you”, “your”, “User” or “Customer” shall refer to any individual or entity who accepts the Agreement, has access to a Customer account at PeopleXplus (“Account”) or uses the Services.

2. CONTRACTING ENTITY AND APPLICABLE TERMS AND POLICIES
Your use of this Site or Services is also governed by the applicable agreements and policies, which are incorporated into these Terms of Service by reference. Such agreements and policies include:
Privacy Policy
Refund Policy
other agreements and policies made available to you on the Site.
When your use of the Site or the Services requires us to process any personal data or personal information, we will do so in accordance with our Privacy Policy.

Your electronic acceptance of these Terms of Service signifies that you have read and understood these Terms of Service, along with the applicable policies and agreements, and agree to be bound by the Agreement.

PeopleXplus may, in its sole and absolute discretion, change or modify these Terms of Service, and any policies or agreements incorporated herein, at any time, and such changes shall be effective immediately upon posting to this Site. Your use of this Site or the Services after such changes or modifications shall constitute your acceptance of the Agreement as last revised.

3. ELIGIBILITY AND AUTHORISATIONS, SANCTIONS COMPLIANCE
This Site and the Services are available only to persons, who can form legally binding contracts under applicable law.
By using this Site or the Services, you represent and warrant that you:
(i) are at least eighteen (18) years old;
(ii) have the legal capacity to enter into an agreement with us;
(iii) are not a person barred from purchasing or receiving the Services under the laws applicable to these Terms of Service or other applicable jurisdiction;

If you are entering into this Agreement on behalf of a corporate entity, you represent and warrant that you have the legal authority to bind such corporate entity to this Agreement and to act on behalf of such entity with respect to any actions you take in connection with the Site or Services (in such cases, the terms “you”, “your”, “User” or “Customer” shall refer to such corporate entity).

4. ACCOUNT AND ITS MANAGEMENT
Account and information. In order to access certain features of this Site or use the Services, you will have to create an Account. You represent and warrant to PeopleXplus that all information you provide when creating your Account is accurate, current and complete. You agree to maintain and promptly update Account information and any other information you provide to PeopleXplus, to keep it accurate, current and complete.

Account security. You are solely responsible for all the activity on your Account. You agree to:
(i) keep your Account secure and follow our security recommendations, including, but not limited to, using strong passwords that adhere to industry-standard security criteria, keeping different login credentials for different Accounts and service providers, changing your password regularly for each Account, enabling two-factor authentication for an added layer of security;
(ii) maintain the confidentiality of your password and other information related to the security of your Account.
(iii) notify PeopleXplus immediately of any breach of security or unauthorized use of your Account.

PeopleXplus will not be liable for any loss you incur due to any unauthorized use of your Account.

5. AVAILABILITY OF SITE AND SERVICES
You acknowledge and agree that from time to time this Site may be inaccessible or inoperable for any reason including, but not limited to, maintenance, repairs or upgrades, or factors beyond our reasonable control (including, but not limited to, equipment failure, network issues, other failures or unforeseeable disruptions). You acknowledge and agree that we assume no liability to you or any other party with regard thereto.

6. GENERAL RULES OF CONDUCT
1. The Site and the Services are intended for your commercial or professional use. By utilizing them, you acknowledge and agree that your purpose is commercial or professional in nature.
2. You agree to use this Site and the Services in full compliance with the Agreement.
3. You are prohibited from using this Site or the Services in a manner (as determined by PeopleXplus in its sole and absolute discretion) that:
is illegal, promotes or encourages illegal content, activity, products or services;
infringes on the intellectual property rights or other proprietary rights of another Customer or any other person or entity;
violates the privacy or publicity rights of another Customer or any other person or entity;
contains or installs any viruses, worms, bugs, Trojan horses or other code, files or programs designed to, or capable of, using many resources, disrupting, damaging or limiting the functionality of any software or hardware;
interferes with the operation of this Site or the Services found at this Site.

7. CUSTOMER CONTENT AND CUSTOMER FEEDBACK
You are solely responsible for any and all Customer Content and Customer Feedback and any transactions or other activities related thereof conducted on or through the Account. By posting or publishing Customer Content or Customer Feedback to this Site or to the Services, you represent and warrant to PeopleXplus that you have all necessary rights, licenses, consents, and permissions to distribute Customer Content or Customer Feedback in such manner.

8. PEOPLE X PLUS CONTENT
Content ownership. Except for Customer Content, the content on this Site and the Services, including the data, text, software, scripts, source code, APIs, computer code, applications, graphics, photos, sounds, music, videos, interactive features, artwork, designs, animations, interfaces, algorithms, trademarks, service marks, trade names, and other proprietary identifiers (“PeopleXplus Content”), are owned by or licensed to PeopleXplus. PeopleXplus Content is protected by copyright laws.

9. MONITORING OF CUSTOMER CONTENT
By using this Site and (or) any Service, you agree not to make available or accessible any illegal content or content that is incompatible with or violates the Agreement. PeopleXplus generally does not pre-screen Customer Content. However, PeopleXplus reserves the right (but undertakes no duty) to do so and decide whether any item of Customer Content is appropriate and (or) complies with this Agreement.

10. ADDITIONAL RESERVATION OF RIGHTS
PeopleXplus expressly reserves the right to deny, cancel, terminate, suspend, lock, or modify (including access to or control of) any Account and (or) Services for any reason (as determined by PeopleXplus in its sole and absolute discretion).

11. LINKS TO THIRD-PARTY WEBSITES
This Site and the Services may include (through hyperlinks, banner advertising or otherwise) links to third-party websites that are not owned or controlled by PeopleXplus (“Linked Sites”). PeopleXplus assumes no responsibility for the content, terms and conditions, privacy policies, or practices of any Linked Sites and does not monitor or modify their content. By using this Site or the Services, you expressly release PeopleXplus from all liability arising from your use of any Linked Sites.

12. FEES, PAYMENTS, REFUNDS AND AUTO-RENEWAL
General terms. You agree that your Payment Method will be charged by PeopleXplus in the course of purchasing Services.
All our paid Services are provided on a subscription basis, unless indicated otherwise. You choose the period of Services and the Payment Method yourself when you purchase the Services. After your chosen first subscription period ends, the provision of Services will be auto-renewed for an additional (subsequent) subscription period.
By purchasing Services on a subscription basis and submitting your payment-related information to make a purchase of the Services, you explicitly agree and consent that (i) Services will be auto-renewed until you disable auto-renewal feature, and (ii) you are authorizing recurring payments.
"""

def text_to_html(text):
    lines = text.strip().split('\n')
    html_out = []
    
    in_list = False
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        # Check if heading (starts with Number.)
        if re.match(r'^\d+\.', line):
            if in_list:
                html_out.append("</ul>")
                in_list = False
            html_out.append(f'<h3 class="text-xl font-bold text-black uppercase tracking-wider mt-10 mb-4">{line}</h3>')
        # Check if list item (starts with lowercase letter or roman numeral)
        elif line.startswith('(') or (line[0].islower() and not line.startswith('is illegal')) or line.startswith('is illegal') or line.startswith('infringes') or line.startswith('violates') or line.startswith('contains or installs') or line.startswith('interferes'):
            if not in_list:
                html_out.append('<ul class="list-disc pl-5 space-y-2 text-gray-700">')
                in_list = True
            html_out.append(f'<li>{line}</li>')
        else:
            if in_list:
                html_out.append("</ul>")
                in_list = False
            html_out.append(f'<p class="mb-4 text-gray-700">{line}</p>')
            
    if in_list:
        html_out.append("</ul>")
        
    return "\n".join(html_out)


html_content = text_to_html(text)

# Read Terms of Service file
path = r"d:\project pxp\website\terms-and-conditions.html"
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace content
start_marker = '<div class="prose prose-gray max-w-none text-gray-700 space-y-6">'
end_marker = '</div>\n        </div>\n    </div>\n\n    <!-- FOOTER -->'

start_idx = content.find(start_marker)
end_idx = content.find(end_marker)

if start_idx != -1 and end_idx != -1:
    new_content = content[:start_idx + len(start_marker)] + "\n" + html_content + "\n            " + content[end_idx:]
    with open(path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Successfully updated terms-and-conditions.html")
else:
    print("Could not find insertion points")
