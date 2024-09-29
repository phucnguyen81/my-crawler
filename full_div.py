import os

# Function to create a full HTML page with "Previous" and "Next" buttons
def create_full_html(div_content, page_num, total_pages):
    previous_button = f'<a href="div_{page_num - 1}.html"><button>Previous</button></a>' if page_num > 1 else '<button disabled>Previous</button>'
    next_button = f'<a href="div_{page_num + 1}.html"><button>Next</button></a>' if page_num < total_pages else '<button disabled>Next</button>'

    # Create a basic HTML structure with navigation buttons in the header and footer
    full_html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Page {page_num}</title>
    </head>
    <body>
        <header>
            <nav>
                {previous_button} {next_button}
            </nav>
        </header>

        <main>
            {div_content}
        </main>

        <footer>
            <nav>
                {previous_button} {next_button}
            </nav>
        </footer>
    </body>
    </html>
    """
    return full_html

# Iterate over all HTML files and create full HTML pages with navigation buttons
total_pages = 24  # Total number of pages (div_1.html to div_24.html)

for page_num in range(1, total_pages + 1):
    div_filename = f"divs/div_{page_num}.html"
    output_filename = f"full_divs/div_{page_num}.html"

    if os.path.exists(div_filename):
        try:
            # Read the content from div_X.html
            with open(div_filename, 'r', encoding='utf-8') as div_file:
                div_content = div_file.read()

            # Create a full HTML page with navigation buttons
            full_html = create_full_html(div_content, page_num, total_pages)

            # Write the full HTML page to output file
            with open(output_filename, 'w', encoding='utf-8') as output_file:
                output_file.write(full_html)

            print(f"Created {output_filename}")
        except (IOError, OSError) as e:
            print(f"Error processing {div_filename}: {e}")
    else:
        print(f"{div_filename} not found.")
