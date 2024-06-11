Schema: conceptual structure of the data
Data structure: how the data is managed/implemented

Data model: mathematical description of describing the data

Description includes structure of the data, operations on the data, and constraints of the data.

Constraints: limits on the data
Ex: name can never be longer than 30 characters
Multiple types of constraints: 
Domain type: what limits are on the attribute for the domain? age cannot be negative
Integrity constraint: value is unique across all instances


Common data models: Relational, Key-Value, Semistructured

Relational:
Data structured as tables
Query language can be RA, RC, SQL
Can add constraints on attributes

Key-value:
Key is an integer or string, value can be anything
Query operators are get(key) and put(key, value)
Constraints on the data could be that the key is unique or the value is not null

Semistructured:
Data is structured as a tree
Example constraints: each person needs an id and birthdate associated with them


Schema:
shows the logical structure of the data
Defined at setup time

Instance:
Represents the data content
All entities that belong to a specific group?

Ex:
Schema for User: User(uid, name, class)
Instance: {(1, "a", CMPT300), (2, "b", CMPT254)}

Core operators:
Selection, projection, cross product, union, difference, renaming

Derived operators:
Join, natural join, intersection

Selection: $\sigma_{p}R$, where p is the condition for keeping a row, R is the relation. Monotone.

Projection: $\pi_{a}R$, where a is the set of attributes to access, R is the relation. Monotone.

Remember: you can use boolean operators ($\land, \lor$), and the result of projecting 
attributes is a set

Cross product: $X$, is commutative since the ordering of the columns does not matter in a tuple. Monotone.

Theta join: $R \bowtie_{p} S = \sigma_{p}(R X S)$, joins R and S on some condition P. Monotone.

Natural join: $R \bowtie S = \pi_{l}(R \bowtie_{p} S)$. Only keeps columns which have  
matching values for columns common to R and S. Monotone.

Difference: $R - S$, monotone with respect to R.

For union and intersection, R and S must have the same schema

Union: $R \cup S$, combines records from both R and S. Monotone.

Intersection: $R \cap S = R - (R - S) = R \bowtie S$. Get what is common to both R and S. Monotone

Rename: $\rho_{new_title}(A1, A2, A3, ... AN)R$ will rename R to new_title and rename each 
attribute to R to its matching attribute in (A1, A2, A3, ... AN).

