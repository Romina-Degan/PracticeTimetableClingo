time(T):-T=1..32.
date(DA):-DA=1..7.

1{assignment(C,TID,U,ID,D,T,DA) :user(U,ID,MI,MX),time(T),date(DA),T>=MI, T<=MX}1 :- 
        preferredTask(C,D,PID,TID), PID=ID,
        preferredDays(DY,DID),
        DY= DA, ID=DID.

:- assignment(C,_,_,ID1,D,T,DA) ,  assignment(C,_,_,ID2,D,T,DA), ID1!=ID2 .
:- assignment(C1,_,_,ID,D1,T,DA), assignment(C2,_,_,ID,D2,T,DA), C1!=C2.
:- assignment(C,_,_,ID1,D,T1,_), assignment(C,_,_,ID2,D,T2,_),preferredTask(C,D,_,_), ID1!=ID2, abs(T1-T2)< D.
:- assignment(C1,_,_,ID,D1,T1,DA), assignment(C2,_,_,ID,D2,T2,DA), T1<T2, T1+D1> T2.

% :-assignment(_,TID,_,_,_,_,_,_), preferredTask(_,_,R,_,TID,_), #count{CID :assignment(_,TID,_,_,_,_,_,_), CID=TID}>R.






    % date(DA),
    % preferredDays(DY,DID),
    % preferredTask(C,D,R,PID,TID,MT),
    % user(U,ID,MI,MX),

    % DY= DA, ID=DID, 
    % PID=ID.


% firstTime(T1) :- assignment(_,TID,_,_,_,T1,_,_).
% secondTime(T2) :-assignment(_,TID,_,_,_,T2,_,_).
% duration(D):-assignment(_,_,_,_,D,_,_,_).
% #show firstTime(T1).
%&diff {T1-T2}>=D :- firstTime(T1),secondTime(T2),duration(D).

% 1{start(TID): preferredTask(_,_,_,_,TID,_)}1.
% permutation(TID1,C2) :- assignment(_,TID,_,_,_,_,_,_)
% assigmnet(_,TID,_,ID,D,T1,_,DA)

%  &diff {T1-T2} <=D :-assignment(_,TID,_,ID,D,T1,_,DA), assignment(_,TID,_,ID,D,T2,_,DA).
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