import glob
import re

html_files = glob.glob('*.html')

theme_script = """<script>
    if (localStorage.theme === 'dark' || (!('theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
        document.documentElement.classList.add('dark')
    } else {
        document.documentElement.classList.remove('dark')
    }
</script>"""

count = 0
for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    modified = False
    
    if "localStorage.theme" not in content:
        content = re.sub(r'(<head[^>]*>)', r'\1\n' + theme_script, content, count=1, flags=re.IGNORECASE)
        modified = True
        
    old_onclick = "onclick=\"document.documentElement.classList.toggle('dark');\""
    new_onclick = "onclick=\"document.documentElement.classList.toggle('dark'); localStorage.theme = document.documentElement.classList.contains('dark') ? 'dark' : 'light';\""
    
    if old_onclick in content:
        content = content.replace(old_onclick, new_onclick)
        modified = True
        
    if modified:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        count += 1

print(f"Updated {count} HTML files for theme persistence.")
