CREATE DATABASE IF NOT EXISTS cine_db;

USE cine_db;

CREATE TABLE IF NOT EXISTS admins(
	ID_admin INT NOT NULL AUTO_INCREMENT,
    a_nombre VARCHAR(45) NOT NULL,
    a_appat VARCHAR(45) NOT NULL,
    a_apmat VARCHAR(45),
    a_usuario VARCHAR(45) NOT NULL,
    a_email VARCHAR(45) NOT NULL,
    a_password VARCHAR(16) NOT NULL,
    UNIQUE(a_usuario),
    PRIMARY KEY(ID_admin)
)ENGINE = INNODB;


CREATE TABLE IF NOT EXISTS movies(
	ID_movie INT NOT NULL AUTO_INCREMENT,
    m_titulo VARCHAR(45) NOT NULL,
    m_genero VARCHAR(45) NOT NULL,
    m_clasificacion VARCHAR(4) NOT NULL,
    m_director VARCHAR(45) NOT NULL,
    m_actores VARCHAR(280) NOT NULL,
    m_synopsis VARCHAR(350) NOT NULL,
    m_fecha DATE NOT NULL,
    m_idioma VARCHAR(25) NOT NULL,
    m_subtitulos VARCHAR(25),
    m_formato ENUM('2D', '3D') NOT NULL,
    UNIQUE(m_titulo, m_idioma, m_formato),
    PRIMARY KEY(ID_movie)
)ENGINE = INNODB;




CREATE TABLE IF NOT EXISTS halls(
	ID_hall INT NOT NULL,
    h_no_asiento INT NOT NULL,
    h_formato ENUM('Tradicional','Premium','VIP') NOT NULL,
    h_precio FLOAT NOT NULL,
    PRIMARY KEY(ID_hall)
)ENGINE = INNODB;



CREATE TABLE IF NOT EXISTS schedule_cinema(
	ID_schedule INT NOT NULL AUTO_INCREMENT,
    sc_pelicula INT NOT NULL,
    sc_sala INT NOT NULL,
    sc_hora TIME NOT NULL,
    UNIQUE(sc_sala, sc_hora),
    PRIMARY KEY(ID_schedule),
    CONSTRAINT fkHall_Schcin FOREIGN KEY(sc_sala)
		REFERENCES  halls(ID_hall)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    CONSTRAINT fkIDMovie_Schcin FOREIGN KEY(sc_pelicula)
		REFERENCES movies(ID_movie)
        ON DELETE CASCADE
        ON UPDATE CASCADE
)ENGINE = INNODB;

INSERT INTO schedule_cinema  VALUES ('12', 'Star Wars 3', '4111', '10:10');
INSERT INTO schedule_cinema  VALUES ('123', 'john wick 3', '4112', '11:10');
INSERT INTO schedule_cinema  VALUES ('1', 'Avengers 3', '5113', '12:10');


CREATE TABLE IF NOT EXISTS seat(
	ID_seat VARCHAR(3) NOT NULL,
    s_sala INT NOT NULL,
    PRIMARY KEY(ID_Seat, s_sala),
    CONSTRAINT fkHall_Seat FOREIGN KEY(s_sala)
		REFERENCES halls(ID_hall)
        ON DELETE CASCADE
        ON UPDATE CASCADE
)ENGINE = INNODB;

CREATE TABLE IF NOT EXISTS ticket(
	ID_ticket INT NOT NULL AUTO_INCREMENT,
    t_fecha DATE NOT NULL,
    t_calendario INT NOT NULL,
    t_asiento VARCHAR(3) NOT NULL,
    PRIMARY KEY(ID_ticket),
    CONSTRAINT fkIDSch_ticket FOREIGN KEY(t_calendario)
		REFERENCES schedule_cinema(ID_schedule)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
	CONSTRAINT fkSeat_ticket FOREIGN KEY(t_asiento)
		REFERENCES seat(ID_seat)
        ON DELETE CASCADE
        ON UPDATE CASCADE
)ENGINE = INNODB;
