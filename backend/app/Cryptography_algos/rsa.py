import random
import base64
# this is explecily wrong and cuased issues regerding pow belongs to which one so we do the following to fix it
import sympy
import math
import sys
from rich.console import Console
from sympy.ntheory.primetest import is_square

# #publickey module -
# from Crypto.PublicKey import RSA

# #from Crypto.PublicKey import PKCS1_OAEP
# #binary to hexidecimal 
# from binascii import hexlify


# def RSA_Key():
#  # new Rsa key 
#  # GEnerating a RSA key pair 
#  key = RSA.generate(1024)
#  # Lets set the key to private key 
#  private_key  = key 
#  #Drive the public key from the private key 
#  public_key  = key.public_key()
 
console = Console()
 
 
 

 
 
 
 
 






# def Get_data():
#     return 0 




#  #ENCRYPTION
# def RSA_ENC():
#     return 0
 






































# # import math
# # import random
# # import time
# # from dataclasses import dataclass
# # from typing import Dict, Iterable, List, Optional, Tuple

# # from rich.console import Console
# # from rich.table import Table


# # @dataclass(frozen=True)
# # class RSAKeyPair:
# #     label: str
# #     p: int
# #     q: int
# #     n: int
# #     e: int
# #     d: int


# # @dataclass(frozen!1=True)
# # class AttackResult:
# #     name: str
# #     success: bool
# #     factors: Optional[Tuple[int, int]]
# #     duration_ms: float
# #     notes: str


# # @dataclass(frozen=True)
# # class GraphEdge:
# #     left: str
# #     right: str
# #     shared_factor: int


# # class KeyGenerator:
# #     def __init__(self, bits: int = 128, seed_time: bool = True) -> None:
# #         seed = int(time.time()) if seed_time else None
# #         self._rng = random.Random(seed)
# #         self.bits = bits

# #     def _biased_randbits(self, bits: int) -> int:
# #         raw = self._rng.getrandbits(bits)
# #         return (raw >> 8) << 8

# #     def _is_probable_prime(self, n: int, rounds: int = 8) -> bool:
# #         if n < 2:
# #             return False
# #         small_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
# #         if n in small_primes:
# #             return True
# #         if any(n % p == 0 for p in small_primes):
# #             return False
# #         r, d = 0, n - 1
# #         while d % 2 == 0:
# #             r += 1
# #             d //= 2
# #         for _ in range(rounds):
# #             a = self._rng.randrange(2, n - 2)
# #             x = pow(a, d, n)
# #             if x in (1, n - 1):
# #                 continue
# #             for _ in range(r - 1):
# #                 x = pow(x, 2, n)
# #                 if x == n - 1:
# #                     break
# #             else:
# #                 return False
# #         return True

# #     def _next_prime(self, start: int) -> int:
# #         candidate = start | 1
# #         while not self._is_probable_prime(candidate):
# #             candidate += 2
# #         return candidate

# #     def _generate_prime(self) -> int:
# #         while True:
# #             candidate = self._biased_randbits(self.bits) | (1 << (self.bits - 1)) | 1
# #             if self._is_probable_prime(candidate):
# #                 return candidate

# #     def generate_close_primes(self, gap_max: int = 1 << 12) -> Tuple[int, int]:
# #         p = self._generate_prime()
# #         gap = self._rng.randint(2, gap_max)
# #         q = self._next_prime(p + gap)
# #         return p, q

# #     def generate_weak_keypair(self, label: str) -> RSAKeyPair:
# #         p, q = self.generate_close_primes()
# #         return self._build_keypair(label, p, q)

# #     def generate_small_d_keypair(self, label: str, max_d: int = 1 << 16) -> RSAKeyPair:
# #         p = self._generate_prime()
# #         q = self._generate_prime()
# #         while p == q:
# #             q = self._generate_prime()
# #         phi = (p - 1) * (q - 1)
# #         d = self._rng.randint(3, max_d)
# #         while math.gcd(d, phi) != 1:
# #             d = self._rng.randint(3, max_d)
# #         e = modinv(d, phi)
# #         n = p * q
# #         return RSAKeyPair(label=label, p=p, q=q, n=n, e=e, d=d)

# #     def generate_shared_factor_keys(self, label_prefix: str, count: int = 3) -> List[RSAKeyPair]:
# #         shared_p = self._generate_prime()
# #         keys = []
# #         for idx in range(count):
# #             q = self._generate_prime()
# #             while q == shared_p:
# #                 q = self._generate_prime()
# #             keys.append(self._build_keypair(f"{label_prefix}-{idx + 1}", shared_p, q))
# #         return keys

# #     def _build_keypair(self, label: str, p: int, q: int) -> RSAKeyPair:
# #         n = p * q
# #         phi = (p - 1) * (q - 1)
# #         e = 65537
# #         if math.gcd(e, phi) != 1:
# #             e = 3
# #             while math.gcd(e, phi) != 1:
# #                 e += 2
# #         d = modinv(e, phi)
# #         return RSAKeyPair(label=label, p=p, q=q, n=n, e=e, d=d)


