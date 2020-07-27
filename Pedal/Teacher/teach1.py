from pedal.toolkit.utilities import *
from pedal.toolkit.printing import *
from pedal.environments import setup_pedal
from pedal.source.source import *

ast, student, resolve = setup_pedal()

if "$" in get_program():
    explain("You should not use the dollar sign ($) anywhere in your code!", priority='verifier')

ast = parse_program()
print(ast)

# 함수 호출 여부 확인
if function_is_called('add_prices'):
    print("1111")
    prints = ensure_prints(1)
    if prints:
        gently("참인 경우 수행")
    else:
        gently("거짓인 경우 수행 ")
resolve()