import os
import glob

# Get all HTML files in current directory
html_files = glob.glob("*.html")

# Print each HTML file found
if html_files:
    print("HTML files found:")
    for file in html_files:
        print(file)
else:
    print("No HTML files found in current directory")