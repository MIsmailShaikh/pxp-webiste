import os
import glob

base_dir = r"d:\project pxp\website"
html_files = glob.glob(os.path.join(base_dir, "*.html"))

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Replace desktop Log in
    content = content.replace(
        '<a href="#" class="hidden sm:block text-sm font-medium hover:opacity-70 px-4">Log in</a>',
        '<a href="login.html" class="hidden sm:block text-sm font-medium hover:opacity-70 px-4">Log in</a>'
    )
    
    # Replace mobile Log in
    content = content.replace(
        '<a href="#" class="px-3 py-2.5 rounded-xl hover:bg-gray-50 text-sm font-semibold text-gray-900 transition-colors">Log in</a>',
        '<a href="login.html" class="px-3 py-2.5 rounded-xl hover:bg-gray-50 text-sm font-semibold text-gray-900 transition-colors">Log in</a>'
    )
    
    # Replace desktop Get started
    content = content.replace(
        '<a href="#"\n                class="hidden sm:flex bg-black text-white px-5 py-2.5 rounded-full text-sm font-medium hover:bg-gray-800 transition-all items-center gap-2 group shadow-lg shadow-black/20">\n                Get started',
        '<a href="pricing.html"\n                class="hidden sm:flex bg-black text-white px-5 py-2.5 rounded-full text-sm font-medium hover:bg-gray-800 transition-all items-center gap-2 group shadow-lg shadow-black/20">\n                Get started'
    )
    # Also without newlines in case it's minified or different
    content = content.replace(
        '<a href="#" class="hidden sm:flex bg-black text-white px-5 py-2.5 rounded-full text-sm font-medium hover:bg-gray-800 transition-all items-center gap-2 group shadow-lg shadow-black/20">\n                Get started',
        '<a href="pricing.html" class="hidden sm:flex bg-black text-white px-5 py-2.5 rounded-full text-sm font-medium hover:bg-gray-800 transition-all items-center gap-2 group shadow-lg shadow-black/20">\n                Get started'
    )
    
    # Replace mobile Get started
    content = content.replace(
        '<a href="#" class="mt-2 w-full bg-black text-white px-5 py-3 rounded-xl text-sm font-medium hover:bg-gray-800 transition-all flex items-center justify-center gap-2 group shadow-lg shadow-black/20">\n                    Get started',
        '<a href="pricing.html" class="mt-2 w-full bg-black text-white px-5 py-3 rounded-xl text-sm font-medium hover:bg-gray-800 transition-all flex items-center justify-center gap-2 group shadow-lg shadow-black/20">\n                    Get started'
    )
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Updated navbars in all HTML files.")
