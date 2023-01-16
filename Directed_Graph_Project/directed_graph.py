import networkx as nx
import matplotlib.pyplot as plt
import inspect
import os
import logging
from enums import RecordFormat, DegreeType
from io_graph import IoGraph


class DirectedGraph:
    """
    Developer: Magno Leite
    Date: 16/01/2023
    Description: Class responsible for creating and ploting the Directed Graph
                 Graph can be created based on list or retrieving the graph from a graph file with graph data
    Dependencies: networkx, matplotlib, inspect, os, logging, enums, io_graph
    """    
    # Constructor receiving dictionary with either List of nodes/edges or fileName
    def __init__(self, args): 
        self.load_graph_from_file    = False if not args.get("load_graph_from_file") else args.get("load_graph_from_file"),
        self.file_name               = self.file_name if not args.get("file_name") else args.get("file_name")
        self.file_format             = self.file_format if not args.get("file_format") else args.get("file_format")
        self.full_file_name          = "{}.{}".format(self.file_name, self.file_format)
        # Check if nodes and edges are correct if not we can stop processing here and show how they are expected
        self.nodes                   = args.get("nodes")
        self.edges                   = args.get("edges")
        self.di_graph                = None

        self.logger = DirectedGraph._set_logger()
        self.logger.debug(str("File name: " + __name__ + " - Method: " + inspect.stack()[0][3] + " - Args: " + str(args)))
        
        if(not args.get("load_graph_from_file")):
            if (not self.nodes) or (not self.edges):
                raise Exception("Nodes and Edges list are mandatory when load_graph_from_file = False.")
            self.di_graph = nx.DiGraph()
            DirectedGraph._create_graph(self) 
        else:
            if not os.path.exists(self.full_file_name):
                self.logger.error(str("File name: " + __name__ + " - Method: " + inspect.stack()[0][3] + " - File " + full_file_name + " doesn't exist "))                
                raise Exception("File " + full_file_name + " doesn't exist.")
            DirectedGraph._deserialize(self)

    def _create_graph(self):
        di_graph = self.di_graph
        di_graph.add_nodes_from(self.nodes)
        di_graph.add_edges_from(self.edges)
        pos = nx.spring_layout(di_graph)
        nx.draw_networkx_nodes(di_graph, pos, node_size=500)
        nx.draw_networkx_edges(di_graph, pos, edgelist=di_graph.edges(), edge_color='black')
        nx.draw_networkx_labels(di_graph, pos)


    def show_graph(graph):
        """
        Plot the graph in a pop up window
        """          
        plt.show()

    def get_number_of_edges(self):
        """
        Get number of edges of the graph
        """          
        return self.di_graph.number_of_edges()

    def get_number_of_nodes(self):
        """
        Get number of nodes of the graph
        """        
        return self.di_graph.number_of_nodes()

    def get_in_node_degrees(self):
        """
        Get a dictionary with in degree for all nodes of the graph
        """ 
        dict_in={}
        for item in self.di_graph.nodes():
            dict_in[item]=self.get_node_degrees(item, DegreeType.IN.value)
        return dict_in

    def get_out_node_degrees(self):
        """
        Get a dictionary with out degree for all nodes of the graph
        """         
        dict_out={}
        for item in self.di_graph.nodes():
            dict_out[item]=self.get_node_degrees(item, DegreeType.OUT.value)
        return dict_out        

    def get_node_degrees(self, node_name=None, degreeType=DegreeType.OUT.value):
        """
        Get the number of in or out degree for a specific node of the graph
        default: for out degree
        """         
        if degreeType == DegreeType.IN.value:
            return self.di_graph.in_degree(node_name) 
        else:
            return self.di_graph.out_degree(node_name)

    def serialize(self):
        """
        Serialize graph to a file
        """ 
        self.logger.info(str("File name: " + __name__ + " - Method: " + inspect.stack()[0][3] + " - Serializing file to ./" + self.full_file_name))        
        IoGraph.serialize(self.di_graph, nx, self.file_format, self.full_file_name)
    
    def _deserialize(self):
        """
        Load graph from a file
        """         
        self.logger.info(str("File name: " + __name__ + " - Method: " + inspect.stack()[0][3] + " - Deserializing file from ./" + self.full_file_name))
        self.di_graph = IoGraph.deserialize(nx, self.file_format, self.full_file_name)

    def _set_file_format(self, file_format):
        self.file_format = file_format

    def _set_file_name(self, file_name):
        self.file_name = file_name
   
    def _set_logger():
        logger = logging.getLogger("direct_graph_logger")
        # set the logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        logger.setLevel(logging.DEBUG)
        # create a file handler
        file_handler = logging.FileHandler("directed_graph_1.log")
        # create a formatter
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        # add the formatter to the file handler
        file_handler.setFormatter(formatter)
        # add the file handler to the logger
        logger.addHandler(file_handler)  
        return logger
