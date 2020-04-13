-- gets all the images ids and paths
SELECT IdImage,Path FROM Images

-- counts the number of points of each user
SELECT Username,COUNT(idPoint) FROM Users,Points
WHERE Users.IdUser=Points.IdUser
GROUP BY Users.IdUser
ORDER BY COUNT(idPoint) desc

-- counts the number of points of each user for image 1
SELECT Username,COUNT(idPoint) FROM Users,Points
WHERE Users.IdUser=Points.IdUser
AND Points.IdImage=1
GROUP BY Users.IdUser
ORDER BY COUNT(idPoint) desc



