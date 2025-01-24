import subprocess
from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel
from rich.text import Text

def change_hostname(new_hostname):
    try:
        subprocess.run(['sudo', 'scutil', '--set', 'HostName', new_hostname], check=True)
        subprocess.run(['sudo', 'scutil', '--set', 'LocalHostName', new_hostname], check=True)
        subprocess.run(['sudo', 'scutil', '--set', 'ComputerName', new_hostname], check=True)
        return True
    except subprocess.CalledProcessError:
        return False

def main():
    console = Console()

    console.print(Panel("Welcome to the macOS Hostname Changer!", style="bold green"), justify="center")
    
    new_hostname = Prompt.ask("Enter the new hostname")
    
    if new_hostname and len(new_hostname.strip()) > 0:
        console.print(f"[bold blue]Trying to change hostname to:[/bold blue] {new_hostname}", justify="center")
        
        # Change hostname
        if change_hostname(new_hostname):
            console.print(f"[bold green]Success! Your hostname has been changed to {new_hostname}.[/bold green]", justify="center")
        else:
            console.print("[bold red]Error: Could not change hostname. Please try again.[/bold red]", justify="center")
    else:
        console.print("[bold red]Invalid hostname. Please provide a valid hostname.[/bold red]", justify="center")

if __name__ == "__main__":
    main()
