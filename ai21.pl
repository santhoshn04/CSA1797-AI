% Define the Towers of Hanoi predicate
hanoi(N, A, B, C, Moves) :-
    move(N, A, B, C, Moves).

% Base case: moving 0 discs requires 0 moves
move(0, _, _, _, []).
% Recursive case: move N discs from A to C using B as an auxiliary peg
move(N, A, B, C, Moves) :-
    M is N - 1,
    move(M, A, C, B, FirstMoves),
    append(FirstMoves, [(A, C)], TempMoves),
    move(M, B, A, C, SecondMoves),
    append(TempMoves, SecondMoves, Moves).
