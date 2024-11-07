import os
import shutil
import markdown
import geocoder
from datetime import date, datetime

# --- NECESSARY FILE LOCATIONS ---
cwd = os.getcwd() # CWD
markdown_files = cwd + "\\blog\\md_files\\posts" # CWD -> markdown posts
rendered_files = cwd + "\\blog\\entry" # CWD -> rendered-HTML posts
post_list = cwd + "blog\\index.html" # index file of the post list (newest->oldest)
template = cwd + "\\blog\\entry\\1970-1-1_Template_=D\\index.html" # post page template

# --- TIME-LOC POSTING ---
local_time = datetime.now().astimezone().strftime("%H:%M:%S") # gets your local time
loc = geocoder.ip("me") # gets your generic location

# cool kids only beyond this point
class Post:
    def __init__(self, name):

        self.name = name

        self.md_folder = '' # the post dir under the vault
        self.md_assets = '' # the assets subdir
        self.md_file = '' # the .md file
        self.render_folder = '' # folder for the site containing the HTML
        self.index = '' # file in which the post is actually posted
        self.body = f'PUT IT IN REVERSE TERRY' # fill just in case
        self.location = f"{loc.state}, {loc.country}" if loc.country == "US" else f"{loc.city}, {loc.country}"
        self.stamp = f'{local_time} ' \
                     f'({self.location})'
        self.images = []
        self.date = date.today()

    # Create MD file structure at CWD
    def create_empty_post(self):
        folders = [f"{markdown_files}\\{self.date}_{self.name}", f"{markdown_files}\\{self.date}_{self.name}\\assets"]

        # make parent folders
        for folder in folders:
            if not os.path.exists(folder):
                os.makedirs(folder)
            else:
                print("### Folder already exists.")

        self.md_folder = folders[0]
        self.md_assets = folders[1]

        # try to make the md file
        try:
            self.md_file = open(f"{markdown_files}\\{self.date}_{self.name}\\{self.date}_{self.name}.md", "x")
            self.md_file.write(f'{self.date} | {self.stamp}\n\n---')
            self.md_file = f"{markdown_files}\\{self.date}_{self.name}\\{self.date}_{self.name}.md"
        except:
            self.md_file = f"{markdown_files}\\{self.date}_{self.name}\\{self.date}_{self.name}.md"
            print("### File already exists.")

        return self

    # create render output directory
    def create_render_location(self):
        # Create post folder and index file

        if not os.path.exists(f'{rendered_files}\\{self.date}_{self.name}\\'):
            os.makedirs(f'{rendered_files}\\{self.date}_{self.name}\\')

        self.render_folder = f'{rendered_files}\\{self.date}_{self.name}\\'

        try:
            with open(f"{rendered_files}\\{self.date}_{self.name}\\index.html", "x") as file:
                file.write(f'{self.date} | {self.stamp}\n\n---')
            print('### Made render location')
        except:
            print(f'### HTML File already exists at {rendered_files}\\{self.date}_{self.name}\\index.html')

        self.index = f"{rendered_files}\\{self.date}_{self.name}\\index.html"

        return self

    def render(self):
        print('ARE YOU SURE? (Y/N)')
        x = input()
        if x == 'Y':
            # read template file
            with open(template, "r", encoding="utf-8") as template_file:
                post_template = template_file.read()
                self.body = markdown.markdown(post_template)

            # read input file
            with open(self.md_file, "r", encoding="utf-8") as input_file:
                file = input_file.read()
                render = f"" + markdown.markdown(file)

            # back fill template with html text
            self.body = self.body.replace("%title%", self.name)
            self.body = self.body.replace("%body%", render)

            # get images from MD assets and move to post images
                # get list of images in assets
            md_images = next(os.walk(self.md_assets), (None, None, []))[2]  # [] if no file
            render_images = next(os.walk(self.render_folder))


                # if the image isnt in the render folder, copy it
                # also add the image to the images of this object
            for image in md_images:
                print('### moved image ' + image)
                self.images.append(image)
                if image not in render_images:
                    shutil.copyfile(self.md_assets + f'\\{image}', self.render_folder + f'{image}')
                else:
                    print(f'### {image} was found in destination already, skipping')

                self.body = self.body.replace(f'![[{image}]]', f'</p><p><img style="  display: block; margin-left: auto; margin-right: auto; width: 50%;" src="{image}">')

            # write to a new html file
            with open(f'{rendered_files}\\{self.date}_{self.name}\\index.html', "w") as output_file:
                output_file.write(self.body)

            output_file.close()

            print('### file rendered.')

        elif x == 'N':
            print('CANCELING.')
        else:
            print('INPUT INVALID, CANCELING.')

    def post(self):
        # read template file
        with open(template, "r", encoding="utf-8") as template_file:
            post_template = template_file.read()
            self.body = markdown.markdown(post_template)



post = Post("Concern, apathy, confusion")
post.create_empty_post()
post.create_render_location()
post.render()

# Works good so far, next i need to make it so that it dumps it into the html template for posts.
# Template is built,
# Need to add a clause that fills the title tag with the name of the file/ post :D
# need to do some auto filling