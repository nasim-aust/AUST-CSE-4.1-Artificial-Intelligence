%List Predicates
member(Y,[Y|_]).
member(Y,[_|T]):-member(Y,T).
append([],L,L).
append(A,B,C):- [H|T] = A, [H|T1]= C, append(T,B,T1).

%Grammar Rules

person(X) :- member(X,[thanos,"Captain America","Peter Parker","Tony Stark",nebula,drax,thor]).
place(X):-member(X,[titan, brooklyn,queens,manhattam,xander,asgard]).
thing(X):-member(X,["Infinity Gaunlet",shield,"his fingers",webs]).
adjective(X):-member(X,[young,obsessive,marcissist,narcissist,vengeful,worthy,red,blue]).
adverb(X):-member(X,[vigorously,anxious]).
verb(X):-member(X,[destroy,snap,wield,wave,fight]).
personVerb(X):-member(X,[destroys,snaps,wields,weaves,fights]).
auxiliaryPresent(X):-member(X,[is]).
auxiliaryFuture(X):-member(X,[will]).
continuousVerb(X):-member(X,[destroying,snapping,wielding,weaving,fighting]).
preposition(X):-member(X,[from,in]).

%1st-1
personPersonVerb([M,N]) :- person(M),personVerb(N).
%2nd-1
pTPAdverb([M,N]) :- place(M);thing(M);person(M), adverb(N).
%3RD-1
personAPresent([M,N]) :- person(M),auxiliaryPresent(N).
%4th-1
continousVerbTPPP([M,N]) :- continuousVerb(N),place(N);thing(N);person(N).
%5TH-1
continousVerbTPPPAdverb([M,N]) :- continousVerbTPPP(M),adverb(N).
%6th-1
personAFuture([M,N]) :- person(M),auxiliaryFuture(N).
verbTPP([M,N]) :- verb(M), place(N);thing(N);person(N).
%7t-1
verbTPPAdverb([M,N]) :- verbTPP(M), adverb(N).
%8th-1
prepositionPlace([M,N]) :- preposition(M), place(N).

%1st
isValidSentence(C):- personPersonVerb(A),place(B);thing(B);person(B),append(A,B,C).
%2nd
isValidSentence(C):- personPersonVerb(A),pTPAdverb(B),append(A,B,C).
%3rd
isValidSentence(C):- personAPresent(A),adjective(B),append(A,B,C).
%4th
isValidSentence(C):- personAPresent(A),continousVerbTPPP(B),append(A,B,C).
%5th
isValidSentence(C):- personAPresent(A),continousVerbTPPPAdverb(B),append(A,B,C).
%6th
isValidSentence(C):- personAFuture(A),verbTPP(B),append(A,B,C).
%7th
isValidSentence(C):- personAFuture(A),verbTPPAdverb(B),append(A,B,C).
%8th
isValidSentence(C):- personAPresent(A),prepositionPlace(B),append(A,B,C).

% isValidSentence(["Captain America",wields,shield]).
