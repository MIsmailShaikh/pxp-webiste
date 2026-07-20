import os
import re

def main():
    css_dir = 'css'
    js_dir = 'js'
    
    if not os.path.exists(css_dir):
        os.makedirs(css_dir)
    if not os.path.exists(js_dir):
        os.makedirs(js_dir)
        
    html_files = [f for f in os.listdir('.') if f.endswith('.html')]
    
    for file in html_files:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        base_name = os.path.splitext(file)[0]
        css_file_name = f"{base_name}.css"
        js_file_name = f"{base_name}.js"
        
        # 1. Extract CSS
        style_matches = re.finditer(r'<style[^>]*>(.*?)</style>', content, re.DOTALL | re.IGNORECASE)
        extracted_css = []
        for match in style_matches:
            extracted_css.append(match.group(1).strip())
            
        # 2. Extract JS (only inline scripts, i.e., no src attribute)
        # Using a regex that captures `<script...>` but ensures `src=` is not present
        script_matches = re.finditer(r'<script(?![^>]*src=)[^>]*>(.*?)</script>', content, re.DOTALL | re.IGNORECASE)
        extracted_js = []
        for match in script_matches:
            code = match.group(1).strip()
            if code: # ignore empty script tags
                extracted_js.append(code)
                
        # Remove matched tags from HTML
        # Be careful to remove the same ones we extracted
        new_content = re.sub(r'<style[^>]*>.*?</style>', '', content, flags=re.DOTALL | re.IGNORECASE)
        new_content = re.sub(r'<script(?![^>]*src=)[^>]*>.*?</script>', '', new_content, flags=re.DOTALL | re.IGNORECASE)
        
        has_css = len(extracted_css) > 0
        has_js = len(extracted_js) > 0
        
        if has_css:
            with open(os.path.join(css_dir, css_file_name), 'w', encoding='utf-8') as f:
                f.write('\n\n'.join(extracted_css))
            
            # Inject link tag right before </head>
            link_tag = f'\n    <link rel="stylesheet" href="css/{css_file_name}">\n'
            head_end = new_content.find('</head>')
            if head_end != -1:
                new_content = new_content[:head_end] + link_tag + new_content[head_end:]
            else:
                # If no </head>, put it at top
                new_content = link_tag + new_content
                
        if has_js:
            with open(os.path.join(js_dir, js_file_name), 'w', encoding='utf-8') as f:
                # Wrap all extracted JS in an IIFE to prevent variable collisions? 
                # Actually, since it's one file per page, collisions only happen if they declared the same variable in multiple inline scripts on the same page.
                # If they did, it worked before, so it will work now. Let's just concatenate them.
                f.write('\n\n'.join(extracted_js))
                
            # Inject script tag right before </body>
            script_tag = f'\n    <script src="js/{js_file_name}"></script>\n'
            body_end = new_content.rfind('</body>')
            if body_end != -1:
                new_content = new_content[:body_end] + script_tag + new_content[body_end:]
            else:
                new_content = new_content + script_tag
                
        if has_css or has_js:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Processed {file}: Extracted {'CSS' if has_css else ''} {'JS' if has_js else ''}")

if __name__ == '__main__':
    main()
