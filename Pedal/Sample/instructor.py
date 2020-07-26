from pedal.quick import *
code, student, resolve = setup_pedal()
print(student.report.feedback)

from pedal.source import verify
verify()

# Generic, friendly feedback on undeclared variables, among others
from pedal.tifa import tifa_analysis
tifa_analysis()

# Partial credit for good progress
from pedal.cait import parse_program
ast = parse_program()
print(ast)

# Give feedback by finding a common problem-specific mistake
from pedal.cait import find_matches
matches = find_matches("for _expr_ in _list_:\n ___ = ____ + _list_")

if matches:
    explain("list_inside_loop", "You shouldn't use the list inside the for loop123.")
else:
    explain("AAAA")

from pedal.sandbox import run
from pedal.assertions import assert_equal
student = run()
#assert_has_function(student, 'add_prices', list)
assert_equal(student.add_prices([1,2,3]), 10)

resolve()