time(T):-T=1..32.
date(DA):-DA=1..7.


%:-chore(C,T1), chore(C,T2), T1<T2.
min(MI):- user(_,_,MI,_).
max(MX):- user(_,_,_,MX).
%The assigmnet value here is determined by the number at the start so 4 timeslots and 4 tasks min will be asigned to the user

1{assignment(C,TID,U,ID,D,T,R,DA) :time(T)}7 :- 
    date(DA),
    preferredDays(DY,DID),
    preferredTask(C,D,R,PID,TID,MT),
    user(U,ID,MI,MX), 
    time(T), 
    T>=MI, T<=MX,T>=MT, 
    DY= DA, ID=DID, 
    PID=ID.

    % TRY ADDING A SUM CONDITION HERE THAT IS DESIGNED TO LIMIT THE AMOUNT OF TIMES A TASK IS DONE IN ONE DAY 
    % assignment(_,TID1,U,ID1,_,T1,_,DA1),assigmnet(_,TID2,U,ID2,_,T2,_,DA2),
    % TID1!=TD.




%KEEEEP THISSS
%{assignment(C,TID,U,ID,D,T,R) :user(U,ID,MI,MX),preferredTask(C,D,R,ID,TID),time(T)}=R:- .
%KEEEEP THISSS

%:- assignment(C1,_,_,_,_,_,_), assignment(C2,_,_,_,_,_,_), C1=C2.


%#minimize {T@1,C,U: assigmnet(C,U,_,_,T,_,_)}.
%:-assignment(_,_,ID1,_,_,_,_), assignment(_,_,ID2,_,_,_,_), pref()

%R{assignment(C,U,D,T,DA,R) :time(T),days(DA)} 32 :- task(C,D,R,U),user(U,ID).


%timeConflict(C1,T1, DA1, C2,T2,DA2,U) :- assignment(C1,U,_,T1,DA1,_), assignment(C2,U,_,T2,DA2,_), T1!=T2, DA1!=DA2. 
%:- assignment(C1,U1,_,T,DA,_), assignment(C2,U2,_,T,DA,_), U1 !=U2, C1!=C2.


%timeConflict(C1,C2,T1,T2) :- ass


%The order is that the chores, users, duration,time, days 
%Need to make sure that the assignment of task not at the same time
%assignment(C,U,D,T) :-  assignment(C,U,T), tasks(C,D).

%:- assignment(C,T1), assignment(C,T2), T1!=T2.


% #minimize{1@2,U :avaliableUser(U)}.
% #minimize{T@1,U: assignment(D,U,C,T)}.

%1 { assignment(C,U,D,T,DA) : user(U,ID),time(T),days(DA)}  :- task(C,D).

%Need to represent the idea of the total time of the tasks assigned to the user does not exceed a certain amount


%A constraint is defined to make sure that the same task is not assigned to the same


%NUMBER

% Defines a task and its relevant taskID in the 
% JSON file, also acts as a way of retriving only the
%taskID of a certain task
% time(1..4).
% 1{assignment(D,U,C,T): date(D), user(U), chore(C), time(T)} 1:-chore(C).
% %This accounts for the conflict between two chores being assigned at the same time 
% :- assignment(D,U,C1,T1), assignment(D,U,C2,T2), C1!=C2, T1!=T2.

% avaliableUser(U) :- assignment(_,U,_,_).
% #minimize{1@2,U :avaliableUser(U)}.
% #minimize{T@1,U: assignment(D,U,C,T)}.