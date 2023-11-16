% Facts about fruits and their colors
fruit_color(apple, red).
fruit_color(banana, yellow).
fruit_color(grape, purple).
fruit_color(orange, orange).
fruit_color(watermelon, green).

% Predicate to query for a fruit and its color using backtracking
fruit_and_color(Fruit, Color) :-
    fruit_color(Fruit, Color).

% Example Queries
% Query: fruit_and_color(Fruit, red).
% This will find fruits that are red.

% Query: fruit_and_color(apple, Color).
% This will find the color of an apple.

% Query: fruit_and_color(Fruit, Color).
% This will backtrack and find all combinations of fruits and colors.
