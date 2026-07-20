import os

files_to_update = ['pricing.html', 'index11.html']
base_dir = r"d:\project pxp\website"

for filename in files_to_update:
    filepath = os.path.join(base_dir, filename)
    if not os.path.exists(filepath):
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # We need to find onclick="requireAuth('checkout.html...'"
    # and replace it with onclick="requireAuth('checkout.html...')"
    
    import re
    # This regex looks for requireAuth('...'" and replaces with requireAuth('...')")
    # Actually, the current state is onclick="requireAuth('checkout.html?plan=abc'"
    # So we want to replace '" with ')" ONLY for requireAuth.
    # Let's use re.sub
    
    content = re.sub(r'onclick="requireAuth\((.*?)\'"', r'onclick="requireAuth(\1\')" ', content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Fixed syntax errors successfully.")
