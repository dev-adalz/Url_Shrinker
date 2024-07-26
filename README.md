# URL Shrinker CLI

This is a simple command-line interface (CLI) tool for URL shrinking, written in Python 3.11. The tool uses the `requests` module to interact with a URL shortening API, the `colorama` module to add some color to the CLI, and the `os` module to handle some background tasks. 
![Home Page](https://github.com/user-attachments/assets/12fabeaf-19bc-41dd-b40e-f75b5e7f477a)
![Generating links](https://github.com/user-attachments/assets/4f90e5e0-e007-444a-8b37-c905865060a7)
![Result](https://github.com/user-attachments/assets/90788129-0f26-4368-9855-c24a794beeb1)


## Features

- Shrinks long URLs into short, manageable links.
- Adds colorful output to the CLI using `colorama`.
- Automates certain tasks using the `os` module.
- Bulk shrinker
- password protective option
- usage of custom alias for the short link

## Prerequisites

- Python 3.11

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/dev-adalz/Url_Shrinker.git
    ```

2. Navigate to the project directory:

    ```bash
    cd Url_Shrinker
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

To use the URL Shrinker CLI, simply run the script with the URL you wish to shorten:

```bash
python main.py
```



## Dependencies
Api that was used:

- `https://spoo.me/api`: The api for shrinking url

The project uses the following Python modules:

- `requests`: For making HTTP requests to the URL shortening API.
- `colorama`: For colorful CLI output.
- `os`: For handling system tasks.
- `Tkinter`: For file dialogue box

## Author

This script is written by 𝗗𝗘𝗩-𝗔𝗗𝗔𝗟𝗭 ™.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```
