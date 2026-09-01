import glob
import re

html_files = sorted(glob.glob('*.html'))

old_drawer_header = r'<div class="p-lg flex justify-between items-center border-b border-outline-variant/30">\s*<span class="text-headline-sm font-headline-sm font-bold text-primary">Menu</span>\s*<button id="close-mobile-menu"'

new_drawer_header = '''<div class="p-lg flex justify-between items-center border-b border-outline-variant/30">
    <div class="flex items-center gap-2">
        <div class="w-8 h-8 rounded-lg bg-gradient-to-br from-primary to-secondary p-[1.5px] shadow-sm">
            <div class="w-full h-full bg-surface dark:bg-surface-container-highest rounded-[6px] flex items-center justify-center p-0.5">
                <img src="images/logo-icon.svg" alt="CARZDRIZ Logo" class="w-full h-full object-contain">
            </div>
        </div>
        <span class="text-lg font-black font-display tracking-tight text-primary dark:text-on-surface">CARZ<span class="text-brand-orange">DRIZ</span></span>
    </div>
    <button id="close-mobile-menu"'''

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    if re.search(old_drawer_header, content):
        content = re.sub(old_drawer_header, new_drawer_header, content)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated mobile drawer logo in {file_path}")

print("Mobile drawer logos updated.")
