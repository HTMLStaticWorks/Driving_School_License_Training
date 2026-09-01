import re
import glob

print("Starting Driving School & License Training visual & content overhaul...")

# 1. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

# Replace Hero section in index.html
new_index_hero = '''<!-- Hero Section -->
<section class="px-gutter py-2xl max-w-container-max mx-auto overflow-hidden relative">
<div class="grid md:grid-cols-2 gap-xl items-center">
<div class="flex flex-col gap-lg z-10 text-center md:text-left items-center md:items-start">
<div class="flex flex-wrap gap-2 justify-center md:justify-start">
    <div class="inline-flex items-center gap-sm bg-secondary-container/20 text-on-secondary-container dark:text-brand-teal px-md py-xs rounded-full border border-secondary-container/30">
        <span class="material-symbols-outlined text-[16px] text-brand-orange icon-fill">verified</span>
        <span class="font-label-caps text-label-caps uppercase tracking-wider font-bold">DMV & DVSA Approved Driving School</span>
    </div>
    <div class="inline-flex items-center gap-xs bg-primary/5 dark:bg-surface-container-high text-primary dark:text-on-surface px-md py-xs rounded-full border border-outline-variant/30">
        <span class="material-symbols-outlined text-[16px] text-secondary">directions_car</span>
        <span class="font-label-caps text-label-caps uppercase tracking-wider">Dual-Control Safety Fleet</span>
    </div>
</div>
<h1 class="font-display-lg text-headline-lg-mobile md:text-display-lg text-primary dark:text-on-surface leading-tight">
    Master the Road. <br/><span class="text-secondary dark:text-brand-teal">Pass Your Test.</span> <br/><span class="text-brand-orange">Get Your Driver's License.</span>
</h1>
<p class="font-body-lg text-body-lg text-on-surface-variant max-w-lg mx-auto md:mx-0">
    Certified 1-on-1 driving instruction, dual-controlled training vehicles, hazard perception prep, and express driver licensing programs tailored for all experience levels.
</p>
<div class="flex flex-col sm:flex-row flex-wrap gap-md pt-sm justify-center md:justify-start w-full sm:w-auto">
    <a class="inline-flex items-center justify-center gap-2 font-label-caps text-label-caps bg-brand-orange hover:bg-[#e6692e] text-white border-2 border-transparent px-lg py-md rounded-lg shadow-md hover:shadow-lg hover:-translate-y-[1px] transition-all uppercase tracking-wider w-full sm:w-auto min-h-[48px] whitespace-nowrap font-bold" href="contact.html">
        <span class="material-symbols-outlined text-[20px]">directions_car</span>
        Book a Driving Lesson
    </a>
    <a class="inline-flex items-center justify-center gap-2 font-label-caps text-label-caps text-secondary dark:text-brand-teal border-2 border-secondary dark:border-brand-teal px-lg py-md rounded-lg hover:bg-secondary/10 transition-colors uppercase tracking-wider w-full sm:w-auto min-h-[48px] whitespace-nowrap font-bold" href="lesson.html">
        <span class="material-symbols-outlined text-[20px]">badge</span>
        View License Packages
    </a>
</div>
<!-- Key Trust Badges -->
<div class="grid grid-cols-3 gap-md pt-md border-t border-outline-variant/30 w-full">
    <div class="flex flex-col items-center md:items-start">
        <span class="font-headline-md text-[22px] font-bold text-primary dark:text-on-surface">96%</span>
        <span class="text-[11px] font-medium text-on-surface-variant uppercase tracking-wide">1st-Time Pass Rate</span>
    </div>
    <div class="flex flex-col items-center md:items-start">
        <span class="font-headline-md text-[22px] font-bold text-secondary dark:text-brand-teal">15,000+</span>
        <span class="text-[11px] font-medium text-on-surface-variant uppercase tracking-wide">Licensed Graduates</span>
    </div>
    <div class="flex flex-col items-center md:items-start">
        <span class="font-headline-md text-[22px] font-bold text-brand-orange">100%</span>
        <span class="text-[11px] font-medium text-on-surface-variant uppercase tracking-wide">Certified ADI Team</span>
    </div>
</div>
</div>
<div class="relative h-[440px] md:h-[600px] rounded-2xl overflow-hidden shadow-2xl border border-outline-variant/20 group">
<div class="absolute inset-0 bg-gradient-to-tr from-primary/30 via-transparent to-transparent z-10 mix-blend-multiply"></div>
<img class="absolute inset-0 w-full h-full object-cover object-top group-hover:scale-105 transition-transform duration-700" data-alt="A professional driving instructor in a modern dual-control car, smiling encouragingly at a young female student driver behind the wheel." src="https://lh3.googleusercontent.com/aida-public/AB6AXuBtlLmysGiGeVVtk842RbG_rQ8BPeh2LMNrhaeIG1CXxUsGAYJJ_vbflIYbz2clB8tYxzgi7NWgRlAN2WLw8NlLiRI_Cg3HzH5JD_LzZo5iYnwGt7G2-DaeLBhTXXk8sXfUBUaFhJH2U5z8WdBvTDOj3NGsh9wI4Lb-yl-4t5Nwy0OPkRZQx62ufDav7PA-S1ybkQ8zAz-gKi6YBOq-9ZdiK7MY1XOfHEgSc0DR72YIfFpXX9S4IYFM"/>

<!-- Floating Overlay Badge 1 -->
<div class="absolute bottom-6 left-6 z-20 bg-surface/95 dark:bg-surface-container-highest/95 backdrop-blur-md p-md rounded-xl border border-outline-variant/40 shadow-xl flex items-center gap-md max-w-[280px]">
    <div class="w-10 h-10 rounded-lg bg-secondary/10 dark:bg-secondary/20 flex items-center justify-center text-secondary dark:text-brand-teal shrink-0">
        <span class="material-symbols-outlined text-[24px]">workspace_premium</span>
    </div>
    <div>
        <h4 class="font-bold text-body-sm text-primary dark:text-on-surface">Guaranteed Test Ready</h4>
        <p class="text-[12px] text-on-surface-variant">Full mock examiner route testing</p>
    </div>
</div>
<!-- Floating Overlay Badge 2 -->
<div class="absolute top-6 right-6 z-20 bg-surface/95 dark:bg-surface-container-highest/95 backdrop-blur-md px-md py-sm rounded-full border border-outline-variant/40 shadow-lg flex items-center gap-sm">
    <span class="w-2.5 h-2.5 rounded-full bg-emerald-500 animate-pulse"></span>
    <span class="text-[12px] font-bold text-primary dark:text-on-surface">Dual-Control Safety Fleet</span>
</div>
</div>
</div>
</section>'''

