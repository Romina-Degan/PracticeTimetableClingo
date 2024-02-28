time(1..32).




1 { assignment(C,U,D,A,T) : user(U,A),time(T)} 1 :- task(C,D).

%Need to represent the idea of the total time of the tasks assigned to the user does not exceed a certain amount

%:- assignment(C1, U,_,_), assignment(C2,U,_,_), C1 != C2.




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