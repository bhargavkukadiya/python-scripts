import os
import json
import argparse

def list_directory(path, include_hidden=False, recursive=False):
    result = []

    def should_include(name):
        return include_hidden or not name.startswith('.')

    def explore(current_path):
        for entry in os.scandir(current_path):
            if should_include(entry.name):
                item = {
                    'name': entry.name,
                    'path': entry.path,
                    'type': 'folder' if entry.is_dir() else 'file'
                }
                result.append(item)
                if recursive and entry.is_dir():
                    explore(entry.path)

    explore(path)
    return result

def main():
    parser = argparse.ArgumentParser(description="List files and folders in a directory.")
    parser.add_argument("folder", help="Path to the folder")
    parser.add_argument("-R", "--recursive", action="store_true", help="Include subdirectories")
    parser.add_argument("-H", "--hidden", action="store_true", help="Include hidden files and folders")
    args = parser.parse_args()

    if not os.path.isdir(args.folder):
        print(json.dumps({"error": "Provided path is not a directory"}, indent=2))
        return

    data = list_directory(args.folder, include_hidden=args.hidden, recursive=args.recursive)
    print(json.dumps(data, indent=2))

if __name__ == "__main__":
    main()
