import os

files = [
    r"d:\project pxp\website\privacy-policy.html",
    r"d:\project pxp\website\refund-policy.html",
    r"d:\project pxp\website\terms-and-conditions.html"
]

script_to_add = """
    <!-- Fix Sidebar Navigation History -->
    <script>
        document.addEventListener('DOMContentLoaded', () => {
            const sidebarLinks = document.querySelectorAll('.sticky a');
            sidebarLinks.forEach(link => {
                link.addEventListener('click', (e) => {
                    e.preventDefault();
                    window.location.replace(link.href);
                });
            });
        });
    </script>
"""

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if "<!-- Fix Sidebar Navigation History -->" not in content:
        content = content.replace("</body>", script_to_add + "\n</body>")
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filepath}")
