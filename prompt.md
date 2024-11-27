**Task:**
Develop an application in python that generates ER (Entity-Relationship) diagrams using Peter Chen's notation from a code-based description. The application should allow users to visually manipulate the entities and relationships within a graphical interface. Additionally, the application should save the coordinates of the entities and relationships to a separate file for future reference.
**Requirements:**
1. **Entities:**
   - Represented as rectangular tables with attributes.
   - Primary keys are underlined.
   - Example:
     ```markdown
     | Man        |
     | ---------- |
     | <u>id</u>  |
     | first_name |
     | last_name  |
     | email      |
     | phone      |
     ```
   - Examples of entities: Student, Teacher, Course.
   - Examples of attributes: Student Name, Enrollment Number, Course Title.
2. **Relationships:**
   - Represented as ovals connecting two or more entities.
   - Relationships can have attributes similar to entities.
   - Examples of relationships: Student studies Course, Teacher teaches Course.
   - Examples of relationship attributes: Student's grade in the Course.
3. **Cardinality:**
   - Indicates the number of instances of one entity that can be related to instances of another entity.
   - Types of cardinality:
     - One-to-One (1:1)
     - One-to-Many (1:N)
     - Many-to-Many (N:M)
   - Cardinality is represented by two numbers: the minimum and maximum number of relationships.
   - Example:
     ```
     Subject --[1,1]-- (define) --[0,N]-- Variant
     ```
     - A Subject can have between 0 and N Variants.
     - A Variant must be associated with exactly one Subject.
4. **Example of code description:**
```
#Entity(Entity1_name) 
{
    attr1_name
    attr2_name
}
#Entity(Entity2_name) 
{
    attr1_name
}
#Relation(Relation1_name) 
{
    Entity1_name
    Entity2_name
    [1,1]
    [0,N]
}
```

   