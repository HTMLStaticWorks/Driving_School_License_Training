import sys, re, os, glob

target_dir = r'd:\project 2\Driving School & Licence Training'
os.chdir(target_dir)

new_footer = """<footer class="bg-primary text-on-primary mt-auto">
<div class="grid grid-cols-1 md:grid-cols-4 lg:grid-cols-5 gap-xl px-gutter py-2xl max-w-container-max mx-auto border-b border-primary-fixed-dim/20">
    <!-- Brand & Contact -->
    <div class="flex flex-col gap-md col-span-1 md:col-span-2">
        <div class="flex items-center gap-sm">
            <span class="material-symbols-outlined text-on-primary text-headline-md icon-fill">directions_car</span>
            <span class="text-headline-md font-headline-md font-bold text-on-primary tracking-tight">Elite Driving Academy</span>
        </div>
        <p class="font-body-sm text-body-sm text-on-primary/70 max-w-sm">
            Precision in every turn. Empowering the next generation of safe, confident drivers with professional instructors and modern vehicles.
        </p>
        <div class="flex flex-col gap-xs mt-sm">
            <div class="flex items-center gap-sm text-on-primary/80">
                <span class="material-symbols-outlined text-[18px]">location_on</span>
                <span class="font-body-sm text-body-sm">123 Driving School Lane, Cityville, ST 12345</span>
            </div>
            <div class="flex items-center gap-sm text-on-primary/80">
                <span class="material-symbols-outlined text-[18px]">call</span>
                <span class="font-body-sm text-body-sm">(555) 123-4567</span>
            </div>
            <div class="flex items-center gap-sm text-on-primary/80">
                <span class="material-symbols-outlined text-[18px]">mail</span>
                <span class="font-body-sm text-body-sm">info@elitedriving.com</span>
            </div>
        </div>
    </div>

    <!-- Quick Links -->
    <div class="flex flex-col gap-md">
        <h4 class="font-label-caps text-label-caps uppercase text-secondary-fixed tracking-widest">Quick Links</h4>
        <div class="flex flex-col gap-sm">
            <a class="font-body-sm text-body-sm text-on-primary/70 hover:text-secondary-fixed transition-colors" href="index.html">Home</a>
            <a class="font-body-sm text-body-sm text-on-primary/70 hover:text-secondary-fixed transition-colors" href="about.html">About Us</a>
            <a class="font-body-sm text-body-sm text-on-primary/70 hover:text-secondary-fixed transition-colors" href="services.html">Services</a>
            <a class="font-body-sm text-body-sm text-on-primary/70 hover:text-secondary-fixed transition-colors" href="instructors.html">Instructors</a>
            <a class="font-body-sm text-body-sm text-on-primary/70 hover:text-secondary-fixed transition-colors" href="lesson.html">Lesson Packages</a>
        </div>
    </div>

    <!-- Legal & Support -->
    <div class="flex flex-col gap-md">
        <h4 class="font-label-caps text-label-caps uppercase text-secondary-fixed tracking-widest">Support</h4>
        <div class="flex flex-col gap-sm">
            <a class="font-body-sm text-body-sm text-on-primary/70 hover:text-secondary-fixed transition-colors" href="dashboard.html">Student Dashboard</a>
            <a class="font-body-sm text-body-sm text-on-primary/70 hover:text-secondary-fixed transition-colors" href="login.html">Login</a>
            <a class="font-body-sm text-body-sm text-on-primary/70 hover:text-secondary-fixed transition-colors" href="register.html">Sign Up</a>
            <a class="font-body-sm text-body-sm text-on-primary/70 hover:text-secondary-fixed transition-colors" href="#">Privacy Policy</a>
            <a class="font-body-sm text-body-sm text-on-primary/70 hover:text-secondary-fixed transition-colors" href="#">Terms of Service</a>
        </div>
    </div>

    <!-- Newsletter -->
    <div class="flex flex-col gap-md col-span-1 md:col-span-2 lg:col-span-1">
        <h4 class="font-label-caps text-label-caps uppercase text-secondary-fixed tracking-widest">Newsletter</h4>
        <p class="font-body-sm text-body-sm text-on-primary/70">Subscribe for driving tips and exclusive offers.</p>
        <form class="flex flex-col gap-sm mt-xs" onsubmit="event.preventDefault();">
            <input type="email" placeholder="Your email address" class="w-full bg-primary-container text-on-primary-container border-none rounded-lg px-md py-sm font-body-sm focus:ring-2 focus:ring-secondary-fixed outline-none" required>
            <button type="submit" class="w-full bg-secondary text-on-secondary font-label-caps text-label-caps uppercase tracking-wider py-sm rounded-lg hover:bg-secondary-container hover:text-on-secondary-container transition-colors shadow-sm">Subscribe</button>
        </form>
    </div>
</div>

<!-- Bottom Bar -->
<div class="px-gutter py-md max-w-container-max mx-auto text-center md:text-left flex flex-col md:flex-row justify-between items-center gap-sm">
    <span class="font-body-sm text-body-sm text-on-primary/50">© 2024 Elite Driving Academy. All rights reserved.</span>
    
    <!-- Social Icons using SVG for actual brands instead of just material icons -->
    <div class="flex gap-md opacity-80">
        <a href="#" class="hover:text-secondary-fixed hover:opacity-100 transition-all text-on-primary" aria-label="Facebook">
            <svg class="w-5 h-5 fill-current" viewBox="0 0 24 24"><path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.469h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.469h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/></svg>
        </a>
        <a href="#" class="hover:text-secondary-fixed hover:opacity-100 transition-all text-on-primary" aria-label="Twitter">
            <svg class="w-5 h-5 fill-current" viewBox="0 0 24 24"><path d="M23.953 4.57a10 10 0 01-2.825.775 4.958 4.958 0 002.163-2.723c-.951.555-2.005.959-3.127 1.184a4.92 4.92 0 00-8.384 4.482C7.69 8.095 4.067 6.13 1.64 3.162a4.822 4.822 0 00-.666 2.475c0 1.71.87 3.213 2.188 4.096a4.904 4.904 0 01-2.228-.616v.06a4.923 4.923 0 003.946 4.827 4.996 4.996 0 01-2.212.085 4.936 4.936 0 004.604 3.417 9.867 9.867 0 01-6.102 2.105c-.39 0-.779-.023-1.17-.067a13.995 13.995 0 007.557 2.209c9.053 0 13.998-7.496 13.998-13.985 0-.21 0-.42-.015-.63A9.935 9.935 0 0024 4.59z"/></svg>
        </a>
        <a href="#" class="hover:text-secondary-fixed hover:opacity-100 transition-all text-on-primary" aria-label="Instagram">
            <svg class="w-5 h-5 fill-current" viewBox="0 0 24 24"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zM12 0C8.741 0 8.333.014 7.053.072 2.695.272.273 2.69.073 7.052.014 8.333 0 8.741 0 12c0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98C8.333 23.986 8.741 24 12 24c3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98C15.668.014 15.259 0 12 0zm0 5.838a6.162 6.162 0 100 12.324 6.162 6.162 0 000-12.324zM12 16a4 4 0 110-8 4 4 0 010 8zm6.406-11.845a1.44 1.44 0 100 2.881 1.44 1.44 0 000-2.881z"/></svg>
        </a>
    </div>
</div>
</footer>"""

for f in glob.glob('*.html'):
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Check if footer exists
    match = re.search(r'<footer.*?>.*?</footer>', content, re.DOTALL | re.IGNORECASE)
    
    if match:
        # replace existing footer
        content = content[:match.start()] + new_footer + content[match.end():]
        print(f'Replaced footer in {f}')
    else:
        # inject before </body> if no footer exists, but make sure body exists
        if '<body' in content:
            # find closing body tag
            body_match = re.search(r'</body>', content, re.IGNORECASE)
            if body_match:
                content = content[:body_match.start()] + '\n' + new_footer + '\n' + content[body_match.start():]
                print(f'Added footer to {f}')
            else:
                content = content + '\n' + new_footer
                print(f'Added footer at end of {f}')
                
    # One small fix: ensure the body or parent has min-h-screen flex col so footer sticks to bottom on short pages like login.html
    # We can inject this in the <body class="...">
    if 'min-h-screen' not in content and 'class="' in content:
        content = re.sub(r'<body class="([^"]+)"', r'<body class="\1 flex flex-col min-h-screen"', content, count=1, flags=re.IGNORECASE)
        
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
