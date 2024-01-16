class Function:
    def __init__(self, name:str, global_order:int, params:list=[], expected_return:str=None, short_description:str=None) -> None:
        self.name = name
        self.global_order = global_order
        self.params = params
        self.expected_return = expected_return
        self.short_description = short_description