index_content = re.sub(r'<!-- Hero Section -->.*?<!-- Stats Section -->', new_index_hero + '\n<!-- Stats Section -->', index_content, flags=re.DOTALL)

# Insert Roadmap Section after Stats section
new_roadmap_section = '''
<!-- 4-Step License Roadmap Section -->
<section class="py-2xl px-gutter max-w-container-max mx-auto bg-surface-container-low/50 dark:bg-surface-container-lowest/30 border-y border-outline-variant/20">
<div class="text-center mb-xl flex flex-col items-center gap-sm">
    <span class="font-label-caps text-label-caps uppercase text-brand-orange tracking-widest font-bold">Your Road to Success</span>
    <h2 class="font-headline-md text-headline-md text-primary dark:text-on-surface">4-Step Driver License Roadmap</h2>
    <p class="font-body-md text-body-md text-on-surface-variant max-w-2xl">Our structured step-by-step curriculum takes you from a complete beginner to a confident, fully licensed driver.</p>
</div>
<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-lg relative">
    <!-- Step 1 -->
    <div class="bg-surface dark:bg-surface-container-high p-lg rounded-xl border border-outline-variant/30 shadow-sm hover:shadow-md transition-all flex flex-col gap-md relative group">
        <div class="w-12 h-12 rounded-xl bg-primary/10 dark:bg-primary/20 text-primary dark:text-brand-teal flex items-center justify-center font-bold font-headline-md text-xl">01</div>
        <div>
            <h3 class="font-headline-md text-[18px] text-primary dark:text-on-surface mb-xs">Theory & Permit Prep</h3>
            <p class="font-body-sm text-body-sm text-on-surface-variant">Master rules of the road, road signs, and hazard perception prep to pass your written permit exam.</p>
        </div>
        <div class="mt-auto pt-sm border-t border-outline-variant/20 flex items-center gap-2 text-[12px] font-bold text-secondary dark:text-brand-teal">
            <span class="material-symbols-outlined text-[16px]">menu_book</span> Written Test Readiness
        </div>
    </div>
    <!-- Step 2 -->
    <div class="bg-surface dark:bg-surface-container-high p-lg rounded-xl border border-outline-variant/30 shadow-sm hover:shadow-md transition-all flex flex-col gap-md relative group">
        <div class="w-12 h-12 rounded-xl bg-secondary/10 dark:bg-secondary/20 text-secondary dark:text-brand-teal flex items-center justify-center font-bold font-headline-md text-xl">02</div>
        <div>
            <h3 class="font-headline-md text-[18px] text-primary dark:text-on-surface mb-xs">Dual-Control Basics</h3>
            <p class="font-body-sm text-body-sm text-on-surface-variant">Build confidence behind the wheel with 1-on-1 instruction in quiet residential areas using dual controls.</p>
        </div>
        <div class="mt-auto pt-sm border-t border-outline-variant/20 flex items-center gap-2 text-[12px] font-bold text-secondary dark:text-brand-teal">
            <span class="material-symbols-outlined text-[16px]">directions_car</span> Vehicle Control Mastery
        </div>
    </div>
    <!-- Step 3 -->
    <div class="bg-surface dark:bg-surface-container-high p-lg rounded-xl border border-outline-variant/30 shadow-sm hover:shadow-md transition-all flex flex-col gap-md relative group">
        <div class="w-12 h-12 rounded-xl bg-brand-orange/10 text-brand-orange flex items-center justify-center font-bold font-headline-md text-xl">03</div>
        <div>
            <h3 class="font-headline-md text-[18px] text-primary dark:text-on-surface mb-xs">Traffic & Maneuvers</h3>
            <p class="font-body-sm text-body-sm text-on-surface-variant">Master parallel parking, 3-point turns, roundabout navigation, and urban traffic integration.</p>
        </div>
        <div class="mt-auto pt-sm border-t border-outline-variant/20 flex items-center gap-2 text-[12px] font-bold text-brand-orange">
            <span class="material-symbols-outlined text-[16px]">alt_route</span> Maneuver Precision
        </div>
    </div>
    <!-- Step 4 -->
    <div class="bg-surface dark:bg-surface-container-high p-lg rounded-xl border border-outline-variant/30 shadow-sm hover:shadow-md transition-all flex flex-col gap-md relative group">
        <div class="w-12 h-12 rounded-xl bg-emerald-500/10 text-emerald-600 dark:text-emerald-400 flex items-center justify-center font-bold font-headline-md text-xl">04</div>
        <div>
            <h3 class="font-headline-md text-[18px] text-primary dark:text-on-surface mb-xs">Mock Exam & License</h3>
            <p class="font-body-sm text-body-sm text-on-surface-variant">Rehearse actual test routes with a mock examiner, pass your official road test, and get licensed!</p>
        </div>
        <div class="mt-auto pt-sm border-t border-outline-variant/20 flex items-center gap-2 text-[12px] font-bold text-emerald-600 dark:text-emerald-400">
            <span class="material-symbols-outlined text-[16px]">verified</span> Driver License Issued
        </div>
    </div>
</div>
</section>
'''

