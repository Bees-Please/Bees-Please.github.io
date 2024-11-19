import os
import geocoder
import sys
from datetime import date, datetime

# --- NECESSARY FILE LOCATIONS ---
cwd = os.getcwd() # CWD
to_render = sys.argv[1]
conf = sys.argv[2]
markdown_files = cwd + "\\blog\\md_files\\posts" # CWD -> markdown posts
rendered_files = cwd + "\\blog\\entry" # CWD -> rendered-HTML posts
post_list = cwd + "blog\\index.html" # index file of the post list (newest->oldest)
template = cwd + "\\blog\\entry\\1970-1-1_Template_=D\\index.html" # post page template

# --- TIME-LOC POSTING ---
local_time = datetime.now().astimezone().strftime("%H:%M:%S") # gets your local time
loc = geocoder.ip("me") # gets your generic location
date = date.today()

# basic steps:
# try and read the md file
#   check if the file is md, if its not reject and exit
#   close file
#
# perform render -> render_text
# open HTML template
#
