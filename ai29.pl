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

% Forward Chaining Rule
infer_condition(Person, Condition) :-
    has_condition(Person, Condition).

% Example Queries
% Query: infer_condition(john, Condition).
% This will infer John's medical condition based on his symptoms.

% Query: infer_condition(mary, Condition).
% This will infer Mary's medical condition based on her symptoms.
