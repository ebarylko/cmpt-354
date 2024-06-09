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

Selection: $\sigma_{p}R$, where p is the condition for keeping a row, R is the relation

Projection: $\pi_{a}R$, where a is the set of attributes to access, R is the relation

Remember: you can use boolean operators ($\land, \lor$)

