import os
import re

text = """
1. INTRODUCTION
PeopleXplus group entity, the details of which are indicated in the PeopleXplus's Terms of Service, ("PeopleXplus") provides you workforce management, payroll, and related products and service.

PeopleXplus seeks to ensure the highest level of data privacy when offering its variety of quality products and services to PeopleXplus customers and subscribers ("Subscribers") (collectively, "You", or "Users").

At PeopleXplus, the privacy and security of our Users is of paramount importance. PeopleXplus is committed to protecting the data you share with us.

When this Policy mentions "PeopleXplus", "we," "us", or "our", it refers to PeopleXplus that is responsible for protection of your personal information in line with this Privacy Policy ("Data Controller").

This Privacy Policy ("Policy") explains how PeopleXplus processes information that can be used to directly or indirectly identify an individual ("Personal Data") collected on our Site, our services ("Service"), forums and our mobile applications ("Platform").

All personal data are processed in accordance with the General Data Protection Regulation (EU) 2016/679 ("GDPR").

For any questions regarding this Policy or any requests regarding the processing of personal data, please contact us at privacy@peoplexplus.com.

2. GENERAL PRINCIPLES. CONFIDENTIALITY
PeopleXplus shall process all Personal Data adhering to the general data processing principles:

lawfully, fairly and in a transparent manner in relation to the data subject (lawfulness, fairness, and transparency);
collect and process Personal Data only for specified, explicit and legitimate purposes and not further processed in a manner that is incompatible with those purposes (purpose limitation);
ensure that Personal Data is adequate, relevant and limited to what is necessary for relation to the purposes for which they are processed (data minimization);
ensure that Personal Data is accurate and, where necessary, kept up to date (accuracy);
ensure that Personal Data is kept in a form which permits identification of data subjects for no longer than is necessary for the purposes for which the personal data are processed (storage limitation);
process Personal Data in a manner that ensures appropriate security of the personal data, including protection against unauthorized or unlawful processing and against accidental loss, destruction or damage, using appropriate technical or organizational measures (integrity and confidentiality).

All and any information stored on PeopleXplus's Platform is treated as strictly confidential. All information is stored securely and is accessed by qualified and authorized personnel only.

3. INFORMATION WE COLLECT
3.1. Information You provide to us.

Information that is necessary for the use of the PeopleXplus Platform

We ask for and collect the following personal information about you when you use the PeopleXplus Platform. This information is necessary for the adequate performance of the contractual arrangement which is in place between you and us and to allow us to comply with our legal obligations. Failing to provide any of this data or decision to delete or object to the processing of any of such data may result in de-activation of your PeopleXplus Account.

Account Signup Information. When you sign up to PeopleXplus, we require you to provide minimum information - email address and password. In some particular cases we ask you to provide more information - such as your first and last name, identity verification, contact details.
Login information. We collect Login scope and Email scope from Google, and email from Facebook/Microsoft.
Identity verification information. Before the onboarding of your business or thereafter, PeopleXplus may collect identity verification information (such as images of your passport, national ID card, valid driving license or other documents as required or permitted by applicable laws or regulations).
Operational verification information. In certain operational, legal, abuse-prevention, or compliance-related situations, we may collect and process additional information and supporting documentation necessary to investigate, verify, or resolve requests and disputes.
Payment Information. To order and use features of the PeopleXplus Platform, we may require you to provide certain financial information in order to facilitate the processing of payments. We use 3rd party (payment processor) services, so we do not collect and store credit card information.
Communications, Chats, Messaging. When you communicate with PeopleXplus, we collect information about your communication and any information you choose to provide or disclose.
Job applicants' information. We also collect information that you provided to us by applying to any of the open career positions.
Participation information. When you apply to, register for, or participate in any programme, partnership, or initiative offered by PeopleXplus, we collect the information you provide.
Visitors and users of our User's websites or services. We may also collect information pertaining to visitors and users of our User's websites or services ("Users-of-Users"), solely for and on our Users' behalf.

3.2. Information We Collect when You use the Platform
When you use the PeopleXplus Platform or contact us directly by any communication channel, we may collect information, including personal information, about the services you use and how you use them.

Log data and Device information. We automatically collect log data and device information when you access and use the PeopleXplus Platform.
Tracking technologies and Cookies. We use cookies, beacons, tags, scripts and other similar technologies.
Usage information. We use tools to collect information about your interactions with the PeopleXplus Platform.
Geo-location data. We collect information about your approximate location as determined by data such as your IP address.

4. HOW WE USE YOUR DATA?
We use, store, combine and process information, including personal information, about you to provide, understand, improve, and develop the PeopleXplus Platform, create and maintain a trusted and safer environment and comply with our legal obligations.

To Identify. Personal identification information is collected and processed for the purposes of User identification.
To Create and Maintain Trusted Environment. We verify or authenticate information or identifications provided by you.
To Create Aggregated Statistical Data. To Carry out Market Research and Analysis necessary for running out our business.
To Stay Connected. We use information about data usage, devices, operating systems to diagnose problems.
To Send Service and Billing Messages. PeopleXplus may also contact you with important information regarding our Services.

5. SECURITY
PeopleXplus has implemented security measures designed to protect the Personal Information you share with us, including physical, electronic and procedural measures. Among other things, we offer HTTPS secure access to most areas on our Services. We also regularly monitor our systems for possible vulnerabilities and attacks.

Regardless of the measures and efforts taken by PeopleXplus, we cannot and do not guarantee the absolute protection and security of your Personal Information.

6. YOUR RIGHTS
You are entitled to a range of rights regarding the protection of your Personal Data, which are subject to limitations, restrictions and conditions as laid down in GDPR and applicable law. Those rights are:
the right to access the information we process about you;
the right to rectify incorrect/inaccurate information about you;
the right to transfer all or part of the information collected about you to you or another data controller;
the right to erase any data concerning you;
the right to the restriction of data processing;
the right to object to the processing of Personal Data.

Where the processing of your personal data is based on your consent, you can withdraw your consent at any time by contacting us at privacy@peoplexplus.com.
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
        # Check if list item (starts with lowercase letter or short phrase without punctuation at end of previous)
        elif line.endswith(';') or line.endswith(';)'):
            if not in_list:
                html_out.append('<ul class="list-disc pl-5 space-y-2 text-gray-700">')
                in_list = True
            html_out.append(f'<li>{line}</li>')
        else:
            if in_list:
                # end list if previous was list item and this doesn't look like one
                html_out.append("</ul>")
                in_list = False
            html_out.append(f'<p class="mb-4 text-gray-700">{line}</p>')
            
    if in_list:
        html_out.append("</ul>")
        
    return "\n".join(html_out)


html_content = text_to_html(text)

# Read privacy policy file
path = r"d:\project pxp\website\privacy-policy.html"
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
    print("Successfully updated privacy-policy.html")
else:
    print("Could not find insertion points")
