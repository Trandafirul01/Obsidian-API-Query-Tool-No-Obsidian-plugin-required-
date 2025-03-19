import os
import json
import requests
from tkinter import Tk, filedialog

# Function to extract API details from the .md file
def extract_api_details(md_file_path):
    with open(md_file_path, "r") as file:
        content = file.read()

    # Look for the ` ```api` block
    start_idx = content.find("```api")
    end_idx = content.find("```", start_idx + 6)  # End of the code block
    
    if start_idx == -1 or end_idx == -1:
        raise ValueError("API request block not found in the file")
    
    api_code = content[start_idx + 6:end_idx].strip()
    return api_code

# Function to send the API request
def send_api_request(api_code):
    # Extract request method, URL, headers, and body from the api_code
    lines = api_code.splitlines()
    
    method, url = lines[0].split(" ", 1)
    headers = json.loads(lines[1].split(":", 1)[1].strip())
    body = json.loads(lines[2].split(":", 1)[1].strip())
    
    # Send the API request based on the extracted details
    response = requests.request(method, url, headers=headers, json=body)
    return response

# Function to update the .md file with the response
def update_md_file(md_file_path, response):
    with open(md_file_path, "r") as file:
        content = file.read()

    # Find the start and end of the ` ```api` block
    start_idx = content.find("```api")
    end_idx = content.find("```", start_idx + 6)

    if start_idx == -1 or end_idx == -1:
        raise ValueError("API request block not found in the file")

    # Replace the ` ```api` block with the response
    updated_content = content[:start_idx] + f"```response\n{response.text}\n```" + content[end_idx + 3:]
    
    # Save the updated content back to the file
    with open(md_file_path, "w") as file:
        file.write(updated_content)

# Function to allow file selection from Obsidian
def select_md_file():
    Tk().withdraw()  # Hide the Tkinter root window
    file_path = filedialog.askopenfilename(filetypes=[("Markdown files", "*.md")])
    return file_path

def main():
    try:
        # Allow user to select the markdown file
        md_file_path = select_md_file()
        
        if not md_file_path:
            print("No file selected. Exiting.")
            return
        
        print(f"Selected file: {md_file_path}")
        
        # Extract the API code block from the file
        api_code = extract_api_details(md_file_path)
        
        # Send the API request and get the response
        response = send_api_request(api_code)
        
        # Update the .md file with the response
        update_md_file(md_file_path, response)
        
        print("File successfully updated with API response!")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
