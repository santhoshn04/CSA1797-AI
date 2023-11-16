% Facts
male(john).
male(bob).
male(mike).
male(jack).
male(jason).
female(lisa).
female(susan).
female(anne).
female(emily).

% Parent relationships
parent(john, bob).
parent(john, lisa).
parent(bob, mike).
parent(bob, anne).
parent(susan, mike).
parent(susan, anne).
parent(mike, jason).
parent(anne, emily).
parent(jason, jack).

% Rules
father(Father, Child) :-
    male(Father),
    parent(Father, Child).

mother(Mother, Child) :-
    female(Mother),
    parent(Mother, Child).

sibling(Sibling1, Sibling2) :-
    parent(Parent, Sibling1),
    parent(Parent, Sibling2),
    Sibling1 \= Sibling2.

grandparent(Grandparent, Grandchild) :-
    parent(Grandparent, Parent),
    parent(Parent, Grandchild).

ancestor(Ancestor, Descendant) :-
    parent(Ancestor, Descendant).
ancestor(Ancestor, Descendant) :-
    parent(Ancestor, Intermediate),
    ancestor(Intermediate, Descendant).
