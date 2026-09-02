import os
import sys

ROOT_BASE = r"."

def generate_directory_tree(start_path, output_file='directory_tree.txt'):
    """
    Genates a text file representing the directory tree starting from start_path.
    """
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            abs_start = os.path.abspath(start_path)
            rel_path = os.path.relpath(abs_start, ROOT_BASE)
            if rel_path.startswith('..'):
                f.write(f"[Error: The directory is not under {ROOT_BASE}]\n")
                print(f"Error: '{start_path}' is not under {ROOT_BASE}")
                return

            f.write(f"{os.path.basename(abs_start)}/ \n")
            f.write("-" * 50 + "\n")

            _walk_directory(start_path, f, indent='')

        print(f"Saved: {output_file}")
        print(f"  Starting from: {start_path}")

    except Exception as e:
        print(f"Error while generating the tree: {e}")

def _walk_directory(path, file_handle, indent):
    try:
        entries = os.listdir(path)
        
        # Filter
        filtered_entries = []
        for entry in entries:
            if entry.startswith('.'):
                continue
            if entry in ('old', '__pycache__'):
                continue
            entry_path = os.path.join(path, entry)
            filtered_entries.append((entry, entry_path))
        
        # Order (case-insensitive)
        filtered_entries.sort(key=lambda x: (not os.path.isdir(x[1]), x[0].lower()))
        
        total = len(filtered_entries)
        for index, (entry, entry_path) in enumerate(filtered_entries):
            is_last_item = (index == total - 1)
            connector = '└── ' if is_last_item else '├── '
            next_indent = indent + ('    ' if is_last_item else '│   ')
            
            # Write element
            file_handle.write(f"{indent}{connector}{entry}")
            if os.path.isdir(entry_path):
                file_handle.write('/')
            file_handle.write('\n')
            
            # Recursion for directories
            if os.path.isdir(entry_path):
                _walk_directory(entry_path, file_handle, next_indent)

    except PermissionError:
        file_handle.write(f"{indent}└── [Permission denied]\n")
    except Exception as e:
        file_handle.write(f"{indent}└── [Error: {e}]\n")


def main():
    if len(sys.argv) != 2:
        print("Usage: python tree_generator.py <SubfolderName>")
        print(f"   Example: python tree_generator.py Dir2txt")
        print(f"   → Generates tree for: {ROOT_BASE}\\Dir2txt")
        sys.exit(1)

    subfolder = sys.argv[1].strip()
    
    # Build the full path
    start_path = os.path.join(ROOT_BASE, subfolder)
    
    # check if the path exists and is a directory
    if not os.path.exists(start_path):
        print(f"Error: The folder does not exist:")
        print(f"   {start_path}")
        sys.exit(1)
    
    if not os.path.isdir(start_path):
        print(f"Error: '{start_path}' is not a directory.")
        sys.exit(1)

    # Generate the directory tree and save it to a file
    generate_directory_tree(start_path, 'directory_tree.txt')


if __name__ == "__main__":
    main()