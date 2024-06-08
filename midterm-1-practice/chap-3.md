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
FDs: 

$s \rightarrow n, b$ 
                   
$as \rightarrow  am$ 
                   
$cs \rightarrow cn, cb$
                   
MVDs: 

$s \twoheadrightarrow cn, cs, cb$

$s \twoheadrightarrow as, am$

b)

For the relation $R(n, s, b, cn, cs, cb, as, am)$, I have that the
MVD $s  \twoheadrightarrow cn, cs, cb$ is not a superkey (the same parent
may have multiple children or cars). I can then split up R into 
$R2(n, s, b, cn, cs, cb)$ and $R3(n, s, b, as, am)$.

For $R2$, the following FDs and MVDs hold:

$s \twoheadrightarrow cn, cs, cb$

$cs \twoheadrightarrow n, s, b$

$s \rightarrow n, b$

$cs \rightarrow cn, cb$


