## Triggers

It is a form of rejecting certain events occurring if a specific 
condition occurs.

Statement level triggers activate regardless of how many rows were impacted.
Row level triggers fire if one or more rows have been impacted.

Statement level triggers are needed for taking action with regard to the 
overall state of the table. Row level triggers only view the updated/deleted
rows one at a time.

Syntax: 

CREATE TRIGGER name 

(BEFORE | AFTER | INSTEAD OF) (DELETE | INSERT | UPDATE event) ON table

For row-level triggers:

REFERENCING (NEW | OLD) ROW AS name

FOR EACH ROW

WHEN condition

action

For statement-level triggers:

Referencing (NEW | OLD) TABLE as name

FOR EACH STATEMENT 

action




INSERT: can only use the new row or table

DELETE: can only use old row or table

UPDATE: can use old and new row. Ask professor about this


## Views

Views are used to generate meaningful data representing what is being 
worked with in the domain. They provide logical data independence
since the underlying schema can be changed without affecting the view.

Syntax to create a view: 

CREATE VIEW AS name 

Query to generate the table

Syntax to drop a view:

DROP VIEW name

Updatable views are those with no joins, aggregations, or subqueries

### Triggers which work on views

Syntax: 

CREATE TRIGGER name

INSTEAD OF UPDATE ON table_name

referencing [content]

FOR EACH (ROW | STATEMENT)

action

## SQL programming

SQL does give access to high level operations, but it lacks the power 
contained in a programming language. Some potential solutions are 
to add features of a programming language to SQL or to use SQL and 
a programming language in tandem.

Impedance mismatch: 

SQL works on sets of items, but programming languages work on single items in 
a list. The solution for this is to define a construct called a cursor.
The cursor will iterate over the results of a query, allowing the 
interaction between SQL and programming languages.

SQL injection:

Passing in strings which contain valid SQL statements which are meant 
to have an adverse effect.

