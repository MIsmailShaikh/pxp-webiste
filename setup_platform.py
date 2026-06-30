import re

with open('d:\\project pxp\\website\\index11.html', 'r', encoding='utf-8') as f:
    content = f.read()

nav_match = re.search(r'(.*?</nav>)', content, re.DOTALL)
head_nav = nav_match.group(1) if nav_match else ''

footer_match = re.search(r'(<!-- NEW SECTION: Footer -->.*)', content, re.DOTALL)
footer = footer_match.group(1) if footer_match else '</body></html>'

skeleton = head_nav + """

    <!-- MAIN PLATFORM CONTENT -->
    <main class="pt-20">
        <!-- HERO SECTION -->
        <section class="bg-black text-white px-2 md:px-4 lg:px-6 py-20 min-h-screen relative overflow-hidden flex items-center justify-center">
        </section>

        <!-- HRM WORKFLOW SECTION -->
        <section class="bg-[#f8fafc] px-2 md:px-4 lg:px-6 py-32 relative overflow-hidden">
        </section>

        <!-- PAYROLL ENGINE SECTION -->
        <section class="bg-white px-2 md:px-4 lg:px-6 py-32 relative overflow-hidden">
        </section>

        <!-- MAIL SERVER SECTION -->
        <section class="bg-[#F3F5F7] px-2 md:px-4 lg:px-6 py-32 relative overflow-hidden">
        </section>
    </main>

""" + footer

with open('d:\\project pxp\\website\\platform.html', 'w', encoding='utf-8') as f:
    f.write(skeleton)

print('Skeleton created in platform.html')
