# Cookie-Bucket

A professional desktop application for managing enterprise authentication tokens, featuring a modern graphical user interface. Built with Python & CustomTkinter.

![Cookie Bucket Screenshot](https://github.com/user-attachments/assets/ce8a9a89-b52e-4cc7-8041-f8dcff9cff1a)

## ✨ Features

*   **Modern & Clean UI**: A sleek and intuitive user interface built with the `customtkinter` library, featuring a dark theme.
*   **One-Click Token Retrieval**: Easily fetch authentication tokens for different account types (e.g., RSMY, Red Smith).
*   **Auto-Copy to Clipboard**: Retrieved tokens are automatically copied to your clipboard for immediate use.
*   **Real-time Status Updates**: The application provides clear feedback on the status of token retrieval.
*   **Cross-Platform**: As a Python and Tkinter-based application, it can run on Windows, macOS, and Linux.

## 🚀 Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### Prerequisites

*   Python 3.7 or newer
*   `pip` (Python package installer)

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/lahirusanjika/Cookie-Bucket.git
    cd Cookie-Bucket
    ```

2.  **Create and activate a virtual environment (recommended):**
    ```bash
    # For Linux/macOS
    python3 -m venv venv
    source venv/bin/activate

    # For Windows
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

Run the application with the following command:

```bash
python3 cookie_bucket.py
```

Once the application is running:
1.  Click on either the **"RSMY ACCOUNT"** or **"RED SMITH ACCOUNT"** button.
2.  The application will fetch the corresponding authentication token.
3.  The token will be displayed in the output text area and automatically copied to your clipboard.
4.  The status label will confirm that the token has been copied.

## 🛠️ Built With

*   [Python](https://www.python.org/) - The programming language used.
*   [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) - The UI toolkit for creating the modern GUI.
*   [Requests](https://requests.readthedocs.io/en/latest/) - For making HTTP requests to fetch the tokens.
