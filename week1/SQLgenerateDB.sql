CREATE DATABASE IF NOT EXISTS project_mysticquest;
CREATE TABLE IF NOT EXISTS dialogue (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    npc_id INT REFERENCES npc(id) ,
    player_id INT REFERENCES player(id),
    text VARCHAR(255)
);


CREATE TABLE IF NOT EXISTS guild (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) UNIQUE ,
    leader_id INT UNIQUE REFERENCES player(id),
    founded_date DATETIME,
    members INT
);


CREATE TABLE IF NOT EXISTS player (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    class_name VARCHAR(255),
    guild_id INT REFERENCES guild(id),
    item_id INT,
    last_login DATETIME,
    kingdom_id INT REFERENCES kingdom(id),
    experience INT,
    health INT,
    level INT,
    gold INT,
    CONSTRAINT uq_first_name_last_name UNIQUE (first_name, last_name)
    
);


CREATE TABLE IF NOT EXISTS item (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) UNIQUE,
    description VARCHAR(255),
    price INT,
    required_level INT
);


CREATE TABLE IF NOT EXISTS enemy (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) UNIQUE,
    type VARCHAR(255),
    level INT,
    health INT,
    attack INT,
    defense INT,
    drop_items INT REFERENCES item(id)
);


CREATE TABLE IF NOT EXISTS team (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) UNIQUE,
    leader_id INT REFERENCES player(id),
    member_count INT,
    kingdom_id INT REFERENCES kingdom(id)
);

CREATE TABLE IF NOT EXISTS event (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255),
    event_date DATETIME
);

CREATE TABLE IF NOT EXISTS npc (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255),
    type VARCHAR(255),
    location VARCHAR(255),
    dialogue_id INT REFERENCES dialogue(id),
    quest_id INT REFERENCES quest(id)
);


CREATE TABLE IF NOT EXISTS kingdom (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255)  UNIQUE ,
    ruler_id INT REFERENCES ruler(id),
    population INT
);
CREATE TABLE IF NOT EXISTS ruler (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255),
    kingdom_id INT REFERENCES kingdom(id)
);


CREATE TABLE IF NOT EXISTS combat (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    player_id INT REFERENCES player(id),
    enemy_id INT REFERENCES enemy(id),
    turns INT,
    winner_id INT
);

CREATE TABLE IF NOT EXISTS transaction (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    sender_id INT,
    receiver_id INT,
    item_id INT,
    amount INT,
    kingdom_id INT,
    timestamp DATETIME 
);

CREATE TABLE IF NOT EXISTS quest (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255),
    reward INT,
    player_id INT REFERENCES player(id),
    difficulty INT ,
    completition_time INT
);



CREATE TABLE IF NOT EXISTS groupchat (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255)
);


CREATE TABLE IF NOT EXISTS chat (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    sender_id 	INT,
    name VARCHAR(255),
    message VARCHAR(255)
);





