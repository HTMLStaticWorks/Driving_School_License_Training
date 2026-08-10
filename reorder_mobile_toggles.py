import glob

html_files = glob.glob('*.html')

old_str = """        <button onclick="document.documentElement.dir = document.documentElement.dir === 'rtl' ? 'ltr' : 'rtl';" class="px-lg py-md flex items-center gap-sm text-on-surface hover:bg-surface-container transition-colors font-label-caps text-[14px] uppercase tracking-wider text-left w-full">
            <span class="material-symbols-outlined text-[18px] mr-2">swap_horiz</span> RTL Mode
        </button>
        <button onclick="document.documentElement.classList.toggle('dark'); localStorage.theme = document.documentElement.classList.contains('dark') ? 'dark' : 'light';" class="px-lg py-md flex items-center gap-sm text-on-surface hover:bg-surface-container transition-colors font-label-caps text-[14px] uppercase tracking-wider text-left w-full">
            <span class="material-symbols-outlined text-[18px] mr-2">dark_mode</span> Toggle Theme
        </button>
        <div class="h-px w-full bg-outline-variant/30 my-sm"></div>
        <a href="register.html" class="px-lg py-md text-primary font-bold hover:bg-primary/5 transition-colors font-label-caps text-[14px] uppercase tracking-wider">Sign Up</a>
        <a href="login.html" class="px-lg py-md text-secondary hover:bg-secondary/5 transition-colors font-label-caps text-[14px] uppercase tracking-wider">Login</a>"""

new_str = """        <div class="h-px w-full bg-outline-variant/30 my-sm"></div>
        <a href="register.html" class="px-lg py-md text-primary font-bold hover:bg-primary/5 transition-colors font-label-caps text-[14px] uppercase tracking-wider">Sign Up</a>
        <a href="login.html" class="px-lg py-md text-secondary hover:bg-secondary/5 transition-colors font-label-caps text-[14px] uppercase tracking-wider">Login</a>
        <div class="h-px w-full bg-outline-variant/30 my-sm"></div>
        <button onclick="document.documentElement.dir = document.documentElement.dir === 'rtl' ? 'ltr' : 'rtl';" class="px-lg py-md flex items-center gap-sm text-on-surface hover:bg-surface-container transition-colors font-label-caps text-[14px] uppercase tracking-wider text-left w-full">
            <span class="material-symbols-outlined text-[18px] mr-2">swap_horiz</span> RTL Mode
        </button>
        <button onclick="document.documentElement.classList.toggle('dark'); localStorage.theme = document.documentElement.classList.contains('dark') ? 'dark' : 'light';" class="px-lg py-md flex items-center gap-sm text-on-surface hover:bg-surface-container transition-colors font-label-caps text-[14px] uppercase tracking-wider text-left w-full">
            <span class="material-symbols-outlined text-[18px] mr-2">dark_mode</span> Toggle Theme
        </button>"""

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if old_str in content:
        content = content.replace(old_str, new_str)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {file}")
