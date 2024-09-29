import os
from bs4 import BeautifulSoup

# Function to extract the HTML content from the div with id="textToRead" and remove <script> tags
def extract_html_from_div(html_file):
    try:
        with open(html_file, 'r', encoding='utf-8') as file:
            soup = BeautifulSoup(file, 'html.parser')

            # Find the div with id="textToRead"
            text_div = soup.find('div', id='textToRead')

            # Check if the div exists
            if text_div:
                # Remove all <script> tags from the div
                for script_tag in text_div.find_all('script'):
                    script_tag.decompose()  # This removes the <script> tag and its content

                # Return the cleaned HTML content as-is
                return str(text_div).strip()
            else:
                print(f"Div 'textToRead' is empty or missing in {html_file}")
                return None
    except (IOError, OSError) as e:
        print(f"Error reading {html_file}: {e}")
        return None

# Iterate over all HTML files and write the cleaned HTML content to div_X.html files
for page_num in range(1, 25):  # Assuming pages 1 to 24
    html_filename = f"pages/page_{page_num}.html"
    div_filename = f"div_{page_num}.html"

    if os.path.exists(html_filename):
        # Extract the cleaned HTML content from the div
        div_html = extract_html_from_div(html_filename)

        if div_html:
            try:
                # Write the cleaned HTML content to the corresponding div_X.html file
                with open(div_filename, 'w', encoding='utf-8') as div_file:
                    div_file.write(div_html)
                print(f"Extracted and cleaned HTML from {html_filename} and wrote to {div_filename}")
            except (IOError, OSError) as e:
                print(f"Error writing to {div_filename}: {e}")
    else:
        print(f"{html_filename} not found.")
