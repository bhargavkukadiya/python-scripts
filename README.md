# 📁 File Explorer Script

This Python script allows you to explore a folder and return a list of files and directories in JSON format.

## 🚀 Features

- List all files and folders in a specified directory
- Optionally include hidden files and folders
- Optionally list files and folders recursively
- Output results in JSON format

## 🛠️ Requirements

- Python 3.x

## 📦 Directory Structure

```
📂 your-folder/
├── script.py
└── README.md
```

## 📄 Usage

```bash
python script.py /path/to/folder
```

### Include Hidden Files

```bash
python script.py /path/to/folder --hidden
```

### Include Recursively

```bash
python script.py /path/to/folder --recursive
```

### Combine Both

```bash
python script.py /path/to/folder --hidden --recursive
```

## 🔧 Arguments

| Argument         | Description                       |
|------------------|-----------------------------------|
| `-h`, `--hidden` | Include hidden files and folders  |
| `-r`, `--recursive` | Include files recursively     |

## 📤 Output Example

```json
{
    "files": [
        "file1.txt",
        ".hiddenfile"
    ],
    "folders": [
        "subfolder",
        ".hiddendir"
    ]
}
```

## 📃 License

MIT License
