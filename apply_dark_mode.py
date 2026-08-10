import json
import re
import colorsys
import os
import glob

def invert_color(hex_color):
    hex_color = hex_color.strip().lstrip('#')
    if len(hex_color) != 6: return '#' + hex_color
    try:
        r, g, b = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
        h, l, s = colorsys.rgb_to_hls(r/255.0, g/255.0, b/255.0)
        
        # Keep hue, invert lightness, reduce saturation slightly for dark mode
        # Make very light colors very dark, and vice versa
        new_l = 1.0 - l
        
        # adjust extremes to avoid pure white or pure black usually
        if new_l < 0.1: new_l = 0.12
        if new_l > 0.9: new_l = 0.88
        
        new_s = s * 0.8 # desaturate slightly
        
        nr, ng, nb = colorsys.hls_to_rgb(h, new_l, new_s)
        return '#{:02x}{:02x}{:02x}'.format(int(nr*255), int(ng*255), int(nb*255))
    except:
        return '#' + hex_color

colors = {
    "inverse-surface": "#2f3032",
    "background": "#faf9fb",
    "secondary-container": "#7af5f5",
    "surface-container-highest": "#e3e2e4",
    "on-tertiary-fixed": "#291800",
    "primary-fixed-dim": "#b0c9e8",
    "on-tertiary-container": "#ad8a5a",
    "error-container": "#ffdad6",
    "primary-fixed": "#d1e4ff",
    "surface-container": "#efedf0",
    "tertiary": "#201100",
    "surface-variant": "#e3e2e4",
    "on-tertiary-fixed-variant": "#5d4119",
    "outline-variant": "#c3c6ce",
    "secondary": "#006a6a",
    "tertiary-container": "#3b2400",
    "on-surface-variant": "#43474d",
    "on-primary": "#ffffff",
    "on-primary-fixed-variant": "#314863",
    "primary-container": "#102a43",
    "inverse-on-surface": "#f2f0f3",
    "on-error": "#ffffff",
    "surface-container-lowest": "#ffffff",
    "surface": "#faf9fb",
    "tertiary-fixed-dim": "#e8c08c",
    "primary": "#00152a",
    "secondary-fixed-dim": "#5bd9d8",
    "outline": "#74777e",
    "on-surface": "#1b1c1e",
    "on-secondary-fixed-variant": "#004f4f",
    "on-secondary": "#ffffff",
    "inverse-primary": "#b0c9e8",
    "on-primary-container": "#7a92b0",
    "on-tertiary": "#ffffff",
    "error": "#ba1a1a",
    "on-primary-fixed": "#011d35",
    "surface-tint": "#49607c",
    "surface-container-high": "#e9e8ea",
    "surface-bright": "#faf9fb",
    "secondary-fixed": "#7af5f5",
    "surface-dim": "#dbd9dc",
    "on-error-container": "#93000a",
    "surface-container-low": "#f4f3f5",
    "on-background": "#1b1c1e",
    "on-secondary-container": "#007070",
    "on-secondary-fixed": "#002020",
    "tertiary-fixed": "#ffddb4",
    "brand-teal": "#00A6A6",
    "brand-orange": "#FF7A3D"
}

# Special manual overrides for better dark mode aesthetics
dark_overrides = {
    "background": "#121212",
    "surface": "#1e1e1e",
    "surface-variant": "#2a2a2a",
    "on-background": "#e0e0e0",
    "on-surface": "#e0e0e0",
    "on-surface-variant": "#b0b0b0",
    "primary": "#90caf9",
    "on-primary": "#0d47a1",
    "primary-container": "#1976d2",
    "on-primary-container": "#bbdefb",
    "secondary": "#80cbc4",
    "on-secondary": "#004d40",
    "secondary-container": "#00695c",
    "on-secondary-container": "#b2dfdb"
}

# 1. Generate CSS vars for tailwind config
tailwind_colors = {}
for k in colors:
    tailwind_colors[k] = f"var(--color-{k})"

# 2. Generate root (light) CSS
root_css = ":root {\n"
for k, v in colors.items():
    root_css += f"  --color-{k}: {v};\n"
root_css += "}\n"

# 3. Generate .dark CSS
dark_css = ".dark {\n"
for k, v in colors.items():
    dark_val = dark_overrides.get(k, invert_color(v))
    dark_css += f"  --color-{k}: {dark_val};\n"
dark_css += "}\n"

css_block = root_css + dark_css

# We need to replace the colors dict in the HTML tailwind config with tailwind_colors string
# and prepend css_block to the <style> block.

target_dir = r'd:\project 2\Driving School & Licence Training'
os.chdir(target_dir)

for f in glob.glob('*.html'):
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # 1. Replace the colors dict
    # finding the exact colors dict is tricky with regex, let's use the one we extracted
    colors_pattern = r'"colors":\s*\{[^\}]+\}'
    new_colors_str = '"colors": ' + json.dumps(tailwind_colors, indent=22)
    new_content = re.sub(colors_pattern, new_colors_str, content)
    
    # 2. Inject CSS block inside <style>
    if ":root {" not in new_content: # prevent double injection
        new_content = re.sub(r'<style>', f'<style>\n{css_block}', new_content)
    
    # 3. Ensure body has transition for smooth dark mode switching
    new_content = new_content.replace('<body class="', '<body class="transition-colors duration-300 ')
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(new_content)
    
    print(f'Processed {f}')
