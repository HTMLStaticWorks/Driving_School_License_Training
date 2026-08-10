import os
import re

files = ['login.html', 'register.html']

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove nav
    content = re.sub(r'<nav.*?</nav>', '', content, flags=re.DOTALL)
    
    # Remove footer
    content = re.sub(r'<footer.*?</footer>', '', content, flags=re.DOTALL)
    
    # Remove mobile menu and script
    content = re.sub(r'<!-- Mobile Menu Overlay -->.*?</script>', '', content, flags=re.DOTALL)
    
    # Remove empty lines left behind by regex (optional cleanup)
    content = re.sub(r'\n\s*\n', '\n', content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
