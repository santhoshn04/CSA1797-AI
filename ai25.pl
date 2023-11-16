% Initial state: monkey at door, on floor, bananas on ceiling, chair at center
initial_state(state(at_door, on_floor, at_center, on_ceiling)).

% Define moves
% Monkey can walk from the door to the center
move(state(at_door, on_floor, X, Y), grasp, state(at_center, on_floor, X, Y)).
% Monkey can walk from the center to the door
move(state(at_center, on_floor, X, Y), release, state(at_door, on_floor, X, Y)).
% Monkey can push the chair from the door to the center
move(state(at_door, on_floor, X, Y), climb, state(at_center, on_chair, X, Y)).
% Monkey can push the chair from the center to the door
move(state(at_center, on_floor, X, Y), descend, state(at_door, on_chair, X, Y)).
% Monkey can reach the bananas if it's on the chair at the center
move(state(P, on_chair, at_center, on_ceiling), grasp, state(P, on_chair, at_center, has_bananas)).

% Define the goal state
goal_state(state(_, _, _, has_bananas)).

% Define the solve predicate
solve(State, Actions) :-
    goal_state(State),          % If the current state is the goal state, no further actions needed
    Actions = [].
solve(State1, [Action | Rest]) :-
    move(State1, Action, State2),  % Try a possible move
    solve(State2, Rest).           % Recursively solve the resulting state

