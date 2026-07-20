import os
import glob

html_files = glob.glob(r"d:\project pxp\website\*.html")

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # We want to replace the bad exclusion CSS
    bad_css = """        /* Ensure navbar and sidebars are excluded from global staggers if caught */
        nav, nav *, .w-64, .w-64 * {
            animation: none !important;
            opacity: 1 !important;
            transform: none !important;
        }"""
        
    good_css = """        /* Ensure navbar and sidebars are excluded from global staggers if caught */
        nav, nav *, .w-64, .w-64 * {
            animation: none !important;
        }"""
        
    if bad_css in content:
        content = content.replace(bad_css, good_css)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed navbar transform bug in {os.path.basename(file_path)}")
