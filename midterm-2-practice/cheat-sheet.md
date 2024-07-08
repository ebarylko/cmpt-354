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


## Two tier architecture

Client/server architecture. Server implements the business logic and 
data management.

Separate presentation from obtaining the data.

## Three tier architecture

The three tiers are database, client, and server

The server layer handles requests to the database 

The database layer handles the data in one or more databases and processes the queries

The client server passes requests to the server layer and displays outputs to the user

## ACID

Atomicity: A transaction either completes or aborts

Consistency: All invariants must be satisfied before and after a transaction completes

Isolation: All transactions must run as if there were no other transactions occurring

Durability: If the database crashes after it makes a transaction, the effects of the 
transaction must be present when the database restores itself


## Transactions

COMMIT stores the transaction, ROLLBACK undoes the state of the database to before the transaction started.

Schema operations implicitly commit the current transaction

Atomicity is achieved using logging so steps which violate any constraint are noted and 
the database can move back to a previous state.

Transactions are done using a serializable schedule, which allows transactions to interleave 
and execute concurrently. However, the result must be the same as if the transactions were 
executed in serial order.

### Isolation levels

An isolation level only affect the data that the specific transaction sees. Just because 
one transaction is read committed, it does not mean any of the other transactions are 
read committed. 

Serializable: every transaction with this isolation can only read data that occurred before 
this transaction began. Cannot read uncommitted data from other transactions.

Read-uncommitted: the transaction can read data from other transactions which have not been 
committed. 

Read-committed: the transaction can only read data that has been committed by other transactions.
This does not prevent it from obtaining different results from the same query if the 
query is accessing data which has been committed. 

Repeatable-read: the transaction will see the same data along with potentially more data 
it had when running the first query on subsequent queries.

