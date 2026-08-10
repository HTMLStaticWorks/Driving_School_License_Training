import os
import glob
import re

target_dir = r'd:\project 2\Driving School & Licence Training'
os.chdir(target_dir)

favicon_html = r"""<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🚗</text></svg>">"""

for f in glob.glob('*.html'):
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # insert favicon right after </title>
    # ensuring we don't add it twice
    if 'rel="icon"' not in content:
        content = re.sub(r'(</title>)', r'\1\n' + favicon_html, content, flags=re.IGNORECASE)
        
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f'Added favicon to {f}')
