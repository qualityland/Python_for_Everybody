INSERT INTO Users (name, email) VALUES ('Kristin', 'kf@umich.edu');
DELETE FROM Users WHERE email='ted@umich.edu';
UPDATE Users SET name='Charles' WHERE email='csev@umich.edu';
SELECT * FROM Users;
SELECT * FROM Users WHERE email='csev@umich.edu';
SELECT * FROM Users ORDER BY email;
