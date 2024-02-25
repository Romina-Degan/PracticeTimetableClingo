% Defines a task and its relevant taskID in the 
% JSON file, also acts as a way of retriving only the
%taskID of a certain task
time(1...4).
1{assignment(D,U,C,T): date(D), user(U), chore(C), time(T)} 1:-chore(C)
%This accounts for the conflict between two chores being assigned at the same time 
:- assignment(D,U,C1,T1), assignment(D,U,C2,T2), C1!=C2, T1!=T2

avaliableUser(U) :- assignment(_,U,_,_)
