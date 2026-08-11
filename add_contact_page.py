import os
import glob
import re

# 1. Create contact.html from about.html
with open('about.html', 'r', encoding='utf-8') as f:
    about_content = f.read()

# Extract sections
# Head
head_match = re.search(r'(<!DOCTYPE html>.*?</nav>)', about_content, re.DOTALL)
head_nav = head_match.group(1)

# Footer and below
footer_match = re.search(r'(<!-- Footer JSON Component -->.*)', about_content, re.DOTALL)
footer_below = footer_match.group(1)

# Replace active nav link in head_nav if any
head_nav = head_nav.replace('About', 'About') # keep about as is
# Actually, the active link in about.html is About. We want Contact to be active.
head_nav = head_nav.replace(
    '<a class="text-secondary font-label-caps text-label-caps font-bold border-b-2 border-secondary pb-1 transition-colors duration-200 uppercase" href="about.html">About</a>',
    '<a class="text-on-surface-variant font-label-caps text-label-caps hover:text-secondary transition-colors duration-200 uppercase" href="about.html">About</a>'
)

# Insert contact link in head_nav
lesson_link = '<a class="text-on-surface-variant font-label-caps text-label-caps hover:text-secondary transition-colors duration-200 uppercase" href="lesson.html">Lesson</a>'
contact_link_active = '<a class="text-secondary font-label-caps text-label-caps font-bold border-b-2 border-secondary pb-1 transition-colors duration-200 uppercase" href="contact.html">Contact</a>'

if lesson_link in head_nav:
    head_nav = head_nav.replace(lesson_link, lesson_link + '\n' + contact_link_active)

contact_body = """
<!-- 1. Hero Section -->
<section class="relative min-h-[50vh] flex items-center pt-2xl pb-xl overflow-hidden bg-surface-container-low">
    <div class="relative z-10 w-full px-gutter max-w-container-max mx-auto text-center scroll-reveal">
        <h1 class="text-display-lg font-display-lg text-primary mb-sm leading-tight">
            Get in <span class="text-secondary">Touch</span>
        </h1>
        <p class="text-body-lg font-body-lg text-on-surface-variant max-w-2xl mx-auto">
            Have questions about our driving lessons, schedules, or pricing? We're here to help you get on the road safely.
        </p>
    </div>
</section>

<!-- 2. Contact Information & Form -->
<section class="py-2xl bg-surface relative overflow-hidden">
    <div class="w-full px-gutter max-w-container-max mx-auto">
        <div class="flex flex-col lg:flex-row gap-xl">
            <!-- Contact Info -->
            <div class="w-full lg:w-1/3 scroll-reveal flex flex-col gap-lg">
                <div class="bg-surface-container-lowest p-lg rounded-xl premium-shadow border border-outline-variant/20 flex flex-col gap-sm">
                    <div class="w-12 h-12 rounded-full bg-primary/10 flex items-center justify-center text-primary mb-xs">
                        <span class="material-symbols-outlined text-[24px]">location_on</span>
                    </div>
                    <h3 class="text-headline-md font-headline-md text-primary">Visit Us</h3>
                    <p class="text-body-md font-body-md text-on-surface-variant">123 Driving School Lane<br>Cityville, ST 12345</p>
                </div>
                
                <div class="bg-surface-container-lowest p-lg rounded-xl premium-shadow border border-outline-variant/20 flex flex-col gap-sm">
                    <div class="w-12 h-12 rounded-full bg-secondary/10 flex items-center justify-center text-secondary mb-xs">
                        <span class="material-symbols-outlined text-[24px]">call</span>
                    </div>
                    <h3 class="text-headline-md font-headline-md text-primary">Call Us</h3>
                    <p class="text-body-md font-body-md text-on-surface-variant">Main: (555) 123-4567<br>Support: (555) 987-6543</p>
                </div>
                
                <div class="bg-surface-container-lowest p-lg rounded-xl premium-shadow border border-outline-variant/20 flex flex-col gap-sm">
                    <div class="w-12 h-12 rounded-full bg-tertiary/10 flex items-center justify-center text-tertiary mb-xs">
                        <span class="material-symbols-outlined text-[24px]">mail</span>
                    </div>
                    <h3 class="text-headline-md font-headline-md text-primary">Email Us</h3>
                    <p class="text-body-md font-body-md text-on-surface-variant">info@elitedriving.com<br>support@elitedriving.com</p>
                </div>
            </div>
            
            <!-- Contact Form -->
            <div class="w-full lg:w-2/3 scroll-reveal delay-100">
                <div class="bg-surface-container-lowest p-xl rounded-xl premium-shadow border border-outline-variant/20">
                    <h2 class="text-headline-lg font-headline-lg text-primary mb-sm">Send us a Message</h2>
                    <p class="text-body-md font-body-md text-on-surface-variant mb-lg">Fill out the form below and our team will get back to you within 24 hours.</p>
                    
                    <form class="flex flex-col gap-lg" onsubmit="event.preventDefault(); alert('Message sent successfully!');">
                        <div class="grid grid-cols-1 md:grid-cols-2 gap-lg">
                            <div class="flex flex-col gap-xs">
                                <label for="name" class="text-label-caps font-label-caps text-on-surface-variant uppercase tracking-wider">Full Name</label>
                                <input type="text" id="name" class="bg-surface text-on-surface border border-outline-variant/50 rounded-lg px-md py-sm focus:ring-2 focus:ring-secondary focus:border-secondary outline-none transition-all" placeholder="John Doe" required>
                            </div>
                            <div class="flex flex-col gap-xs">
                                <label for="email" class="text-label-caps font-label-caps text-on-surface-variant uppercase tracking-wider">Email Address</label>
                                <input type="email" id="email" class="bg-surface text-on-surface border border-outline-variant/50 rounded-lg px-md py-sm focus:ring-2 focus:ring-secondary focus:border-secondary outline-none transition-all" placeholder="john@example.com" required>
                            </div>
                        </div>
                        
                        <div class="flex flex-col gap-xs">
                            <label for="subject" class="text-label-caps font-label-caps text-on-surface-variant uppercase tracking-wider">Subject</label>
                            <input type="text" id="subject" class="bg-surface text-on-surface border border-outline-variant/50 rounded-lg px-md py-sm focus:ring-2 focus:ring-secondary focus:border-secondary outline-none transition-all" placeholder="How can we help you?" required>
                        </div>
                        
                        <div class="flex flex-col gap-xs">
                            <label for="message" class="text-label-caps font-label-caps text-on-surface-variant uppercase tracking-wider">Message</label>
                            <textarea id="message" rows="5" class="bg-surface text-on-surface border border-outline-variant/50 rounded-lg px-md py-sm focus:ring-2 focus:ring-secondary focus:border-secondary outline-none transition-all resize-y" placeholder="Write your message here..." required></textarea>
                        </div>
                        
                        <button type="submit" class="bg-primary text-on-primary font-label-caps text-label-caps uppercase tracking-wider py-md px-xl rounded-lg hover:bg-primary-container hover:text-on-primary-container transition-colors shadow-sm self-start mt-sm">
                            Send Message
                        </button>
                    </form>
                </div>
            </div>
        </div>
    </div>
</section>
"""

