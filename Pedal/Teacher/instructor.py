from pedal.cait import find_matches
from pedal.environments import setup_pedal
student_code = "print('Hello world!')"
ast, student, resolve = setup_pedal(student_code)

# ... More instructor logic can go here ...
from pedal import gently, set_success, give_partial, compliment
gently("You failed to solve the question correctly!", "incorrect_answer")
set_success()
give_partial(45)
compliment("You've almost got it!")

matches = find_matches("answer = 5")
if matches:
    gently("The variable `answer` should not be assigned the value `5`.", "assigned_literal_value_to_answer")

if find_matches("answer = ___"):
    gently("You assigned something to the variable `answer`", "assigned_to_answer")


if 'sum' in student.data and student.data['sum'] == 47:
    set_success()

integer_variables = student.get_variables_by_type(int)
for name, value in integer_variables:
    if value == 47:
        gently("You should not have assigned the value 47 to the variable "+name)


if "Hello world!" not in student.output:
    gently("You need to print the string 'Hello world!'")

if "Complex\nText" in student.raw_output:
    gently("You should have the precise text we gave you in there.")

result = student.call("add_numbers", 5, 7)
if result == 13:
    set_success()

from pedal.assertions import *

assert_equal(student.call('add', 5, 7), 13)

assert_prints(student.call("print_values", [1,2,3]), ["1", "2", "3"])

from pedal.toolkit.functions import unit_test, output_test

if unit_test('add', [ (3, 4, 7), (5, 5, 10), (-3, -3, -6) ]):
    set_success()

from pedal.toolkit.functions import match_signature

if not match_signature('add', 2):
    gently("The `add` function should have 2 parameters.")

from pedal.toolkit.functions import all_documented

all_documented()

from pedal.toolkit.utilities import only_printing_variables

if not only_printing_variables():
    gently("You should only be printing variables' values, not literal values.")

from pedal.toolkit.utilities import prevent_operation

prevent_operation("/")
prevent_operation("*")

resolve()