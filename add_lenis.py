import os
import glob

html_files = glob.glob(r"d:\project pxp\website\*.html")

lenis_script = """
    <!-- Lenis Smooth Scrolling -->
    <script src="https://unpkg.com/@studio-freight/lenis@1.0.42/dist/lenis.min.js"></script>
    <script>
        document.addEventListener("DOMContentLoaded", function() {
            if (typeof Lenis !== 'undefined') {
                const lenis = new Lenis({
                    duration: 1.2,
                    easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)), // https://www.desmos.com/calculator/brs54l4xou
                    direction: 'vertical',
                    gestureDirection: 'vertical',
                    smooth: true,
                    mouseMultiplier: 1,
                    smoothTouch: false,
                    touchMultiplier: 2,
                    infinite: false,
                })

                function raf(time) {
                    lenis.raf(time)
                    requestAnimationFrame(raf)
                }

                requestAnimationFrame(raf)
            }
        });
    </script>
"""

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if Lenis is already added
    if "lenis.min.js" not in content:
        # Replace </body> with the lenis script + </body>
        content = content.replace("</body>", lenis_script + "\n</body>")
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Added Lenis to {os.path.basename(file_path)}")
    else:
        print(f"Lenis already exists in {os.path.basename(file_path)}")
