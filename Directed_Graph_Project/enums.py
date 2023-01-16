from enum import Enum

class RecordFormat(Enum):
    """
    Developer: Magno Leite
    Date: 16/01/2023
    Description: File format
    Dependencies: Enum
    Values: GRAPHML and GML
    """
    GRAPHML  = "graphml"
    GML = "gml"

class DegreeType(Enum):
    """
    Developer: Magno Leite
    Date: 16/01/2023
    Description: Degree types
    Dependencies: Enum
    Value: IN and OUT
    """    
    IN  = 1
    OUT = 2