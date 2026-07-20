import os
import glob
import re

html_files = glob.glob(r"d:\project pxp\website\*.html")

old_footer_company = """                        <ul class="space-y-2 md:space-y-4 text-[9px] sm:text-[11px] md:text-sm text-gray-400">
                            <li><a href="#" class="hover:text-white transition-colors">About Us</a></li>
                            <li><a href="#" class="hover:text-white transition-colors">Career</a></li>
                            <li><a href="#" class="hover:text-white transition-colors">Case Studies</a></li>
                            <li><a href="#" class="hover:text-white transition-colors">Contact Us</a></li>
                        </ul>"""

new_footer_company = """                        <ul class="space-y-2 md:space-y-4 text-[9px] sm:text-[11px] md:text-sm text-gray-400">
                            <li><a href="about-us.html" class="hover:text-white transition-colors">About Us</a></li>
                            <li><a href="career.html" class="hover:text-white transition-colors">Career</a></li>
                            <li><a href="case-studies.html" class="hover:text-white transition-colors">Case Studies</a></li>
                            <li><a href="support.html" class="hover:text-white transition-colors">Contact Us</a></li>
                        </ul>"""

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if old_footer_company in content:
        content = content.replace(old_footer_company, new_footer_company)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {os.path.basename(file_path)}")
