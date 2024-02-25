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
    # minTime:int
    # maxTime:int

class Task(Predicate):
    name:ConstantStr
    # duration:int

class Assignment(Predicate):
    task:ConstantStr
    user:ConstantStr
    time:int 



def main():
   
    # durations=[task['duration'] for task in taskDetails['TaskDescriptions']]
    # taskNames=[task['name'] for task in taskDetails['TaskDescriptions']]

    ctrl=Control(unifier=[User,Task,Assignment])
    ctrl.load(ASP_PROGRAM)


    #So it does actually add to the factbase but it isnt in a way that is understandable for the parser
    #Users work when there is only one value within it?
    users=[User(name=userValues['name']) for userValues in userDetails['userSpecifications']]
    tasks=[Task(name=taskValues['taskName'])for taskValues in taskDetails['TaskDescriptions']]

    
    instances=FactBase(users+tasks)
  
       

    ctrl.add_facts(instances)
    ctrl.ground([("base", [])])
   

    solution=None
    
    def on_model(model):
        nonlocal solution
        solution=model.facts(unifier=[User,Task,Assignment], atoms=True,raise_on_empty=True)
    
    ctrl.solve(on_model=on_model)
    if not solution:
        raise ValueError("YOU IDIOT >:(")

    query = solution.query(Assignment).where(Assignment.user == ph1_).order_by(Assignment.time)
    for u in users:
        assignments = list(query.bind(u.name).all())
        if not assignments:
            print("THIS IS NOT WORKING..YIPEE".format(u.name))
        else:
            print("User {} assigned to: ".format(u.name))
            for a in assignments:
                print("\t chore {}".format(a.task))
    
    

if __name__=="__main__":
    main()