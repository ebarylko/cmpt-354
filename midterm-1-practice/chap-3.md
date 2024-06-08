## Section 3.6

### Exercise 3.6.2
s = Social Security number

n = name

b = birthdate

cn = child name

cs = Social Security number of child

cb = child birthdate

as = serial number of automobile n owns

am = make of the automobile with serial number as

a) 
FDs: $s \rightarrow n, b$, 

$as \rightarrow  am$, 

$cs \rightarrow cn, cb$,

$as \rightarrow am$

MVDs: $n, s, b \twoheadrightarrow cn, cs, cb$

$n, s, b \twoheadrightarrow as, am$