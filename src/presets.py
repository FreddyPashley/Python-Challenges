from call import *
from function import *
from parameter import *
from variable import *

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