import os
import re

text = """
1. STANDARD REFUND TERMS
Products purchased from PeopleXplus may be refunded only if canceled within 30 days of the date of the transaction.

Note: Due to their nature, cryptocurrencies, tokens and digital assets are generally irreversible and their exchange rates are highly volatile and transitory. We can not be responsible for any risk including but not limited to exchange rate risk and market risk. Products purchased using cryptocurrencies, tokens or digital assets will not be refunded.

Note: If a client's actions are found to violate applicable laws or PeopleXplus's Terms of Services, any payments made to PeopleXplus will not be refunded.

“Date of the transaction,” for the purpose of this Refund Policy, means the date of purchase of any product or service, which includes the date any renewal is processed by PeopleXplus in accordance with the terms and conditions of the applicable product or service agreement (Terms of Use). You may cancel a product at any time, but a refund will only be issued if cancellation is requested within the refund timeframe specified for the applicable product, if available at all. Note: Some products have different policies or requirements for a refund associated with them, including some products that are not eligible for a refund under any circumstance. Please see below for refund terms applicable to such products:

2. PRODUCTS AVAILABLE FOR REFUND UNDER STANDARD TERMS
Workforce OS Subscriptions (Annual Plans)
Payroll Engine Subscriptions (Annual Plans)
Access Control Subscriptions (Annual Plans)
Priority Support Add-on

3. PRODUCTS NOT AVAILABLE FOR REFUNDS
Monthly Subscription Renewals (after the first month)
One-Time Setup Fees
Custom Development or Integration Services
Hardware Devices (Biometric Scanners, Access Cards) once shipped and opened
White-label Branding Add-ons
On-site Training or Consulting Services
Any products or services that were suspended, canceled, or terminated due to the abusive usage of the products, services, or any other violation of the Terms and Conditions are not eligible for a refund.

The purpose of the refund is for customers to try and understand whether the services provided by PeopleXplus suit their needs. In any way, PeopleXplus will not tolerate abusive usage of refunds (i.e., refunding the same services multiple times and (or) repetitively purchasing and asking for a refund for services purchased in bulk, etc.). PeopleXplus remains a right to unilaterally decline the request for a refund if any of the signs related to the abusage of the refunds occur.

4. REFUNDS FOR SPECIAL DEALS
From time to time, PeopleXplus offers special deals such as a free hardware scanner when buying a 24-month Access Control plan.

Such free hardware provided as part of special deals is non-refundable and cannot be exchanged. If a refund is requested on the software subscription, PeopleXplus remains the right to deduct the retail price of the free hardware from the refunded amount.

5. CHARGEBACKS
If at any time, we record a decline, chargeback, reversal, payment dispute, risk of payment fraud or other rejection of a charge of any payable fees on your PeopleXplus account (“Chargeback”), this will be considered as a breach of your payment obligations hereunder, therefore you agree that PeopleXplus may pursue all available lawful remedies in order to obtain payment, including but not limited to, immediate termination, without notice to you, of your PeopleXplus account and any services active on your behalf (“Services”).

In the event a Chargeback is performed, your PeopleXplus account may be blocked without the option to re-purchase or re-use it, and any data contained in such a PeopleXplus account may be subject to cancellation and loss of data.

Your use of the PeopleXplus Services will not resume until you:
verify the payment method used for the disputed transaction.
pay any applicable fees in full, including any fees and expenses incurred by PeopleXplus.

If you have any questions or concerns regarding a payment made to PeopleXplus, we encourage you to first contact our Customer Support team at support@peoplexplus.com before filing a Chargeback.
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
        # Check if list item (doesn't start with Note:, starts without punctuation but is short and no period at end, or we manually enforce based on content)
        # For simplicity, if a line doesn't end in punctuation and doesn't start with Note, we'll treat it as a list item if it's under 100 chars
        elif not line.endswith('.') and not line.endswith(')') and not line.startswith('Note:') and len(line) < 100:
            if not in_list:
                html_out.append('<ul class="list-disc pl-5 space-y-2 text-gray-700">')
                in_list = True
            html_out.append(f'<li>{line}</li>')
        else:
            if in_list:
                html_out.append("</ul>")
                in_list = False
            
            # Format notes in bold or a light grey box
            if line.startswith('Note:'):
                line = f'<span class="font-bold">{line[:5]}</span>{line[5:]}'
                
            html_out.append(f'<p class="mb-4 text-gray-700">{line}</p>')
            
    if in_list:
        html_out.append("</ul>")
        
    return "\n".join(html_out)


html_content = text_to_html(text)

# Read refund policy file
path = r"d:\project pxp\website\refund-policy.html"
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
    print("Successfully updated refund-policy.html")
else:
    print("Could not find insertion points")
