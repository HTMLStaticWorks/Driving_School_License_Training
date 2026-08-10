import os, glob, re

target_dir = r'd:\project 2\Driving School & Licence Training'
os.chdir(target_dir)

with open('nav_block.txt', 'r', encoding='utf-8') as f:
    new_nav = f.read()

# For files that use <nav ...> ... </nav> at the top level (right after <body> or <!-- comments -->)
# Or for about.html which uses <header ...> ... </header>

files_to_update = ['services.html', 'lesson.html', 'home2.html', 'about.html']

for f in files_to_update:
    if not os.path.exists(f): continue
    
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # We will replace the first <nav ...> ... </nav> or <header ...> ... </header> that contains the top menu
    # Be careful not to replace footer or sidebars.
    if f == 'about.html':
        # about.html uses <header> for its top nav
        content = re.sub(r'<header class="bg-surface border-b[^>]*>.*?</header>', new_nav, content, count=1, flags=re.DOTALL)
    else:
        # others use <nav>
        # we will replace the first <nav> that has "sticky" or "docked"
        content = re.sub(r'<nav class="[^"]*(?:sticky|docked)[^"]*"[^>]*>.*?</nav>', new_nav, content, count=1, flags=re.DOTALL)
        
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f'Updated {f}')
