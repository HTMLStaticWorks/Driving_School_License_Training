import glob, re
for f in glob.glob('*.html'):
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    mobile_menu_match = re.search(r'<div id="mobile-menu" .*?>(.*?)</div>\s*</div>', content, re.DOTALL)
    if mobile_menu_match:
        print(f'--- {f} ---')
        links = re.findall(r'<a.*?href="(.*?)".*?>(.*?)</a>', mobile_menu_match.group(1))
        for href, text in links:
            print(f'{href}: {text}')
