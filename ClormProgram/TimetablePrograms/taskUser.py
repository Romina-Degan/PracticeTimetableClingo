import json

with open(r"C:\Users\romin\DISS\PracticeTimetableClingo\instances\Task.json") as taskFile:
    taskDetails=json.load(taskFile)

with open(r"C:\Users\romin\DISS\PracticeTimetableClingo\instances\CBW.json") as userFile:
    userDetails=json.load(userFile)

from clorm import monkey
monkey.patch()

from clingo import Control
from clorm import ConstantStr, FactBase,StringField,IntegerField, Predicate, ph1_

ASP_PROGRAM =r"C:\Users\romin\DISS\PracticeTimetableClingo\ClormProgram\TimetablePrograms\taskUser.lp"

class DateValue(Predicate):
    date:ConstantStr
class User(Predicate):
    name:ConstantStr
    minAvailableTime:int
    maxAvailableTime:int

class Task(Predicate):
    name:ConstantStr
    duration:int

class Assignment(Predicate):
    date:DateValue
    user:User
    time:int 



def main():
    timeValues=[600,700,800,900,1000,1100,1200,1300,1400,1500,1600,1700,1800,1900,2000]
    instances=FactBase()
    # durations=[task['duration'] for task in taskDetails['TaskDescriptions']]
    # taskNames=[task['name'] for task in taskDetails['TaskDescriptions']]

    ctrl=Control(unifier=[User,Task,Assignment])
    ctrl.load(ASP_PROGRAM)

    for userValues in userDetails['userSpecifications']:
        predicateUser=User(name=userValues['name'],minAvailableTime=userValues['availableMin'], maxAvailableTime=userValues['avaliableMax'])
        instances.add(predicateUser)
        assert predicateUser in instances
    
    for taskValues in taskDetails['TaskDescriptions']:
        predicateTask=[Task(name=taskValues['name'], duration=taskValues['duration'])]
        instances.add(predicateTask)
       

    ctrl.add_facts(instances)
    ctrl.ground([("base", [])])
    solution=None
    
    def on_model(model):
        nonlocal solution
        solution=model.facts(atoms=True)
    
    ctrl.solve(on_model=on_model)
    if not solution:
        raise ValueError("YOU IDIOT >:(")
    query=solution.query(Assignment).where(Assignment.user==ph1_).order_by(Assignment.time)
    
    

if __name__=="__main__":
    main()