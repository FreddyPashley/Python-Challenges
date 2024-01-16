from call import *
from function import *
from parameter import *
from variable import *

bubbleSort = {
    "initial_code": [
        "myList = [6, 1, 7, 2, 8, 3, 9, 10, 4, 5]"
    ],
    "expected_output": "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]",
    "functions": [
        Function(
            name="bubbleSort",
            params=[Parameter("myList", list)],
            expected_return="myList",
            global_order=0,
            short_description="bubbleSort"
        )
    ],
    "calls": [
        Call(
            "bubbleSort",
            content="myList",
            assignment="sortedList",
            global_order=1
        ),
        Call(
            name="print",
            content="sortedList",
            global_order=2
        )
    ]
}

addTwoNums = {
    "expected_output" : "5",
    "functions": [
        Function(
            name="addTwo",
            params=[Parameter("x", int), Parameter("y", int)],
            expected_return="x+y",
            global_order=0
        )
    ],
    "calls": [
        Call(
            name="addTwo",
            content="2, 3",
            assignment="result",
            global_order=1
        ),
        Call(
            name="print",
            content="result",
            global_order=2
        )
    ]
}