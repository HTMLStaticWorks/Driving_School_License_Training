import re

with open(r'index.html', 'r', encoding='utf-8') as f:
    text = f.read()
    match = re.search(r'"colors":\s*\{(.*?)\}', text, re.DOTALL)
    if match:
        colors_text = match.group(1)
        print(colors_text)
