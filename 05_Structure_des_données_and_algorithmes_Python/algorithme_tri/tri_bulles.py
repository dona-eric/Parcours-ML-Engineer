"""
Algorithme de tri à bulles (Bubble Sort)
Le tri à bulles est un algorithme de tri simple qui fonctionne en répétant plusieurs
 passes sur la liste à trier, en comparant chaque paire d'éléments adjacents et en les échangeant
 si nécessaire. L'algorithme continue jusqu'à ce que la liste soit triée, c'est-à-dire qu'aucun échange n'est nécessaire
 lors d'une passe complète.

 L'algorithme a une complexité temporelle de O(n^2) dans le pire des cas, ce qui le rend inefficace pour les grandes listes.
 Exemple d'utilisation :
```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Flag to check if any swaps were made
        swapped = False
        for j in range(0, n-i-1):
            # Compare adjacent elements
            if arr[j] > arr[j+1]:
                # Swap if they are in the wrong order
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        # If no swaps were made, the array is sorted
        if not swapped:
            break
    return arr
```
Implémentation de l'algorithme de tri à bulles en Python.
"""

def bubbles_algo(my_list):
    # the length of liste
    length_liste = len(my_list)
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for i in range(length_liste - 1):
            # Compare adjacent elements
            if my_list[i] > my_list[i + 1]:
                # Swap if they are in the wrong order
                my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
                is_sorted = False

            length_liste -= 1
    return my_list

my_list=[12, 2,3, 8, 5, 6, 7, 1, 4, 9, 10, 11, 100]
print(bubbles_algo(my_list))