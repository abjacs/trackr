CREATE TABLE users (userkey integer NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,username varchar UNIQUE)

CREATE TABLE tracks (trackkey integer NOT NULL PRIMARY KEY AUTOINCREMENT,mac varchar NOT NULL,userkey integer NOT NULL)
