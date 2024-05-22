-- create user user_0d_1 and password set
-- should have all privileges
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
GRANT ALL PRIVILEGES ON hbtn_0d_2.* TO 'user_0d_1'@'localhost';
