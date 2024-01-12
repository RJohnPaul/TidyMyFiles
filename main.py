import os
import shutil
import logging
from collections import defaultdict
import configparser
from tqdm import tqdm

def load_config():
    """
    Load configuration settings from a file.

    Returns:
    - config (configparser.ConfigParser): Configuration settings.
    """
    config = configparser.ConfigParser()
    config_file = 'organize_config.ini'

    if os.path.exists(config_file):
        config.read(config_file)
    else:
        # Default settings
        config['General'] = {
            'SkipFileTypes': 'log,ini',
            'OverwriteExistingFiles': 'False',
            'LogLevel': 'INFO'
        }

        with open(config_file, 'w') as configfile:
            config.write(configfile)

    return config

def organize_files(directory_path, config):
    """
    Organizes files in a directory and its subdirectories by categorizing them into folders based on their extensions.

    Parameters:
    - directory_path (str): The path to the directory containing the files to be organized.
    - config (configparser.ConfigParser): Configuration settings.
    """
    try:
        # Create a subdirectory called 'Organized' within the specified directory
        organized_dir = os.path.join(directory_path, 'Organized')
        os.makedirs(organized_dir, exist_ok=True)

        # Configure logging to save information about the organization process
        log_file = os.path.join(organized_dir, 'organize_log.txt')
        log_level = config.get('General', 'LogLevel').upper()
        logging.basicConfig(filename=log_file, level=getattr(logging, log_level), format='%(asctime)s - %(levelname)s: %(message)s')

        # List all files in the directory and its subdirectories
        files = []
        for root, _, filenames in os.walk(directory_path):
            files.extend([os.path.join(root, filename) for filename in filenames])

        # Initialize a defaultdict to count the number of files moved to each category
        files_count = defaultdict(int)

        # Skip file types from configuration
        skip_file_types = [ext.strip().lower() for ext in config.get('General', 'SkipFileTypes').split(',')]

        # Determine whether to overwrite existing files or rename them uniquely
        overwrite_files = config.getboolean('General', 'OverwriteExistingFiles')

        # Iterate through each file and organize it based on its extension
        for file_path in tqdm(files, desc='Organizing Files', unit='file'):
            _, file_ext = os.path.splitext(file_path)

            # Check if the file type should be skipped
            if file_ext[1:].lower() in skip_file_types:
                continue

            # Create a directory for the file extension if it doesn't exist
            ext_dir = os.path.join(organized_dir, file_ext[1:].lower())  # Ignore the leading dot
            os.makedirs(ext_dir, exist_ok=True)

            # Check for duplicate file names in the target directory
            counter = 1
            new_file_name = os.path.basename(file_path)
            new_file_path = os.path.join(ext_dir, new_file_name)

            while os.path.exists(new_file_path):
                if overwrite_files:
                    os.remove(new_file_path)
                    break
                else:
                    base_name, ext = os.path.splitext(new_file_name)
                    new_file_name = f"{base_name}_{counter}{ext}"
                    new_file_path = os.path.join(ext_dir, new_file_name)
                    counter += 1

            # Move the file to the corresponding directory
            shutil.move(file_path, new_file_path)

            # Log the file movement
            logging.info(f"Moved '{file_path}' to '{ext_dir}' as '{new_file_name}'")

            # Update the count for the category
            files_count[file_ext[1:].lower()] += 1

        print("Files successfully organized.")
        logging.info("Organization process completed.")

        # Display a summary of the organization process
        print("\nSummary:")
        for category, count in files_count.items():
            print(f"  {category}: {count} files")

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        logging.error(f"Error during organization process: {str(e)}")

# Example usage
directory_path = "/path/to/your/directory"
config = load_config()
organize_files(directory_path, config)
