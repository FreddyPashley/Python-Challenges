from errors import PythonError, LogicError

def check(code_lines:list, functions:list=[], calls:list=[], variables:list=[], expected_output=None) -> bool:
    """
    """
    print(code_lines)

    # Run python to catch normal errors
    pass

    # Get idea of order from prereq
    look_for = {}
    for iter in [functions, calls, variables]:
        for obj in iter:
            obj_type = str(type(obj)).replace("<class ","").replace(">","").replace("'","").split(".")[1].lower()
            if str(obj.global_order) in look_for:
                msg = f"Global order for {obj.name} {obj_type} ({obj.global_order}) appears multiple times"
                raise Exception(msg)
            else:
                look_for[str(obj.global_order)] = obj

    # Logic errors for task
    actual = {}
    for i, line in enumerate(code_lines):
        if "def " in line:
            # check against short desc
            function_call = line.replace("def ","").strip(":")
            function_name = function_call.split("(")[0]
            params = [p.strip() for p in function_call.replace(function_name+"(","").strip(")").split(",")]
            actual[str(i)] = f"function {function_name} {' '.join(params)}"

    return actual

def sterilise(x:str) -> list:
    """
    """
    operators = ["+", "-", "*", "//", "/"]
    lines = x.split("\n")
    while lines[0] == "": lines.pop(0)
    while lines[-1] == "": lines.pop(-1)
    for i, line in enumerate(lines):
        if line == "": continue

        # Clear operator spacing
        for operator in operators:
            if operator in line:
                while f" {operator} " in line:
                    line = line.replace(f" {operator} ", operator)
                while f"{operator} " in line:
                    line = line.replace(f"{operator} ", operator)
                while f" {operator}" in line:
                    line = line.replace(f" {operator}", operator)        

        # Replace new line for any changes made
        lines[i] = line

    return lines