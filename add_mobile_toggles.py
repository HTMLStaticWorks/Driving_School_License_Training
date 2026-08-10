import glob

html_files = glob.glob('*.html')

buttons_html = """        <button onclick="document.documentElement.dir = document.documentElement.dir === 'rtl' ? 'ltr' : 'rtl';" class="px-lg py-md flex items-center gap-sm text-on-surface hover:bg-surface-container transition-colors font-label-caps text-[14px] uppercase tracking-wider text-left w-full">
            <span class="material-symbols-outlined text-[18px] mr-2">swap_horiz</span> RTL Mode
        </button>
        <button onclick="document.documentElement.classList.toggle('dark'); localStorage.theme = document.documentElement.classList.contains('dark') ? 'dark' : 'light';" class="px-lg py-md flex items-center gap-sm text-on-surface hover:bg-surface-container transition-colors font-label-caps text-[14px] uppercase tracking-wider text-left w-full">
            <span class="material-symbols-outlined text-[18px] mr-2">dark_mode</span> Toggle Theme
        </button>
        <div class="h-px w-full bg-outline-variant/30 my-sm"></div>"""

search_str = '        <div class="h-px w-full bg-outline-variant/30 my-sm"></div>'

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if search_str in content and 'Toggle Theme' not in content:
        content = content.replace(search_str, buttons_html)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {file}")
