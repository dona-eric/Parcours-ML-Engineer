"""
Tri fusion (Merge Sort) en Python
Le tri fusion est un algorithme de tri basé sur la technique de "diviser pour régner".
Il divise la liste en deux moitiés, trie chaque moitié de manière récursive, 
puis fusionne les deux moitiés triées pour obtenir une liste triée complète. 
Cet algorithme est efficace pour les grandes listes et a une complexité temporelle de O(n log n) dans le pire des cas.
"""

def merge_sort(my_list):
    # verifions si la longueur de la liste est inférieure ou égale à 1
    if len(my_list) <= 1:
        return my_list
    elif len(my_list)>1:
        # divisons la liste en deux moitiés
        mid_list = len(my_list) // 2
        left_list = my_list[:mid_list]
        right_list = my_list[mid_list:]
    # recursivité sur les deux moitiés
        merge_sort(left_list)
        merge_sort(right_list)
    i=j=k=0

    while i <len(left_list) and j< len(right_list):
        if left_list[i] < right_list[j]:
            my_list[k] = left_list[i]
            i += 1
        else:
            my_list[k] = right_list[j]
            j += 1
        k += 1

    while i < len(left_list):
        my_list[k] = left_list[i]
        i += 1
        k += 1
    while j < len(right_list):
        my_list[k] = right_list[j]
        j += 1
        k += 1


my_list = []
for i in range(10000, 0, -1):
    my_list.append(i)
merge_sort(my_list)
print(my_list)