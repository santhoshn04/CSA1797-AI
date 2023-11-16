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
