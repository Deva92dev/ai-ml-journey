class Vector:
    def __init__(self, components):
        if len(components) == 0:
            raise ValueError("List can not have 0 elements")
        
        self.components = components

    def __repr__(self):
        return f"({self.components})"
    
    def __len__(self, components):
        return len(components)


class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
