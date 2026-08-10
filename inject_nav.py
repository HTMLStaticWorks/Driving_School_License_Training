import sys, re

with open('nav_block.txt', 'r', encoding='utf-8') as f:
    nav_html = f.read()

for f_name in ['instructors.html', 'login.html', 'register.html']:
    with open(f_name, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if '<nav class="sticky' not in content:
        # inject after body tag
        content = re.sub(r'(<body[^>]*>)', r'\1\n' + nav_html + '\n', content, count=1, flags=re.IGNORECASE)
        with open(f_name, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Added nav to {f_name}')
