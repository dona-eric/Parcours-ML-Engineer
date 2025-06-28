"""
Hachages à tables en Python
- En Python, les hachages sont implémentés à l'aide de dictionnaires (dict).
- Un dictionnaire est une structure de données qui stocke des paires clé-valeur
- Les clés sont uniques et sont utilisées pour accéder aux valeurs associées.
- Les dictionnaires sont optimisés pour des opérations de recherche, d'insertion et de suppression
  en temps constant en moyenne, ce qui les rend très efficaces pour de nombreuses applications.
- Les dictionnaires en Python utilisent une fonction de hachage pour convertir les clés en indices
  dans une table de hachage, ce qui permet un accès rapide aux valeurs associées
- Les dictionnaires peuvent contenir des types de données variés comme clés et valeurs, y compris
  des chaînes de caractères, des nombres, des tuples, et même d'autres dictionnaires
- Les dictionnaires sont dynamiques, ce qui signifie qu'ils peuvent croître et rétrécir
  automatiquement en fonction des besoins, sans nécessiter de redimensionnement manuel.
- Les dictionnaires en Python sont implémentés en utilisant des tables de hachage,
  ce qui permet une gestion efficace de la mémoire et des performances optimales pour les opérations courantes
  telles que l'insertion, la suppression et la recherche d'éléments.    
"""

my_menu = {

  'lasagna': 14.75,

  'moussaka': 21.15,

  'sushi': 16.05,

  'paella': 21,

  'samosas': 14

}

for keys, values in my_menu.items():
    print(f"{keys} : {values} €")


my_menu = {

  'sushi' : {

    'price' : 19.25,

    'best_served' : 'cold'

  },

  'paella' : {

    'price' : 15,

    'best_served' : 'hot'

  },

  'samosa' : {

    'price' : 14,

    'best_served' : 'hot'

  },

  'gazpacho' : {

    'price' : 8,

    'best_served' : 'cold'

  }

}

for dish, values in my_menu.items():
  # Print whether the dish must be served cold or hot
  print(f"{dish.title()} is best served {values['best_served']}.")