# Update page title
head_nav = head_nav.replace('<title>About Us - CARZDRIZ</title>', '<title>Contact Us - CARZDRIZ</title>')

contact_html = head_nav + '\n' + contact_body + '\n' + footer_below

with open('contact.html', 'w', encoding='utf-8') as f:
    f.write(contact_html)

# 2. Update navigation in all HTML files
lesson_link_reg = '<a class="text-on-surface-variant font-label-caps text-label-caps hover:text-secondary transition-colors duration-200 uppercase" href="lesson.html">Lesson</a>'
lesson_link_active = '<a class="text-secondary font-label-caps text-label-caps font-bold border-b-2 border-secondary pb-1 transition-colors duration-200 uppercase" href="lesson.html">Lesson</a>'
contact_link_reg = '<a class="text-on-surface-variant font-label-caps text-label-caps hover:text-secondary transition-colors duration-200 uppercase" href="contact.html">Contact</a>'

footer_lesson = '<a class="text-on-primary/70 font-label-caps text-label-caps hover:text-secondary transition-colors duration-200 uppercase" href="lesson.html">Lesson Packages</a>'
footer_lesson_active = '<a class="text-secondary font-label-caps text-label-caps font-bold border-b-2 border-secondary pb-1 transition-colors duration-200 uppercase" href="lesson.html">Lesson Packages</a>'
footer_contact = '<a class="text-on-primary/70 font-label-caps text-label-caps hover:text-secondary transition-colors duration-200 uppercase" href="contact.html">Contact</a>'

mobile_lesson = '<a href="lesson.html" class="px-lg py-md text-on-surface hover:bg-surface-container transition-colors font-label-caps text-[14px] uppercase tracking-wider">Lesson</a>'
mobile_contact = '<a href="contact.html" class="px-lg py-md text-on-surface hover:bg-surface-container transition-colors font-label-caps text-[14px] uppercase tracking-wider">Contact</a>'

html_files = glob.glob('*.html') + ['nav_block.txt']

for filepath in html_files:
    if not os.path.exists(filepath):
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Skip if contact is already added
    if 'href="contact.html"' in content and filepath != 'contact.html':
        continue
        
    new_content = content

    # Replace Top Nav
    if lesson_link_reg in new_content:
        new_content = new_content.replace(lesson_link_reg, lesson_link_reg + '\n' + contact_link_reg)
    elif lesson_link_active in new_content:
        new_content = new_content.replace(lesson_link_active, lesson_link_active + '\n' + contact_link_reg)

    # Replace Footer Nav
    if footer_lesson in new_content:
        new_content = new_content.replace(footer_lesson, footer_lesson + '\n            ' + footer_contact)
    elif footer_lesson_active in new_content:
        new_content = new_content.replace(footer_lesson_active, footer_lesson_active + '\n            ' + footer_contact)

    # Replace Mobile Nav
    if mobile_lesson in new_content:
        new_content = new_content.replace(mobile_lesson, mobile_lesson + '\n        ' + mobile_contact)

    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f'Updated {filepath}')

print('Done.')
