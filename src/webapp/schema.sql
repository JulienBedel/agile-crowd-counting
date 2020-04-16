DROP TABLE IF EXISTS points;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS images;

CREATE TABLE users (
	id INTEGER,
	username VARCHAR(255) NOT NULL UNIQUE,
    PRIMARY KEY (id)
);

CREATE TABLE images (
    id INTEGER,
    path VARCHAR(255) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE points (
	id INTEGER,
    x_coord INT NOT NULL,
    y_coord INT NOT NULL,
    user_id INT NOT NULL,
    image_id INT NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (image_id) REFERENCES images(id)
);