import os, glob, re

target_dir = r'd:\project 2\Driving School & Licence Training'
os.chdir(target_dir)

new_nav = '''<div class="hidden md:flex items-center gap-lg">
<a class="text-on-surface-variant font-label-caps text-label-caps hover:text-secondary transition-colors duration-200 uppercase" href="index.html">Home</a>
<a class="text-on-surface-variant font-label-caps text-label-caps hover:text-secondary transition-colors duration-200 uppercase" href="home2.html">Home 2</a>
<a class="text-on-surface-variant font-label-caps text-label-caps hover:text-secondary transition-colors duration-200 uppercase" href="about.html">About</a>
<a class="text-on-surface-variant font-label-caps text-label-caps hover:text-secondary transition-colors duration-200 uppercase" href="services.html">Services</a>
<a class="text-on-surface-variant font-label-caps text-label-caps hover:text-secondary transition-colors duration-200 uppercase" href="instructors.html">Instructors</a>
<a class="text-on-surface-variant font-label-caps text-label-caps hover:text-secondary transition-colors duration-200 uppercase" href="lesson.html">Lesson</a>
</div>
<div class="flex items-center gap-md">
<button onclick="document.documentElement.dir = document.documentElement.dir === 'rtl' ? 'ltr' : 'rtl';" aria-label="Toggle RTL" class="hidden md:flex items-center text-on-surface-variant font-label-caps text-label-caps hover:text-primary transition-colors uppercase tracking-wider">
RTL
</button>
<button onclick="document.documentElement.classList.toggle('dark');" aria-label="Toggle Dark Mode" class="hidden md:flex items-center text-on-surface-variant hover:text-primary transition-colors p-sm rounded-full hover:bg-surface-container">
<span class="material-symbols-outlined">dark_mode</span>
</button>
<a class="inline-flex items-center justify-center font-label-caps text-label-caps bg-primary text-on-primary px-lg py-sm rounded-lg shadow-sm hover:shadow-md hover:bg-primary-container hover:text-on-primary-container transition-all uppercase tracking-wider" href="register.html">Sign Up</a>
</div>'''

for f in glob.glob('*.html'):
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Try replacing in files with the same structure as index.html
    new_content, count = re.subn(r'<div class="hidden md:flex(?: gap-lg)? items-center(?: gap-lg)?">\s*<a[^>]*?>Lessons</a>.*?(?:Sign Up</a>|</button>)\s*</div>', new_nav, content, flags=re.DOTALL | re.IGNORECASE)
    
    if count > 0:
        with open(f, 'w', encoding='utf-8') as file:
            file.write(new_content)
        print(f'Updated {f}')
