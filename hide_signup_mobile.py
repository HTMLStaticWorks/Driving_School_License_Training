import os
import glob

html_files = glob.glob('*.html')

search_str = '<a class="inline-flex items-center justify-center font-label-caps text-label-caps bg-primary text-on-primary px-lg py-sm rounded-lg shadow-sm hover:shadow-md hover:bg-primary-container hover:text-on-primary-container transition-all uppercase tracking-wider" href="register.html">Sign Up</a>'
replace_str = '<a class="hidden xl:inline-flex items-center justify-center font-label-caps text-label-caps bg-primary text-on-primary px-lg py-sm rounded-lg shadow-sm hover:shadow-md hover:bg-primary-container hover:text-on-primary-container transition-all uppercase tracking-wider" href="register.html">Sign Up</a>'

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if search_str in content:
        content = content.replace(search_str, replace_str)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {file}")
