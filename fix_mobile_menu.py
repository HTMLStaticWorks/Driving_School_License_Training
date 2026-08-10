import os
import glob
import re

html_files = glob.glob('*.html')

hamburger_btn_str = """<button aria-label="Open Menu" class="flex xl:hidden items-center text-on-surface-variant hover:text-primary transition-colors p-sm rounded-full hover:bg-surface-container">
<span class="material-symbols-outlined">menu</span>
</button>
"""

new_hamburger_btn_str = """<button id="mobile-menu-btn" aria-label="Open Menu" class="flex xl:hidden items-center text-on-surface-variant hover:text-primary transition-colors p-sm rounded-full hover:bg-surface-container">
<span class="material-symbols-outlined">menu</span>
</button>
"""

mobile_menu_html = """
<!-- Mobile Menu Overlay -->
<div id="mobile-menu-overlay" class="fixed inset-0 bg-surface-dim/80 backdrop-blur-sm z-[60] hidden opacity-0 transition-opacity duration-300"></div>
<!-- Mobile Menu Sidebar -->
<div id="mobile-menu" class="fixed top-0 right-0 h-full w-64 max-w-sm bg-surface z-[70] transform translate-x-full transition-transform duration-300 shadow-2xl flex flex-col">
    <div class="p-lg flex justify-between items-center border-b border-outline-variant/30">
        <span class="text-headline-sm font-headline-sm font-bold text-primary">Menu</span>
        <button id="close-mobile-menu" class="text-on-surface-variant hover:text-primary p-sm rounded-full hover:bg-surface-container transition-colors">
            <span class="material-symbols-outlined">close</span>
        </button>
    </div>
    <div class="flex flex-col py-md overflow-y-auto">
        <a href="index.html" class="px-lg py-md text-on-surface hover:bg-surface-container transition-colors font-label-caps text-[14px] uppercase tracking-wider">Home</a>
        <a href="home2.html" class="px-lg py-md text-on-surface hover:bg-surface-container transition-colors font-label-caps text-[14px] uppercase tracking-wider">Home 2</a>
        <a href="about.html" class="px-lg py-md text-on-surface hover:bg-surface-container transition-colors font-label-caps text-[14px] uppercase tracking-wider">About</a>
        <a href="services.html" class="px-lg py-md text-on-surface hover:bg-surface-container transition-colors font-label-caps text-[14px] uppercase tracking-wider">Services</a>
        <a href="instructors.html" class="px-lg py-md text-on-surface hover:bg-surface-container transition-colors font-label-caps text-[14px] uppercase tracking-wider">Instructors</a>
        <a href="lesson.html" class="px-lg py-md text-on-surface hover:bg-surface-container transition-colors font-label-caps text-[14px] uppercase tracking-wider">Lesson</a>
        <div class="h-px w-full bg-outline-variant/30 my-sm"></div>
        <a href="register.html" class="px-lg py-md text-primary font-bold hover:bg-primary/5 transition-colors font-label-caps text-[14px] uppercase tracking-wider">Sign Up</a>
        <a href="login.html" class="px-lg py-md text-secondary hover:bg-secondary/5 transition-colors font-label-caps text-[14px] uppercase tracking-wider">Login</a>
    </div>
</div>
<script>
    document.addEventListener('DOMContentLoaded', () => {
        const mobileMenuBtn = document.getElementById('mobile-menu-btn');
        const closeMobileMenuBtn = document.getElementById('close-mobile-menu');
        const mobileMenu = document.getElementById('mobile-menu');
        const mobileMenuOverlay = document.getElementById('mobile-menu-overlay');

        function openMenu() {
            if (!mobileMenu) return;
            mobileMenuOverlay.classList.remove('hidden');
            setTimeout(() => {
                mobileMenuOverlay.classList.remove('opacity-0');
                mobileMenu.classList.remove('translate-x-full');
            }, 10);
            document.body.style.overflow = 'hidden'; 
        }

        function closeMenu() {
            if (!mobileMenu) return;
            mobileMenuOverlay.classList.add('opacity-0');
            mobileMenu.classList.add('translate-x-full');
            setTimeout(() => {
                mobileMenuOverlay.classList.add('hidden');
            }, 300);
            document.body.style.overflow = '';
        }

        if (mobileMenuBtn) {
            mobileMenuBtn.addEventListener('click', openMenu);
        }
        if (closeMobileMenuBtn) {
            closeMobileMenuBtn.addEventListener('click', closeMenu);
        }
        if (mobileMenuOverlay) {
            mobileMenuOverlay.addEventListener('click', closeMenu);
        }
    });
</script>
"""

for filepath in html_files:
    if filepath == 'dashboard.html':
        continue

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Remove ALL instances of the old hamburger button
    content = content.replace(hamburger_btn_str, '')

    # 2. Inject the correct hamburger button just before the Sign Up button inside the nav
    # We find the Sign Up button inside the nav. 
    sign_up_match = re.search(r'<a class="inline-flex[^>]*?href="register\.html"[^>]*?>Sign Up</a>\s*</div>\s*</nav>', content)
    if sign_up_match:
        nav_sign_up = sign_up_match.group(0)
        content = content.replace(nav_sign_up, new_hamburger_btn_str + nav_sign_up)

    # 3. Add the mobile menu HTML and JS right before </body>
    if '<!-- Mobile Menu Overlay -->' not in content:
        content = content.replace('</body>', mobile_menu_html + '\n</body>')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
