time(T):-T=1..32.
date(DA):-DA=1..7.

%One to one assignment set for assigning a user to a time, date value based on their preferred time/date/task values
1{assignment(C,TID,U,ID,D,T,DA) :user(U,ID,MI,MX),time(T),date(DA),T>=MI, T<=MX}1 :- 
        preferredTask(C,D,PID,TID), PID=ID,
        preferredDays(DY,DID),
        DY= DA, ID=DID.

%Ensures that different users are not assigned the same chore for the same date/time value
:- assignment(C,_,_,ID1,D,T,DA) ,  assignment(C,_,_,ID2,D,T,DA), ID1!=ID2 .

%Ensures the same chore is not assigned to the user on the same time values
:- assignment(C1,_,_,ID,D1,T,DA), assignment(C2,_,_,ID,D2,T,DA), C1!=C2.

%Calculates the absolute value of the time it takes to complete a task for different users, specifically for shared personal tasks - ensures no overlap in assigned time values
:- assignment(C,_,_,ID1,D,T1,_), assignment(C,_,_,ID2,D,T2,_),preferredTask(C,D,_,_), ID1!=ID2, abs(T1-T2)< D.

%Ensures that the assigned time values for chores assigned to one user does not overlap with how long it takes to complete the task
:- assignment(C1,_,_,ID,D1,T1,DA), assignment(C2,_,_,ID,D2,T2,DA), T1<T2, T1+D1> T2.