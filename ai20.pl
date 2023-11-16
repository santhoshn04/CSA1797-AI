% Facts
planet(mercury, rocky, 0.39).
planet(venus, rocky, 0.72).
planet(earth, rocky, 1.00).
planet(mars, rocky, 1.52).
planet(jupiter, gas_giant, 5.20).
planet(saturn, gas_giant, 9.58).
planet(uranus, ice_giant, 19.22).
planet(neptune, ice_giant, 30.05).

% Rules
rocky_planet(Name) :-
    planet(Name, rocky, _).

gas_giant(Name) :-
    planet(Name, gas_giant, _).

ice_giant(Name) :-
    planet(Name, ice_giant, _).

% Example Queries
% Which planets are rocky?
% Query: rocky_planet(Planet).

% Which planets are gas giants?
% Query: gas_giant(Planet).

% Which planets are ice giants?
% Query: ice_giant(Planet).
