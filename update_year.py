import os, glob

target_dir = r'd:\project 2\Driving School & Licence Training'
os.chdir(target_dir)

for f in glob.glob('*.html'):
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    if '© 2024' in content:
        content = content.replace('© 2024', '© 2026')
        
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f'Updated year in {f}')
