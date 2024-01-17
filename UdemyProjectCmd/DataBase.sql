CREATE DATABASE IF NOT EXISTS udemyCmd;
USE udemyCmd;

CREATE TABLE IF NOT EXISTS users(
    ID        int(20) auto_increment not null,
    names     varchar(100),
    lastName  varchar(100),
    mail      varchar(100) not null,
    password  varchar(100) not null,
    date      date not null,
    CONSTRAINT pk_users PRIMARY KEY(ID),
    CONSTRAINT pk_mail UNIQUE(mail)
) ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS notes(
    ID           int(20) auto_increment not null,
    user_id      int(25) not null,
    Title        varchar(255) not null,
    Descriptions MEDIUMTEXT,
    date         date not null,
    CONSTRAINT pk_notes PRIMARY KEY(ID),
    CONSTRAINT fk_note_user FOREIGN KEY(user_id) REFERENCES users(ID)
) ENGINE = InnoDB;
