from pedal.toolkit.printing import *
from pedal.toolkit.utilities import *
from pedal.environments import setup_pedal

ast, student, resolve = setup_pedal()

if "$" in student.get_program():
    explain("You should not use the dollar sign ($) anywhere in your code!", priority='verifier')

ast = parse_program()
if function_is_called('round'):
    prints = ensure_prints(1)
    if prints:
        nums = ast.find_all('Num')
        if nums and nums[0].n == 9.50:
            if len(nums) > 1:
                gently("You should only have one literal number in your code.")
            elif ast.find_all("Str"):
                gently("You should have no literal strings in your code.")
            elif len(student.get_output()) == 1:
                if student.get_output()[0] in ("10", "10.0"):
                    student.set_success()
                else:
                    gently("Incorrect output")
            else:
                gently("You should only be printing one thing.")
        else:
            gently("You need to make sure you have 9.50 in your code")
else:
    gently("Make sure you are using the <code>round</code> function!")