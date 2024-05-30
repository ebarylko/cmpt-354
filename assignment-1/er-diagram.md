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
    
    class Enrollments {
        <<weak_entity>>
            year: Key
    }

    Courses "1" -- "0..1" Offerings: Offered in
    Teachers "1"-- "*" Offerings: Teaches
    Departments "1" *-- "*" Courses: Offers
%%    Enrollments -- Offerings
        
    Enrollments "*" -- "1" Students: Registered in
    Enrollments "*" -- "1" Courses: Being offered
    
%%     Students "*"  -- "*" Offerings: Studies

    Students "*" -- "*" Courses: Favorite classes

    Departments "1..*" -- "*" Students: Belongs to

    Departments "1..*" -- "*" Teachers: Belongs to

    Departments "0..1" -- "1" Teachers: Head

    Clubs "*" -- "1" Departments: Belongs to

    Clubs "*" -- "*" Students: Member
 ```
Offerings depends on the year, course, and professor
Enrollments depends on the student, course, and year
Enrollments * - 1 Students
Enrollments * - 1 Course
Enrollments * - 1 Year