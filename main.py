from casos.c100x500 import data, Vertex_Edges

import numpy as np
import pandas as pd

adj_matrix = np.zeros((Vertex_Edges[1],Vertex_Edges[1]), dtype = int)
for row in data:
    adj_matrix[row[0]-1][row[1]-1] = row[2]
    adj_matrix[row[1]-1][row[0]-1] = row[2]