if '4-Step Driver License Roadmap' not in index_content:
    index_content = index_content.replace('</section>\n<!-- Packages Section', '</section>\n' + new_roadmap_section + '\n<!-- Packages Section')

# Update Apex Advantage headline text
index_content = index_content.replace('The Apex Advantage', 'The CARZDRIZ Advantage')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(index_content)

print("Updated index.html hero and license roadmap.")

# 2. Update home2.html
with open('home2.html', 'r', encoding='utf-8') as f:
    home2_content = f.read()

home2_content = home2_content.replace('Learn to Drive. Drive With Confidence.', 'Learn to Drive. Pass Your Road Test. Get Licensed.')
home2_content = home2_content.replace('The Apex Advantage', 'The CARZDRIZ Driving School Advantage')

with open('home2.html', 'w', encoding='utf-8') as f:
    f.write(home2_content)

# 3. Update services.html
with open('services.html', 'r', encoding='utf-8') as f:
    services_content = f.read()

services_content = services_content.replace('Our Professional Services', 'Driver License Training Programs & Services')
services_content = services_content.replace('Tailored driving lessons for every stage of your journey.', 'Comprehensive behind-the-wheel instruction, dual-controlled training, and road test certification.')

with open('services.html', 'w', encoding='utf-8') as f:
    f.write(services_content)

# 4. Update instructors.html
with open('instructors.html', 'r', encoding='utf-8') as f:
    instructors_content = f.read()

instructors_content = instructors_content.replace('Meet Our Expert Instructors', 'Certified ADI & DMV Driving Instructors')
instructors_content = instructors_content.replace('Professional, patient, and dedicated to your success on the road.', 'State-certified 1-on-1 instructors with dual-control safety vehicles and top first-time pass rates.')

with open('instructors.html', 'w', encoding='utf-8') as f:
    f.write(instructors_content)

# 5. Update lesson.html
with open('lesson.html', 'r', encoding='utf-8') as f:
    lesson_content = f.read()

lesson_content = lesson_content.replace('Driving Lesson Packages', 'Driver License & Training Packages')
lesson_content = lesson_content.replace('Structured programs designed for your specific skill level.', 'From zero experience to road test ready. Choose manual or automatic dual-control instruction.')

with open('lesson.html', 'w', encoding='utf-8') as f:
    f.write(lesson_content)

# 6. Update about.html
with open('about.html', 'r', encoding='utf-8') as f:
    about_content = f.read()

about_content = about_content.replace('About Us - CARZDRIZ', 'About CARZDRIZ - Certified Driving & License Academy')
about_content = about_content.replace('Empowering Drivers Since 2014', 'Empowering Safe Drivers & Licensing Graduates Since 2014')

with open('about.html', 'w', encoding='utf-8') as f:
    f.write(about_content)

# 7. Update contact.html
with open('contact.html', 'r', encoding='utf-8') as f:
    contact_content = f.read()

contact_content = contact_content.replace('Book a Lesson', 'Book a Driving Lesson / License Training')
contact_content = contact_content.replace('Get in Touch', 'Get in Touch with CARZDRIZ Driving Academy')

with open('contact.html', 'w', encoding='utf-8') as f:
    f.write(contact_content)

print("Driving School & License Training overhaul complete.")
