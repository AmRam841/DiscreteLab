import typer
from logic.TruthTable import Truth_table
#from Cryptography_algos.rsa import Rsa_Main
from rich.console import Console
from Cryptography_algos import AES
import questionary
from GraphModels.graph import Graph
import random
import sys


#class Main_Menu:

console = Console()
app = typer.Typer(help="DiscreteLab — Discrete Mathematics Demonstration Tool")




@app.command()
def interactive_Menu():
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
        global choice_main_menu_var;
        choice_main_menu_var = typer.prompt("Select an option")
        match choice_main_menu_var:
            case "1":
                # logic_var  = typer.prompt("Enter Your Logic vals ")
                # logic_exprstion = typer.prompt("Enter logical expresion")
                # Truth_table(logic_var , logic_exprstion)
                Truth_table()
                Returnto_main_menu.Return_to_main_menu()
            case "2":
                run_rsa_demo()
            case "3":
                # choice = Graph.ChooseAlgoMenu.ChooseAlgo()
                # num_nodes = random.randint(6, 10)
                # G = Graph.ShortestPath.Random_Creat_Graph(num_nodes)
                # print(f"\nGenerated graph with {num_nodes} nodes.")
                # print(f"Node weights: {[G.nodes[i]['weight'] for i in G.nodes()]}")
                # print("Nodes:", list(G.nodes()))

                # start = int(input("Choose start node: "))
                # end = int(input("Choose end node: "))

                # length, path = Graph.ChooseAlgoMenu.run_algo(G, choice, start, end)
                
                # print(f"Shortest path: {path}")
                # print(f"Total distance: {length}")
                
                choice = Graph.ChooseAlgoMenu.ChooseAlgo()
                num_nodes = random.randint(6, 10)
                G = Graph.ShortestPath.Random_Creat_Graph(num_nodes)

                print(f"\nGenerated graph with {num_nodes} nodes.")
                print("Nodes:", list(G.nodes()))

                start = int(input("Choose start node: "))
                end = int(input("Choose end node: "))

                length, path = Graph.ChooseAlgoMenu.run_algo(G, choice, start, end)

                if path is not None:
                    print(f"Shortest path: {path}")
                    print(f"Total distance: {length}")

                

            case "4":
                AES.main()
                Returnto_main_menu.Return_to_main_menu()
            case _:
                console.print("[red] invalid , you gotta give me somthing mannnn[/red]")
                
class Returnto_main_menu:  
    
                 
    def Return_to_main_menu():
        
            returns  = input("Do you want to go back to the Main menu ?(y/n) ").strip().lower()
            if returns == "y" :
               interactive_Menu()
            #elif returns == "n":
            # how can i just grab the choice_main_menu_var and urn it again 
                
        
            
            
                
    

        

# @app.command()
# def truth_table(expr: str):
#     """
#     Generate and display the truth table for a logical expression.
#     """
#     Truth_table(Logic  , formula)

# @app.command()
# def rsa():
#     """
#     Demonstrate RSA using discrete mathematics concepts.
#     """
#     run_rsa_demo()
# 
# 
if __name__ == "__main__":
 app()
