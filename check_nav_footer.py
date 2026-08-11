import glob, re
for f in glob.glob('*.html'):
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    footer_match = re.search(r'<footer.*?</footer>', content, re.DOTALL)
    if footer_match:
        links = re.findall(r'<a.*?href="(.*?)".*?>(.*?)</a>', footer_match.group(0))
        for href, text in links:
            if 'html' in href:
                print(f'{f} footer -> {href}: {text}')
