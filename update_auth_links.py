import os
import re

files_to_update = ['pricing.html', 'index11.html']
base_dir = r"d:\project pxp\website"

for filename in files_to_update:
    filepath = os.path.join(base_dir, filename)
    if not os.path.exists(filepath):
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Replace the checkout redirect
    content = content.replace("onclick=\"window.location.href='checkout.html", "onclick=\"requireAuth('checkout.html")
    
    # Inject auth-guard script if not present
    if "auth-guard.js" not in content:
        # Add to head
        head_end = content.find("</head>")
        if head_end != -1:
            injection = '    <script src="js/auth-guard.js"></script>\n'
            content = content[:head_end] + injection + content[head_end:]
            
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Updated files successfully.")
