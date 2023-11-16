% Facts
teacher(john_doe, math101).
teacher(jane_smith, physics202).
teacher(bob_jones, history303).

student(alice, math101).
student(bob, physics202).
student(charlie, history303).
student(david, math101).


% Rules
teaches_subject(Teacher, Subject) :-
    teacher(Teacher, Subject).

enrolled_in(Student, Subject) :-
    student(Student, Subject).


% Example Queries
% Who teaches the subject 'math101'?
% Query: teaches_subject(Teacher, math101).
%
% Which students are enrolled in 'physics202'?
% Query: enrolled_in(Student, physics202).
%
% What is the course code for 'history303'?
% Query: subject_code(history303, Code).
