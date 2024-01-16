class Call:
    def __init__(self, name:str, content:str, global_order:int, assignment:str=None) -> None:
        self.name = name
        self.content = content
        self.global_order = global_order
        self.assignment = assignment