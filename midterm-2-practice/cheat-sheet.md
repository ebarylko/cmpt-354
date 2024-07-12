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
this transaction began. Cannot read uncommitted data from other transactions. Lock ranges to
prevent insertions.

Read-uncommitted: the transaction can read data from other transactions which have not been 
committed. Short-duration lock: lock, access, and release immediately


Read-committed: the transaction can only read data that has been committed by other transactions.
This does not prevent it from obtaining different results from the same query if the 
query is accessing data which has been committed. Long duration write locks: do not release 
write locks until commit

Repeatable-read: the transaction will see the same data along with potentially more data 
it had when running the first query on subsequent queries. Long duration locks on all 
data items accessed.


## Structured vs unstructured data

Relational databases require a schema, which mean all rows must conform to it. Adding or 
removing an attribute requires the entire schema to be modified.

Unstructured data has no schema, which means you can add what you like. However, there are 
no guarantees about what the types of what you are working with.

Semi-structured data is self describing and allows the structure of the data to be updated easily.

HTML mixes content and presentation, while XML solely describes the content.

With XML, you can describe any structure and can ship it across different platforms. 

## XML

You have opening and closing tags. Ex: `<book> </book>`.

Empty elements have the structure of `<elment/>`.

Elements have attributes. Ex: `<element> a="1" b="2" </element>`.

Nested structures permit arbitrary graphs.

Ordering is forced by document format.

### Well formed XML requirements

Follows lexical conventions by using `&lt` instead of `<`, `&gt` instead of `>`, and `&amp` instead of `&`.

Contains a single root element.

Has properly matched tags and nested elements.

### Additional features

Ids must start with a non-digit. Ex: `<person id='o11'> <name> John </name>  </person>`

Namespaces allow you to use items stemming from different locations. Ex: `<v1:product xmlns:v1="[link to schema]"> [more content within] </v1:product>`

An XML document can have a DTD (Document Type Definition) which defines how the structure
of the data will be. It also restricts the values present in the tags.

### DTD

#PCDATA: means that the element has a value which is text and no other elements are nested 
within.
Ex: `<!ELEMENT name (#PCDATA)`> means that within `<name>` and `</name>`, text will appear.

`<ATLIST! element-name attribute-name type (#REQUIRED | #IMPLIED)>`: means that the attribute is an element of 
`element-name` and has type `type`

Potential types:

CDATA: character string data, like #PCDATA.

#REQUIRED: the attribute must be present

#IMPLIED: the attribute may not be present

Examples:

`<!ELEMENT section (title, content?, section*)>`: A section has a title, optional content, and 
0 or more sections.

The benefits of a DTD is that you know the structure of the data and it helps with processing.
Makes the transfer of XML easier if everyone uses the same DTD.

The benefits to avoiding a DTD is that you have no limits on your structure and avoid the 
overhead of validation.


## XPATH

Takes an expression and evaluates it going through the tree of the document.

Commands:

/: separating steps between paths

name: matches any child element with name `name`

*: matches any child element

@name: matches any attribute with `name`

@*: matches any attribute

//: matches any descendent element or the current element

.: matches the current element

..: Matches the parent element

Ex: /bibliography/books will get all the books. /bibliography/* will get all articles used 
in the book. 

`[condition]`: matches the current element if condition evaluates to true on the current element.

Ex: /bibliography/book[author='a'] will get books where one of the authors was 'a'

You can use predicates `and`, `or`, and `not`

Remember, you are searching for the documents where one of the elements matches the condition,
not all of them.

If a book had multiple prices, checking for a price within a certain ranges requires 
/bibliography/book[price[. >= x and . <= y]]

### Operators

`contains(x, y)`: true if string x contains y.

`count(x)`: returns how many nodes are in x.

`position()`: returns the position of the current node being looked at.

The positions are one based.

`last()`: returns the position of the last element in the node set

`name()`: returns the name tag of the current node

## JSON

Has arrays and objects, which are key value pairs with the keys being strings.

Simple types: numbers, strings, true, false, null

Thing: simple value/array/object

## MongoDB

Database = a number of “collections”
• Collection = a list of “documents”
• Document = a JSON object
• Must have an _id attribute whose value can uniquely identify a document
within the collection

Queries must be of the form db.collection.other-operations

### Operations

find({values to filter by}, {values to project}).

Remember, find cannot be used in an aggregation pipeline. Also, you must have {_id: 0} if you 
want to get rid of _id.

If passing nothing to find, returns all values.

Regex can be used as {field: /expression/}.

sort: takes key-val pairs of attribute to sort by and whether it should be in ascending order (1) or
descending order (-1)

Greater than = gt, less than = lt, 

and: takes a vector where each element is another predicate to satisfy.

Ex: get books with price in between 70 and 100 dollars.
db.bib.find({$and: [{price: {$lt: 100}}, {price: {$gt 70}}])

Note: if you try to match a field with an object, what will be checked is that the field
has the exact same structure as the object you passed.

unwind: takes a collection and expands the collection so that if you have 
{a: 1, b: [1, 2]}, {$unwind: b} will return {a: 1, b: 1}, {a: 1, b: 2}. 

Group:
{$group: {_id: {all the things you want to group by}, other fields to generate}}

In and nin:
{x: {$in: [1, 2, 3]}}. Checks for x values that fall within 1, 2, 3.

elemMatch:
{arr: {$elemMatch: {key-val pairs of conditions which must be satisfied}

Ex:
db.restaurants.find({grades: {$elemMatch: {date: ISODate("2014-08-11T00:00:00Z"), grade: "A", score: 11}}}, {restaurant_id : 1,name: 1, grades: 1, _id: 0})
