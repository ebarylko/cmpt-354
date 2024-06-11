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

INTERSECT 

UNION 

EXCEPT 

Bag operations: 

INTERSECT ALL - takes the minimum of an occurence of a value v in both R and S. $\{1, 2, 1, 3\} \cap \{1, 2\} = \{1, 2\}$


UNION ALL - joins all the occurences of a value v in both R and S. $\{1, 2, 1, 3\} \cup \{1, 2\} = \{1, 2, 1, 3, 1, 2\}$


EXCEPT ALL - takes the proper difference of sets R and S. $\{1, 2, 1, 3\} - \{1, 2\} = \{1, 3\}


Quantified subqueries:

Where x op ALL(subquery): true iff for all t in the results of the subquery, x op t.

Where x op ANY/SOME(subquery): true iff for for at least one t in the results of the subquery, x op t.

Order of keywords:

SELECT 
FROM 
WHERE
GROUP BY
HAVING 
ORDER BY

Remember: ORDER BY automatically sorts ascending. To change this, you must add DESC to the attribute being ordered by.

Outer joins:

Full outer join: gives the result of $R \bowtie S$ plus the addition of any tuples from R and S which did not have a common attribute between them.

Left outer join: gives the result of $R \bowtie S$ plus the addition of the dangling R tuples padded with NULL values.


Left outer join: gives the result of $R \bowtie S$ plus the addition of the dangling S tuples padded with NULL values.


Syntax: A (FULL | RIGHT | LEFT) OUTER JOIN B ON p, where p is the predicate determining if the join should occur.


Inserting values: 

INSERT INTO table VALUES [value to be inserted]

INSERT INTO table [result of a subquery]

Delete values:

DELETE FROM table: removes everything in the table

DELETE FROM table [condition]: removes items from the table which satisfy the condition

Updating values:

The values must already exist in the table.

UPDATE table_name SET new_value_assignments [WHERE condition]: performs the new value assignments to the given table 
if the condition is true.


Creating tables:

CREATE TABLE table_name (
attribute declarations
)

For attribute declarations, the format is name type constraint


Constraints:

Help assure certain qualities about your data and helps the DBMS optimize.

NOT NULL: attribute can not be NULL

PRIMARY KEY: attribute is primary key (a primary key can never be NULL). At most one primary key per table.

UNIQUE: attribute is unique among all other instances of the relation. Can have any amount of unique keys in a table. 

To form a primary key with multiple attributes, you must put into the table creation PRIMARY KEY(attribute list)

Referenced keys in a table must refer to a primary key.

Referencing a foreign key:

Name type constraint REFERENCES table(attributes) or FOREIGN KEY (attributes) REFERENCES table(attributes) (second form mustbe below the other attribute declarations)

Maintaining referential integrity:

If table A has a foreign key in table B, then if 
we add or update a tuple in A such that the foreign key does not point to 
a value existing in B, the DBMS will reject that.

If we delete or update a tuple in B, then there are three options:

1. The tuple in A that depended on the value in B is deleted
2. The tuple in A that depended on the value in B is updated to match the deleted/updated tuple in B (if v is deleted in B, then t in A is deleted. If v is updated, then t is updated)
3. The tuple in A has the value that refers to a tuple in B to NULL regardless if the tuple in B was updated/deleted

Syntax: attr_a references table(attr_b) [on update set (null | cascade)] [on delete set (null | cascade)]

Defering checks:

If you can defer a check till before a transaction completes, you can avoid violating certain properties in the 
tables, ie foreign keys.

Initially defered: checking only occurs before each transaction commits.

Initially immediate: check will be made after each statement.

Assertions:

Conditions on a table that are always checked to make sure they hold.

Syntax: CREATE ASSERTION name CHECK condition

Checks:

Make sure that an attribute mantains a certain property

Syntax for in a table declaration: name type [constraints,] CHECK condition

A check in a table about a foreign key does not monitor the changes to the table from where the key is referenced from

Modifying the table: 

Add or drop column: ALTER TABLE name (ADD | DROP) COLUMN column_name 

Rename column: ALTER TABLE name RENAME COLUMN old_name TO new_name

Modify datatype: ALTER TABLE name ALTER COLUMN column_name type

Add constraint: ALTER TABLE name ADD CONSTRAINT name constraint

Remove constraint: ALTER TABLE name DROP CONSTRAINT name



