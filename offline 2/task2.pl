n --> [thanos];["Captain America"];["Peter Parker"];["Tony Stark"];[nebula];[drax]; [thor].
p-->[titan];[brooklyn];[queens];[manhattan];[xander];[asgard].
t-->["Infinity Gauntlet"];[shield];["his fingers"];[webs].
adj-->[young];[obsessive];[marcissist];[narcissist];[vengeful];[worthy];[red];[blue].
adv-->[vigorously];[anxious].
rv --> [destroy];[snap];[wield];[wave];[fight].
tpv --> [destroys];[snaps];[wields];[weaves];[fights].
av --> [is].
fv --> [will].
cv --> [destroying];[snapping];[wielding];[weaving];[fighting].
pre-->[in];[from].

s-->np, vp.
np --> n.
vp -->tpv,t;p;n.
vp --> tpv,n;p;t,adv.
vp-->av,adj.
vp-->av,cv,n;t;p.
vp-->av,cv,n;t;p,adv.
vp-->fv,rv,n;t;p.
vp-->fv,rv,n;t;p,adv.
vp-->av,pre,p.


isValidSentence(X) :- s(X,[]). 

%isValidSentence([nebula, will,fight,thanos],[]).