# # def modinv(a: int, modulus: int) -> int:
# #     g, x, _ = extended_gcd(a, modulus)
# #     if g != 1:
# #         raise ValueError("No modular inverse")
# #     return x % modulus


# # def extended_gcd(a: int, b: int) -> Tuple[int, int, int]:
# #     if b == 0:
# #         return a, 1, 0
# #     g, x1, y1 = extended_gcd(b, a % b)
# #     return g, y1, x1 - (a // b) * y1


# # class AttackEngine:
# #     def fermat_attack(self, n: int, max_iterations: int = 1_000_000) -> Optional[Tuple[int, int]]:
# #         a = math.isqrt(n)
# #         if a * a < n:
# #             a += 1
# #         for _ in range(max_iterations):
# #             b2 = a * a - n
# #             b = math.isqrt(b2)
# #             if b * b == b2:
# #                 return a - b, a + b
# #             a += 1
# #         return None

# #     def pollards_rho(self, n: int, max_iterations: int = 100_000) -> Optional[Tuple[int, int]]:
# #         if n % 2 == 0:
# #             return 2, n // 2
# #         rng = random.Random(42)
# #         for _ in range(5):
# #             x = rng.randrange(2, n - 1)
# #             y = x
# #             c = rng.randrange(1, n - 1)
# #             d = 1
# #             for _ in range(max_iterations):
# #                 x = (pow(x, 2, n) + c) % n
# #                 y = (pow(y, 2, n) + c) % n
# #                 y = (pow(y, 2, n) + c) % n
# #                 d = math.gcd(abs(x - y), n)
# #                 if d == 1:
# #                     continue
# #                 if d == n:
# #                     break
# #                 return d, n // d
# #         return None

# #     def wiener_attack(self, e: int, n: int) -> Optional[Tuple[int, int]]:
# #         for k, d in continued_fraction_convergents(e, n):
# #             if k == 0:
# #                 continue
# #             if (e * d - 1) % k != 0:
# #                 continue
# #             phi = (e * d - 1) // k
# #             b = n - phi + 1
# #             disc = b * b - 4 * n
# #             if disc < 0:
# #                 continue
# #             root = math.isqrt(disc)
# #             if root * root != disc:
# #                 continue
# #             p = (b + root) // 2
# #             q = (b - root) // 2
# #             if p * q == n:
# #                 return p, q
# #         return None

# #     def gcd_batch_attack(self, moduli: Iterable[Tuple[str, int]]) -> List[GraphEdge]:
# #         items = list(moduli)
# #         edges: List[GraphEdge] = []
# #         for idx, (label_a, n_a) in enumerate(items):
# #             for label_b, n_b in items[idx + 1 :]:
# #                 g = math.gcd(n_a, n_b)
# #                 if g != 1 and g != n_a and g != n_b:
# #                     edges.append(GraphEdge(left=label_a, right=label_b, shared_factor=g))
# #         return edges


# # class Visualization:
# #     def __init__(self, console: Console) -> None:
# #         self.console = console

# #     def render_relationships(self, edges: List[GraphEdge]) -> None:
# #         table = Table(title="Modulus Relationship Graph", show_lines=True)
# #         table.add_column("Key A")
# #         table.add_column("Key B")
# #         table.add_column("Shared Factor")
# #         if not edges:
# #             table.add_row("(none)", "(none)", "(none)")
# #         for edge in edges:
# #             table.add_row(edge.left, edge.right, hex(edge.shared_factor))
# #         self.console.print(table)

# #     def render_attack_timings(self, results: Dict[str, List[AttackResult]]) -> None:
# #         table = Table(title="Time-to-Break vs Key Structure", show_lines=True)
# #         table.add_column("Key")
# #         table.add_column("Attack")
# #         table.add_column("Success")
# #         table.add_column("Duration (ms)")
# #         table.add_column("Notes")
# #         for label, attacks in results.items():
# #             for attack in attacks:
# #                 table.add_row(
# #                     label,
# #                     attack.name,
# #                     "✅" if attack.success else "❌",
# #                     f"{attack.duration_ms:.2f}",
# #                     attack.notes,
# #                 )
# #         self.console.print(table)

# #     def render_conclusion(self) -> None:
# #         self.console.print("\n[bold magenta]Conclusion[/bold magenta]")
# #         self.console.print("• 2048-bit RSA ≠ secure by itself — entropy and key hygiene matter.")
# #         self.console.print("• Real security depends on randomness quality, not just modulus size.")
# #         self.console.print("• RSA is a protocol of assumptions; break any assumption and it falls.")


# # def continued_fraction_convergents(numerator: int, denominator: int) -> Iterable[Tuple[int, int]]:
# #     coeffs = []
# #     while denominator:
# #         q = numerator // denominator
# #         coeffs.append(q)
# #         numerator, denominator = denominator, numerator - q * denominator
# #     for idx in range(len(coeffs)):
# #         num, den = 1, 0
# #         for a in reversed(coeffs[: idx + 1]):
# #             num, den = den + num * a, num
# #         yield num, den


