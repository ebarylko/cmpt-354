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
db.restaurants.find({borough: {$in: ["Bronx", "Brooklyn", "Queens", "Staten Island"]}}, {name: 1, borough: 1, cuisine: 1, restaurant_id: 1, _id: 0})

19. Write a MongoDB query to find the restaurant Id, name, borough and cuisine for those restaurants which are not belonging to the borough Staten Island or Queens or Bronxor Brooklyn.
db.restaurants.find({borough: {$nin: ["Bronx", "Brooklyn", "Queens", "Staten Island"]}}, {name: 1, borough: 1, cuisine: 1, restaurant_id: 1, _id: 0})

22. Write a MongoDB query to find the restaurant Id, name, and grades for those restaurants which achieved a grade of "A" and scored 11 on an ISODate "2014-08-11T00:00:00Z" among many of survey dates.. 
db.restaurants.find({grades: {$elemMatch: {date: ISODate("2014-08-11T00:00:00Z"), grade: "A", score: 11}}}, {restaurant_id : 1,name: 1, grades: 1, _id: 0})

23. Write a MongoDB query to find the restaurant Id, name and grades for those restaurants where the 2nd element of grades array contains a grade of "A" and score 9 on an ISODate "2014-08-11T00:00:00Z"
db.restaurants.find({"grades.1": {grade: "A", score: 9, date: ISODate("2014-08-11T00:00:00Z")}})
db.restaurants.find({"grades.1.grade": "A", "grades.1.score": 9, "grades.1.date": ISODate("2014-08-11T00:00:00Z")}, {restaurant_id: 1, name: 1, grades: 1, _id: 0})
db.restaurants.find({}, {"grade": "$grades.1"})

24. Write a MongoDB query to find the restaurant Id, name, address and geographical location for those restaurants where 2nd element of coord array contains a value which is more than 42 and upto 52.. 
db.restaurants.find({"address.coord.1": {$gt: 42 ,$lte: 52}}, {restaurant_id: 1, name: 1, address: 1, _id: 0})

48. Write a MongoDB query to find the restaurants that have all grades with a score greater than 5. 
db.restaurants.find({"grades": {$not: {$elemMatch: {score: {$lte: 5}}}}})

51.Write a MongoDB query to find the average score for each restaurant. 
db.restaurants.aggregate({$sort: {name: 1}}, {$project: {name: 1, avg_score: {$avg: "$grades.score"}, _id: 0}})
Preguntar el profesor si lo que hiciste esta bien. Tambien preguntarle porque estas recibiendo dos copias del mismo score para un restaurante.
db.restaurants.aggregate([{
    $unwind: "$grades"
  },
  {
    $group: {
      _id: "$name",
      avgScore: {
        $avg: "$grades.score"
      }
    }
  },
{$project: {name: "$_id", avg_score: "$avgScore", _id: 0}},
{$sort: {name: 1}}
]).toArray()
52.Write a MongoDB query to find the highest score for each restaurant. 
db.restaurants