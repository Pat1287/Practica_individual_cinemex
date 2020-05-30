from mysql import connector

class Model:

    def __init__(self, config_db_file='config.txt'):
        self.config_db_file = config_db_file
        self.config_db = self.read_config_db()
        self.connect_to_db()

    def read_config_db(self):
        d = {}
        with open(self.config_db_file) as f_r:
            for line in f_r:
                (key, val) = line.strip().split(':')
                d[key] = val
        return d
    
    def connect_to_db(self):
        self.cnx = connector.connect(**self.config_db)
        self.cursor = self.cnx.cursor()
    
    def close_db(self):
        self.cnx.close()

    "Administrador"

    def create_admin(self, nombre, appat, apmat, usuario, email, password):
        try:
            sql = 'INSERT INTO admins (`a_nombre`, `a_appat`, `a_apmat`, `a_usuario`, `a_email`, `a_password`) VALUES (%s, %s, %s, %s, %s, %s)'
            vals = (nombre, appat, apmat, usuario, email, password)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_a_admin(self, ID_admin):
        try:
            sql = "SELECT * FROM admins WHERE ID_admin = %s"
            vals = (ID_admin,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_all_admins(self):
        try:
            sql = 'SELECT * FROM admins'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_username_password(self, usuario, password):
        try:
            sql = 'SELECT admins.a_usuario, admins.a_password FROM admins WHERE a_usuario = %s AND a_password = %s'
            vals = (usuario, password)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def update_admin(self, fields, vals):
        try:
            sql = 'UPDATE admins SET '+','.join(fields)+'WHERE ID_admin = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_admin(self, ID_admin):
        try:
            sql = 'DELETE FROM admins WHERE ID_admin = %s'
            vals = (ID_admin,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err

    "Peliculas"

    def create_movie(self, titulo, genero, clasificacion, director, actores, synopsis, fecha, idioma, subtitulos, m_formato):
        try:
            sql = 'INSERT INTO movies (`m_titulo`, `m_genero`, `m_clasificacion`, `m_director`, `m_actores`, `m_synopsis`, `m_fecha`, `m_idioma`, `m_subtitulos`, `m_formato`) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
            vals = (titulo, genero, clasificacion, director, actores, synopsis, fecha, idioma, subtitulos, m_formato)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_a_movie(self, titulo):
        try:
            sql = "SELECT * FROM movies WHERE m_titulo = %s"
            vals = (titulo,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_a_movie_id(self, ID_movie):
        try:
            sql = "SELECT * FROM movies WHERE ID_movie = %s"
            vals = (ID_movie,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_all_movies(self):
        try:
            sql = 'SELECT * FROM movies'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err
        
    def read_movies_language(self, idioma):
        try:
            sql = 'SELECT * FROM movies WHERE m_idioma = %s'
            vals = (idioma,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err
        
    def read_movies_format(self, formato):
        try:
            sql = 'SELECT * FROM movies WHERE m_formato = %s'
            vals = (formato,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_movies_hour(self, hour):
        try:
            sql = 'SELECT movies.m_titulo, movies.m_clasificacion, schedule_cinema.* FROM movies JOIN schedule_cinema ON movies.ID_movie = schedule_cinema.sc_movie AND schedule_cinema.sc_hora = %s'
            vals = (hour,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_movies_clasification(self, clasification):
        try:
            sql = 'SELECT * FROM movies WHERE m_clasification = %s'
            vals = (clasification,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def update_movie(self, fields, vals):
        try:
            sql = 'UPDATE movies SET '+','.join(fields)+'WHERE ID_movie = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_movie(self, ID_movie):
        try:
            sql = 'DELETE FROM movies WHERE ID_movie = %s'
            vals = (ID_movie,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err

    "schedule"

    def create_schedule(self, ID_movie, sala, hora):
        try:
            sql = 'INSERT INTO schedule_cinema (`sc_pelicula`, `sc_sala`, `sc_hora`) VALUES(%s, %s, %s)'
            vals = (ID_movie, sala, hora)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            return err
    
    def read_a_schedule(self, hora):
        try:
            sql = 'SELECT schedule_cinema.*, movies.m_titulo FROM schedule_cinema JOIN movies ON schedule_cinema.sc_pelicula = movies.ID_movie AND schedule_cinema.sc_hora = %s'
            vals = (hora,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_a_schedule_id(self, ID_schedule):
        try:
            sql = 'SELECT schedule_cinema.*, movies.m_titulo FROM schedule_cinema JOIN movies ON schedule_cinema.sc_pelicula = movies.ID_movie AND schedule_cinema.ID_schedule = %s'
            vals = (ID_schedule,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_all_schedules(self):
        try:
            sql = 'SELECT schedule_cinema.*, movies.m_titulo FROM schedule_cinema JOIN movies ON schedule_cinema.sc_pelicula = movies.ID_movie'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err
    
    def read_schedule_hall(self, sala):
        try:
            sql = 'SELECT schedule_cinema.*, movies.m_title FROM schedule_cinema JOIN movies ON schedule_cinema.sc_movie = movies.ID_movie JOIN halls ON schedule_cinema.sc_hall = halls.ID_hall AND schedule_cinema.sc_hall = %s'
            vals = (sala,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_schedule_movie(self, titulo):
        try:
            sql = 'SELECT schedule_cinema.*, movies.m_title FROM schedule_cinema JOIN movies ON schedule_cinema.sc_movie = movies.ID_movie AND movies.m_title = %s'
            vals = (titulo,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def update_schedule(self, fields, vals):
        try:
            sql = 'UPDATE schedule_cinema SET '+','.join(fields)+'WHERE ID_schedule = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_schedule(self, ID_schedule):
        try:
            sql = 'DELETE FROM schedule_cinema WHERE ID_schedule = %s'
            vals = (ID_schedule,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err

    "sala"

    def read_a_hall(self, sala):
        try:
            sql = 'SELECT * FROM halls WHERE ID_hall = %s'
            vals = (sala,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_all_halls(self):
        try:
            sql = 'SELECT * FROM halls'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_halls_seats(self, Noasiento):
        try:
            sql = 'SELECT * FROM halls WHERE h_no_asiento = %s'
            vals = (Noasiento ,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err
    
    def read_hall_format(self, formato_h):
        try:
            sql = 'SELECT * FROM halls WHERE h_formato = %s'
            vals = (formato_h,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err
    
    def update_hall(self, fields, vals):
        try:
            sql = 'UPDATE halls SET '+','.join(fields)+'WHERE ID_hall = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    "Asientos"

    def read_a_seat(self, ID_seat, sala):
        try:
            sql = 'SELECT * FROM seat WHERE ID_seat = %s AND s_sala = %s'
            vals = (ID_seat, sala)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_all_seats(self):
        try:
            sql = 'SELECT * FROM seat'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_seats_hall(self, sala):
        try:
            sql = 'SELECT * FROM seat WHERE s_sala = %s'
            vals = (sala,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_seats_taken(self, calendario, fecha):
        try:
            sql = 'SELECT ticket.t_asiento FROM ticket JOIN schedule_cinema ON schedule_cinema.ID_schedule = ticket.t_calendario AND ticket.t_caledario = %s AND ticket.t_fecha = %s JOIN halls ON halls.ID_hall = schedule_cinema.sc_sala JOIN movies ON movies.ID_movie = schedule_cinema.sc_pelicuala'
            vals = (calendario, fecha)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err
        
    def update_seat(self, fields, vals):
        try:
            sql = 'UPDATE seat SET '+','.join(fields)+'WHERE ID_seat = %s AND s_sala = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    """Ticket Methods"""

    def create_ticket(self, fecha, ID_schedule, asiento):
        try:
            sql = 'INSERT INTO ticket (`t_fecha`, `t_calendario`, `t_asiento`) VALUES(%s, %s, %s)'
            vals = (fecha, ID_schedule, asiento)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            return err

    def read_hall_from_schedule(self, calendario):
        try:
            sql = 'SELECT schedule_cinema.sc_sala FROM schedule_cinema WHERE schedule_cinema.ID_schedule = %s'
            vals = (calendario,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err
    
    def read_a_ticket(self, ID_ticket):
        try:
            sql = 'SELECT ticket.ID_ticket, ticket.t_asiento, ticket.t_fecha, schedule_cinema.sc_sala, schedule_cinema.sc_hora, halls.h_formato, halls.h_precio, movies.m_titulo, movies.m_clasificacion, movies.m_idioma, movies.m_subtitulos, movies.m_formato FROM ticket JOIN schedule_cinema ON schedule_cinema.ID_schedule = ticket.t_fecha AND ticket.ID_ticket = %s JOIN halls ON halls.ID_hall = schedule_cinema.sc_sala JOIN movies ON movies.ID_movie = schedule_cinema.sc_pelicula'
            vals = (ID_ticket,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_a_ticket_ssd(self, calendario, asiento, fecha):
        try:
            sql = 'SELECT ticket.ID_ticket, ticket.t_asiento, ticket.t_fecha, schedule_cinema.sc_sala, schedule_cinema.sc_hora, halls.h_formato, halls.h_precio, movies.m_titulo, movies.m_clasificacion, movies.m_idioma, movies.m_subtitulos, movies.m_formato FROM ticket JOIN schedule_cinema ON schedule_cinema.ID_schedule = ticket.t_calendario AND ticket.t_fecha = %s AND ticket.t_calendario = %s AND ticket.t_asiento = %s  JOIN halls ON halls.ID_hall = schedule_cinema.sc_sala JOIN movies ON movies.ID_movie = schedule_cinema.sc_pelicula'
            vals = (calendario, asiento, fecha)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_all_tickets(self):
        try:
            sql = 'SELECT ticket.ID_ticket, ticket.t_asiento, ticket.t_fecha, schedule_cinema.sc_sala, schedule_cinema.sc_hora, halls.h_formato, halls.h_precio, movies.m_titulo, movies.m_clasificacion, movies.m_idioma, movies.m_subtitulos, movies.m_formato FROM ticket JOIN schedule_cinema ON schedule_cinema.ID_schedule = ticket.t_calendario JOIN halls ON halls.ID_hall = schedule_cinema.sc_sala JOIN movies ON movies.ID_movie = schedule_cinema.sc_pelicual'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_tickets_schedule(self, ID_schedule):
        try:
            sql = 'SELECT ticket.ID_ticket, ticket.t_asiento, ticket.t_fecha, schedule_cinema.sc_sala, schedule_cinema.sc_hora, halls.h_formato, halls.h_precio, movies.m_titulo, movies.m_clasificacion, movies.m_idioma, movies.m_subtitulos, movies.m_formato FROM ticket JOIN schedule_cinema ON schedule_cinema.ID_schedule = ticket.t_calendario AND ticket.t_calendario = %s JOIN halls ON halls.ID_hall = schedule_cinema.sc_sala JOIN movies ON movies.ID_movie = schedule_cinema.sc_pelicula'
            vals = (ID_schedule,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_tickets_date(self, fecha):
        try:
            sql = 'SELECT ticket.ID_ticket, ticket.t_asiento, ticket.t_fecha, schedule_cinema.sc_sala, schedule_cinema.sc_hora, halls.h_formato, halls.h_precio, movies.m_titutlo, movies.m_clasificacion movies.m_idioma, movies.m_subtitulos, movies.m_formato FROM ticket JOIN schedule_cinema ON schedule_cinema.ID_schedule = ticket.t_calendario AND ticket.t_fecha = %s JOIN halls ON halls.ID_hall = schedule_cinema.sc_sala JOIN movies ON movies.ID_movie = schedule_cinema.sc_pelicualas'
            vals = (fecha,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err
            
    def read_tickets_movie(self, ID_movie):
        try:
            sql = 'SELECT ticket.ID_ticket, ticket.t_asiento, ticket.t_fecha, schedule_cinema.sc_sala, schedule_cinema.sc_hora, halls.h_formato, halls.h_precio, movies.m_titulo, movies.m_clasificacion, movies.m_idioma, movies.m_subtitulos, movies.m_formato FROM ticket JOIN schedule_cinema ON schedule_cinema.ID_schedule = ticket.t_calendario JOIN movies ON movies.ID_movie = schedule_cinema.sc_pelicula AND movies.ID_movie = %s JOIN halls ON halls.ID_hall = schedule_cinema.sc_sala'
            vals = (ID_movie,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_tickets_hall(self, s_sala):
        try:
            sql = 'SELECT ticket.ID_ticket, ticket.t_sala, ticket.t_fecha, schedule_cinema.sc_sala, schedule_cinema.sc_hora, halls.h_formato, halls.h_precio, movies.m_titulo, movies.m_clasificacion, movies.m_idioma, movies.m_subtitulos, movies.m_formato FROM ticket JOIN schedule_cinema ON schedule_cinema.ID_schedule = ticket.t_calendario AND schedule_cinema.sc_sala= %s JOIN movies ON movies.ID_movie = schedule_cinema.sc_pelicula JOIN halls ON halls.ID_hall = schedule_cinema.sc_sala'
            vals = (s_sala,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def update_ticket(self, fields, vals):
        try:
            sql = 'UPDATE ticket SET '+','.join(fields)+'WHERE ID_ticket = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_ticket(self, ID_ticket):
        try:
            sql = 'DELETE FROM ticket WHERE ID_ticket = %s'
            vals = (ID_ticket,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err




            