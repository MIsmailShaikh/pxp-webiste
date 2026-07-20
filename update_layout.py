import os
import re

def update_files():
    # Read index11.html
    with open('index11.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract Nav
    nav_match = re.search(r'(<nav.*?</nav>)', content, re.DOTALL)
    if not nav_match:
        print("Could not find nav in index11.html")
        return
    nav_html = nav_match.group(1)

    # Extract Footer
    footer_match = re.search(r'(<footer.*?</footer>)', content, re.DOTALL)
    if not footer_match:
        print("Could not find footer in index11.html")
        return
    footer_html = footer_match.group(1)

    # Hardcode JS to insert because regex extraction can be fragile
    js_code = """
        // Mobile Menu Toggle Logic
        const mobileMenuBtn = document.getElementById('mobile-menu-btn');
        const mobileMenu = document.getElementById('mobile-menu');
        let isMobileMenuOpen = false;

        if (mobileMenuBtn && mobileMenu) {
            mobileMenuBtn.addEventListener('click', (event) => {
                event.stopPropagation();
                isMobileMenuOpen = !isMobileMenuOpen;
                if (isMobileMenuOpen) {
                    mobileMenu.classList.remove('hidden');
                    // Small delay to allow display block to apply before animating
                    setTimeout(() => {
                        mobileMenu.classList.remove('opacity-0', 'scale-y-95');
                        mobileMenu.classList.add('opacity-100', 'scale-y-100');
                    }, 10);
                    // Change icon to close (X)
                    mobileMenuBtn.innerHTML = '<i data-lucide="x" class="w-6 h-6 text-gray-900"></i>';
                    if (window.lucide) window.lucide.createIcons();
                } else {
                    mobileMenu.classList.remove('opacity-100', 'scale-y-100');
                    mobileMenu.classList.add('opacity-0', 'scale-y-95');
                    setTimeout(() => {
                        mobileMenu.classList.add('hidden');
                    }, 300); // Wait for transition
                    // Change icon back to menu
                    mobileMenuBtn.innerHTML = '<i data-lucide="menu" class="w-6 h-6 text-gray-900"></i>';
                    if (window.lucide) window.lucide.createIcons();
                }
            });

            // Close mobile menu when clicking outside
            document.addEventListener('click', (event) => {
                // Ensure we only close if the click is outside the menu
                if (isMobileMenuOpen && !mobileMenu.contains(event.target)) {
                    mobileMenuBtn.click();
                }
            });
        }
"""

    html_files = [f for f in os.listdir('.') if f.endswith('.html') and f != 'index11.html']

    for file in html_files:
        try:
            with open(file, 'r', encoding='utf-8') as f:
                file_content = f.read()
        except UnicodeDecodeError:
            print(f"Skipping {file} due to encoding issues")
            continue
        
        modified = False
        
        # Replace nav
        if re.search(r'<nav.*?</nav>', file_content, re.DOTALL):
            # Using a lambda handles backslashes correctly during regex replacement
            file_content = re.sub(r'<nav.*?</nav>', lambda _: nav_html, file_content, flags=re.DOTALL)
            modified = True
            
        # Replace footer
        if file != 'workforce-os.html':
            if re.search(r'<footer.*?</footer>', file_content, re.DOTALL):
                file_content = re.sub(r'<footer.*?</footer>', lambda _: footer_html, file_content, flags=re.DOTALL)
                modified = True
                
        # Inject JS if not present
        if 'mobileMenuBtn.addEventListener' not in file_content:
            # We'll inject it before the last </script> tag
            script_match = list(re.finditer(r'</script>', file_content))
            if script_match:
                last_script_end = script_match[-1].start()
                file_content = file_content[:last_script_end] + js_code + file_content[last_script_end:]
                modified = True
            else:
                # no script tag, add one before body
                body_match = file_content.rfind('</body>')
                if body_match != -1:
                    file_content = file_content[:body_match] + '<script>' + js_code + '</script>\n' + file_content[body_match:]
                    modified = True

        if modified:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(file_content)
            print(f"Updated {file}")

if __name__ == '__main__':
    update_files()
