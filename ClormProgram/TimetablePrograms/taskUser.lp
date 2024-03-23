time(T):-T=1..32.
days(DA):-DA=1..7.

assignment(C):- assignment(C,_,_,_,_).




%:-chore(C,T1), chore(C,T2), T1<T2.


%The assigmnet value here is determined by the number at the start so 4 timeslots and 4 tasks min will be asigned to the user

R{assignment(C,U,D,T,DA,R) :time(T),days(DA)} 32 :- task(C,D,R),user(U,ID).

%timeConflict(C1,C2,T1,T2) :- ass



%tconflict(C,T1), tconflict(C,T2) :- assignment (C,U,_,T1,_), assigmnet(C,U,_,T2,_), T1!=T2.


%conflict(C,T) :- assigmnet(C,U1,_,T,_) , assigmnet(C,U2,_,T,_), U1 !=U2.


%:-time(T1),time(T2), T1!=T2, assignment(C,T1), assignment(C,T2).

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