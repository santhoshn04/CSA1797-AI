% Facts about diseases and corresponding diet suggestions
diet_suggestion(heart_disease, low_fat).
diet_suggestion(diabetes, low_sugar).
diet_suggestion(hypertension, low_salt).
diet_suggestion(celiac_disease, gluten_free).

% Rule to suggest a diet based on the disease
suggest_diet(Person, Disease, Diet) :-
    has_disease(Person, Disease),
    diet_suggestion(Disease, Diet).

% Example Facts (you can extend this with more data)
has_disease(john, heart_disease).
has_disease(lisa, diabetes).
has_disease(bob, hypertension).
has_disease(susan, celiac_disease).

'
