import os
import glob
import re

html_files = glob.glob(r"d:\project pxp\website\*.html")

old_footer_support = """                        <ul class="space-y-2 md:space-y-4 text-[9px] sm:text-[11px] md:text-sm text-gray-400">
                            <li><a href="#" class="hover:text-white transition-colors">FAQ</a></li>
                            <li><a href="#" class="hover:text-white transition-colors">Documentation</a></li>
                            <li><a href="#" class="hover:text-white transition-colors">Tutorial</a></li>
                            <li><a href="#" class="hover:text-white transition-colors">Support</a></li>
                        </ul>"""

new_footer_support = """                        <ul class="space-y-2 md:space-y-4 text-[9px] sm:text-[11px] md:text-sm text-gray-400">
                            <li><a href="index11.html#faq" class="hover:text-white transition-colors">FAQ</a></li>
                            <li><a href="documentation.html" class="hover:text-white transition-colors">Documentation</a></li>
                            <li><a href="tutorial.html" class="hover:text-white transition-colors">Tutorial</a></li>
                            <li><a href="support.html" class="hover:text-white transition-colors">Support</a></li>
                        </ul>"""

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    modified = False
    
    # Update Footer Links
    if old_footer_support in content:
        content = content.replace(old_footer_support, new_footer_support)
        modified = True
        
    # Add id="faq" to index11.html
    if 'index11.html' in file_path:
        old_section = '<!-- NEW SECTION: FAQ Accordion -->\n    <section class="px-2 md:px-4 lg:px-6 pb-32 bg-white">'
        new_section = '<!-- NEW SECTION: FAQ Accordion -->\n    <section id="faq" class="px-2 md:px-4 lg:px-6 pb-32 bg-white">'
        if old_section in content:
            content = content.replace(old_section, new_section)
            modified = True
            
    if modified:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {os.path.basename(file_path)}")
