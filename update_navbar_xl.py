import os
import glob

html_files = glob.glob('*.html')

for filepath in html_files:
    if filepath == 'dashboard.html':
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # update dashboard sidebar and main content margin
        content = content.replace('hidden lg:flex', 'hidden xl:flex')
        content = content.replace('ml-0 lg:ml-64', 'ml-0 xl:ml-64')
        # update dashboard hamburger
        content = content.replace('<div class="flex items-center lg:hidden">', '<div class="flex items-center xl:hidden">')
        content = content.replace('<div class="hidden lg:block">', '<div class="hidden xl:block">')
        content = content.replace('<div class="lg:hidden">', '<div class="xl:hidden">')
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        continue

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Check if TopNavBar exists (even implicitly)
    if '<nav class="sticky w-full top-0' in content:
        # 1. Change links container from lg:flex to xl:flex
        content = content.replace('<div class="hidden lg:flex items-center gap-lg">', '<div class="hidden xl:flex items-center gap-lg">')
        
        # 2. Change RTL button from lg:flex to xl:flex
        content = content.replace('class="hidden lg:flex items-center text-on-surface-variant', 'class="hidden xl:flex items-center text-on-surface-variant')
        
        # 3. Change hamburger button from lg:hidden to xl:hidden
        content = content.replace('class="flex lg:hidden items-center text-on-surface-variant', 'class="flex xl:hidden items-center text-on-surface-variant')

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
