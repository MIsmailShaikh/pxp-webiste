import os
import re

file_path = r"d:\project pxp\website\tutorial.html"
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the Filter Tabs
old_filters = """        <!-- Filter/Tabs -->
        <div class="flex flex-wrap justify-center gap-2 mb-12">
            <button class="px-6 py-2.5 rounded-full bg-black text-white text-sm font-semibold shadow-md">All Videos</button>
            <button class="px-6 py-2.5 rounded-full bg-gray-100 text-gray-600 text-sm font-medium hover:bg-gray-200 transition-colors">Getting Started</button>
            <button class="px-6 py-2.5 rounded-full bg-gray-100 text-gray-600 text-sm font-medium hover:bg-gray-200 transition-colors">Payroll</button>
            <button class="px-6 py-2.5 rounded-full bg-gray-100 text-gray-600 text-sm font-medium hover:bg-gray-200 transition-colors">Admin Tools</button>
        </div>"""

new_filters = """        <!-- Filter/Tabs -->
        <div class="flex flex-wrap justify-center gap-2 mb-12" id="filter-buttons">
            <button data-filter="all" class="filter-btn active px-6 py-2.5 rounded-full bg-black text-white text-sm font-semibold shadow-md transition-colors">All Videos</button>
            <button data-filter="getting-started" class="filter-btn px-6 py-2.5 rounded-full bg-gray-100 text-gray-600 text-sm font-medium hover:bg-gray-200 transition-colors">Getting Started</button>
            <button data-filter="payroll" class="filter-btn px-6 py-2.5 rounded-full bg-gray-100 text-gray-600 text-sm font-medium hover:bg-gray-200 transition-colors">Payroll</button>
            <button data-filter="admin" class="filter-btn px-6 py-2.5 rounded-full bg-gray-100 text-gray-600 text-sm font-medium hover:bg-gray-200 transition-colors">Admin Tools</button>
        </div>"""

content = content.replace(old_filters, new_filters)

# Replace the Video Grid items to add categories and modal triggers
old_card1 = """            <!-- Card 1 -->
            <div class="group cursor-pointer">"""
new_card1 = """            <!-- Card 1 -->
            <div class="video-card group cursor-pointer transition-all duration-300" data-category="getting-started">"""

old_card2 = """            <!-- Card 2 -->
            <div class="group cursor-pointer">"""
new_card2 = """            <!-- Card 2 -->
            <div class="video-card group cursor-pointer transition-all duration-300" data-category="payroll">"""

old_card3 = """            <!-- Card 3 -->
            <div class="group cursor-pointer">"""
new_card3 = """            <!-- Card 3 -->
            <div class="video-card group cursor-pointer transition-all duration-300" data-category="admin">"""

content = content.replace(old_card1, new_card1)
content = content.replace(old_card2, new_card2)
content = content.replace(old_card3, new_card3)

# Add Modal and Script just before </body>
modal_and_script = """
    <!-- Video Modal -->
    <div id="video-modal" class="fixed inset-0 z-50 flex items-center justify-center bg-black/80 backdrop-blur-sm opacity-0 pointer-events-none transition-opacity duration-300">
        <div class="relative w-full max-w-4xl mx-4 bg-gray-900 rounded-2xl overflow-hidden shadow-2xl scale-95 transition-transform duration-300" id="video-modal-content">
            <button id="close-modal" class="absolute top-4 right-4 z-10 w-10 h-10 bg-white/10 hover:bg-white/20 rounded-full flex items-center justify-center text-white transition-colors">
                <i data-lucide="x" class="w-5 h-5"></i>
            </button>
            <div class="aspect-video bg-black flex items-center justify-center relative border border-white/10 rounded-2xl m-2">
                <div class="text-center">
                    <i data-lucide="video" class="w-12 h-12 text-gray-500 mx-auto mb-4 opacity-50"></i>
                    <p class="text-white font-medium text-lg">Video Player Placeholder</p>
                    <p class="text-gray-400 text-sm mt-2">Your uploaded video will play here.</p>
                </div>
            </div>
        </div>
    </div>

    <!-- Interactivity Script -->
    <script>
        document.addEventListener('DOMContentLoaded', () => {
            // Filtering logic
            const filterBtns = document.querySelectorAll('.filter-btn');
            const videoCards = document.querySelectorAll('.video-card');

            filterBtns.forEach(btn => {
                btn.addEventListener('click', () => {
                    // Update active button styles
                    filterBtns.forEach(b => {
                        b.classList.remove('bg-black', 'text-white', 'shadow-md', 'active');
                        b.classList.add('bg-gray-100', 'text-gray-600');
                    });
                    btn.classList.remove('bg-gray-100', 'text-gray-600');
                    btn.classList.add('bg-black', 'text-white', 'shadow-md', 'active');

                    const filter = btn.getAttribute('data-filter');

                    // Filter cards
                    videoCards.forEach(card => {
                        if (filter === 'all' || card.getAttribute('data-category') === filter) {
                            card.style.display = 'block';
                            setTimeout(() => {
                                card.style.opacity = '1';
                                card.style.transform = 'translateY(0)';
                            }, 50);
                        } else {
                            card.style.opacity = '0';
                            card.style.transform = 'translateY(10px)';
                            setTimeout(() => {
                                card.style.display = 'none';
                            }, 300);
                        }
                    });
                });
            });

            // Modal logic
            const modal = document.getElementById('video-modal');
            const modalContent = document.getElementById('video-modal-content');
            const closeBtn = document.getElementById('close-modal');

            function openModal() {
                modal.classList.remove('opacity-0', 'pointer-events-none');
                modalContent.classList.remove('scale-95');
                modalContent.classList.add('scale-100');
            }

            function closeModal() {
                modal.classList.add('opacity-0', 'pointer-events-none');
                modalContent.classList.remove('scale-100');
                modalContent.classList.add('scale-95');
            }

            videoCards.forEach(card => {
                card.addEventListener('click', openModal);
            });

            closeBtn.addEventListener('click', closeModal);
            modal.addEventListener('click', (e) => {
                if(e.target === modal) closeModal();
            });
            
            // Allow Lucide icons to render in the modal
            if(typeof lucide !== 'undefined') {
                lucide.createIcons();
            }
        });
    </script>
"""

# Re-read content and safely insert script before Lenis or </body>
content = content.replace("<!-- Lenis Smooth Scrolling -->", modal_and_script + "\n    <!-- Lenis Smooth Scrolling -->")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated tutorial.html with filtering and modal logic.")
