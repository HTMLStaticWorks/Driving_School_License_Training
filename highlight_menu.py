import os
import glob
import re

target_dir = r'd:\project 2\Driving School & Licence Training'
os.chdir(target_dir)

# Define the base class string that all nav items currently have
# Note: we will use a regex to match the class string flexibly because of spacing
active_classes = "text-secondary font-label-caps text-label-caps font-bold border-b-2 border-secondary pb-1 transition-colors duration-200 uppercase"
inactive_classes = "text-on-surface-variant font-label-caps text-label-caps hover:text-secondary transition-colors duration-200 uppercase"

for f in glob.glob('*.html'):
    # only modify files that correspond to menu items (or all files if we just check the basename)
    basename = os.path.basename(f)
    
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # We want to replace the class of the <a href="basename"> inside the nav
    # Let's find all nav links
    def replacer(match):
        href = match.group(2)
        if href == basename:
            # this is the active link
            return f'<a class="{active_classes}" href="{href}">'
        else:
            # inactive link
            return f'<a class="{inactive_classes}" href="{href}">'
            
    # The regex targets links inside the nav block
    # We can isolate the nav block first, replace links inside it, and put it back
    nav_match = re.search(r'(<div class="hidden md:flex(?: gap-lg)? items-center(?: gap-lg)?">)(.*?)(</div>\s*<div class="flex items-center gap-md">)', content, flags=re.DOTALL | re.IGNORECASE)
    
    if nav_match:
        nav_start = nav_match.group(1)
        nav_links = nav_match.group(2)
        nav_end = nav_match.group(3)
        
        # In `about.html`, the nav structure is slightly different: it uses <nav> instead of <div> for the links container.
        # Let's handle both.
        pass

    # Actually, a simpler way is just to replace the class directly for all <a> tags that match the expected hrefs
    # since these hrefs are unique to the nav bar typically.
    # To be safe, we only replace inside the nav container.

    # Let's find the nav container: either <nav class="hidden md:flex gap-lg items-center"> or <div class="hidden md:flex items-center gap-lg">
    # Wait, earlier we replaced them all so they might all be <div class="hidden md:flex items-center gap-lg"> except those we didn't touch properly?
    # No, I manually updated about.html to use `<nav class="hidden md:flex gap-lg items-center">`.

    # Let's just do a global replace for the specific known links if they have the inactive or active classes
    
    # Reset all links to inactive first
    content = re.sub(r'<a class="[^"]*" href="(index\.html|home2\.html|about\.html|services\.html|instructors\.html|lesson\.html)">', 
                     lambda m: f'<a class="{inactive_classes}" href="{m.group(1)}">', 
                     content)
                     
    # Now set the active one
    content = re.sub(f'<a class="{inactive_classes}" href="{basename}">',
                     f'<a class="{active_classes}" href="{basename}">',
                     content)

    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
        
    print(f'Processed {f}')
