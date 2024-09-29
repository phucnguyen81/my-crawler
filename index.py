# Function to create the index.html file
def create_index_html(total_pages):
    toc_items = ""

    # Generate a list of links to each div_X.html page
    for page_num in range(1, total_pages + 1):
        toc_items += f'        <li><a href="div_{page_num}.html">Page {page_num}</a></li>\n'

    # Create the full HTML for the index page
    index_html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Table of Contents</title>
</head>
<body>
    <h1>Table of Contents</h1>
    <ul>
{toc_items}
    </ul>
</body>
</html>
    """
    return index_html

# Write the index.html file
total_pages = 24  # Total number of pages (div_1.html to div_24.html)
index_filename = "index.html"

try:
    # Generate the index HTML content
    index_html_content = create_index_html(total_pages)

    # Write the index.html file
    with open(index_filename, 'w', encoding='utf-8') as index_file:
        index_file.write(index_html_content)

    print(f"Created {index_filename}")
except (IOError, OSError) as e:
    print(f"Error writing to {index_filename}: {e}")
