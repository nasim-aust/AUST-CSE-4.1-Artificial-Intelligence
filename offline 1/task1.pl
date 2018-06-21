person(thanos).
person("Captain America").
person("Peter Parker").
person("Tony Stark").
person(nebula).
person(drax).
person(thor).

place(titan).
place(brooklyn).
place(queens).
place(manhattam).
place(xander).
place(asgard).

thing("Infinity Gaunlet").
thing(shield).
thing("his fingers").
thing(webs).

adjective(young).
adjective(obsessive).
adjective(marcissist).
adjective(narcissist).
adjective(vengeful).
adjective(worthy).
adjective(red).
adjective(blue).

adverb(vigorously).
adverb(anxious).

verb(destroy).
verb(snap).
verb(wield).
verb(wave).
verb(fight).

person_verb(destroys).
person_verb(snaps).
person_verb(wields).
person_verb(weaves).
person_verb(fights).

auxiliary_present(is).
auxiliary_future(will).

continuous_verb(destroying).
continuous_verb(snapping).
continuous_verb(wielding).
continuous_verb(weaving).
continuous_verb(fighting).

preposition(from).
preposition(in).

%1st sentence
isValidSentence1(A,B,C):- person(A),person_verb(B),thing(C);person(C);place(C).

%2nd sentence
isValidSentence2(A,B,C,D):- person(A),person_verb(B),thing(C);person(C);place(C),adverb(D).

%3rd sentence
isValidSentence3(A,B,C):- person(A),auxiliary_present(B),adjective(C).

%4th sentence
isValidSentence4(A,B,C,D):- person(A),auxiliary_present(B),continuous_verb(C),thing(D);place(D);person(D).

%5th sentence
isValidSentence5(A,B,C,D,E):- person(A),auxiliary_present(B),continuous_verb(C),place(D);person(D);thing(D),adverb(E).

%6th sentence
isValidSentence6(A,B,C,D):- person(A),auxiliary_future(B),verb(C),place(D);person(D);thing(D).

%7th sentence
isValidSentence7(A,B,C,D,E):- person(A),auxiliary_future(B),verb(C),place(D);person(D);thing(D),adverb(E).

%8th sentence
isValidSentence8(A,B,C,D):- person(A),auxiliary_present(B),preposition(C),place(D).
