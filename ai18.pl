% Database of names and dates of birth
dob(john, date(1990, 5, 15)).
dob(susan, date(1985, 10, 20)).
dob(mike, date(1995, 3, 8)).
dob(lisa, date(1980, 7, 12)).
dob(david, date(2000, 12, 3)).

% Query to get the date of birth for a specific person
get_dob(Person, DateOfBirth) :-
    dob(Person, DateOfBirth).

% Query to check if a person is born in a specific year
born_in_year(Person, Year) :-
    dob(Person, date(Year, _, _)).

% Query to check if a person is born in a specific month
born_in_month(Person, Month) :-
    dob(Person, date(_, Month, _)).

% Query to check if a person is born on a specific day
born_on_day(Person, Day) :-
    dob(Person, date(_, _, Day)).
