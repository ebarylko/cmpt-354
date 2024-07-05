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







