import json

with open(r"C:\Users\romin\DISS\PracticeTimetableClingo\instances\Task.json") as taskFile:
    taskDetails=json.load(taskFile)

with open(r"C:\Users\romin\DISS\PracticeTimetableClingo\instances\CBW.json") as userFile:
    userDetails=json.load(userFile)

from clorm import monkey
from typing import Tuple,List
monkey.patch()
from enum import Enum
import clingo
from datetime import datetime, timedelta
from clorm import ConstantStr,define_enum_field,FactBase,IntegerField,StringField,ContextBuilder, Predicate,ConstantField,field,refine_field, ph1_
cb=ContextBuilder
ASP_PROGRAM =r"C:\Users\romin\DISS\PracticeTimetableClingo\ClormProgram\TimetablePrograms\taskUser.lp"

class DateField(StringField):
    pytocl=lambda dt:dt.strftime("%d/%m/%Y")
    cltopy=lambda s:datetime.datetime.strptime(s,"%d/%m/%Y").date()

def dateRange(start,end):
    incrementDays = timedelta(days=1)
    tmp=[]
    while start<end:
        tmp.append(start)
        start +=incrementDays
    return list(enumerate(tmp))

class AvaliableDays(Predicate):
    nameOfDay:str 


#daysField=define_enum_field(ConstantField,AvaliableDays)
#avaliableDays=refine_field(ConstantField, ["Monday","Teusday","Wednesday","Thursday","Friday","Saturday","Sunday"])
#ENUM FIELD IS NOT SOMETHING YOU WANT THEY CANNOT BE QUERIED?
class DayVals(Predicate):
    mon:bool
    tue:bool
    wed:bool
    thu:bool 
    fri:bool
    sat:bool
    sun:bool

class User(Predicate):
    name:ConstantStr
    avaliable:DayVals
    # ?minTime:int
    # maxTime:int

class Task(Predicate):
    name:ConstantStr
    duration:int
    #reward: int

class Assignment(Predicate):
    taskValue:ConstantStr
    user:ConstantStr
    duration:int
    avaliable:DayVals
    time:int


def main():
   
    # durations=[task['duration'] for task in taskDetails['TaskDescriptions']]
    # taskNames=[task['name'] for task in taskDetails['TaskDescriptions']]
    ctrl=clingo.Control(unifier=[User,Task,Assignment])
    clingoCtrl=clingo.Control()
    ctrl.load(ASP_PROGRAM)
    # startDate = taskDetails["TaskValues"][1]["DateDescription"][0]["startDate"]
    # endDate = taskDetails["TaskValues"][1]["DateDescription"][0]["endDate"]
    # dateGenerator="""date(@dateRange(startDate,endDate))"""
   

    #So it does actually add to the factbase but it isnt in a way that is understandable for the parser
    #Users work when there is only one value within it?
    users=[User(name=userValues['name'],avaliable=DayVals(mon=userValues['Mon'],tue=userValues['Tue'],wed=userValues['Wed'],thu=userValues['Thur'],fri=userValues['Fri'],sat=userValues['Sat'],sun=userValues['Sun'])) for userValues in userDetails['userSpecifications']]
    tasks=[Task(name=taskValues['taskName'],duration=taskValues['duration'])for taskValues in taskDetails["TaskValues"][0]["TaskDescriptions"]]  
    instances=FactBase(users+tasks)
    print(instances)
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
                print("\t chore {}, at time {}".format(a.taskValue,a.time))
                
    
    

if __name__=="__main__":
    main()