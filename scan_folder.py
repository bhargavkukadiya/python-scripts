import os
import json
import argparse

def list_directory(path, include_hidden=False, recursive=False, files_only=False):
    """
    Lists files and/or folders in a given path.

    Args:
        path (str): The path to the directory to list.
        include_hidden (bool): If True, includes hidden files and folders.
        recursive (bool): If True, lists contents of subdirectories recursively.
        files_only (bool): If True, only lists files and omits folders.

    Returns:
        list: A list of dictionaries, each representing a file or folder.
    """
    result = []

    def should_include(name):
        """Checks if a file/folder should be included based on the hidden flag."""
        return include_hidden or not name.startswith('.')

    def explore(current_path):
        """Recursively explores a directory and appends items to the result list."""
        try:
            for entry in os.scandir(current_path):
                if should_include(entry.name):
                    is_dir = entry.is_dir()
                    
                    # If it's a directory
                    if is_dir:
                        # Add the folder to the result list if we are not in files_only mode
                        if not files_only:
                            item = {
                                'name': entry.name,
                                'path': entry.path,
                                'type': 'folder'
                            }
                            result.append(item)
                        # If recursive is enabled, explore this directory
                        if recursive:
                            explore(entry.path)
                    # If it's a file, always add it to the result list
                    else:
                        item = {
                            'name': entry.name,
                            'path': entry.path,
                            'type': 'file'
                        }
                        result.append(item)
        except OSError as e:
            # Handle potential permission errors gracefully
            print(json.dumps({"error": f"Cannot access '{current_path}': {e}"}, indent=2))


    explore(path)
    return result

def main():
    """Parses command-line arguments and prints the directory listing."""
    parser = argparse.ArgumentParser(description="List files and folders in a directory, with an interactive prompt for the output format.")
    parser.add_argument("folder", help="Path to the folder to be listed.")
    parser.add_argument("-R", "--recursive", action="store_true", help="List subdirectories recursively.")
    parser.add_argument("-H", "--hidden", action="store_true", help="Include hidden files and folders (those starting with a dot).")
    parser.add_argument("-F", "--files-only", action="store_true", help="Only list files, do not include folders in the output.")
    args = parser.parse_args()

    # Check if the provided path is a valid directory
    if not os.path.isdir(args.folder):
        print(json.dumps({"error": "The provided path is not a directory or does not exist."}, indent=2))
        return

    # Get the directory listing based on the provided arguments
    data = list_directory(
        args.folder, 
        include_hidden=args.hidden, 
        recursive=args.recursive, 
        files_only=args.files_only
    )
    
    # If no data, exit early
    if not data:
        print("No items found matching the criteria.")
        return

    # Interactive prompt for output format
    while True:
        print("\nPlease select an output format:")
        print("  1: JSON")
        print("  2: List")
        choice = input("Enter your choice (1 or 2): ")

        if choice == '1':
            print(json.dumps(data, indent=2))
            break
        elif choice == '2':
            for item in data:
                # Add a prefix to distinguish between files and folders in list view
                prefix = "[D]" if item['type'] == 'folder' else "[F]"
                print(f"{prefix} {item['path']}")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")


if __name__ == "__main__":
    main()
