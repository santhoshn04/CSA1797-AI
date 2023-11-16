% Sample graph representation with costs
edge(a, b, 2).
edge(a, c, 1).
edge(b, d, 3).
edge(c, d, 2).
edge(c, e, 4).
edge(d, e, 1).

% Heuristic function (h function)
heuristic(Node, H) :-
    goal(Goal),
    edge(Node, Goal, H).

% Best First Search algorithm
best_first_search(Start, Path) :-
    best_first_search([node(Start, 0, 0, [])], [], Path).

best_first_search([node(Current, _, _, Path) | _], _, Path) :-
    goal(Current).

best_first_search([node(Current, _, _, Path) | Rest], Visited, FinalPath) :-
    findall(
        node(Next, Cost, H, [Next | Path]),
        (
            edge(Current, Next, Cost),
            \+ member(Next, Visited),
            heuristic(Next, H)
        ),
        NextNodes
    ),
    append(NextNodes, Rest, NewQueue),
    sort_queue(NewQueue, SortedQueue),
    best_first_search(SortedQueue, [Current | Visited], FinalPath).% Facts about symptoms and possible medical conditions
symptom(john, fever).
symptom(john, cough).
symptom(mary, headache).
symptom(mary, fatigue).

condition(fever, flu).
condition(cough, cold).
condition(headache, stress).
condition(fatigue, anemia).

% Rule for diagnosing medical conditions
diagnose(Person, Condition) :-
    symptom(Person, Symptom),
    condition(Symptom, Condition).

% Example Query
% Query: diagnose(john, X).
% This will attempt to diagnose John's medical condition based on his symptoms.
% Facts about symptoms and possible medical conditions
symptom(john, fever).
symptom(john, cough).
symptom(mary, headache).
symptom(mary, fatigue).

condition(fever, flu).
condition(cough, cold).
condition(headache, stress).
condition(fatigue, anemia).

% Rule for diagnosing medical conditions
diagnose(Person, Condition) :-
    symptom(Person, Symptom),
    condition(Symptom, Condition).

% Example Query
% Query: diagnose(john, X).
% This will attempt to diagnose John's medical condition based on his symptoms.


% Sorting the queue based on heuristic
sort_queue(Queue, SortedQueue) :-
    predsort(compare_nodes, Queue, SortedQueue).

compare_nodes(Order, node(_, _, H1, _), node(_, _, H2, _)) :-
    compare(Order, H1, H2).

% Example goal
goal(e).

% Example query
% Query: best_first_search(a, Path).
% This will find the best-first search path from 'a' to 'e' in the given graph.
