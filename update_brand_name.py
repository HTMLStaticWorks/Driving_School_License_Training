import glob

html_files = glob.glob('*.html')
old_brand = "Elite Driving Academy"
new_brand = "CARZDRIZ"

count = 0
for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if old_brand in content:
        content = content.replace(old_brand, new_brand)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        count += 1

print(f"Updated {count} HTML files, replacing '{old_brand}' with '{new_brand}'.")
