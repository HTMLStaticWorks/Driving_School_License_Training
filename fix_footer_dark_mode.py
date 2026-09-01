import glob
import re

html_files = sorted(glob.glob('*.html'))

new_footer_html = '''<footer class="bg-primary dark:bg-[#090F1B] text-on-primary dark:text-on-surface mt-auto border-t border-primary-fixed-dim/20 dark:border-outline-variant/20 transition-colors duration-300">
<div class="grid grid-cols-1 md:grid-cols-4 lg:grid-cols-5 gap-xl px-gutter py-2xl max-w-container-max mx-auto border-b border-primary-fixed-dim/20 dark:border-outline-variant/20">
    <!-- Brand & Contact -->
    <div class="flex flex-col gap-md col-span-1 md:col-span-2">
        <a href="index.html" class="flex items-center gap-3 group focus:outline-none shrink-0" aria-label="CARZDRIZ Home">
            <div class="relative flex items-center justify-center w-11 h-11 rounded-xl bg-gradient-to-br from-secondary-fixed via-brand-teal to-brand-orange p-[2px] shadow-sm group-hover:shadow-md group-hover:scale-105 transition-all duration-300">
                <div class="w-full h-full bg-primary-container dark:bg-surface-container-highest rounded-[10px] flex items-center justify-center overflow-hidden p-1">
                    <img src="images/logo-icon.svg" alt="CARZDRIZ Logo" class="w-full h-full object-contain">
                </div>
            </div>
            <div class="flex flex-col leading-none">
                <div class="flex items-center text-2xl font-black font-display tracking-tight">
                    <span class="text-on-primary dark:text-on-surface">CARZ</span>
                    <span class="text-brand-orange">DRIZ</span>
                </div>
                <span class="text-[9px] font-bold uppercase tracking-[0.22em] text-on-primary/70 dark:text-on-surface-variant mt-0.5">Driving Academy</span>
            </div>
        </a>
        <p class="font-body-sm text-body-sm text-on-primary/80 dark:text-on-surface-variant max-w-sm">
            Precision in every turn. Empowering the next generation of safe, confident drivers with professional instructors and modern vehicles.
        </p>
        <div class="flex flex-col gap-xs mt-sm">
            <div class="flex items-center gap-sm text-on-primary/90 dark:text-on-surface-variant">
                <span class="material-symbols-outlined text-[18px] text-brand-orange">location_on</span>
                <span class="font-body-sm text-body-sm">123 Driving School Lane, Cityville, ST 12345</span>
            </div>
            <div class="flex items-center gap-sm text-on-primary/90 dark:text-on-surface-variant">
                <span class="material-symbols-outlined text-[18px] text-brand-orange">call</span>
                <span class="font-body-sm text-body-sm">(555) 123-4567</span>
            </div>
            <div class="flex items-center gap-sm text-on-primary/90 dark:text-on-surface-variant">
                <span class="material-symbols-outlined text-[18px] text-brand-orange">mail</span>
                <span class="font-body-sm text-body-sm">info@carzdriz.com</span>
            </div>
        </div>
    </div>

    <!-- Quick Links -->
    <div class="flex flex-col gap-md">
        <h4 class="font-label-caps text-label-caps uppercase text-secondary-fixed dark:text-brand-teal tracking-widest font-bold">Quick Links</h4>
        <div class="flex flex-col gap-sm">
            <a class="font-body-sm text-body-sm text-on-primary/80 dark:text-on-surface-variant hover:text-brand-orange dark:hover:text-brand-orange transition-colors" href="index.html">Home</a>
            <a class="font-body-sm text-body-sm text-on-primary/80 dark:text-on-surface-variant hover:text-brand-orange dark:hover:text-brand-orange transition-colors" href="about.html">About Us</a>
            <a class="font-body-sm text-body-sm text-on-primary/80 dark:text-on-surface-variant hover:text-brand-orange dark:hover:text-brand-orange transition-colors" href="services.html">Services</a>
            <a class="font-body-sm text-body-sm text-on-primary/80 dark:text-on-surface-variant hover:text-brand-orange dark:hover:text-brand-orange transition-colors" href="instructors.html">Instructors</a>
            <a class="font-body-sm text-body-sm text-on-primary/80 dark:text-on-surface-variant hover:text-brand-orange dark:hover:text-brand-orange transition-colors" href="lesson.html">Lesson Packages</a>
        </div>
    </div>

    <!-- Legal & Support -->
    <div class="flex flex-col gap-md">
        <h4 class="font-label-caps text-label-caps uppercase text-secondary-fixed dark:text-brand-teal tracking-widest font-bold">Support</h4>
        <div class="flex flex-col gap-sm">
            <a class="font-body-sm text-body-sm text-on-primary/80 dark:text-on-surface-variant hover:text-brand-orange dark:hover:text-brand-orange transition-colors" href="dashboard.html">Student Dashboard</a>
            <a class="font-body-sm text-body-sm text-on-primary/80 dark:text-on-surface-variant hover:text-brand-orange dark:hover:text-brand-orange transition-colors" href="login.html">Login</a>
            <a class="font-body-sm text-body-sm text-on-primary/80 dark:text-on-surface-variant hover:text-brand-orange dark:hover:text-brand-orange transition-colors" href="register.html">Sign Up</a>
            <a class="font-body-sm text-body-sm text-on-primary/80 dark:text-on-surface-variant hover:text-brand-orange dark:hover:text-brand-orange transition-colors" href="#">Privacy Policy</a>
            <a class="font-body-sm text-body-sm text-on-primary/80 dark:text-on-surface-variant hover:text-brand-orange dark:hover:text-brand-orange transition-colors" href="#">Terms of Service</a>
        </div>
    </div>

    <!-- Newsletter -->
    <div class="flex flex-col gap-md col-span-1 md:col-span-2 lg:col-span-1">
        <h4 class="font-label-caps text-label-caps uppercase text-secondary-fixed dark:text-brand-teal tracking-widest font-bold">Newsletter</h4>
        <p class="font-body-sm text-body-sm text-on-primary/80 dark:text-on-surface-variant">Subscribe for driving tips and exclusive offers.</p>
        <form class="flex flex-col gap-sm mt-xs" onsubmit="event.preventDefault();">
            <div class="relative w-full">
                <input type="email" placeholder="Your email address" class="w-full bg-primary-container/80 dark:bg-surface-container-high text-on-primary dark:text-on-surface placeholder:text-on-primary/60 dark:placeholder:text-on-surface-variant/70 border border-outline-variant/30 dark:border-outline-variant/60 rounded-lg px-md py-sm font-body-sm focus:ring-2 focus:ring-brand-orange focus:border-brand-orange outline-none transition-all" required>
            </div>
            <button type="submit" class="w-full bg-brand-orange hover:bg-[#e6692e] text-white font-label-caps text-label-caps uppercase tracking-wider py-sm rounded-lg transition-all duration-200 shadow-sm hover:shadow-md active:scale-[0.99] font-bold">Subscribe</button>
        </form>
    </div>
</div>

<!-- Bottom Bar -->
<div class="px-gutter py-md max-w-container-max mx-auto text-center md:text-left flex flex-col md:flex-row justify-between items-center gap-sm">
    <span class="font-body-sm text-body-sm text-on-primary/70 dark:text-on-surface-variant/70">© 2026 CARZDRIZ Driving Academy. All rights reserved.</span>
    
    <!-- Social Icons -->
    <div class="flex gap-md opacity-80">
        <a href="#" class="hover:text-brand-orange dark:hover:text-brand-orange hover:opacity-100 transition-all text-on-primary dark:text-on-surface" aria-label="Facebook">
            <svg class="w-5 h-5 fill-current" viewBox="0 0 24 24"><path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.469h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.469h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/></svg>
        </a>
        <a href="#" class="hover:text-brand-orange dark:hover:text-brand-orange hover:opacity-100 transition-all text-on-primary dark:text-on-surface" aria-label="Twitter">
            <svg class="w-5 h-5 fill-current" viewBox="0 0 24 24"><path d="M23.953 4.57a10 10 0 01-2.825.775 4.958 4.958 0 002.163-2.723c-.951.555-2.005.959-3.127 1.184a4.92 4.92 0 00-8.384 4.482C7.69 8.095 4.067 6.13 1.64 3.162a4.822 4.822 0 00-.666 2.475c0 1.71.87 3.213 2.188 4.096a4.904 4.904 0 01-2.228-.616v.06a4.923 4.923 0 003.946 4.827 4.996 4.996 0 01-2.212.085 4.936 4.936 0 004.604 3.417 9.867 9.867 0 01-6.102 2.105c-.39 0-.779-.023-1.17-.067a13.995 13.995 0 007.557 2.209c9.053 0 13.998-7.496 13.998-13.985 0-.21 0-.42-.015-.63A9.935 9.935 0 0024 4.59z"/></svg>
        </a>
        <a href="#" class="hover:text-brand-orange dark:hover:text-brand-orange hover:opacity-100 transition-all text-on-primary dark:text-on-surface" aria-label="Instagram">
            <svg class="w-5 h-5 fill-current" viewBox="0 0 24 24"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zM12 0C8.741 0 8.333.014 7.053.072 2.695.272.273 2.69.073 7.052.014 8.333 0 8.741 0 12c0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98C8.333 23.986 8.741 24 12 24c3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98C15.668.014 15.259 0 12 0zm0 5.838a6.162 6.162 0 100 12.324 6.162 6.162 0 000-12.324zM12 16a4 4 0 110-8 4 4 0 010 8zm6.406-11.845a1.44 1.44 0 100 2.881 1.44 1.44 0 000-2.881z"/></svg>
        </a>
    </div>
</div>
</footer>'''

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    match = re.search(r'<footer.*?>.*?</footer>', content, re.DOTALL | re.IGNORECASE)
    if match:
        content = content[:match.start()] + new_footer_html + content[match.end():]
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated footer in {file_path}")

print("Footer dark mode color contrast fix complete.")
