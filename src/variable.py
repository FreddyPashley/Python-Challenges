class Variable:
    def __init__(self, name:str, py_type, global_order:int=None) -> None:
        self.name = name
        self.type = type
        self.global_order = global_order