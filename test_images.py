import glob, re, urllib.request

html_files = glob.glob('*.html')
urls_to_test = set()

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        urls = re.findall(r'(https://images\.unsplash\.com/[^\s""'']*)', content)
        urls_to_test.update(urls)

for url in urls_to_test:
    try:
        url_without_quotes = url.split('"')[0].split("'")[0]
        code = urllib.request.urlopen(url_without_quotes).getcode()
        if code != 200:
            print(f'{code}: {url_without_quotes}')
    except Exception as e:
        print(f'Error testing {url_without_quotes}: {e}')
