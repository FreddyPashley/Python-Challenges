import subprocess
import os

def sterilise(x:str) -> list:
    """
    Modify the input to make it easier to parse later
    """

    operators = ["+", "-", "*", "//", "/", "==", "="]
    lines = x.split("\n")

    # Remove blank lines at start/end of code
    for i in [0, -1]:
        while lines[i] == "":
            lines.pop(i)

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


def check(code:str, functions:list=[], calls:list=[], variables:list=[], expected_output=None) -> bool:
    """
    The main bit (technical term)
    """

    code_lines = sterilise(code)

    # Run python to catch normal errors
    code_str = "\n".join(code_lines)
    with open("code_to_run.txt","w") as f:
        f.write(code_str)
    p = subprocess.Popen("py code_to_run.txt", shell=True, stdin=subprocess.PIPE, stderr=subprocess.STDOUT, stdout=subprocess.PIPE, close_fds=True)
    out, err = p.communicate()
    out = bytes.decode(out).strip()
    os.remove("code_to_run.txt")
    if err:
        return str(err)
    if expected_output and out != expected_output:
        if "Error" in out:
            before, after = out.replace(out.split(":")[-1], ""), out.split(":")[-1]
            before = before.split()[-1]
            return " ".join([before, after])

    # Get idea of expected order from prereq
    look_for = {}
    for iter in [functions, calls, variables]:
        for obj in iter:
            obj_type = str(type(obj)).replace("<class ","").replace(">","").replace("'","").split(".")[1].lower()
            """
            ## This code is now irrelevant as order is modified in runtime ##

            if str(obj.global_order) in look_for:
                msg = f"Global order for {obj.name} {obj_type} ({obj.global_order}) appears multiple times"
                raise Exception(msg)
            else:
            """
            look_for[str(len(look_for.keys()))] = obj
            if obj_type == "function" and obj.expected_return is not None:
                look_for[str(len(look_for.keys()))] = f"return {obj.expected_return}"

    # Logic errors for task
    actual = {}
    for i, line in enumerate(code_lines):
        if "def " in line:
            # check against short desc for preset functions (e.g. add two args, bubble sort, etc)
            function_call = line.replace("def ","").replace(":","")
            function_call = function_call.replace(")","")
            function_name = function_call.split("(")[0]
            params = [p.strip() for p in function_call.replace(function_name+"(","").strip(")").split(",")]
            actual[str(len(actual.keys()))] = f"function {function_name} {' '.join(params)}"
        if "=" in line and "==" not in line:
            lhs, rhs = line.split("=")
            actual[str(len(actual.keys()))] = f"assignment {lhs} {rhs}"
        if "return " in line:
            to_return = line.split("return")[1].strip()
            actual[str(len(actual.keys()))] = f"return {to_return}"
        if "(" in line and "def " not in line and "=" not in line:
            lhs, rhs = line.split("(")
            rhs = rhs.strip(")")
            actual[str(len(actual.keys()))] = f"call {lhs} {rhs}"

    # Compare programs
    too_much_code = False
    if len(actual) != len(look_for):
        if len(actual) > len(look_for):
            too_much_code = True
        else:
            return "It looks like you haven't finished the task"
        """
        ## Code not required anymore due to being more specific ##

        msg = "Internal error - lengths do not match"
        raise Exception(msg)
        """
    match = True
    for i in range(len(actual.keys())):
        a, l = actual[str(i)], look_for[str(i)]
        l_type = "" if type(l) == str else str(type(l)).replace("<class ","").replace(">","").replace("'","").split(".")[1].lower()
        if l_type == "" and l.startswith("return") and a != l:
            match = "Return statement incorrect"
            break
        else:
            a_type = a.split()[0]
            if a_type == l_type:
                if a_type == "function":
                    a_name, a_params = a.split()[1], a.split()[2:]
                    if a_name != l.name:
                        match = "Function name invalid"
                        break
                    elif a_params != [p.name for p in l.params]:
                        match = "Function arguments invalid"
                elif a_type == "call":
                    if a.split()[1] != l.name:
                        match = "Function call invalid"
                        break
                elif a_type == "variable":
                    pass # need to test with case
            else:
                if a_type == "assignment" and l_type == "call":
                    if l.assignment and l.name:
                        if a.split()[1] != l.assignment or a.split()[2].split("(")[0] != l.name:
                            match = "Assignment invalid"
                            break
                        if a.split()[2].split("(")[0] in [f.name for f in functions]:
                            params = [x.strip() for x in " ".join(a.split()[2:]).split("(")[1].strip(")").split(",")]
                            for fi in range(len(functions)):
                                if functions[fi].name == a.split()[2].split("(")[0]:
                                    break
                            function_ = functions[fi]
                            function_params = function_.params
                            if len(function_params) > len(params):
                                match = "Not enough function arguments"
                                break
                            elif len(function_params) < len(params):
                                match = "Too many function arguments"
                                break
                            for call in calls:
                                if call.name == functions[fi].name:
                                    break
                            expected_args = [x.strip() for x in call.content.split(",")]
                            if params != expected_args:
                                return "Function arguments invalid"
                            a_param_types = ["list" if "[" in x else ("dict" if "{" in x else "int") for x in params]
                            l_param_types = [str(p.type).replace("<class ","").replace(">","").replace("'","") for p in function_params]
                            if l_param_types != [str(x) for x in a_param_types]:
                                match = "Some function arguments are of invalid data types"
                                break
                    else:
                        match = f"Name ({l.name}) not found"
                        break
    
    return match, too_much_code