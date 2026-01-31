from itertools import product
import time
from itertools import product
from rich.live import Live
from rich.console import Console
from rich.table import Table



# WHAT ABOUT XOR!



# def Truth_table(variables , formula):
def Truth_table():  
    #cant use Strip() bc it only removes the start and end white spaces 
    vars = input("Please Enter Variables(Example : q,r) : ").replace(" ","").split(",")
    formula = input("Give me the fromula using python logic (Exapmle : q or r) : ")    
    table = Table(title="Truth Table")
    for var in vars:
        table.add_column(var)

    table.add_column("result")
    #print(" | " .join(variables) + " | Result" )# prints the lines between vars
    #print("-" *( 4 * len(variables) + 9) )# prints the line beneeth the vars and result 
# we have to have 2 arguments with this one . first one the number of state a variable can be in , in this case 2
# secoond repeat means how many times it is going to make groups and try all the combinations 
    for values in product([True , False] , repeat=len(vars)):
        eval_env = dict(zip(vars , values))
        
        try:
            result = eval(formula , {} , eval_env )
            
        except Exception as e:
                print(f"err evaluting formula : {e}")
                return
        
        row_values = [ '1' if v else '0' for v in values ]
        result_str = '1' if result else '0'
        table.add_row(*row_values, result_str)

        
        #row = " | ".join(['1' if v else '0' for v in values]) + " | " + ('1' if result else '0') 
        #print(row)
    console = Console()
    console.print(table)


if __name__ == "__main__" : # for making this useable for anyone who wants to import , the name is equal to main when its directly executed 
     Truth_table()

#satisfiability check
#def is_satisfiable(variables, formula):
    #for values in product([True, False], repeat=len(variables)):
       # eval_env = dict(zip(variables, values))
       # try:
         #   result = eval(formula, {}, eval_env)
        #    if result:
       #         return True
      #  except Exception as e:
     #       print(f"Error evaluating formula: {e}")
    #        return False
   # return False