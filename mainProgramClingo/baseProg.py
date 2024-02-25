from clingo.symbol import Function
from clingo.control import Control
from clingo.backend import Backend
from clorm import monkey

class Observer:
    def rule(self, choice, head, body):
        print("rule:", choice, head,body)
    

ctl=Control()
ctl.register_observer(Observer())

sym_a=Function("a")
with ctl.backend() as backend:
    atm_a=backend.add_atom(sym_a)
    backend.add_rule([atm_a])

ctl.symbolic_atoms[sym_a].is_fact
print(ctl.solve(on_model=print))