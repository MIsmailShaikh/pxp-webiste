import os
import glob
import re

html_files = glob.glob(r"d:\project pxp\website\*.html")

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove Premium Page Transition CSS
    content = re.sub(r'<!-- Premium Page Transition CSS -->.*?</style>\s*', '', content, flags=re.DOTALL)
    
    # Remove Premium Page Transition JS
    content = re.sub(r'<!-- Premium Page Transition JS -->.*?</script>\s*', '', content, flags=re.DOTALL)
    
    # Also just in case there's any lingering Global Page Transition tags from the very first attempt
    content = re.sub(r'<!-- Global Page Transitions CSS -->.*?</style>\s*', '', content, flags=re.DOTALL)
    content = re.sub(r'<!-- Global Page Transitions JS -->.*?</script>\s*', '', content, flags=re.DOTALL)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"Removed all animations from {os.path.basename(file_path)}")
