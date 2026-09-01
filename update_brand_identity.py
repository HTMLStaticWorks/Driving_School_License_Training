import glob
import re

html_files = sorted(glob.glob('*.html'))

nav_logo_old_patterns = [
    r'<div class="flex items-center gap-sm">\s*<span class="material-symbols-outlined text-primary text-headline-md icon-fill">directions_car</span>\s*<span class="text-headline-md font-headline-md font-bold text-primary tracking-tight">CARZDRIZ</span>\s*</div>',
    r'<div class="flex items-center gap-sm">\s*<span class="material-symbols-outlined text-primary text-headline-md icon-fill">directions_car</span>\s*<span class="text-headline-md font-headline-md font-bold text-primary dark:text-primary-fixed">CARZDRIZ</span>\s*</div>',
    r'<div class="flex items-center gap-sm">\s*<span class="material-symbols-outlined text-primary text-headline-md icon-fill">directions_car</span>\s*<span class="text-headline-md font-headline-md font-bold text-primary tracking-tight">Elite Driving Academy</span>\s*</div>',
]

nav_logo_new = '''<a href="index.html" class="flex items-center gap-3 group focus:outline-none shrink-0" aria-label="CARZDRIZ Home">
    <div class="relative flex items-center justify-center w-11 h-11 rounded-xl bg-gradient-to-br from-primary via-secondary to-brand-teal p-[2px] shadow-sm group-hover:shadow-md group-hover:scale-105 transition-all duration-300">
        <div class="w-full h-full bg-surface dark:bg-surface-container-highest rounded-[10px] flex items-center justify-center overflow-hidden p-1">
            <img src="images/logo-icon.svg" alt="CARZDRIZ Logo" class="w-full h-full object-contain">
        </div>
    </div>
    <div class="flex flex-col leading-none">
        <div class="flex items-center text-2xl font-black font-display tracking-tight">
            <span class="text-primary dark:text-on-surface">CARZ</span>
            <span class="text-brand-orange">DRIZ</span>
        </div>
        <span class="text-[9px] font-bold uppercase tracking-[0.22em] text-on-surface-variant/80 mt-0.5">Driving Academy</span>
    </div>
</a>'''

footer_logo_old_patterns = [
    r'<div class="flex items-center gap-sm">\s*<span class="material-symbols-outlined text-on-primary text-headline-md icon-fill">directions_car</span>\s*<span class="text-headline-md font-headline-md font-bold text-on-primary tracking-tight">Elite Driving Academy</span>\s*</div>',
    r'<div class="flex items-center gap-sm">\s*<span class="material-symbols-outlined text-on-primary text-headline-md icon-fill">directions_car</span>\s*<span class="text-headline-md font-headline-md font-bold text-on-primary tracking-tight">CARZDRIZ</span>\s*</div>'
]

footer_logo_new = '''<a href="index.html" class="flex items-center gap-3 group focus:outline-none shrink-0" aria-label="CARZDRIZ Home">
    <div class="relative flex items-center justify-center w-11 h-11 rounded-xl bg-gradient-to-br from-secondary-fixed via-brand-teal to-brand-orange p-[2px] shadow-sm group-hover:shadow-md group-hover:scale-105 transition-all duration-300">
        <div class="w-full h-full bg-primary-container rounded-[10px] flex items-center justify-center overflow-hidden p-1">
            <img src="images/logo-icon.svg" alt="CARZDRIZ Logo" class="w-full h-full object-contain">
        </div>
    </div>
    <div class="flex flex-col leading-none">
        <div class="flex items-center text-2xl font-black font-display tracking-tight">
            <span class="text-on-primary">CARZ</span>
            <span class="text-brand-orange">DRIZ</span>
        </div>
        <span class="text-[9px] font-bold uppercase tracking-[0.22em] text-on-primary/70 mt-0.5">Driving Academy</span>
    </div>
</a>'''

card_logo_old_pattern = r'<div class="mb-xl text-center stagger-anim">\s*<a href="index.html" class="hover:opacity-80 transition-opacity flex flex-col items-center">\s*<div class="w-16 h-16 rounded-xl bg-secondary flex items-center justify-center text-on-secondary shadow-md mb-sm">\s*<span class="material-symbols-outlined icon-fill text-\[32px\]">directions_car</span>\s*</div>\s*<h2 class="text-3xl md:text-4xl text-primary font-bold tracking-tight">CARZDRIZ</h2>\s*</a>\s*</div>'

card_logo_new = '''<div class="mb-xl text-center stagger-anim">
    <a href="index.html" class="hover:opacity-95 transition-all inline-flex flex-col items-center group">
        <div class="relative flex items-center justify-center w-16 h-16 rounded-2xl bg-gradient-to-br from-primary via-secondary to-brand-teal p-[3px] shadow-md group-hover:shadow-lg group-hover:scale-105 transition-all duration-300 mb-sm">
            <div class="w-full h-full bg-surface dark:bg-surface-container-highest rounded-[13px] flex items-center justify-center overflow-hidden p-2">
                <img src="images/logo-icon.svg" alt="CARZDRIZ Logo" class="w-full h-full object-contain">
            </div>
        </div>
        <div class="flex items-center text-3xl md:text-4xl font-black font-display tracking-tight">
            <span class="text-primary dark:text-on-surface">CARZ</span>
            <span class="text-brand-orange">DRIZ</span>
        </div>
        <span class="text-[10px] font-bold uppercase tracking-[0.25em] text-on-surface-variant/80 mt-1">Driving Academy</span>
    </a>
</div>'''

favicon_new = '<link rel="icon" type="image/svg+xml" href="images/favicon.svg">'

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace favicon
    content = re.sub(
        r'<link [^>]*href="data:image/svg\+xml;?<svg.*?</svg>"\s*>/?',
        favicon_new,
        content,
        flags=re.DOTALL
    )
    content = re.sub(
        r'<link [^>]*rel="icon"[^>]*href="data:image/svg\+xml;?<svg.*?</svg>"\s*>/?',
        favicon_new,
        content,
        flags=re.DOTALL
    )

    # Simple favicon replacement fallback
    content = re.sub(
        r'<link rel="icon"\s*href="data:image/svg\+xml,[^"]*">',
        favicon_new,
        content
    )

    # Replace card logo (login/register)
    content = re.sub(card_logo_old_pattern, card_logo_new, content, flags=re.DOTALL)

    # Replace nav logos
    for pattern in nav_logo_old_patterns:
        content = re.sub(pattern, nav_logo_new, content, flags=re.DOTALL)

    # Replace footer logos
    for pattern in footer_logo_old_patterns:
        content = re.sub(pattern, footer_logo_new, content, flags=re.DOTALL)

    # Replace old footer copyright
    content = content.replace('© 2024 Elite Driving Academy. All rights reserved.', '© 2026 CARZDRIZ Driving Academy. All rights reserved.')
    content = content.replace('© 2026 Elite Driving Academy. All rights reserved.', '© 2026 CARZDRIZ Driving Academy. All rights reserved.')

    # Replace support email
    content = content.replace('info@elitedriving.com', 'info@carzdriz.com')

    # Specific title updates if needed
    if file_path == 'register.html':
        content = content.replace('<title>Apex Driving Academy - Register</title>', '<title>Sign Up - CARZDRIZ Driving Academy</title>')
    elif file_path == 'index.html':
        content = content.replace('<title>CARZDRIZ</title>', '<title>CARZDRIZ - Driving School & Licence Training</title>')

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Brand identity script executed successfully.")
