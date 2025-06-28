"""
Les Graphes et les Arbres sont des structures de données fondamentales en informatique, 
utilisées pour modéliser des relations complexes entre les objets.

La différence entre les graphes et les arbres est :
    - Les arbres sont non cycles . C'est comme une arbre généalogique où le père et la mère sont à la tete de la génération et le reste sont des successeurs.Elle suivent
    généralement une relation dépendante plus ou moins linéaire Tandisque
    
    -Les graphes sont cycles qu'on peut parcourir dans n'import quel sens. Un exemple simple c'est le réseax social: 
    Jean -----> Pierre
     |            |
     |            |
    Jacob ------> Max

    Implémentons l'algorithme des arbres et des graphes
"""

"""
Trees
"""

class TreeNode:
    def __init__(self, data, left=None, rigth=None):
        self.data = data
        self.left_child = left
        self.rigth_child=rigth

node1 = TreeNode("B")
node2 = TreeNode("C")
tree_node = TreeNode("A", node1, node2)
print(tree_node)


"""
Graphs: 
"""

class Graphs:
    
    def __init__(self):