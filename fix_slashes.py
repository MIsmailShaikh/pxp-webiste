import os

for f in ['pricing.html', 'index11.html']:
    path = os.path.join(r'd:\project pxp\website', f)
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as file:
            c = file.read()
        
        # Fixing the bad replacement from earlier
        c = c.replace(r"onclick=\"requireAuth('checkout.html?plan=workforce-essential\')\" ", "onclick=\"requireAuth('checkout.html?plan=workforce-essential')\" ")
        c = c.replace(r"\')", "')")
        
        with open(path, 'w', encoding='utf-8') as file:
            file.write(c)
print('Fixed backslashes')
