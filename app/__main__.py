import typer
from logic.TruthTable import Truth_table
#from Cryptography_algos.rsa import Rsa_Main
from rich.console import Console
from Cryptography_algos import AES
from Cryptography_algos import rsa
# from Cryptography_algos.rsa import run_rsa_attack_lab
import questionary
from GraphModels.graph import Graph
import random
import sys
import os
from logic import help_logic


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
        os.system('cls' if os.name == 'nt' else 'clear')
        console.print("\n [bold cyan] Discrete Lab ! [/bold cyan]")
        console.print("1) Truth Table generator")
        console.print("2) Rsa Demo")
        console.print("3) Graph Visualation ")
        console.print("4) AES Encryption(suppourts files too!)")
        global choice_main_menu_var;
        choice_main_menu_var = typer.prompt("Select an option")
        match choice_main_menu_var:
           
           
           
           
           
            case "1":
                os.system('cls' if os.name == 'nt' else 'clear')
                # logic_var  = typer.prompt("Enter Your Logic vals ")
                # logic_exprstion = typer.prompt("Enter logical expresion")
                # Truth_table(logic_var , logic_exprstion)
                help_logic.show_help()
                Truth_table()
                
                Returnto_main_menu.Return_to_main_menu()
           
           
           
           
           
            case "2":
                os.system('cls' if os.name == 'nt' else 'clear')
                randomly_chosen =input("do you want to Generate weak  p , q , e , d  Randomly ? (y/n)").lower().strip()
                #rsa.RGV() if randomly_chosen == "y"  else rsa.Chosen_WEAK_value_by_user()
                gen = rsa.Number_Generation()
                attack = rsa.Rsa_Attacks()
                p, q, n, phi, e, public_key, private_key = gen.RGV().values() if randomly_chosen == "y" else gen.Chosen_WEAK_value_by_user()
                
                
                
                attack_choice = input("Do You want to Go in Attack mode : (y/n)").strip().lower()
                match attack_choice:
                    case "y":
                        
                        console.print("\n [bold cyan] Attack mode ENABLED [/bold cyan]")
                        console.print("\n [bold] 1) Small Primes Attack [/bold]")
                        console.print("\n [bold] 2) Fermat Factorazation Attack [/bold]")
                        console.print("\n [bold] 3) Low Exponent Attack  [/bold]")
                        
                        attack_oprion_Choice = input("\n Give Me the Number You choose : ").strip()
                        match attack_oprion_Choice:
                            
                            case '1':
                                attack.Small_Prime_Attack(n , e)
                            case "2":
                                attack.Fermats_Factorization(n , e)
                            case "3":
                                os.system('cls' if os.name == 'nt' else 'clear')
                                e_attack = 3              
                                m = 2                     
                                n = 6241
                                #c = pow(m , e)
                                c= 8
                                console.print(f" the numbers are fixed due to the nature of this attack the fixed are the following :e : {e} , m : {m} , n = {n} , c = {c}")
                                attack.LowExponent_Attack(n, c, e_attack)
                    
                
                
                Returnto_main_menu.Return_to_main_menu()
                
            case "3":
           
           
             while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                console.print(f"[bold cyan] Grpah Module Activated [/bold cyan]")
                console.print(f"[bold] Choose which one is  \n 1) Graph Visualizer(using pre-given Data set) \n 2) Graph Shortest Path [/bold]")
                chose_vis_short = input().strip()
                match chose_vis_short:
                    case "1":
                        Graph.GraphVisualizer.Visualizer()
                        Returnto_main_menu.Return_to_main_menu()
                        
                    case "2":
                        choice = Graph.ChooseAlgoMenu.ChooseAlgo()
                        num_nodes = random.randint(6, 10)
                        G = Graph.ShortestPath.Random_Creat_Graph(num_nodes)
                        print(f"\nGenerated graph with {num_nodes} nodes.")
                        print(f"Node weights: {[G.nodes[i]['weight'] for i in G.nodes()]}")
                        print("Nodes:", list(G.nodes()))
        
                        start = int(input("Choose start node: "))
                        end = int(input("Choose end node: "))
        
                        length, path = Graph.ChooseAlgoMenu.run_algo(G, choice, start, end)
                        
                        print(f"Shortest path: {path}")
                        print(f"Total distance: {length}")
                        again  = input("run another graph? (y/n)").lower().strip()
                        if again == "n":
                            break
                        Returnto_main_menu.Return_to_main_menu(
                            
                        )
                        
            case "4":
                AES.main()
                Returnto_main_menu.Return_to_main_menu()
            case _:
                console.print("[red] invalid , you gotta give me somthing mannnn[/red]")
                
                
class Returnto_main_menu:  
    
                 
    def Return_to_main_menu():
        
           # returns  = input("Do you want to go back to the Main menu ?(y/n) ").strip().lower()
            returns = input("\nDo you want to go back to the Main menu? (y/n): ").strip().lower()
            if returns == "n":
                print("Goodbye!")
                sys.exit()
                
        
            

if __name__ == "__main__":
 app()
