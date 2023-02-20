# БАЗЫ ДАННЫХ
'''
1) Установка MYSQL
Качаем тут - https://dev.mysql.com/downloads/
Инструкция
https://dev.mysql.com/doc/refman/8.0/en/macos-installation-notes.html

2) Установка - mysql-connector-python


--- КОД SQL ---

-- Создаем БД
CREATE DATABASE vsearchlogDB;
USE vsearchlogDB;

DROP TABLE IF EXISTS vsearchlogDB;


-- Создаем пользователя, чтобы работать не по root
CREATE USER 'vsearch'@'localhost' IDENTIFIED BY 'vsearchpwd';

GRANT ALL PRIVILEGES ON vsearchlogDB.* TO 'vsearch'@'localhost';

-- Удалить пользователя
DROP USER 'vsearch'@'localhost';

-- Создадим таблицу
CREATE TABLE log (
	id int auto_increment primary key,
	ts timestamp default current_timestamp,
	phrase varchar(128) not null,
	letters varchar(32) not null,
	ip varchar(16) not null,
	browser_string varchar(256) not null,
	results varchar(64) not null
);

DESCRIBE log;

'''

# DB-API - помогает подключаться к БД из кода Python
import mysql.connector

# Создаем словар, в котором перечисляем ключи необходимые для соединения с БД
dbconfig = {
    'host': '127.0.0.1',
    'user': 'vsearch',
    'password': 'vsearchpwd',
    'database': 'vsearchlogDB',
}

# Подключаемся к серверу БД с помощью Функции connect()
conn = mysql.connector.connect(**dbconfig)
