import os

target_pages = [
    'privacy-policy.html', 
    'terms-and-conditions.html', 
    'refund-policy.html', 
    'support.html', 
    'about-us.html', 
    'case-studies.html', 
    'career.html', 
    'tutorial.html', 
    'documentation.html'
]

base_dir = r"d:\project pxp\website"

reveal_css = """
    <!-- Scroll Reveal CSS -->
    <style>
        .reveal-text {
            opacity: 0;
            transform: translateY(20px);
            transition: opacity 0.8s cubic-bezier(0.16, 1, 0.3, 1), transform 0.8s cubic-bezier(0.16, 1, 0.3, 1);
        }
        .reveal-text.revealed {
            opacity: 1;
            transform: translateY(0);
        }
    </style>
"""

reveal_js = """
    <!-- Scroll Reveal JS -->
    <script>
        document.addEventListener("DOMContentLoaded", () => {
            // Auto-add reveal class to textual elements in main content area
            document.querySelectorAll('h1, h2, h3, p, .grid > div').forEach((el, index) => {
                // Avoid navbar, footer, and sidebars
                if (!el.closest('nav') && !el.closest('footer') && !el.closest('.w-64') && !el.closest('form')) {
                    if (!el.classList.contains('reveal-text')) {
                        el.classList.add('reveal-text');
                        // Add slight stagger
                        el.style.transitionDelay = `${(index % 5) * 0.1}s`;
                    }
                }
            });

            const observer = new IntersectionObserver((entries, obs) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        entry.target.classList.add('revealed');
                        obs.unobserve(entry.target);
                    }
                });
            }, { threshold: 0.1, rootMargin: '0px 0px -20px 0px' });

            document.querySelectorAll('.reveal-text').forEach(el => observer.observe(el));
        });
    </script>
"""

for page in target_pages:
    file_path = os.path.join(base_dir, page)
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        modified = False
        if "Scroll Reveal CSS" not in content:
            content = content.replace("</head>", reveal_css + "\n</head>")
            modified = True
            
        if "Scroll Reveal JS" not in content:
            content = content.replace("</body>", reveal_js + "\n</body>")
            modified = True
            
        if modified:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Added reveal animations to {page}")
    else:
        print(f"Could not find {page}")
