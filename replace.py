import os
import re

# Directory containing the HTML files
directory = "full_divs"

# Regular expression pattern to match the specific URL with page number
url_pattern = re.compile(r"https://readfrom\.net/iain-hollingshead/page,(\d+),237593-beta_male\.html")

# Function to replace the URL in a single file
def replace_links_in_file(file_path):
    try:
        # Read the content of the HTML file
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        # Replace the URLs using the regular expression pattern
        new_content = url_pattern.sub(r'div_\1.html', content)

        # If any changes were made, overwrite the file with the new content
        if new_content != content:
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(new_content)
            print(f"Updated links in {file_path}")
        else:
            print(f"No links to update in {file_path}")

    except (IOError, OSError) as e:
        print(f"Error processing {file_path}: {e}")

# Iterate over all files in the directory and replace the links
for filename in os.listdir(directory):
    if filename.endswith(".html"):  # Process only HTML files
        file_path = os.path.join(directory, filename)
        replace_links_in_file(file_path)
