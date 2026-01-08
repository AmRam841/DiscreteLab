import typer
from logic.TruthTable import Truth_table
from Cryptography_algos.rsa import Rsa_Main
from rich.console import Console
from Cryptography_algos import AES
import questionary

console = Console()
app = typer.Typer(help="DiscreteLab — Discrete Mathematics Demonstration Tool")

@app.command()
def interactive():
    """
    start interactive mode ! Do it cool! 
    totaly not going to sudo rm rf * you :)
    
    """
    while True : 
        console.print("\n [bold cyan] Discrete Lab ! [/bold cyan]")
        console.print("1) Truth Table generator")
        console.print("2) Rsa Demo")
        console.print("3) Graph Visualation ")
        console.print("4) AES Encryption(suppourts files too!)")
        choice = typer.prompt("Select an option")
        match choice:
            case "1":
                logic_var  = typer.prompt("Enter Your Logic vals ")
                logic_exprstion = typer.prompt("Enter logical expresion")
                Truth_table(logic_var , logic_exprstion)
            case "2":
                run_rsa_demo()
            case "3":
                return True    
            case "4":
                AES.main(input_file1 , output_file1 , password)
            case _:
                console.print("[red] invalid , you gotta give me somthing mannnn[/red]")
            
            
                
    



@app.command()
def truth_table(expr: str):
    """
    Generate and display the truth table for a logical expression.
    """
    Truth_table(Logic  , formula)

@app.command()
def rsa():
    """
    Demonstrate RSA using discrete mathematics concepts.
    """
    run_rsa_demo()

if __name__ == "__main__":
    app()
