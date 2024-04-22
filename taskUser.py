import json
import os


currentDir=os.path.dirname(os.path.realpath(__file__))
filePathTaskVals=os.path.join(currentDir,"instances","Task.json")
#To change the current file that is being tested, please change the second parameter listed Household_
filePathTestVals=os.path.join(currentDir,"instances","Household4.json")

with open(filePathTaskVals) as taskFile:
    taskDetails=json.load(taskFile)

with open(filePathTestVals) as userFile:
    userDetails=json.load(userFile)


from clorm import monkey
from typing import Tuple,List
monkey.patch()
from enum import Enum
import clingo
from datetime import datetime, timedelta
from clorm import ConstantStr,define_enum_field,FactBase,IntegerField,StringField,ContextBuilder, Predicate,ConstantField,field,refine_field, ph1_, ph2_
cb=ContextBuilder
ASP_PROGRAM =r"taskUser.lp"

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

# #ENUM FIELD IS NOT SOMETHING YOU WANT THEY CANNOT BE QUERIED?



    
    #avaliable:DayVals
    # ?minTime:int
    # maxTime:int
    
class Task(Predicate):
    name:ConstantStr
    duration:int
    


class User(Predicate):
    name:ConstantStr
    userID:ConstantStr
    minVal:int
    maxVal:int 

class PreferredTask(Predicate):
    name:ConstantStr
    duration:int
    user:ConstantStr
    taskID:int


class PreferredDays(Predicate):
    dateVal:int
    userID:ConstantStr

class Assignment(Predicate):
    taskValue:ConstantStr
    taskID:int
    user:ConstantStr
    userID:ConstantStr
    duration:int
    time:int
    date:int


def main():
    prefTask=[]
    
    ctrl=clingo.Control(unifier=[User,Assignment,PreferredTask,PreferredDays])
    
    ctrl.load(ASP_PROGRAM)

    #So it does actually add to the factbase but it isnt in a way that is understandable for the parser
    #Users work when there is only one value within it?
    users = [User(name=userValues['name'], 
                  userID=userValues['userID'], 
                  minVal=userValues['availableMin'],
                  maxVal=userValues['avaliableMax'])
                  for userValues in userDetails['userSpecifications']]
    
    
    #tasks=[Task(name=taskValues['taskName'],duration=taskValues['duration'], repetitionVal=taskValues["repetition"])for taskValues in taskDetails["TaskValues"][0]["TaskDescriptions"]] 
   
    instances= FactBase(users)
    lastPref=[]
    ctrl.add_facts(instances)
    for members in users:
        currTask=[]
        currUser=(list(filter(lambda x:(x["userID"]==members.userID),userDetails['userSpecifications'])))
        currPref=currUser[0]['prefer']
        currDay=currUser[0]['dayPrefer']

        for days in currDay:
            instances.add(FactBase(PreferredDays(dateVal=days,userID=members.userID)))
            ctrl.add_facts(instances)
        prefTask={}
        for items in currPref:
            if items in lastPref and items!="Personal": 
                currPref.remove(items)

        for items in currPref:
            for taskValues in  taskDetails["TaskValues"][0]["TaskDescriptions"]:        
                if items in taskValues['label'] or taskValues['label']=="Personal":              
                    currTask=[PreferredTask(name=taskValues['taskName'],duration=taskValues['duration'] ,
                                            user=members.userID, taskID=taskValues['taskID'])]
                    print(currTask)
                    print("\n")
                    instances.add(FactBase(currTask))
                    ctrl.add_facts(instances)
            lastPref.append(items)
    
    ctrl.ground([("base", [])])
    print(instances)
    solution=None
    
    def on_model(model):
        nonlocal solution
        solution=model.facts(unifier=[User,Assignment,PreferredTask,PreferredDays], atoms=True,raise_on_empty=True)
    
    ctrl.solve(on_model=on_model)
    if not solution:
        raise ValueError("No solution Found")

    query = solution.query(Assignment).where(Assignment.user == ph1_).order_by(Assignment.date, Assignment.time)
    
    results={}
    
    for u in users: 
        currentTaskDuration=Assignment.duration
        assignments = list(query.bind(u.name ).all())
        userID=u.userID
        taskVals=[]
        if not assignments:
            print("User not assigned any tasks!".format(u.name))
            
        else:
            print("User {} assigned to: ".format(u.name))
            
            for a in assignments:
                currentDuration=a.duration
                
                print("\t chore {}, at time {} at date{}".format(a.taskValue,a.time,a.date))
                taskVals.append({"TaskValue":a.taskValue, "time": a.time, "date":a.date})

        results[str(userID)] = taskVals
    with open('result.json','w') as fp:
        json.dump(results, fp, indent=1)    

if __name__=="__main__":
    main()