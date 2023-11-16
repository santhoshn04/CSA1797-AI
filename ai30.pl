% Facts
has_symptom(john, fever).
has_symptom(john, cough).
has_symptom(mary, headache).
has_symptom(mary, fatigue).

% Rules
has_condition(Person, flu) :-
    has_symptom(Person, fever),
    has_symptom(Person, cough).

has_condition(Person, cold) :-
    has_symptom(Person, cough).

has_condition(Person, stress) :-
    has_symptom(Person, headache).

has_condition(Person, anemia) :-
    has_symptom(Person, fatigue).

% Backward Chaining Rule
infer_condition(Person, Condition) :-
    has_condition(Person, Condition).

% Example Queries
% Query: infer_condition(john, flu).
% This will check if John has the flu.

% Query: infer_condition(mary, Condition).
% This will find Mary's medical condition.

% Query: infer_condition(john, anemia).
% This will check if John has anemia.
