from rich.console import Console
from rich.table import Table

def show_help():
    console = Console()
    
    # Create the table
    help_table = Table(title="Python Logic Syntax Guide", show_header=True, header_style="bold magenta")
    
    # Add Columns
    help_table.add_column("Logic Concept", style="cyan", no_wrap=True)
    help_table.add_column("Math Symbol", justify="center")
    help_table.add_column("Type this in Python", style="bold green")
    help_table.add_column("Example Input", style="yellow")

    # Add Rows (The "Number One" Cheat Sheet)
    help_table.add_row("AND", "∧", "and", "p and q")
    help_table.add_row("OR", "∨", "or", "p or q")
    help_table.add_row("NOT", "¬", "not", "not p")
    help_table.add_row("XOR", "⊕", "^", "p ^ q")
    help_table.add_row("IF...THEN", "→", "not ... or ...", "not p or q")
    help_table.add_row("IFF (Equals)", "↔", "==", "p == q")

    
    console.print(help_table)
    console.print("\n") 


if __name__ == "__main__":
    show_help()
   