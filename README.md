# Dir2txt

**Dir2txt** is a Python script that generates a visual tree structure of directories and files, exporting it to a `directory_tree.txt` file.

### Key Features
- **AI-Friendly:** Useful for directory flattening and structure context preparation for RAG pipelines.
- **Recursive Generation:** Scans subfolders.
- **Clean Formatting:** Sorts contents by displaying directories first, followed by files, using clean tree connectors (`├──`, `└──`).
- **Automatic Filtering:** Automatically excludes hidden files (starting with `.`) and irrelevant folders like `__pycache__` and `old`.
- **Error Handling:** Verifies folder existence, validates directory hierarchy, and handles permission errors gracefully.

### Usage
```bash
python tree_generator.py <SubfolderName>
```

### output
```
Dir2txt/ 
--------------------------------------------------
├── Example/
│   └── file_in_this_dir.txt
├── directory_tree.txt
├── README.md
└── tree_generator.py
```