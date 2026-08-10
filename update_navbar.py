import os
import glob

html_files = glob.glob('*.html')

for filepath in html_files:
    if filepath == 'dashboard.html':
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # update dashboard sidebar and main content margin
        content = content.replace('hidden md:flex', 'hidden lg:flex')
        content = content.replace('ml-0 md:ml-64', 'ml-0 lg:ml-64')
        # update dashboard hamburger
        content = content.replace('<div class="flex items-center md:hidden">', '<div class="flex items-center lg:hidden">')
        content = content.replace('<div class="hidden md:block">', '<div class="hidden lg:block">')
        content = content.replace('<div class="md:hidden">', '<div class="lg:hidden">')
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        continue

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Check if TopNavBar exists (even implicitly)
    if '<nav class="sticky w-full top-0' in content:
        # 1. Change links container from md:flex to lg:flex
        content = content.replace('<div class="hidden md:flex items-center gap-lg">', '<div class="hidden lg:flex items-center gap-lg">')
        
        # 2. Change RTL button from md:flex to lg:flex
        content = content.replace('class="hidden md:flex items-center text-on-surface-variant', 'class="hidden lg:flex items-center text-on-surface-variant')
        
        # 3. Add hamburger button before the Sign Up button
        sign_up_str = '<a class="inline-flex items-center justify-center font-label-caps text-label-caps bg-primary'
        hamburger_str = '<button aria-label="Open Menu" class="flex lg:hidden items-center text-on-surface-variant hover:text-primary transition-colors p-sm rounded-full hover:bg-surface-container">\n<span class="material-symbols-outlined">menu</span>\n</button>\n'
        
        # prevent duplicate hamburgers
        if hamburger_str not in content:
            content = content.replace(sign_up_str, hamburger_str + sign_up_str)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
