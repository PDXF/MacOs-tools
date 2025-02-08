import os
import shutil
from rich.console import Console


console = Console()

desktop_path = os.path.expanduser("~/Desktop")
documents_path = os.path.expanduser("~/Documents")

file_types = {
    "Photos": [".jpg", ".jpeg", ".png", ".gif"],
    "Python Code": [".py"],
    "Arduino Code": [".ino"],
    "MP4": [".mp4"],
    "Text Files": [".txt"],
    "Documents": [".pdf", ".docx"],
    "Archives": [".zip", ".rar", ".tar", ".gz", ".7z"],
    "HTML": [".html", ".htm"],
    "CSS": [".css"],
    "JavaScript": [".js"],
    "JSON": [".json"],
    "XML": [".xml"],
    "CSV": [".csv"],
    "Markdown": [".md"],
    "PowerPoint": [".pptx"],
    "Excel": [".xlsx", ".xls"],
    "Audio": [".mp3", ".wav", ".flac"],
    "Ebooks": [".epub", ".mobi"],
    "Fonts": [".ttf", ".otf"],
    "Docker": [".dockerfile", ".yml", ".yaml"],
    "Log Files": [".log"],
    "Shell Scripts": [".sh"],
    "Ruby": [".rb"],
    "Java": [".java"],
    "C++": [".cpp", ".h"],
    "icons": [".icns"],
    "rust": [".rs"],
    "test": [".test"]
}

def sort_files():
    sorted_files = []
    folders_added = []
    
    for category in file_types.keys():
        category_path = os.path.join(documents_path, category)
        if not os.path.exists(category_path):
            os.makedirs(category_path)
            folders_added.append(f"[yellow]Created[/yellow] folder: {category}")
    
    for file_name in os.listdir(desktop_path):
        file_path = os.path.join(desktop_path, file_name)
        if os.path.isfile(file_path):
            moved = False
            for category, extensions in file_types.items():
                for ext in extensions:
                    if file_name.endswith(ext):
                        category_path = os.path.join(documents_path, category)
                        destination = os.path.join(category_path, file_name)
                        shutil.move(file_path, destination)
                        sorted_files.append(f"[green]Moved[/green] {file_name} to {category} folder.")
                        moved = True
                        break
                if moved:
                    break

    return sorted_files, folders_added

def main():
    console.print("[bold magenta]Welcome to AutoSorter![/bold magenta]")
    
    confirm = console.input("[yellow]Do you want to proceed with sorting your desktop files? (yes/no): [/yellow]").strip().lower()
    
    if confirm == "yes":
        sorted_files, folders_added = sort_files()
        
        console.print("\n[bold green]Sorting complete![/bold green]")
        
        console.print("\n[bold cyan]Files that were sorted:[/bold cyan]")
        if sorted_files:
            for sorted_file in sorted_files:
                console.print(sorted_file)
        else:
            console.print("[bold yellow]No files were sorted.[/bold yellow]")

        console.print("\n[bold cyan]Folders that were created (if any):[/bold cyan]")
        if folders_added:
            for folder in folders_added:
                console.print(folder)
        else:
            console.print("[bold yellow]No new folders were created.[/bold yellow]")

    else:
        console.print("[bold red]Sorting aborted.[/bold red]")

if __name__ == "__main__":
    main()
