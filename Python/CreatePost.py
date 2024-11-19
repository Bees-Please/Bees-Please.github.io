import os
import geocoder
import sys
from datetime import date, datetime

name = sys.argv[1]
name = name.replace(' ', '_')
print(f'[warning] Creating render space for {name}')


# --- NECESSARY FILE LOCATIONS ---
cwd = os.getcwd() # CWD
markdown_files = cwd + "\\blog\\md_files\\posts" # CWD -> markdown posts
rendered_files = cwd + "\\blog\\entry" # CWD -> rendered-HTML posts
post_list = cwd + "blog\\index.html" # index file of the post list (newest->oldest)
template = cwd + "\\blog\\entry\\1970-1-1_Template_=D\\index.html" # post page template

# --- TIME-LOC POSTING ---
local_time = datetime.now().astimezone().strftime("%H:%M:%S") # gets your local time
loc = geocoder.ip("me") # gets your generic location
date = date.today()


folders = [f"{markdown_files}\\{date}_{name}", f"{markdown_files}\\{date}_{name}\\assets"]

stamp = f'{local_time} ' \
        f'({f"{loc.state}, {loc.country}" if loc.country == "US" else f"{loc.city}, {loc.country}"})'

# make parent folders
for folder in folders:
    if not os.path.exists(folder):
        os.makedirs(folder)
    else:
        print('[warning] Folder already exists.')

md_folder = folders[0]
md_assets = folders[1]
md_file = ''

# try to make the md file
try:
    md_file = open(f"{markdown_files}\\{date}_{name}\\{date}_{name}.md", "x")
    md_file.write(f'{date} | {stamp}\n\n---')
    md_file = f"{markdown_files}\\{date}_{name}\\{date}_{name}.md"
    print("[success] File created.")
except:
    md_file = f"{markdown_files}\\{date}_{name}\\{date}_{name}.md"
    print("[warning] File already exists.")

print(f"md file at {markdown_files}\\{date}_{name}\\{date}_{name}.md")

# Create post folder and index file

if not os.path.exists(f'{rendered_files}\\{date}_{name}\\'):
    os.makedirs(f'{rendered_files}\\{date}_{name}\\')

render_folder = f'{rendered_files}\\{date}_{name}\\'

try:
    open(f"{rendered_files}\\{date}_{name}\\index.html", "x")
    print('[success] Made render location')
except:
    print(f'[warning] HTML File already exists at {rendered_files}\\{date}_{name}\\index.html')

index = f"{rendered_files}\\{date}_{name}\\index.html"