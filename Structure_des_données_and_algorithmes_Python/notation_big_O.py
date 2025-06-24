"""
    la notation Big O est une notation mathématique utilisée pour 
    décrire la complexité algorithmique d'un algorithme. 
    Elle permet de mesurer le temps d'exécution ou l'espace mémoire requis par un algorithme en 
    fonction de la taille de l'entrée.
 """

## Exercise: noous allons implementer un algorithme qui imprime tous ls éléments d'une liste

colors = ['red', 'green', 'blue', 'yellow']

def print_colors(colors):
    for color in colors:
        print(color)

# La complexité temporelle de cette fonction est O(n),
# où n est le nombre d'éléments dans la liste colors.
# Cela signifie que le temps d'exécution de la fonction augmente linéairement avec la taille de la liste.
print_colors(colors)