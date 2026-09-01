import re
import glob

print("Executing site identity overhaul: Alignment with Driving School & License Training...")

# 1. Update index.html fleet section
with open('index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

new_fleet_section = '''<!-- Fleet Showcase -->
<section class="py-2xl px-gutter max-w-container-max mx-auto bg-surface overflow-hidden">
<div class="text-center mb-xl flex flex-col items-center gap-sm animate-on-scroll">
<span class="font-label-caps text-label-caps uppercase text-brand-orange tracking-widest font-bold">Dual-Controlled Fleet</span>
<h2 class="font-headline-md text-headline-md text-primary dark:text-on-surface">Certified Student Training Vehicles</h2>
<p class="font-body-md text-body-md text-on-surface-variant max-w-2xl">Learn safely in late-model, dual-controlled student cars equipped with instructor safety pedals, L-plates, and reversing aids.</p>
</div>
<div class="grid grid-cols-1 md:grid-cols-3 gap-lg">
<!-- Car 1 -->
<div class="bg-surface-container-lowest dark:bg-surface-container-high rounded-2xl border border-outline-variant/30 shadow-md hover:shadow-xl transition-all overflow-hidden flex flex-col group relative">
<div class="h-52 bg-surface-container-highest relative flex items-center justify-center overflow-hidden">
<img src="https://images.unsplash.com/photo-1605559424843-9e4c228bf1c2?auto=format&fit=crop&w=600&q=80" alt="Dual-Control Hatchback Training Car" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
<div class="absolute top-3 left-3 bg-red-600 text-white font-black px-2.5 py-1 rounded text-xs tracking-widest shadow-md uppercase">L-Plate Certified</div>
<div class="absolute bottom-3 right-3 bg-surface/90 dark:bg-surface-container-highest/90 backdrop-blur-md px-2.5 py-1 rounded-full text-[11px] font-bold text-primary dark:text-on-surface border border-outline-variant/30 flex items-center gap-1">
<span class="material-symbols-outlined text-[14px] text-brand-orange">verified</span> Dual Controls Installed
</div>
</div>
<div class="p-lg flex flex-col gap-md">
<div>
<div class="flex justify-between items-center mb-1">
<h3 class="font-headline-md text-[20px] text-primary dark:text-on-surface font-bold">Compact Learner Hatchback</h3>
<span class="bg-brand-teal/10 text-brand-teal px-sm py-xs rounded text-[11px] font-bold uppercase tracking-wider">Automatic</span>
</div>
<p class="font-body-sm text-body-sm text-on-surface-variant">Ideal for beginners — easy steering, tight turning radius, and clear all-round visibility for parking maneuvers.</p>
</div>
<ul class="flex flex-col gap-sm border-t border-outline-variant/20 pt-md">
<li class="flex items-center gap-sm font-body-sm text-body-sm text-on-surface-variant"><span class="material-symbols-outlined text-brand-teal text-[18px]">check_circle</span> Dual Brake & Accelerator Override</li>
<li class="flex items-center gap-sm font-body-sm text-body-sm text-on-surface-variant"><span class="material-symbols-outlined text-brand-teal text-[18px]">check_circle</span> Rear Parking Camera & Sensors</li>
<li class="flex items-center gap-sm font-body-sm text-body-sm text-on-surface-variant"><span class="material-symbols-outlined text-brand-teal text-[18px]">check_circle</span> State DMV & DVSA Test Approved</li>
</ul>
</div>
</div>

<!-- Car 2 -->
<div class="bg-surface-container-lowest dark:bg-surface-container-high rounded-2xl border border-outline-variant/30 shadow-md hover:shadow-xl transition-all overflow-hidden flex flex-col group relative">
<div class="h-52 bg-surface-container-highest relative flex items-center justify-center overflow-hidden">
<img src="https://images.unsplash.com/photo-1549317661-bd32c8ce0db2?auto=format&fit=crop&w=600&q=80" alt="Dual-Control Manual Training Sedan" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
<div class="absolute top-3 left-3 bg-red-600 text-white font-black px-2.5 py-1 rounded text-xs tracking-widest shadow-md uppercase">L-Plate Certified</div>
<div class="absolute bottom-3 right-3 bg-surface/90 dark:bg-surface-container-highest/90 backdrop-blur-md px-2.5 py-1 rounded-full text-[11px] font-bold text-primary dark:text-on-surface border border-outline-variant/30 flex items-center gap-1">
<span class="material-symbols-outlined text-[14px] text-brand-orange">verified</span> Dual Controls Installed
</div>
</div>
<div class="p-lg flex flex-col gap-md">
<div>
<div class="flex justify-between items-center mb-1">
<h3 class="font-headline-md text-[20px] text-primary dark:text-on-surface font-bold">Midsize Training Sedan</h3>
<span class="bg-secondary/10 text-secondary dark:text-brand-teal px-sm py-xs rounded text-[11px] font-bold uppercase tracking-wider">Manual</span>
</div>
<p class="font-body-sm text-body-sm text-on-surface-variant">Perfect for mastering clutch control, gear selection, hill starts, and highway merging for manual driver licensing.</p>
</div>
<ul class="flex flex-col gap-sm border-t border-outline-variant/20 pt-md">
<li class="flex items-center gap-sm font-body-sm text-body-sm text-on-surface-variant"><span class="material-symbols-outlined text-secondary dark:text-brand-teal text-[18px]">check_circle</span> Dual Brake & Clutch Instructor Pedals</li>
<li class="flex items-center gap-sm font-body-sm text-body-sm text-on-surface-variant"><span class="material-symbols-outlined text-secondary dark:text-brand-teal text-[18px]">check_circle</span> Hill-Start Assist Technology</li>
<li class="flex items-center gap-sm font-body-sm text-body-sm text-on-surface-variant"><span class="material-symbols-outlined text-secondary dark:text-brand-teal text-[18px]">check_circle</span> Official Test Center Vehicle Rental</li>
</ul>
</div>
</div>

<!-- Car 3 -->
<div class="bg-surface-container-lowest dark:bg-surface-container-high rounded-2xl border border-outline-variant/30 shadow-md hover:shadow-xl transition-all overflow-hidden flex flex-col group relative">
<div class="h-52 bg-surface-container-highest relative flex items-center justify-center overflow-hidden">
<img src="https://images.unsplash.com/photo-1533473359331-0135ef1b58bf?auto=format&fit=crop&w=600&q=80" alt="Dual-Control SUV Training Vehicle" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
<div class="absolute top-3 left-3 bg-red-600 text-white font-black px-2.5 py-1 rounded text-xs tracking-widest shadow-md uppercase">L-Plate Certified</div>
<div class="absolute bottom-3 right-3 bg-surface/90 dark:bg-surface-container-highest/90 backdrop-blur-md px-2.5 py-1 rounded-full text-[11px] font-bold text-primary dark:text-on-surface border border-outline-variant/30 flex items-center gap-1">
<span class="material-symbols-outlined text-[14px] text-brand-orange">verified</span> Dual Controls Installed
</div>
</div>
<div class="p-lg flex flex-col gap-md">
<div>
<div class="flex justify-between items-center mb-1">
<h3 class="font-headline-md text-[20px] text-primary dark:text-on-surface font-bold">High-Visibility Training SUV</h3>
<span class="bg-brand-teal/10 text-brand-teal px-sm py-xs rounded text-[11px] font-bold uppercase tracking-wider">Automatic</span>
</div>
<p class="font-body-sm text-body-sm text-on-surface-variant">Elevated seating position giving nervous learners maximum road view, 360-degree cameras, and blind-spot detection.</p>
</div>
<ul class="flex flex-col gap-sm border-t border-outline-variant/20 pt-md">
<li class="flex items-center gap-sm font-body-sm text-body-sm text-on-surface-variant"><span class="material-symbols-outlined text-brand-teal text-[18px]">check_circle</span> Dual Instructor Overrides & Safety Mirrors</li>
<li class="flex items-center gap-sm font-body-sm text-body-sm text-on-surface-variant"><span class="material-symbols-outlined text-brand-teal text-[18px]">check_circle</span> 360-Degree Bird\'s-Eye Parking Assist</li>
<li class="flex items-center gap-sm font-body-sm text-body-sm text-on-surface-variant"><span class="material-symbols-outlined text-brand-teal text-[18px]">check_circle</span> Full Student Driver Insurance Coverage</li>
</ul>
</div>
</div>
</div>
</section>'''

index_content = re.sub(r'<!-- Fleet Showcase -->.*?<!-- Student Testimonials -->', new_fleet_section + '\n<!-- Student Testimonials -->', index_content, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(index_content)

print("Updated index.html Fleet section with Dual-Control Training Vehicle badges and titles.")

# Check all HTML files for any leftover dealership or car repair phrases
for file_path in sorted(glob.glob('*.html')):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace Performance Hatchback / dealership terms if present in other files
    content = content.replace('Performance Hatchback', 'Dual-Control Compact Hatchback')
    content = content.replace('Manual Sedan', 'Dual-Control Training Sedan')
    content = content.replace('Automatic SUV', 'Dual-Control Training SUV')
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Site identity overhaul script completed successfully.")
