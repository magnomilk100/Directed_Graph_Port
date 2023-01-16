# Directed_Graph_Port
This project contains classes in order to generate in Python a directed graph.

The main class of the project is DirectedGrapy in directed_graph.py file.
It has a constructor which receives a dictionary.

The graph can be created by 2 different entries:
1. based on a dictionary passed to the constructor of the class DirectedGraph, passing both List, nodes and edges.
2. based on a dictionary passed to teh constructor of the class DirectedGraph, passing an existing file.

To execute the python script/class from the root directory (<Git Files Local Path>/Directed_Graph_Port/Directed_Graph_Project) run: 
- Option 1. py main.py
- Option 2: python -m unittest test_main.p

The code will generate the graph when variable serialize = True
The code will plot/show the graph in a popup windows when show_graph variable = True
The code will show documentation of the class when show_documentation variable = True

The class DirectedGraph will generate:
1. A file called directed_graphy_1.graphml with the graph. File name can be changed based on file_name variable.
2. Log file will be always generated, there is no rolling policy
   Log file name = directed_graph_1.log
   
Below you can find the dictionary used to pass to the constructor of the class DirectedGraph:
**Dictionary to initializer the constructor of DirectedGraph class**
"""
dictionary_initializer = {
    "load_graph_from_file": load_graph_from_file,
    "file_name":            file_name, 
    "file_format":          file_format,
    "nodes":                nodes,
    "edges":                edges
}
"""

These are the variables used in the dictionary just mentioned:
**True to Generate graph from file, False = Generate graph from Lists (dictionary "dictionary_initializer" below)**
load_graph_from_file    = False
**Serialize graph to disk**
serialize               = True 
**True to Plot graph**
show_graph              = True 
**True Show report**
reporting               = True
**True to show documentation**
show_documentation      = True