# # class RSAAttackLab:
# #     def __init__(self, bits: int = 128) -> None:
# #         self.console = Console()
# #         self.generator = KeyGenerator(bits=bits, seed_time=True)
# #         self.attacker = AttackEngine()
# #         self.visualization = Visualization(self.console)

# #     def run(self) -> None:
# #         self.console.print("[bold cyan]RSA Is Secure — Until It Isn’t (Attack Lab)[/bold cyan]")
# #         keys = self._build_key_material()
# #         results = self._run_attacks(keys)
# #         edges = self.attacker.gcd_batch_attack([(key.label, key.n) for key in keys])
# #         self.visualization.render_relationships(edges)
# #         self.visualization.render_attack_timings(results)
# #         self.visualization.render_conclusion()

# #     def _build_key_material(self) -> List[RSAKeyPair]:
# #         close_key = self.generator.generate_weak_keypair("close-primes")
# #         biased_key = self.generator.generate_weak_keypair("biased-rng")
# #         small_d_key = self.generator.generate_small_d_keypair("small-d")
# #         shared_keys = self.generator.generate_shared_factor_keys("shared", count=3)
# #         return [close_key, biased_key, small_d_key, *shared_keys]

# #     def _run_attacks(self, keys: List[RSAKeyPair]) -> Dict[str, List[AttackResult]]:
# #         results: Dict[str, List[AttackResult]] = {}
# #         for key in keys:
# #             attacks = []
# #             attacks.append(self._timed_attack("Fermat", self.attacker.fermat_attack, key.n, "close primes"))
# #             attacks.append(self._timed_attack("Pollard Rho", self.attacker.pollards_rho, key.n, "generic"))
# #             attacks.append(self._timed_attack("Wiener", lambda n: self.attacker.wiener_attack(key.e, n), key.n, "small d"))
# #             results[key.label] = attacks
# #         return results

# #     def _timed_attack(self, name: str, attack_fn, n: int, notes: str) -> AttackResult:
# #         start = time.perf_counter()
# #         factors = attack_fn(n)
# #         duration_ms = (time.perf_counter() - start) * 1000
# #         success = factors is not None
# #         return AttackResult(name=name, success=success, factors=factors, duration_ms=duration_ms, notes=notes)


# # def run_rsa_attack_lab(bits: int = 128) -> None:
# #     lab = RSAAttackLab(bits=bits)
# #     lab.run()


















#-----------------------------------------  writing my own Rsa 
#import random 

# p = random.randint(1,100)
# print(p)
# q = random.randint(1,100)
# print(q)
# multiply = p*q
# phy = p-1 * q-1
# e = random.randint(1 , phy)


# import random
# from math import gcd
# import base64
# # generating a Random p and q 
# p = random.randint(2, 100)
# q = random.randint(2, 100)

# print("p =", p)
# print("q =", q)
# # making n
# n = p * q
# # computing the euler formula 
# phi = (p - 1) * (q - 1)



# # choosing a e that is in compliance with the @ big Rules , e must be coprime with n and phi 
# def make_e(phi , n):
#     while True:
#         e = random.randint(2, phi -1 )
#         if gcd(e , phi) == 1 and gcd(e,n)==1 :
#             return e

# e  = make_e(phi , n)
# # if gcd(phi, e) == 1 and gcd(n , e) == 1 :
# #     print("True E")
# # else:
# #     print("False E")
# print("n =", n)
# print("phi =", phi)

# # this is our public key 
# public_K = (e, n)

# print(f" this is the private Key {public_K}")


# # making a list of d canidates and limiting this to 1 till phi

# d_candidates = list(range(1, phi))
# # satisfying the Formula : d * e Mod phi(n ) == 1  
# for d in d_candidates:
#     if (e * d) % phi == 1:
#         print("d =", d)
#         private_key = (d, n)
#         break
# print(f" this is the private Key {private_key}")


# #------------------------ Tried to make A REAL Rsa key PMe but found out there is levels to this shit : it had rules . its called ASN.1 DER will make that later
# # private_key_string = f"{p}{q}{d}{n}"
# # print(private_key_string)
# # private_key_string_bytes = private_key_string.encode("ascii")
# # private_key_base64_bytes  = base64.encode(private_key_string_bytes)
# # private_key_base64_string = private_key_base64_bytes.decode("ascii")
# # # can we drive a public key from the private key ? 

# #-------------------------------------------------- lets make this better !










# for now i will focus on the Attacking rsa , it is said by computerphile that if you have public key which is just (e , n) you cant use n to find out p and q therfore you cant find the d and you cant use the euler formula 
# but when p and q are small you factor the n and find the p and q ۱ . if the  two numbers are close to each other we can attack it .


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
            
        
        
        
    
    
    
    def LowExponent_Attack():
        
        return True
    
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
        
        
