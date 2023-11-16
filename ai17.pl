% Predicate to sum integers from 1 to N with an accumulator
sum_integers(N, Sum) :-
    sum_integers_helper(N, 0, Sum).

% Base case: Sum of integers from 1 to 0 is the accumulator value.
sum_integers_helper(0, Acc, Acc).

% Recursive case: Update the accumulator and continue with the next integer.
sum_integers_helper(N, Acc, Sum) :-
    N > 0,
    NextN is N - 1,
    NextAcc is Acc + N,
    sum_integers_helper(NextN, NextAcc, Sum).
