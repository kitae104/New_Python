# 표준 환경
from pedal.environments import setup_pedal

student_code = "print('Hello world!')"

ast, student, resolve = setup_pedal(student_code)


# ... More instructor logic can go here ...

resolve()