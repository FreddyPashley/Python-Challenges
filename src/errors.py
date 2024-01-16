class PythonError:
    def __init__(self, line_num:int, description:str) -> None:
        self.line_num = line_num
        self.description = description

class LogicError:
    def __init__(self, line_num:int, description:str) -> None:
        self.line_num = line_num
        self.description = description