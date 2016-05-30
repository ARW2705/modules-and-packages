import os
import sys

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(CURRENT_DIR, 'a_weird_location'))

import a_weird_module
print(a_weird_module.WEIRD_VARIABLE)
