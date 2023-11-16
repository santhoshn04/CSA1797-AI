% Facts
can_fly(sparrow).
can_fly(eagle).
can_fly(swallow).

cannot_fly(penguin).
cannot_fly(ostrich).

% Rules
bird_can_fly(Bird) :-
    can_fly(Bird).

bird_cannot_fly(Bird) :-
    cannot_fly(Bird).

% Example Queries
% Is a sparrow able to fly?
% Query: bird_can_fly(sparrow).

% Is a penguin able to fly?
% Query: bird_cannot_fly(penguin).
