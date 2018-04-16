import sys
import pandas as pd

order_data = pd.read_csv(sys.argv[1])
print(order_data.head())

def validate_state(state):
    invalid_states = ['CT','ID','IL','MA','NJ','OR','PA',]
    if  state in invalid_states:
        return False
    else: return True
