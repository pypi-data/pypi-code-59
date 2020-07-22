# -*- coding: utf-8 -*-

class Graph:
    def __init__(self,
                 vertices=None,
                 matrix=None,
                 edges=None,
                 directed=False):
        """
        Initialisation d'un graphe

        INPUT :

            - vertices, un itérables sur les sommets du graphes
            - matrix, la matrice d'adjacence du graphe suivant les mêmes indices que `vertices`
            - edges, une liste de triplets (v1, v2, c) où v1 et v2 sont des sommets et c un nombre positif

        """
        if vertices is None:
            vertices = []

        self._vertices = vertices
        # création d'un dictionnaire associant son indice à chaque sommet
        # (vous pouvez modifier si ça n'est pas utile à votre implantation)
        self._vertex_indices = {vertices[i]: i for i in range(len(vertices))}
        self._directed = directed

        # on ne peut pas donner à la fois matrix et edges
        if matrix is not None and edges is not None:
            raise ValueError("'matrix' et 'edges' ne peuvent pas être tous les deux initialisés")

        # initialisation différenciée: implantez les méthodes en question
        if matrix is not None:
            self._init_from_matrix(matrix)
        elif edges is not None:
            self._init_from_edges(edges)
        else:
            self._init_empty()

    def _init_empty(self):
        """
        Initialisation d'un graphe vide (sans arêtes)
        """
        # Remplacer la ligne suivante par le code adéquat
        raise NotImplementedError("code non implanté ligne 46");


    def _init_from_matrix(self, matrix):
        """
        Initialisation à partir d'une matrice

        EXAMPLES:

            >>> M = matrix = [[0, 12,  0, 12],
            ...               [0,  0, 23, 0],
            ...               [0,  0,  0, 0],
            ...               [0,  0,  0, 0]]
            >>> G = Graph(vertices = ["A", "B", "C", "D"],
            ...           matrix = M,
            ...           directed = True)
            >>> G.edges()
            (('A', 'B', 12), ('A', 'D', 12), ('B', 'C', 23))
            >>> G.matrix() == M
            True
        """
        # Remplacer la ligne suivante par le code adéquat
        raise NotImplementedError("code non implanté ligne 68");

    def _init_from_edges(self, edges):
        """
        Initialisation à partir d'une liste de triplets
        """
        # Remplacer la ligne suivante par le code adéquat
        raise NotImplementedError("code non implanté ligne 75");

    def is_directed(self):
        """
        Renvoie si le graph est orienté
        """
        return self._directed

    def set_edge_capacity(self, v1, v2, c):
        """
        Donne la capacité `c` à l'arête `(v1,v2)`

        INPUT:

            - v1, un sommet du graphe
            - v2, un sommet du graphe
            - c la capacité de l'arête (v1,v2)
        """
        # à compléter

    def add_vertex(self, v):
        """
        Ajoute le sommet `v` au graphe

        INPUT:

            - v, un sommet du graphe

        """
        # à compléter

    def vertices(self):
        """
        Renvoie la liste des sommets du graphe

        EXAMPLES::

            >>> from graph import examples
            >>> G = examples.cours_1_reseau()
            >>> G.vertices()
            ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        """
        # Remplacer la ligne suivante par le code adéquat
        raise NotImplementedError("code non implanté ligne 118");

    def vertex_number(self):
        """
        Renvoie le nombre de sommets du graphe

        EXAMPLES::

            >>> G = examples.cours_1_reseau()
            >>> G.vertex_number()
            8
        """
        # Remplacer la ligne suivante par le code adéquat
        raise NotImplementedError("code non implanté ligne 131");

    def has_vertex(self, v1):
        """
        Renvoie vrai si v1 est un sommet du graphe

        INPUT:

            - v1, un sommet
        """
        # à compléter

    def edges(self):
        """
        Renvoie un tuple de triplets `(v1,v2,c)` correspondant aux arêtes du graphe avec leur capacité.

        EXAMPLES:

            >>> G = Graph((1,2,3,4))
            >>> G. edges()
            ()
            >>> G = examples.directed()
            >>> sorted(G.edges())
            [(1, 2, 12), (1, 4, 12), (2, 3, 23)]

            >>> G = examples.undirected()
            >>> sorted(G.edges())
            [(1, 2, 12), (2, 1, 12), (2, 3, 23), (3, 2, 23)]
        """
        # Remplacer la ligne suivante par le code adéquat
        raise NotImplementedError("code non implanté ligne 161");

    def edge_number(self):
        """
        Renvoie le nombre d'arêtes du graphe
        """
        # Remplacer la ligne suivante par le code adéquat
        raise NotImplementedError("code non implanté ligne 168");


    def is_edge(self, v1, v2):
        """
        Renvoie si l'arête (v1,v2) existe

        INPUT:

            - v1, un sommet du graphe
            - v2, un sommet du graphe
        """
        return v2 in self.neighbors_out(v1)

    def capacity(self, v1, v2):
        """
        Renvoie la capacité de l'arête (v1,v2) (si l'arête n'existe pas, la capacité est 0)

        INPUT:

            - v1, un sommet du graphe
            - v2, un sommet du graphe

        EXAMPLES::

            >>> G = examples.directed()
            >>> G.capacity(1,2)
            12
            >>> G.capacity(2,1)
            0
            >>> G.capacity(2,3)
            23
            >>> G.capacity(3,2)
            0
        """
        # Remplacer la ligne suivante par le code adéquat
        raise NotImplementedError("code non implanté ligne 204");


    def matrix(self):
        """
        Retourne la matrice associée au graphe

        Soit `n` le nombre de sommets du graphe. Cette méthode renvoie
        une liste `M` de n listes de taille n, de sorte que `M[i][j]`
        est la capacité de l'arête reliant le i-ème sommet au j-ème
        sommet dans le graphe, s'il y en a une, et 0 sinon.

        EXAMPLES::

            >>> G = examples.directed()
            >>> G.matrix()              # doctest: +NORMALIZE_WHITESPACE
            [[0, 12, 0, 12],
             [0, 0, 23, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0]]
        """
        return [[ self.capacity(v1,v2)
                  for v2 in self.vertices() ]
                for v1 in self.vertices() ]

    def to_dict(self):
        """
        Retourne le dictionnaire associé au graphe
        """
        # à compléter

    def neighbors_in(self, v):
        """
        Renvoie la liste des voisins entrants de `v`

        INPUT:

            - v, un sommet du graphe

        EXAMPLES::

            >>> G = examples.cours_1_reseau()
            >>> sorted(G.neighbors_in("H"))
            ['C', 'D', 'E', 'G']
            >>> G = examples.directed()
            >>> G.neighbors_in(1)
            ()
            >>> G.neighbors_in(2)
            (1,)
        """
        # Remplacer la ligne suivante par le code adéquat
        raise NotImplementedError("code non implanté ligne 255");

    def neighbors_out(self, v):
        """
        Renvoie la liste des voisins sortants de `v`

        INPUT:

            - v, un sommet du graphe

        EXAMPLES::

            >>> G = examples.cours_1_reseau()
            >>> sorted(G.neighbors_out("A"))
            ['B', 'F', 'G']
            >>> G = examples.directed()
            >>> sorted(G.neighbors_out(1))
            [2, 4]
            >>> G.neighbors_out(2)
            (3,)
            >>> G.neighbors_out(4)
            ()
        """
        # Remplacer la ligne suivante par le code adéquat
        raise NotImplementedError("code non implanté ligne 279");

    def is_path(self, p):
        """
        Renvoie si `p` est un chemin valide dans le graphe

        INPUT:

            - p, une liste de sommets du graphe

        EXAMPLES::

            >>> G = examples.cours_1_reseau()
            >>> G.is_path([])
            True
            >>> G.is_path(["D"])
            True
            >>> G.is_path(["D", "G"])
            False
            >>> G.is_path(["D", "H"])
            True
            >>> G.is_path(["D", "H", "F"])
            False
            >>> G.is_path(["D", "H", "G", "B", "A"])
            True
        """
        # Remplacer la ligne suivante par le code adéquat
        raise NotImplementedError("code non implanté ligne 306");

    def networkx(self):
        import graph_networkx
        return graph_networkx.Graph(self.vertices(), self.edges(), directed=self.is_directed())

    def show(self):
        return self.networkx().show()

import graph_examples
examples = graph_examples.Examples(Graph)
