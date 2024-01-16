class Function:
    def __init__(self, name:str, global_order:int, params:list=[], short_description:str=None) -> None:
        self.name = name
        self.global_order = global_order
        self.params = params
        self.short_description = short_description