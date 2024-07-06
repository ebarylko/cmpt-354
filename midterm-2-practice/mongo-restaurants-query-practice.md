https://www.w3resource.com/mongodb-exercises/

1. 
db.restaurants.find()



2.
db.restaurants.find({}, {restaurant_id: 1, name: 1, borough: 1, cuisine: 1, _id: 0})

4.   
db.restaurants.find({}, {restaurant_id: 1, name: 1, borough: 1, zip_code: "$address.zipcode", _id: 0})

5. 
db.restaurants.find({borough: "Bronx"})


6      
db.restaurants.find({borough: "Bronx"}).limit(5)

7
db.restaurants.find({borough: "Bronx"}).skip(5).limit(5)

8
db.restaurants.find({"grades.score": {$gt: 90}})

9 
db.restaurants.find({$and: [{"grades.score": {$gt: 80}}, {"grades.score": {$lt: 100}}]})

10. Write a MongoDB query to find the restaurants which locate in latitude value less than -95.754168.
db.restaurants.find({"address.coord.0": {$lt: -95.754168}})

11. Write a MongoDB query to find the restaurants that do not prepare any cuisine of 'American' and their grade score more than 70 and latitude less than -65.754168. 
db.restaurants.find({$and: [{"address.coord.0": {$lt: -65.754168}}, {cuisine: {$ne: "American "}}, {"grades.score": {$gt: 70}}]})

12. Write a MongoDB query to find the restaurants which do not prepare any cuisine of 'American' and achieved a score more than 70 and located in the longitude less than -65.754168.
Note : Do this query without using $and operator. 
db.restaurants.find({ "cuisine" : {$ne : "American "},
                     "grades.score" :{$gt: 70},
                     "address.coord" : {$lt : -65.754168}
                    }
                     )

13. Write a MongoDB query to find the restaurants which do not prepare any cuisine of 'American' and achieved a grade point 'A' not belongs to the borough Brooklyn. The document must be displayed according to the cuisine in descending order. 
db.restaurants.find({cuisine : {$ne : "American "}, 
                    "grades.grade": "A",
                     borough: {$ne: "Brooklyn"}}).sort({cuisine: -1})

14. Write a MongoDB query to find the restaurant Id, name, borough and cuisine for those restaurants which contain 'Wil' as first three letters for its name. 
db.restaurants.find({name: /^Wil.*/}, 
                    {restaurant_id: 1, name: 1, borough: 1, cuisine: 1, _id: 0})

15. Write a MongoDB query to find the restaurant Id, name, borough and cuisine for those restaurants which contain 'ces' as last three letters for its name. 
db.restaurants.find({name: /ces$/},
{restaurant_id: 1, name: 1, borough: 1, cuisine: 1, _id: 0})

17. Write a MongoDB query to find the restaurants which belong to the borough Bronx and prepared either American or Chinese dish. 
db.restaurants.find({borough: "Bronx", cuisine: {$in: ["American ", "Chinese"]}})

18. Write a MongoDB query to find the restaurant Id, name, borough and cuisine for those restaurants which belong to the borough Staten Island or Queens or Bronxor Brooklyn.  
