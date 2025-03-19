# Obsidian API Query Tool (No Obsidian plugin required)

## Overview
This Python script allows users to make API requests directly from a markdown file within Obsidian. The script processes the ```api``` block in the markdown file, makes the corresponding API request, and replaces the block with the API response wrapped in a ```response``` block.

## How to Use

1. **Ensure Python 3.x is installed** on your machine.
2. **Install the required dependencies** by running the following command:
    ```bash
    pip install -r requirements.txt
    ```

    > **Note:** On some systems, `tkinter` may not be installed by default. If you encounter issues with the file selection dialog, you can install it using:
    
    - For **Ubuntu/Debian**:
      ```bash
      sudo apt-get install python3-tk
      ```

    - For **Windows**:
      `tkinter` is usually included with the standard Python installation. If it's missing, you may need to reinstall Python and ensure that the "tcl/tk and IDLE" option is checked during installation.

    - For **macOS**:
      `tkinter` should be included by default with the Python installation, but if you experience issues, you may need to reinstall Python using Homebrew with `brew install python`.

3. **Create a new page in Obsidian** with an ```api``` block containing your API request, for example:
    ```api
    POST https://jsonplaceholder.typicode.com/posts
    headers: {"Content-Type": "application/json"}
    body: {"title": "Hello", "body": "This is a test", "userId": 1}
    ```

4. **Run the script** by executing:
    ```bash
    python api_request.py
    ```

5. **When prompted**, use the file selection dialog to choose the markdown file containing the ```api``` block you want to process.
6. **The script will replace** the ```api``` block with the response from the API, which will appear in a ```response``` block, like so:

    ```response
    {
        "id": 101,
        "title": "Hello",
        "body": "This is a test",
        "userId": 1
    }
    ```

## Example of Full Markdown File:

```api
POST https://jsonplaceholder.typicode.com/posts
headers: {"Content-Type": "application/json"}
body: {"title": "Hello", "body": "This is a test", "userId": 1}
```

## License
This project is available under an open-source license. Please feel free to use it.