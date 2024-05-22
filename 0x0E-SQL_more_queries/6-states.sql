-- creates the database hbtn_0d_usa and the table states
CREATE DATABASE IF NOT EXISTS hbtn_0d_usai;
CREATE TABLE IF NOT EXISTS states(
   id INT NOT NULL PRIMARY KEY(AUTO),
   name VARCHAR(256)
   );
