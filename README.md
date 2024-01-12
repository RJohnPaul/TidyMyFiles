---

# TidyMyFiles

<div align="center">
  <br>
      <img src="https://github.com/RJohnPaul/TidyMyFiles/blob/d224d84f7a811e862747fb749256471ffee9582a/Frame%2022.png" alt="Project Banner">
  </br>
</div>


<div align="center">
  <br>
      <img src="https://github.com/RJohnPaul/Web_Scrapper_Py/blob/4712f33c2d8e06508577dc150a4749bc01362de2/Frame-5.png" alt="Project Banner">
  </br>
</div>
</br>

TidyMyFiles is a Python script that automates the organization of files in a directory and its subdirectories. It categorizes files into folders based on their extensions, providing flexibility through configuration settings. Users can skip specific file types, handle duplicate file names, and customize the logging process.

## Features

- **Organize Files:** Categorize files based on their extensions into folders within an 'Organized' directory.
- **Skip File Types:** Configure the script to skip specific file types during the organization process.
- **Handle Duplicates:** Choose whether to overwrite existing files or rename them uniquely to avoid conflicts.
- **Logging:** Detailed logging of the file organization process for tracking and troubleshooting.
- **Progress Bar:** Interactive progress bar for a visual representation of the organization progress.
- **Configuration File:** Customize settings such as skipped file types, log level, and more using a configuration file.

## Prerequisites

Ensure you have the following prerequisites installed:

- [Python 3.x](https://www.python.org/downloads/)
- [tqdm library](https://github.com/tqdm/tqdm) (install using `pip install tqdm`)
- [configparser library](https://docs.python.org/3/library/configparser.html) (install using `pip install configparser`)

## Usage

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/your-username/TidyMyFiles.git
    cd TidyMyFiles
    ```

2. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Script:**
    ```bash
    python organize_files.py /path/to/your/directory
    ```

4. **Customize Configuration (Optional):**
    Modify the `organize_config.ini` file to adjust settings like skipped file types, log level, and more.

## Configuration Options

- **SkipFileTypes:** List of file extensions to skip during the organization process.
- **OverwriteExistingFiles:** Set to `True` to overwrite existing files; set to `False` to rename files uniquely.
- **LogLevel:** Set the desired log level (e.g., INFO, DEBUG, ERROR) to control the verbosity of logs.

## Example

```python
# Example usage
directory_path = "/path/to/your/directory"
config = load_config()
organize_files(directory_path, config)
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [tqdm](https://github.com/tqdm/tqdm): A fast, extensible progress bar for Python.

<div align="center">
  <br>
      <img src="https://github.com/RJohnPaul/Web_Scrapper_Py/blob/4712f33c2d8e06508577dc150a4749bc01362de2/Frame-5.png" alt="Project Banner">
  </br>
</div>
</br>

---