Motonone operators:
An operator p such that $p(a, b) \subseteq p(a', b)$
Ex: $\{1, 2, 3\} - \{2, 3\}$ is monotone, since you can always add more 
to the first set, and you know that 1 will always be in the resulting set.


Codd's theorem: relational algebra queries are equivalent to relational calculus queries 

Relational algebra has no recursion.

Key: a set of attributes K such that K uniquely identifies an instance of a relation. 
K must be minimal (a proper subset of K cannot function as a Key).
Ex: User(uid, name, age).
uid is key, but age nor {uid, age} is a key

Primary key: one attribute of K

Entity: a thing or item of a collection
Entity set: a collection of entities
Attributes: properties of entities or relationships
Relationship: an association among entities showing how one is related to the other and vice versa

In a relationship, the keys are the keys of the connected entities plus the keys of the relationship.

Multiplicity of relationships:
Many to many: an entitiy in E is related to zero or more entities in F
One to many: each entity in E is related to zero or more entities in F, each entity in F is related 
to zero or one entity in E
One to one: Each entity in E is related to exactly one entity in F and vice versa.

Weak entity set: 
an entity set whose keys come from other entity sets

ISA relationships: B isa A means that B inherits everything A has, including its keys and attributes.

Entity-in-all-superclass:
An entity belongs in the table that represents the subclass they are a part of. 
An entity can be in multiple tables, including the table representing its superclass.
The subclass holds the keys it inherits plus its own attributes.
Note: all the users are in one table, but attributes belonging
to different subclasses are scattered and may not be easily gathered.

Entity-in-most-specific-class:
An entity belongs to the most specific table which describes the subclass they are.
Note: Entities are scattered in different tables, but the only the attributes relevant to the 
table are present

All-entities-in-one-table:
An entity has all values from the base entity plus NULL values for the attributes belonging to 
the subclasses.
Note: Everything is in one table, but it can be complicated if the class hierarchy is complex


Functional dependency:
$X \rightarrow Y$ iff for two tuples A and B who share the same $X$ values, they also share the 
same $Y$ values.

Trivial FD: $RHS \subseteq LHS$ 

Non trivial FD: $RHS \cap LHS = \emptyset$ 

Superkey: a key which has trivial attributes.

Closure of an attribute: for an attribute X, $X^{+}$ is the set of all attributes which can 
be functionally determined by X.

If $X \rightarrow Y$ follows from a set of FDs, it means that $Y \subseteq X^{+}$.

Armstrong's axioms:

Reflexivity: if $Y \subseteq X$, $X \rightarrow Y$.

Augmentation: if $X \rightarrow Y, XZ \rightarrow YZ$ for any Z.

Transitivity: if $X \rightarrow Y$ and $Y \rightarrow Z$, then $X \rightarrow Z$.

Splitting: if $X \rightarrow YZ$, then $X \rightarrow Y$, $X \rightarrow Z$

Combining: if $X \rightarrow Y$ and $X \rightarrow Z$, then $X \rightarrow YZ$


Lossly decomposition: For relations T, R, and S, $R \subset S \bowtie T$.

A lossless decomposition is one where joining the separated tables returns you the 
original table.

R is in BCNF if for any nontrivial FD $X \rightarrow Y$ in R, X is a superkey.

A table can be in BCNF and have redundancy.

MVDs:

Every FD is an MVD.

$X \twoheadrightarrow Y$ means that if two instances agree in the X values, we can 
swap the Y values and obtain tuples which are also in R.

Trivial MVD is one where $LHS \cup RHS$ contains all the attributes of R or $RHS \subseteq LHS$.

If $X \twoheadrightarrow Y$, then $X \twoheadrightarrow R - Y - X$.

Augmentation: If $X \twoheadrightarrow Y$ and $V \subseteq W$, then $XW \twoheadrightarrow VY$.

Transitivity: If $X \twoheadrightarrow Y$ and $Y \twoheadrightarrow Z$, then $X \twoheadrightarrow Z - Y$

Coalescence: if $X \twoheadrightarrow Y$ and $Z \subseteq Y$ and $\exists$ W disjoint from Y such that $W \rightarrow Z$,
then $X \rightarrow Z$.

3NF: 

R with FDs F are in 3NF when for all $X \rightarrow Y$, $Y \in X$ (trivial FD) or X is a superkey of R or Y
is part of some candidate key for R.

4NF:

For every nontrivial MVD $X \twoheadrightarrow Y$, X is a superkey.

Decomposing 4NF violations:
1. Find a nontrivial MVD $X \twoheadrightarrow Y$ where X is not a superkey
2. Decompose R into R2 and R3, where R2 has X and Y, and R3 has X and R - X - Y.
3. Repeat steps 1 and 2 on the new relations until everything is in 4NF




SQL:

Any comparison done with NULL will return NULL. This will affect filtering since 
the values being kept are those which return true for the predicate, and NULL 
is neither true nor false.

Set operations:
INTERSECT, UNION, EXCEPT

Bag operations: 

INTERSECT ALL - takes the minimum of an occurence of a value v in both R and S. $\{1, 2, 1, 3\} \cap \{1, 2\} = \{1, 2\}$


UNION ALL - joins all the occurences of a value v in both R and S. $\{1, 2, 1, 3\} \cup \{1, 2\} = \{1, 2, 1, 3, 1, 2\}$


EXCEPT ALL - takes the proper difference of sets R and S. $\{1, 2, 1, 3\} - \{1, 2\} = \{1, 3\}









