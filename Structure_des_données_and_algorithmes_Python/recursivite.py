"""
La récursivité est une technique de programmation où une fonction 
s'appelle elle-même pour résoudre un problème.

"""

## exemple de fonction récursive pour calculer la factorielle d'un nombre
n = int(input("Entrer un nombre:"))
def factorielle(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return factorielle(n-1)*factorielle(n-2)
    

for i in range(0, n):
    print(f"le calcul factoriel de n donne {factorielle(i)}")


## suite de fibonnacci avec recursivité
#fib(n) = fib(n-1)+fib(n-2)+fib(n-3)+.....

def fibonacci(n):
    if n<=1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)
    
for i in range(0, n):
    print(f"La suite de fibonnacci par recursivite donne: {fibonacci(i)}")



def hanoi(num_disks, from_rod, to_rod, aux_rod):
  # Correct the base case
  if num_disks >= 1:
    # Correct the calls to the hanoi function
    hanoi(num_disks-1, from_rod, aux_rod, to_rod)
    print("Moving disk", num_disks, "from rod", from_rod,"to rod",to_rod)
    hanoi(num_disks-1, aux_rod, to_rod, from_rod)   
'''  '''
num_disks = 4
source_rod = 'A'
auxiliar_rod = 'B'
target_rod = 'C'

hanoi(num_disks, source_rod, target_rod, auxiliar_rod)