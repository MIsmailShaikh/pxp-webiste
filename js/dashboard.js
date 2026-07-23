document.addEventListener('DOMContentLoaded', async () => {
    const token = localStorage.getItem('pxp_token');
    
    // If no token, auth-guard will redirect, but just in case
    if (!token) return;

    try {
        // Fetch user data from the new endpoint
        const response = await fetch('/api/user/me', {
            method: 'GET',
            headers: {
                'Authorization': `Bearer ${token}`
            }
        });

        if (!response.ok) {
            throw new Error('Failed to fetch user data');
        }

        const user = await response.json();
        
        // Hide loader, show content
        document.getElementById('loader').classList.add('hidden');
        document.getElementById('dashboard-content').classList.remove('hidden');
        document.getElementById('dashboard-content').classList.add('flex');

        // Update welcome message
        const firstName = user.full_name ? user.full_name.split(' ')[0] : 'User';
        document.getElementById('welcome-message').textContent = `Hi, ${firstName}! Welcome back.`;

        // Render Plans
        renderPlans(user);

    } catch (error) {
        console.error('Error loading dashboard:', error);
        // Fallback UI or redirect to login
        localStorage.removeItem('pxp_logged_in');
        localStorage.removeItem('pxp_token');
        window.location.href = 'login.html';
    }
});

function renderPlans(user) {
    const container = document.getElementById('plans-container');
    
    // Check what plans they have. 
    // In our schema, we have `current_plan` and `subscription_status`.
    // For this example, let's assume they have no paid plan if `subscription_status` is 'free'.
    
    if (user.subscription_status === 'free' || !user.current_plan) {
        // Render empty state card
        container.innerHTML = `
            <div class="bg-white border border-gray-200 rounded-2xl p-6 shadow-sm">
                <div class="flex flex-col items-center justify-center text-center py-8">
                    <div class="w-16 h-16 bg-gray-100 rounded-full flex items-center justify-center mb-4">
                        <i data-lucide="package-open" class="w-8 h-8 text-gray-400"></i>
                    </div>
                    <h3 class="text-lg font-bold text-gray-900 mb-1">No active services</h3>
                    <p class="text-gray-500 text-sm max-w-md mb-6">You are currently on the free tier. Upgrade your account to access Corporate Email, Workforce OS, and Payroll Engine.</p>
                    <a href="pricing.html" class="bg-primary text-white hover:bg-primaryHover font-semibold py-2.5 px-6 rounded-full transition-colors shadow-md shadow-primary/20">
                        Upgrade Plan
                    </a>
                </div>
            </div>
        `;
    } else {
        // Render Active Plan Card (Hostinger Style)
        
        // Format the plan name to look nice (e.g. 'business' -> 'Business Plan')
        const planName = (user.current_plan || 'Business').charAt(0).toUpperCase() + (user.current_plan || 'business').slice(1) + ' Plan';
        
        container.innerHTML = `
            <div class="bg-white border border-gray-200 rounded-2xl shadow-sm overflow-visible relative group">
                <!-- Header of card -->
                <div class="p-5 border-b border-gray-100 flex justify-between items-center">
                    <div>
                        <h3 class="text-lg font-bold text-gray-900">${planName}</h3>
                        <p class="text-xs text-gray-500 mt-0.5">Status: <span class="text-green-600 font-semibold uppercase tracking-wider text-[10px]">Active</span></p>
                    </div>
                    <div class="flex gap-2">
                        <button class="hidden sm:block px-4 py-1.5 text-sm font-semibold text-primary border border-primary/20 rounded-md hover:bg-primary/5 transition-colors">
                            Upgrade
                        </button>
                        <button class="px-4 py-1.5 text-sm font-semibold bg-primary text-white rounded-md hover:bg-primaryHover transition-colors shadow-md shadow-primary/20">
                            Manage Services
                        </button>
                    </div>
                </div>
                
                <!-- Sub-items inside card -->
                <div class="p-5 flex flex-col gap-4">
                    
                    <!-- App: Workforce OS -->
                    <div class="flex items-center justify-between border border-gray-100 bg-gray-50/50 p-4 rounded-xl">
                        <div class="flex items-center gap-4">
                            <div class="w-10 h-10 bg-white rounded-lg border border-gray-200 shadow-sm flex items-center justify-center shrink-0">
                                <i data-lucide="users" class="w-5 h-5 text-gray-700"></i>
                            </div>
                            <div>
                                <h4 class="text-sm font-bold text-gray-900">Workforce OS</h4>
                                <p class="text-xs text-gray-500 mt-0.5">HR & Attendance Dashboard</p>
                            </div>
                        </div>
                        <div class="flex items-center gap-3">
                            <a href="workforce-os.html" class="px-3 py-1.5 text-xs font-semibold bg-white border border-gray-200 text-gray-700 rounded hover:bg-gray-50 transition-colors">Launch App</a>
                        </div>
                    </div>

                    <!-- App: Corporate Email -->
                    <div class="flex items-center justify-between border border-gray-100 bg-gray-50/50 p-4 rounded-xl">
                        <div class="flex items-center gap-4">
                            <div class="w-10 h-10 bg-white rounded-lg border border-gray-200 shadow-sm flex items-center justify-center shrink-0">
                                <i data-lucide="mail" class="w-5 h-5 text-gray-700"></i>
                            </div>
                            <div>
                                <h4 class="text-sm font-bold text-gray-900">Corporate Email</h4>
                                <p class="text-xs text-gray-500 mt-0.5">5 active mailboxes</p>
                            </div>
                        </div>
                        <div class="flex items-center gap-3">
                            <button class="px-3 py-1.5 text-xs font-semibold text-gray-600 hover:text-gray-900 transition-colors">Settings</button>
                            <a href="corporate-email.html" class="px-3 py-1.5 text-xs font-semibold bg-white border border-gray-200 text-gray-700 rounded hover:bg-gray-50 transition-colors">Inbox</a>
                        </div>
                    </div>

                </div>
            </div>
        `;
    }
    
    // Re-initialize icons for newly injected HTML
    lucide.createIcons();
}
