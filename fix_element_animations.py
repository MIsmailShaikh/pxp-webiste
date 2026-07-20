import os
import glob
import re

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

# Pure CSS approach is infinitely robust and causes no "stuck" invisible text
robust_css = """
    <!-- Robust Reveal CSS -->
    <style>
        /* Animate standard textual elements on load */
        .prose > *, .max-w-3xl > *, .max-w-7xl > *, .grid > div {
            animation: robustFadeUp 0.8s cubic-bezier(0.16, 1, 0.3, 1) both;
        }
        
        /* Stagger the animations so they cascade beautifully */
        .prose > *:nth-child(1), .max-w-3xl > *:nth-child(1) { animation-delay: 0.05s; }
        .prose > *:nth-child(2), .max-w-3xl > *:nth-child(2) { animation-delay: 0.1s; }
        .prose > *:nth-child(3), .max-w-3xl > *:nth-child(3) { animation-delay: 0.15s; }
        .prose > *:nth-child(4), .max-w-3xl > *:nth-child(4) { animation-delay: 0.2s; }
        .prose > *:nth-child(5), .max-w-3xl > *:nth-child(5) { animation-delay: 0.25s; }
        .prose > *:nth-child(n+6), .max-w-3xl > *:nth-child(n+6) { animation-delay: 0.3s; }
        
        /* Ensure navbar and sidebars are excluded from global staggers if caught */
        nav, nav *, .w-64, .w-64 * {
            animation: none !important;
            opacity: 1 !important;
            transform: none !important;
        }

        @keyframes robustFadeUp {
            from {
                opacity: 0;
                transform: translateY(25px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
    </style>
"""

for page in target_pages:
    file_path = os.path.join(base_dir, page)
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Strip old broken JS approach
        content = re.sub(r'<!-- Scroll Reveal CSS -->.*?</style>\s*', '', content, flags=re.DOTALL)
        content = re.sub(r'<!-- Scroll Reveal JS -->.*?</script>\s*', '', content, flags=re.DOTALL)
        
        # Inject new robust CSS
        if "Robust Reveal CSS" not in content:
            content = content.replace("</head>", robust_css + "\n</head>")
            
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
            
        print(f"Fixed animations in {page} with robust CSS")
