import glob, re
for f in glob.glob('*.html'):
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    nav_match = re.search(r'<nav.*?</nav>', content, re.DOTALL)
    if nav_match:
        print(f'--- {f} ---')
        desktop_nav = re.search(r'<div class="hidden [^>]*flex items-center gap-lg">(.*?)</div>', nav_match.group(0), re.DOTALL)
        if desktop_nav:
            links = re.findall(r'<a.*?href="(.*?)".*?>(.*?)</a>', desktop_nav.group(1))
            for href, text in links:
                print(f'{href}: {text}')
        else:
            print('No desktop nav found')
