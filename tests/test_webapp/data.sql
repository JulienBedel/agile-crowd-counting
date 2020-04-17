-- creating 3 images, third left with no record
INSERT INTO images(path) VALUES ('/web-data/images/image1.png');
INSERT INTO images(path) VALUES ('/web-data/images/image2.png');
INSERT INTO images(path) VALUES ('/web-data/images/image3.png');

-- creating 3 users
INSERT INTO users(username) VALUES ('user1');
INSERT INTO users(username) VALUES ('user2');
INSERT INTO users(username) VALUES ('user3');

-- user 1 focuses on the first image
INSERT INTO points(x_coord, y_coord, user_id, image_id) VALUES (49, 18, 1, 1);
INSERT INTO points(x_coord, y_coord, user_id, image_id) VALUES (64, 52, 1, 1);
INSERT INTO points(x_coord, y_coord, user_id, image_id) VALUES (47, 42, 1, 1);
INSERT INTO points(x_coord, y_coord, user_id, image_id) VALUES (12, 14, 1, 1);
INSERT INTO points(x_coord, y_coord, user_id, image_id) VALUES (78, 54, 1, 2);

-- user 2 focuses on the second image
INSERT INTO points(x_coord, y_coord, user_id, image_id) VALUES (49, 18, 2, 2);
INSERT INTO points(x_coord, y_coord, user_id, image_id) VALUES (64, 52, 2, 2);
INSERT INTO points(x_coord, y_coord, user_id, image_id) VALUES (47, 42, 2, 2);
INSERT INTO points(x_coord, y_coord, user_id, image_id) VALUES (12, 14, 2, 2);
INSERT INTO points(x_coord, y_coord, user_id, image_id) VALUES (78, 54, 2, 2);
INSERT INTO points(x_coord, y_coord, user_id, image_id) VALUES (14, 26, 2, 1);

-- user 3 does a bit of each image
INSERT INTO points(x_coord, y_coord, user_id, image_id) VALUES (49, 18, 3, 2);
INSERT INTO points(x_coord, y_coord, user_id, image_id) VALUES (64, 52, 3, 2);
INSERT INTO points(x_coord, y_coord, user_id, image_id) VALUES (12, 14, 3, 1);
INSERT INTO points(x_coord, y_coord, user_id, image_id) VALUES (14, 26, 3, 1);