import unittest
import logging
from directed_graph import DirectedGraph
from enums import RecordFormat, DegreeType


def show_report1(directed_graph):
    print("\n*** DEGREES REPORT **** ")
    print("***** IN DEGREES ****** ")
    for key, value in directed_graph.get_in_node_degrees().items():
        print("Node " + key + " has " + str(value) + " IN degrees.")
    print("\n***** OUT DEGREES ***** ")
    for key, value in directed_graph.get_out_node_degrees().items():
        print("Node " + key + " has " + str(value) + " OUT degrees.")

def run_test_case_1_from_list():
        # True to Generate graph from file, False = Generate graph from Lists (dictionary "dictionary_initializer" below)
    load_graph_from_file    = False
    # Serialize graph to disk
    serialize               = True 
    # True to Plot graph
    show_graph              = False 
    # True Show report
    reporting               = True
    # True to show documentation
    show_documentation      = False
    # Switch Comment/Uncomment below for file_format to GML or GRAPML file format (persistency)
    # Record format, it impacts in the record/retrieve effiency (for types check: RecordFormat Enum)
    # file_format = RecordFormat.GML.value # Record format, impacts in the effiency (for types check: RecordFormat Enum)
    file_format             = RecordFormat.GRAPHML.value
    # just file name without file extension
    file_name               = "directed_graphy_1" 
    nodes                   = [ 'A', 'B', 'C' ]
    edges                   = [ ('A', 'B'), ('A', 'C'), ( 'B','C'), ('A', 'E') ]

    # Dictionary to initializer the constructor of DirectedGraph class
    dictionary_initializer = {
        "load_graph_from_file": load_graph_from_file,
        "file_name":            file_name, 
        "file_format":          file_format,
        "nodes":                nodes,
        "edges":                edges
    }

    directed_graph = DirectedGraph(dictionary_initializer)

    if reporting:
        show_report1(directed_graph)

    if show_graph:
        directed_graph.show_graph()

    if serialize:
        directed_graph.serialize()

    if show_documentation:
        help(DirectedGraph)
        #print(DirectedGraph.__doc__)        

class TestDirectedGraph(unittest.TestCase):
    
    def test_main1(self):
        with self.assertLogs(level=logging.INFO) as cml:
            print("Test case 1: From List")
            run_test_case_1_from_list()
        self.assertEqual(cml.output, ["INFO:direct_graph_logger:File name: directed_graph - Method: serialize - Serializing file to ./directed_graphy_1.graphml"])
    
if __name__ == '__main__':
    unittest.main()        







