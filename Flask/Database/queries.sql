---- 1. INSTALL EXTENSIONS
---- 2. CREATING STUDENT TABLE

--CREATE TABLE Students(id INTEGER PRIMARY KEY AUTOINCREMENT,
--                    firstname TEXT NOT NULL,
--                    lastname TEXT NOT NULL,
--                    dob TEXT NOT NULL);

---- 3. CREATE MARKS TABLE

--CREATE TABLE Marks(id INTEGER PRIMARY KEY AUTOINCREMENT,
--                    student_id INTEGER,
--                    subject TEXT NOT NULL,
--                    mark INTEGER);

---- 4. INSERT STUDENTS

--INSERT INTO Students(firstname, lastname, dob)
--            VALUES('Lachlan', 'Snake', '26/09/2007')

--INSERT INTO Students(firstname, lastname, dob) VALUES
--                    ('Bobby', 'Bob', '3/01/2008'),
--                    ('Bjorn', 'Johnson', '28/02/2007');

--INSERT INTO Students(firstname, lastname, dob) VALUES
--                    ('Tabitha', 'Michael', '23/10/2007'),
--                    ('Bart', 'Simpson', '25/11/2007'),
--                    ('Jennifer', 'Rose', '14/09/2007'),
--                    ('Lequisha', 'Dequavious', '11/10/2007'),
--                    ('Jill', 'Bloodborne', '28/03/2007');

-- INSERT INTO Marks(id, student_id, subject, mark) VALUES
--                    (1, 1, 'English', 50),
--                    (2, 2, 'Maths', 100),
--                    (3, 3, 'English', 67),
--                    (4, 4, 'Science', 80),
--                    (5, 5, 'English', 24),
--                    (6, 6, 'English', 97),
--                    (7, 7, 'Maths', 82),
--                    (8, 8, 'Science', 5);

---- 5. FETCHING STUDENTS

--SELECT * FROM Students;

--SELECT firstname, lastname FROM Students;

--SELECT * FROM Students LIMIT 5;

--SELECT firstname, dob FROM Students
--    WHERE firstname LIKE 'B%';

--SELECT lastname, dob FROM Students;

--SELECT firstname, lastname FROM Students
--    ORDER BY lastname ASC;

--SELECT firstname, lastname, dob FROM Students
--    WHERE dob LIKE '%2007%';

--SELECT mark FROM Marks;

--SELECT mark FROM Marks
--    WHERE subject = 'English';

--SELECT subject, mark FROM Marks
--    WHERE mark < 50;

--SELECT subject, mark FROM Marks
--    WHERE mark >= 50;

---- 6. UPDATING DATA

--UPDATE Students
--    SET firstname = 'Nick'
--    WHERE id = 2;

--UPDATE Marks
--    SET subject = 'Maths Advanced'
--    WHERE subject = 'Maths';

--UPDATE Students
--    SET lastname = 'Simpson'
--    WHERE firstname = 'Jill';

--UPDATE Marks
--    SET subject = 'English Advanced'
--    WHERE subject = 'English';

--UPDATE Marks
--    SET mark = 150
--    WHERE subject = 'Science';

---- 7. DELETEING DATA

--DELETE FROM Students
--    WHERE id = 2;

--INSERT INTO Students(firstname, lastname, dob)
--    VALUES ('Bobby', 'Bob', '3/1/2008');

--DELETE FROM Marks
--    WHERE mark < 25;

--DELETE FROM Students
--    WHERE lastname = 'Simpson';

--DELETE FROM Marks
--    WHERE mark > 100;

---- 8. GROUPING DATA

--SELECT COUNT(id), firstname
--    FROM Students
--    GROUP BY firstname;

--SELECT SUM(mark), subject
--    FROM Marks
--    GROUP BY subject;

--SELECT AVG(mark), subject
--    FROM Marks
--    GROUP BY subject;

--SELECT COUNT(id), lastname
--    FROM Students
--    GROUP BY lastname;

--SELECT MAX(mark), subject
--    FROM Marks
--    GROUP BY Subject;

--SELECT COUNT(mark), subject
--    FROM Marks
--    GROUP BY Subject;

---- 9. JOIN STUDENTS

--SELECT Students.firstname, Students.lastname,
--        Marks.subject, Marks.mark
--FROM Students JOIN Marks
--ON Students.id=Marks.student_id;

--INSERT INTO Marks(student_id, mark, subject) VALUES
--    (1, 100, 'Science'),
--    (2, 100, 'Science'),
--    (3, 100, 'Science'),
--    (4, 100, 'Science'),
--    (5, 100, 'Science'),
--    (6, 100, 'Science'),
--    (7, 100, 'Science');

--SELECT *
--FROM Students JOIN Marks
--ON Students.id=Marks.student_id;

--SELECT *
--FROM Students JOIN Marks
--ON Students.id=Marks.student_id
--WHERE mark >= 50;

SELECT Students.firstname, Students.lastname, Marks.subject, Marks.mark
FROM Students JOIN Marks
ON Students.id=Marks.student_id
WHERE subject = 'English Advanced';






