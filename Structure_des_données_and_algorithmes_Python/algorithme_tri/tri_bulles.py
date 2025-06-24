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
"""