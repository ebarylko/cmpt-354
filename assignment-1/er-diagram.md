```mermaid
classDiagram

   class People {
        name
        id: Key
        phone
    }
    class Students {
        year-entered
        favorite-classes
    }
   
    class Teachers {
       
    }
    
   
    People <|-- Students
    People <|-- Teachers
    
    class Courses {
        name: Key
    }

    class Departments {
        name: Key

    }

    class Offerings {
        <<weak_entity>>
        year: Key
    }

    class Clubs {
        <<weak_entity>>
        name: Key
    }

    Courses "1" -- "0..1" Offerings
    Teachers "1"-- "*" Offerings
     Departments "1" *-- "*" Courses: Offers

     Students "*"  -- "*" Offerings: Studies

     Students "*" -- "*" Courses: Favorite classes

     Departments "1..*" -- "*" Students: Belongs to

     Departments "1..*" -- "*" Teachers: Belongs to

     Departments "0..1" -- "1" Teachers: Head

     Clubs "*" -- "1" Departments: Belongs to

     Clubs "*" -- "*" Students: Member
 ```