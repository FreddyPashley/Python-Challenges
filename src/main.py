from utils import *
from function import Function
from call import Call
from parameter import Parameter
from variable import Variable

test_input = """
def func1(x, y):
    return x + y

r = func1(2, 3)
print(r)"""

steralised = sterilise(test_input)

is_correct = check(
    steralised,
    functions=[
        Function(
            name="func1",
            params=[Parameter("x", int), Parameter("y", int)],
            short_description="add_args",
            global_order=0
        )
    ],
    calls=[
        Call(
            name="func1",
            content="2, 3",
            assignment="r",
            global_order=1
        ),
        Call(
            name="print",
            content="r",
            global_order=2
        )
    ]
    )
print(is_correct)