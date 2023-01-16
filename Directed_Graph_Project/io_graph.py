import networkx as nx
from enums import RecordFormat

class IoGraph:
    """
    Developer: Magno Leite
    Date: 16/01/2023
    Description: Class responsible for performing any activity related to io, storage, retrieve data
    Dependencies: networkx and enums
    Notes: Logging not implemented in this class yet
    """
    #def __init__(self, di_graph, nx, file_format, full_file_name):
    def __init__(self):
        pass
        """
        self.file_format
        self.di_graph = di_graph
        self.nx = nx
        self.file_name = file_name
        print(nx)
        """
    @classmethod
    def serialize(cls, di_graph, nx, file_format, full_file_name):
        """
        Serialize graph to file
        """        
        if file_format==RecordFormat.GRAPHML.value:
            nx.write_graphml(di_graph, full_file_name)
        else:
            nx.write_gml(di_graph, full_file_name)
        print("Serializing graph to file ", full_file_name)    

    @classmethod
    def deserialize(cls, nx, file_format, full_file_name):
        """
        Load/Deserialize graph from file
        """           
        if file_format==RecordFormat.GRAPHML.value:
            di_graph = nx.read_graphml(full_file_name)
        else:
            di_graph = nx.read_gml(full_file_name) 
        print("Loading/Deserializing graph from existing file ", full_file_name)    
        nx.draw(di_graph, with_labels=True)

        return di_graph