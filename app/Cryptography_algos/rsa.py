# for now i will focus on the Attacking rsa , it is said by computerphile that if you have public key which is just (e , n) you cant use n to find out p and q therfore you cant find the d and you cant use the euler formula 
# but when p and q are small you factor the n and find the p and q ۱ . if the  two numbers are close to each other we can attack it .
import random
import base64
# this is explecily wrong and cuased issues regerding pow belongs to which one so we do the following to fix it
import sympy
import math
import sys
from rich.console import Console
from sympy.ntheory.primetest import is_square



console = Console()


class Number_Generation:


    def RGV(self):
        '''
        WEAK Random Genrated Values for Genrating a New Value including
        p , q , e , d
        and Showing it to the user

        ''' 

        # generating a Random p and q 
        # there is a part that allow user to test what happens if he chosses the same number 
        p = sympy.randprime(2, 100)
        q = sympy.randprime(2, 100)

        n = p * q
        phi = (p - 1) * (q - 1)


        while True:
            e = random.randint(2 , phi -1)
            
            if math.gcd(e, phi) == 1:
                break
            
            
        public_key_random = (n , e)     

        arr_ch = []
        #there is a function called pow(x,y,z) x to the power of y % Z
        d_canidates_ch = list(range(1 , phi))
        console.print(f"[bold] d = canidates are : {d_canidates_ch}[/bold]")
        for d in d_canidates_ch : 
            if (e *d) % phi == 1:
                arr_ch.append(d)
                console.print(f"[bold] d ={d} [/bold]")
                private_key_random = (d, n)


    
        console.print(f" [bold] \n \n \n this is p :{p} \n this is q :{q}\n this is the n : {n} \n this is the phi : {phi} \n this is the e : {e}  \n \n \n [/bold]")
        


        return {"p":p ,
                "q": q ,
                "n": n ,
                "phi": phi ,
                "e":e ,
                "public_key": public_key_random ,
                "private_key": private_key_random
        }


    def Chosen_WEAK_value_by_user(self) -> int:
        """_summary_
        Values Chosen by user instead of Randomly (this is for p , q , e )
        """ 
        p = int(input("Give me a number for p").strip())
        q = int(input("Give me a number for q").strip())
        n = p * q
        phi = (p - 1) * (q - 1)


        while True:
            e = int(input("Give me a number for e").strip())
            if math.gcd(e, phi) == 1:
                break
            else :
                print("wong wong the number your gave me is WRONG . give me a number just a number : ")


        arr = []
        #there is a function called pow(x,y,z) x to the power of y % Z
        d_canidates = list(range(1 , phi))
        print(f"d = canidates are : {d_canidates}")
        for d in d_canidates : 
            if (e *d) % phi == 1:
                arr.append(d)
                print("d =", d)
                private_key_ch = (d, n)

            public_key_ch = (n , e)

        print(f"this is the acceptable d vals : {arr}")
        return {"p":p ,
                "q": q ,
                "n": n ,
                "phi": phi ,
                "e":e ,
                "public_key": public_key_ch ,
                "private_key": private_key_ch
        }







class Rsa_Attacks:
    
    
    
    
    
    #Educational attack: exponential in bit-size, infeasible for real RSA
    def Small_Prime_Attack(self , n , e):
        p = q = None
        print(f" Attacking Mode : Small Prime Attack \n Variables : n = {n} And e = {e}")
        for i in range(2, math.isqrt(n) +1 ):
            if n % i == 0 :
                p = i
                q =  n // i
                break
        if p is None :
            print("prime not found ")
            return None 
        
            
            
        
        
    
        
        phi = (p-1) * (q-1)
        console.print(f"\n [bold] Your phi is {phi}  [/bold]")
    
        d = pow(e , -1 , phi)
        
        
        
        return {
            "p": p,
            "q": q,
            "phi": phi,
            "d": d
        } 
            
        
        
        
    
    
    
    def LowExponent_Attack(self, n, c, e):
        """_summary_
        Works if m^e < n
        """
        
        if pow(c, e) >= n:
            console.print("Attack Failed - c^e >= n")
            return

        m = round(c ** (1/e))
        if pow(m, e) == c:
            console.print(f"Recovered Message m = {m}")
            return m
        else:
            console.print(f"Failed - m^e != c")
            return None

        
        
        
        
        
        
    def Fermats_Factorization(self ,n:int , e : int ):
        """_summary_
        
        Fermat’s Factorization :(Close Primes)
        This is a classic vulnerability where the user picks p and q that are very close to each other in value.
        The Math: Fermat showed that if p and q are close, $n$ can be represented as a difference of squares: $n = a^2 - b^2$.
        We can find a and b much faster than standard factoring.
        """
        #using pow
        
        
        #n = pow(a ,2 - pow(b ,2))  this wont Work 
        # lets build a logic :
        # for i in range(1 , math.isqrt(n)): cant do this , this goes trough the numbers befor the sqrt of n 
        # its 3 Am man my brain is  mush
        
        
        start = math.isqrt(n)
        if start*start<n:
            start +=1
        for i in range( start , n):
            a = i 
            b2 = a*a - n
            b = math.isqrt(b2)
            
            # checking if this b is a perfect square
            if  b*b == b2 :
                console.print(f"[bold] Factors Found [/bold]")
                break
        p = a - b 
        q = a + b
        phi = (p-1) * (q-1)
        d = pow(e , -1 , phi)
        console.print(f"\n [bold] Your phi is {phi}  [/bold]")
        console.print(f"\n [bold] Your Public Key is ({n} , {e} ) \n Your Private Key is ({n} , {d})  [/bold]")
        
        
