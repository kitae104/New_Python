from pedal.toolkit.utilities import *
from pedal.toolkit.files import *
from pedal.core.commands import *
from pedal.environments import setup_pedal

ast, student, resolve = setup_pedal()
ast = parse_program()
suppress("analyzer", "Iterating over non-list")
suppress("analyzer", "Iterating over empty list")
resolve()