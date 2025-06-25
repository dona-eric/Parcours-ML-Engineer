"""
    Algorithmes de tri : Tri par sélection et Tri par insertion
    Le tri par sélection (Selection Sort) et le tri par insertion (Insertion Sort) sont deux algorithmes de tri simples mais efficaces pour des listes de petite taille.
    Le tri par sélection fonctionne en divisant la liste en deux parties : une partie triée et une partie non triée. À chaque itération, l'algorithme sélectionne le plus petit élément de la partie non triée et le place à la fin de la partie triée.
    Le tri par insertion, quant à lui, construit la liste triée en insérant chaque nouvel élément à sa position correcte dans la partie triée. Il fonctionne en parcourant la liste et en
    insérant chaque élément à sa place dans la partie déjà triée, en décalant les éléments plus grands vers la droite.
    Ces algorithmes ont une complexité temporelle de O(n^2) dans le pire des cas, ce qui les rend moins efficaces pour les grandes listes, mais ils sont simples à comprendre
    et à implémenter.
    Exemple d'utilisation :
"""

def selection_sort(my_list):
    length_list = len(my_list)
    for i in range(length_list -1):
        lowest = my_list[i]
        min_index = i

        for j in range(i+1, length_list):
            if my_list[j]<lowest:
                lowest = my_list[j]
                min_index = j

        my_list[i], my_list[min_index] = my_list[min_index], my_list[i]
    return my_list

my_list = [12, 2, 3, 8, 5, 6, 7, 1, 4, 9, 10, 11, 100]
print(selection_sort(my_list))