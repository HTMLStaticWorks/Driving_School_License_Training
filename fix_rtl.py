import glob

for f in glob.glob('*.html'):
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # 1. Update the onclick handlers for the RTL toggle button
    old_onclick = "onclick=\"document.documentElement.dir = document.documentElement.dir === 'rtl' ? 'ltr' : 'rtl';\""
    new_onclick = "onclick=\"document.documentElement.dir = document.documentElement.dir === 'rtl' ? 'ltr' : 'rtl'; localStorage.dir = document.documentElement.dir;\""
    content = content.replace(old_onclick, new_onclick)
    
    # 2. Inject localStorage.dir check in the head script
    old_script_part = "} else {\n        document.documentElement.classList.remove('dark')\n    }"
    new_script_part = "} else {\n        document.documentElement.classList.remove('dark')\n    }\n    if (localStorage.dir) {\n        document.documentElement.dir = localStorage.dir;\n    }"
    
    if 'localStorage.dir' not in content:
        content = content.replace(old_script_part, new_script_part)
    elif 'if (localStorage.dir)' not in content:
        content = content.replace(old_script_part, new_script_part)
        
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
    print('Fixed RTL persistence in', f)
