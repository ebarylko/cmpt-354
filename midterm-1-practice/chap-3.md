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


What do I do now? Neither of the MVDs for R2 are a superkey, but following
the decomposition procedure would not yield a relation with distinct 
attributes. Is there an MVD I am forgetting to add?

### Exercise 3.6.3

a) $R(A, B, C, D)$ with MVD’s $A \rightarrow B and A \twoheadrightarrow C$

The $MVD$ violations are that $A$ is not a superkey for $R$. Decomposing $R$,
I obtain $R2(A, B)$ and $R3(A, C, D)$.

$R3$ has an $MVD$ violation since $A$ does not serve as a superkey. 
Decomposing $R3$, I obtain $R4(A, C)$ and $R5(A, D)$

Decomposing $R$, I have $R2(A, B), R4(A, C)$, and $R5(A, D)$.

