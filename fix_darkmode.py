import os
import glob

html_files = glob.glob('*.html')

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    modified = False

    # Fix hardcoded body background
    if 'body { background-color: #faf9fb; }' in content:
        content = content.replace('body { background-color: #faf9fb; }', '/* removed hardcoded body bg */')
        modified = True

    # Fix hardcoded floating label styles
    if 'background-color: white;' in content and 'color: #006a6a; /* secondary */' in content:
        content = content.replace('background-color: white;', 'background-color: var(--color-surface);')
        content = content.replace('color: #006a6a; /* secondary */', 'color: var(--color-secondary);')
        modified = True

    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
