from model.model import Model
from view.view import View
from datetime import date
from getpass import getpass

class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View()

    def start(self):
        self.view.start()
        self.main_menu()


    def main_menu(self):
        o = '0'
        while o != '3':
            self.view.main_menu()
            self.view.option('3')
            o = input()
            if o == '1':
                self.iam_admin()
            elif o == '2':
                self.iam_client()
            elif o == '3':
                self.view.end()
            else:
                self.view.not_valid_option()
        return

    def update_lists(self, fs, vs):
        fields = []
        vals = []
        for f,v in zip(fs, vs):
            if v !='':
                fields.append(f+' = %s')
                vals.append(v)
        return fields, vals

    "Administrador"
    def iam_admin(self):
        usuario, password = self.ask_admin_login()
        admin = self.model.read_usuario_password(usuario, password)
        if type(admin) == tuple:
            self.main_menu_admin()
        else:
            self.view.fail_to_login()
            return

    def iam_client(self):
        self.main_menu_client()

    

    def main_menu_admin(self):
        o = '0'
        while o != '7':
            self.view.main_menu_admin()
            self.view.option('7')
            o = input()
            if o == '1':
                self.movies_menu_admin()
            elif o == '2':
                self.halls_menu_admin()
            elif o == '3':
                self.schedule_menu_admin()
            elif o == '4':
                self.seats_menu_admin()
            elif o == '5':
                self.tickets_menu_admin()
            elif o == '6':
                self.admins_menu_admin()
            elif o == '7':
                return
            else:
                self.view.not_valid_option()
        return

    def main_menu_client(self):
        o = '0'
        while o != '6':
            self.view.main_menu_client()
            self.view.option('6')
            o = input()
            if o == '1':
                self.movies_menu_client()
            elif o == '2':
                self.halls_menu_client()
            elif o == '3':
                self.schedule_menu_client()
            elif o == '4':
                self.seats_menu_client()
            elif o == '5':
                self.tickets_menu_client()
            elif o == '6':
                return
            else:
                self.view.not_valid_option()
        return

    "Admimins"

    def admins_menu_admin(self):
        o = '0'
        while o != '6':
            self.view.admins_menu_admin()
            self.view.option('6')
            o = input()
            if o == '1':
                self.create_admin()
            elif o == '2':
                self.read_a_admin()
            elif o == '3':
                self.read_all_admins()
            elif o == '4':
                self.update_admin()
            elif o == '5':
                self.delete_admin()
            elif o == '6':
                return
            else:
                self.view.not_valid_option()
        return

    def ask_admin_create(self):
        self.view.ask('Nombre: ')
        nombre = input()
        self.view.ask('Primer apellido: ')
        appat = input()
        self.view.ask('Segundo apellido (Vacio si no tienes): ')
        apmat = input()
        self.view.ask('Nombre de usuario: ')
        usuario = input()
        self.view.ask('Correo electronico: ')
        email = input()
        self.view.ask('Contrasenia: ')
        password = input()
        return [nombre, appat, apmat, usuario, email, password]

    def ask_admin_login(self):
        self.view.ask('Nombre de usuario: ')
        usuario = input()
        self.view.ask('Contrasenia: ')
        password = getpass()
        return [usuario, password]

    def create_admin(self):
        nombre, appat, apmat, usuario, email, password = self.ask_admin_create()
        out = self.model.create_admin(nombre, appat, apmat, usuario, email, password)
        if out == True:
            self.view.ok(usuario, 'agregó')
        else:
            self.view.error('No se pudo agregar el admin. Verifica.')
        return

    def read_a_admin(self):
        self.view.ask('ID del admin: ')
        ID_admin = input()
        admin = self.model.read_a_admin(ID_admin)
        if type(admin) == tuple:
            self.view.show_admin_header(' Detalles de la pelicula '+ID_admin+' ')
            self.view.show_a_admin(admin)
            self.view.show_admin_midder()
            self.view.show_admin_footer()
        else:
            if admin == None:
                self.view.error('El administrador no existe')
            else:
                self.view.error('Problema al leer el administrador. Verifica')
        return

    def read_all_admins(self):
        admins = self.model.read_all_admins()
        if type(admins) == list:
            self.view.show_admin_header(' Todos los Administradores ')
            for admin in admins:
                self.view.show_a_admin(admin)
                self.view.show_admin_midder()
            self.view.show_admin_footer()
        else:
            self.view.error('Problema al leer los Administradores. Verifica')
        return

    def update_admin(self):
        self.view.ask('ID del administrador a modificar: ')
        ID_admin = input()
        admin = self.model.read_a_admin(ID_admin)
        if type(admin) == tuple:
            self.view.show_admin_header(' Datos del administrador '+ID_admin+' ')
            self.view.show_a_admin(admin)
            self.view.show_admin_midder()
            self.view.show_admin_footer()
        else:
            if admin == None:
                self.view.error('El administrador no existe')
            else:
                self.view.error('Problema al leer el administrador. Verifica')
            return
        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual): ')
        whole_vals = self.ask_admin_create()
        fields, vals = self.update_lists(['a_nombre', 'a_appat', 'a_apmat', 'a_usuario', 'a_email', 'a_password'], whole_vals)
        vals.append(ID_admin)
        vals = tuple(vals)
        out = self.model.update_admin(fields, vals)
        if out == True:
            self.view.ok(ID_admin, 'Actualizó')
        else:
            self.view.error('No se pudo actualizar el administrador. Verifica')
        return

    def delete_admin(self):
        self.view.ask('ID del administrador a borrar: ')
        ID_admin = input()
        count = self.model.delete_admin(ID_admin)
        if count !=0:
            self.view.ok(ID_admin, 'borró')
        else:
            if count == 0:
                self.view.error('El administrador no existe')
            else:
                self.view.error('Problema al borrar el administrador. Verifica')
        return

    "Pelicualas"

    def movies_menu_admin(self):
        o = '0'
        while o != '10':
            self.view.movies_menu_admin()
            self.view.option('10')
            o = input()
            if o == '1':
                self.create_movie()
            elif o == '2':
                self.read_a_movie()
            elif o == '3':
                self.read_all_movies()
            elif o == '4':
                self.read_movies_language()
            elif o == '5':
                self.read_movies_format()
            elif o == '6':
                self.read_movies_hour()
            elif o == '7':
                self.read_movies_clasification()
            elif o == '8':
                self.update_movie()
            elif o == '9':
                self.delete_movie()
            elif o == '10':
                return
            else:
                self.view.not_valid_option()
        return

    def movies_menu_client(self):
        o = '0'
        while o != '7':
            self.view.movies_menu_client()
            self.view.option('7')
            o = input()
            if o == '1':
                self.read_a_movie()
            elif o == '2':
                self.read_all_movies()
            elif o == '3':
                self.read_movies_language()
            elif o == '4':
                self.read_movies_format()
            elif o == '5':
                self.read_movies_hour()
            elif o == '6':
                self.read_movies_clasification()
            elif o == '7':
                return
            else:
                self.view.not_valid_option()
        return

    def ask_movie(self):
        self.view.ask('Titulo: ')
        titulo = input()
        self.view.ask('Genero: ')
        genero = input()
        self.view.ask('Clasificacion: ')
        clasificacion = input()
        self.view.ask('Director: ')
        director = input()
        self.view.ask('Actores: ')
        actores = input()
        self.view.ask('Sinopsis: ')
        synopsis = input()
        self.view.ask('Fecha de Estreno(yyyy-mm-dd): ')
        release_fecha = input()
        self.view.ask('Idioma: ')
        idioma = input()
        self.view.ask('Subtitulos: ')
        subtitulos = input()
        self.view.ask('Formato(2D/3D): ')
        formato_m = input()
        return [titulo, genero, clasificacion, director, actores, synopsis, release_fecha, idioma, subtitulos, formato_m]

    def create_movie(self):
        titulo, genero, clasificacion, director, actores, synopsis, release_fecha, idioma, subtitulos, formato_m = self.ask_movie()
        out = self.model.create_movie(titulo, genero, clasificacion, director, actores, synopsis, release_fecha, idioma, subtitulos, formato_m)
        if out == True:
            self.view.ok(titulo+' '+idioma+' '+formato_m, 'agregó')
        else:
            self.view.error('No se pudo agregar la pelicula. Verifica.')
        return

    def read_a_movie(self):
        self.view.ask('ID de la pelicula: ')
        ID_movie = input()
        movie = self.model.read_a_movie_id(ID_movie)
        if type(movie) == tuple:
            self.view.show_movie_header(' Detalles de la pelicula '+ID_movie+' ')
            self.view.show_a_movie(movie)
            self.view.show_movie_midder()
            self.view.show_movie_footer()
        else:
            if movie == None:
                self.view.error('La pelicula no existe')
            else:
                self.view.error('Problema al leer la pelicula. Verifica')
        return

    def read_all_movies(self):
        movies = self.model.read_all_movies()
        if type(movies) == list:
            self.view.show_movie_header(' Todas las Peliculas ')
            for movie in movies:
                self.view.show_a_movie(movie)
                self.view.show_movie_midder()
            self.view.show_movie_footer()
        else:
            self.view.error('Problema al leer las peliculas. Verifica')
        return

    def read_movies_language(self):
        self.view.ask('idioma: ')
        idioma = input()
        movies = self.model.read_movies_language(idioma)
        if type(movies) == list:
            self.view.show_movie_header(' Peliculas en '+idioma+' ')
            for movie in movies:
                self.view.show_a_movie(movie)
                self.view.show_movie_midder()
            self.view.show_movie_footer()
        else:
            self.view.error('Problema al leer las peliculas. Verifica')
        return

    def read_movies_format(self):
        self.view.ask('Formato(2D/3D): ')
        formato_m = input()
        movies = self.model.read_movies_format(formato_m)
        if type(movies) == list:
            self.view.show_movie_header(' Peliculas en '+formato_m+' ')
            for movie in movies:
                self.view.show_a_movie(movie)
                self.view.show_movie_midder()
            self.view.show_movie_footer()
        else:
            self.view.error('Problema al leer las peliculas. Verifica')
        return

    def read_movies_hour(self):
        self.view.ask('Hora(hh:mm): ')
        hora_m = input()
        movies = self.model.read_movies_hour(hora_m)
        if type(movies) == list:
            self.view.show_movie_header(' Peliculas a las '+hora_m+' ')
            for movie in movies:
                self.view.show_movies_hour(movie)
                self.view.show_movie_midder()
            self.view.show_movie_footer()
        else:
            self.view.error('Problema al leer las peliculas. Verifica')
        return

    def read_movies_clasification(self):
        self.view.ask('Clasificacion: ')
        clasificacion = input()
        movies = self.model.read_movies_clasification(clasificacion)
        if type(movies) == list:
            self.view.show_movie_header(' Peliculas con clasificacion '+clasificacion+' ')
            for movie in movies:
                self.view.show_a_movie(movie)
                self.view.show_movie_midder()
            self.view.show_movie_footer()
        else:
            self.view.error('Problema al leer las peliculas. Verifica')
        return

    def update_movie(self):
        self.view.ask('ID de la pelicula a modificar: ')
        ID_movie = input()
        movie = self.model.read_a_movie_id(ID_movie)
        if type(movie) == tuple:
            self.view.show_movie_header(' Datos de la pelicula '+ID_movie+' ')
            self.view.show_a_movie(movie)
            self.view.show_movie_midder()
            self.view.show_movie_footer()
        else:
            if movie == None:
                self.view.error('La pelicula no existe')
            else:
                self.view.error('Problema al leer la pelicula. Verifica')
            return
        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual): ')
        whole_vals = self.ask_movie()
        fields, vals = self.update_lists(['m_titulo', 'm_genero', 'm_clasificacion', 'm_director', 'm_actores', 'm_synopsis', 'm_release_fecha', 'm_idioma', 'm_subtitulos', 'm_formato'], whole_vals)
        vals.append(ID_movie)
        vals = tuple(vals)
        out = self.model.update_movie(fields, vals)
        if out == True:
            self.view.ok(ID_movie, 'Actualizó')
        else:
            self.view.error('No se pudo actualizar la pelicula. Verifica')
        return

    def delete_movie(self):
        self.view.ask('ID de pelicula a borrar: ')
        ID_movie = input()
        count = self.model.delete_movie(ID_movie)
        if count !=0:
            self.view.ok(ID_movie, 'borró')
        else:
            if count == 0:
                self.view.error('La pelicula no existe')
            else:
                self.view.error('Problema al borrar la pelicula. Verifica')
        return

    "Salas"

    def halls_menu_admin(self):
        o = '0'
        while o != '6':
            self.view.halls_menu_admin()
            self.view.option('6')
            o = input()
            if o == '1':
                self.read_a_hall()
            elif o == '2':
                self.read_all_halls()
            elif o == '3':
                self.read_halls_seats()
            elif o == '4':
                self.read_halls_format()
            elif o == '5':
                self.update_hall()
            elif o == '6':
                return
            else:
                self.view.not_valid_option()
        return

        "clientes Sala"
    def halls_menu_client(self):
        o = '0'
        while o != '3':
            self.view.halls_menu_client()
            self.view.option('3')
            o = input()
            if o == '1':
                self.read_a_hall()
            elif o == '2':
                self.read_all_halls()
            elif o == '3':
                return
            else:
                self.view.not_valid_option()
        return

    def ask_hall(self):
        self.view.ask('Numero de Sala: ')
        sala = input()
        self.view.ask('Numero de Asientos: ')
        Noasiento = input()
        self.view.ask('Formato de la Sala: ')
        formato_h = input()
        self.view.ask('Precio: ')
        precio = input()
        return [sala, Noasiento, formato_h, precio]

    def read_a_hall(self):
        self.view.ask('Numero de la sala: ')
        ID_hall = input()
        hall = self.model.read_a_hall(ID_hall)
        if type(hall) == tuple:
            self.view.show_hall_header(' Datos de la sala '+ID_hall+' ')
            self.view.show_a_hall(hall)
            self.view.show_hall_midder()
            self.view.show_hall_footer()
        else:
            if hall == None:
                self.view.error('La sala no existe')
            else:
                self.view.error('Problema al leer la sala. Verifica')
        return

    def read_all_halls(self):
        halls = self.model.read_all_halls()
        if type(halls) == list:
            self.view.show_hall_header(' Todas las salas ')
            for hall in halls:
                self.view.show_a_hall(hall)
                self.view.show_hall_midder()
            self.view.show_hall_footer()
        else:
            self.view.error('Problema al leer las salas. Verifica')
        return

    def read_halls_seats(self):
        self.view.ask('Numero de Asientos(132/90/60/35): ')
        Noasientos = input()
        halls = self.model.read_halls_seats(Noasientos)
        if type(halls) == list:
            self.view.show_hall_header(' Salas con formato '+Noasientos+' ')
            for hall in halls:
                self.view.show_a_hall(hall)
                self.view.show_hall_midder()
            self.view.show_hall_footer()
        else:
            self.view.error('Problema al leer las salas. Verifica')
        return

    def read_halls_format(self):
        self.view.ask('Formato(Tradicional/Premium/VIP): ')
        formato_h = input()
        halls = self.model.read_hall_format(formato_h)
        if type(halls) == list:
            self.view.show_hall_header(' Salas con formato '+formato_h+' ')
            for hall in halls:
                self.view.show_a_hall(hall)
                self.view.show_hall_midder()
            self.view.show_hall_footer()
        else:
            self.view.error('Problema al leer las salas. Verifica')
        return

    def update_hall(self):
        self.view.ask('Numero de la sala a modificar: ')
        h_sala = input()
        hall = self.model.read_a_hall(h_sala)
        if type(hall) == tuple:
            self.view.show_hall_header(' Datos de la sala '+h_sala+' ')
            self.view.show_a_hall(hall)
            self.view.show_hall_midder()
            self.view.show_hall_footer()
        else:
            if hall == None:
                self.view.error('La sala no existe')
            else:
                self.view.error('Problema al leer la sala. Verifica')
            return
        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual): ')
        whole_vals = self.ask_hall()
        fields, vals = self.update_lists(['h_sala', 'h_no_asientos', 'h_formato', 'h_precio'], whole_vals)
        vals.append(h_sala)
        vals = tuple(vals)
        out = self.model.update_hall(fields, vals)
        if out == True:
            self.view.ok(h_sala, 'Actualizó')
        else:
            self.view.error('No se pudo actualizar la sala. Verifica')
        return


    def schedule_menu_admin(self):
        o = '0'
        while o != '8':
            self.view.schedule_menu_admin()
            self.view.option('8')
            o = input()
            if o == '1':
                self.create_schedule()
            elif o == '2':
                self.read_a_schedule()
            elif o == '3':
                self.read_all_schedules()
            elif o == '4':
                self.read_schedule_hall()
            elif o == '5':
                self.read_schedule_movie()
            elif o == '6':
                self.update_schedule()
            elif o == '7':
                self.delete_schedule()
            elif o == '8':
                return
            else:
                self.view.not_valid_option()
        return

    def schedule_menu_client(self):
        o = '0'
        while o != '5':
            self.view.schedule_menu_client()
            self.view.option('5')
            o = input()
            if o == '1':
                self.read_a_schedule()
            elif o == '2':
                self.read_all_schedules()
            elif o == '3':
                self.read_schedule_hall()
            elif o == '4':
                self.read_schedule_movie()
            elif o == '5':
                return
            else:
                self.view.not_valid_option()
        return

    def ask_schedule(self):
        self.view.ask('ID de la pelicula en este horario: ')
        ID_movie = input()
        self.view.ask('Sala para este horario: ')
        sala = input()
        self.view.ask('Hora de la funcion: ')
        hora = input()
        return [ID_movie, sala, hora]

    def create_schedule(self):
        ID_movie, sala, hora = self.ask_schedule()
        out = self.model.create_schedule(ID_movie, sala, hora)
        if out == True:
            self.view.ok(ID_movie+' '+sala+' '+hora, 'agregó')
        else:
            self.view.error('No se pudo agregar el horario. Verifica.')
        return

    def read_a_schedule(self):
        self.view.ask('ID del horario: ')
        ID_schedule = input()
        schedule = self.model.read_a_schedule_id(ID_schedule)
        if type(schedule) == tuple:
            self.view.show_schedule_header(' Datos del horario '+ID_schedule+' ')
            self.view.show_a_schedule(schedule)
            self.view.show_schedule_midder()
            self.view.show_schedule_footer()
            return schedule
        else:
            if schedule == None:
                self.view.error('El horario no existe')
            else:
                self.view.error('Problema al leer el horario. Verifica')
        return

    def read_all_schedules(self):
        schedules = self.model.read_all_schedules()
        if type(schedules) == list:
            self.view.show_schedule_header(' Todos los horarios ')
            for schedule in schedules:
                self.view.show_a_schedule(schedule)
                self.view.show_schedule_midder()
            self.view.show_schedule_footer()
        else:
            self.view.error('Problema al leer las salas. Verifica')
        return

    def read_schedule_hall(self):
        self.view.ask('Numero de Sala: ')
        hall = input()
        schedules = self.model.read_schedule_hall(hall)
        if type(schedules) == list:
            self.view.show_schedule_header(' Horarios en la sala '+hall+' ')
            for schedule in schedules:
                self.view.show_a_schedule(schedule)
                self.view.show_schedule_midder()
            self.view.show_schedule_footer()
        else:
            self.view.error('Problema al leer los horarios. Verifica')
        return

    def read_schedule_movie(self):
        self.view.ask('Titulo de la pelicula: ')
        titulo_pelicula = input()
        schedules = self.model.read_schedule_movie(titulo_pelicula)
        if type(schedules) == list:
            self.view.show_schedule_header(' Horarios con la pelicula '+titulo_pelicula+' ')
            for schedule in schedules:
                self.view.show_a_schedule(schedule)
                self.view.show_schedule_midder()
            self.view.show_schedule_footer()
        else:
            self.view.error('Problema al leer los horarios. Verifica')
        return

    def update_schedule(self):
        self.view.ask('ID de horario a modificar: ')
        ID_schedule = input()
        schedule = self.model.read_a_schedule_id(ID_schedule)
        if type(schedule) == tuple:
            self.view.show_schedule_header(' Datos del horario '+ID_schedule+' ')
            self.view.show_a_schedule(schedule)
            self.view.show_schedule_midder()
            self.view.show_schedule_footer()
        else:
            if schedule == None:
                self.view.error('El horario no existe')
            else:
                self.view.error('Problema al leer el horario. Verifica')
            return
        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual): ')
        whole_vals = self.ask_schedule()
        fields, vals = self.update_lists(['sc_pelicula', 'sc_sala', 'sc_hora'], whole_vals)
        vals.append(ID_schedule)
        vals = tuple(vals)
        out = self.model.update_schedule(fields, vals)
        if out == True:
            self.view.ok(ID_schedule, 'Actualizó')
        else:
            self.view.error('No se pudo actualizar el horario. Verifica')
        return

    def delete_schedule(self):
        self.view.ask('ID del horario a borrar: ')
        ID_schedule = input()
        count = self.model.delete_schedule(ID_schedule)
        if count !=0:
            self.view.ok(ID_schedule, 'borró')
        else:
            if count == 0:
                self.view.error('El horario no existe')
            else:
                self.view.error('Problema al borrar el horario. Verifica')
        return

    "Asientos"

    def seats_menu_admin(self):
        o = '0'
        while o != '3':
            self.view.seats_menu_admin()
            self.view.option('3')
            o = input()
            if o == '1':
                self.read_all_seats()
            elif o == '2':
                self.read_seats_hall()
            elif o == '3':
                return
            else:
                self.view.not_valid_option()
        return

    def seats_menu_client(self):
        o = '0'
        while o != '2':
            self.view.seats_menu_client()
            self.view.option('2')
            o = input()
            if o == '1':
                self.read_seats_hall()
            elif o == '2':
                return
            else:
                self.view.not_valid_option()
        return

    def ask_seat(self):
        self.view.ask('Asiento: ')
        ID_seat = input()
        self.view.ask('Sala: ')
        hall = input()
        return [ID_seat, hall]

    def read_a_seat(self):
        self.view.ask('Asiento: ')
        ID_seat = input()
        self.view.ask('Sala: ')
        hall = input()
        seat = self.model.read_a_seat(ID_seat, hall)
        if type(seat) == tuple:
            self.view.show_seat_header(' Datos del asiento '+ID_seat+' Sala '+hall+' ')
            self.view.show_a_seat(seat)
            self.view.show_seat_midder()
            self.view.show_seat_footer()
        else:
            if seat == None:
                self.view.error('El asiento no existe')
            else:
                self.view.error('Problema al leer el asiento. Verifica')
        return

    def read_all_seats(self):
        seats = self.model.read_all_seats()
        if type(seats) == list:
            self.view.show_seat_header(' Todos los asientos ')
            for seat in seats:
                self.view.show_a_seat(seat)
                self.view.show_seat_midder()
            self.view.show_seat_footer()
        else:
            self.view.error('Problema al leer los asientos. Verifica')
        return

    def read_seats_hall(self):
        self.view.ask('Sala: ')
        hall = input()
        seats = self.model.read_seats_hall(hall)
        if type(seats) == list:
            self.view.show_seat_header(' Asientos en la sala '+hall+' ')
            for seat in seats:
                self.view.show_a_seat(seat)
                self.view.show_seat_midder()
            self.view.show_seat_footer()
        else:
            self.view.error('Problema al leer los asientos. Verifica')
        return

    """Controllers for tickets"""

    def tickets_menu_admin(self):
        o = '0'
        while o != '10':
            self.view.ticket_menu_admin()
            self.view.option('10')
            o = input()
            if o == '1':
                self.create_ticket()
            elif o == '2':
                self.read_a_ticket()
            elif o == '3':
                self.read_all_tickets()
            elif o == '4':
                self.read_tickets_schedule()
            elif o == '5':
                self.read_tickets_date()
            elif o == '6':
                self.read_tickets_movie()
            elif o == '7':
                self.read_tickets_hall()
            elif o == '8':
                self.update_ticket()
            elif o == '9':
                self.delete_ticket()
            elif o == '10':
                return
            else:
                self.view.not_valid_option()
        return

    def tickets_menu_client(self):
        o = '0'
        while o != '3':
            self.view.ticket_menu_client()
            self.view.option('3')
            o = input()
            if o == '1':
                self.create_ticket()
            elif o == '2':
                self.read_a_ticket()
            elif o == '3':
                return
            else:
                self.view.not_valid_option()
        return

    def ask_ticket(self):
        self.view.ask('Fecha: ')
        fecha = input()
        self.view.ask('Horario: ')
        schedule = input()
        seats_taken = self.model.read_seats_taken(schedule, fecha)
        schedule_full = self.model.read_hall_from_schedule(schedule)
        if type(seats_taken) == list:
            self.view.seats_taken()
            for seat_taken in seats_taken:
                self.view.show_seats_hall(seat_taken)
                self.view.show_seat_midder()
            self.view.show_seat_footer()
        if type(schedule_full) == tuple:
            hall = schedule_full[0]
            seats_sch = self.model.read_seats_hall(hall)
            if type(seats_sch) == list:
                self.view.show_seats_hall_header(' Asientos en la sala '+str(hall)+' ')
                for seat_sch in seats_sch:
                    self.view.show_seats_hall(seat_sch)
                    self.view.show_seat_midder()
                self.view.show_seat_footer()
            else:
                self.view.error('Problema al leer los asientos. Verifica')
        else:
            self.view.error('El horario no existe')
        self.view.ask('Asiento: ')
        seat = input()
        return [date, schedule, seat]

    def create_ticket(self):
        self.read_all_schedules()
        date, schedule, seat = self.ask_ticket()

        
        ticket = self.model.read_a_ticket_ssd(date, schedule, seat)
        if type(ticket) == tuple:
            self.view.error(' El ticket ya ha sido comprado ')
        else:
            out = self.model.create_ticket(date, schedule, seat) 
            if out == True:
                self.view.ok(date+' '+schedule+' '+seat+' ', 'compró')
                ticket2 = self.model.read_a_ticket_ssd(date, schedule, seat)
                self.view.show_ticket_header(' Datos del ticket ')
                self.view.show_a_ticket(ticket2)
                self.view.show_ticket_midder()
                self.view.show_ticket_footer()
            else:
                self.view.error('No se pudo comprar el ticket. Verifica')
            return
        return
        

    def read_a_ticket(self):
        self.view.ask('ID Ticket: ')
        ID_ticket = input()
        ticket = self.model.read_a_ticket(ID_ticket)
        if type(ticket) == tuple:
            self.view.show_ticket_header(' Datos del ticket '+ID_ticket+' ')
            self.view.show_a_ticket(ticket)
            self.view.show_ticket_midder()
            self.view.show_ticket_footer()
            return ticket
        else:
            if ticket == None:
                self.view.error(' El ticket no existe ')
            else:
                self.view.error('Problema al leer el ticket. Verifica')
        return

    def read_all_tickets(self):
        tickets = self.model.read_all_tickets()
        if type(tickets) == list:
            self.view.show_ticket_header(' Todos los tickets ')
            for ticket in tickets:
                self.view.show_a_ticket(ticket)
                self.view.show_ticket_midder()
            self.view.show_ticket_footer()
        else:
            self.view.error('Problema al leer los tickets. Verifica')
        return

    def read_tickets_schedule(self):
        self.view.ask('ID Horario: ')
        schedule = input()
        tickets = self.model.read_tickets_schedule(schedule)
        if type(tickets) == list:
            self.view.show_ticket_header(' Tickets en el horario '+schedule+' ')
            for ticket in tickets:
                self.view.show_a_ticket(ticket)
                self.view.show_ticket_midder()
            self.view.show_ticket_footer()
        else:
            self.view.error('Problema al leer los tickets. Verifica')
        return

    def read_tickets_date(self):
        self.view.ask('Fecha (yyyy-mm-dd): ')
        date = input()
        tickets = self.model.read_tickets_date(date)
        if type(tickets) == list:
            self.view.show_ticket_header(' Tickets en la fecha '+date+' ')
            for ticket in tickets:
                self.view.show_a_ticket(ticket)
                self.view.show_ticket_midder()
            self.view.show_ticket_footer()
        else:
            self.view.error('Problema al leer los tickets. Verifica')
        return    

    def read_tickets_movie(self):
        self.view.ask('ID de la pelicula: ')
        movie = input()
        tickets = self.model.read_tickets_movie(movie)
        if type(tickets) == list:
            self.view.show_ticket_header(' Tickets de la pelicula '+movie+' ')
            for ticket in tickets:
                self.view.show_a_ticket(ticket)
                self.view.show_ticket_midder()
            self.view.show_ticket_footer()
        else:
            self.view.error('Problema al leer los tickets. Verifica')
        return

    def read_tickets_hall(self):
        self.view.ask('Sala: ')
        hall = input()
        tickets = self.model.read_tickets_hall(hall)
        if type(tickets) == list:
            self.view.show_ticket_header(' Tickets en la sala '+hall+' ')
            for ticket in tickets:
                self.view.show_a_ticket(ticket)
                self.view.show_ticket_midder()
            self.view.show_ticket_footer()
        else:
            self.view.error('Problema al leer los tickets. Verifica')
        return

    def update_ticket(self):
        self.view.ask('ID del ticket a modificar: ')
        ID_ticket = input()
        ticket = self.model.read_a_ticket(ID_ticket)
        if type(ticket) == tuple:
            self.view.show_ticket_header(' Datos del ticket '+ID_ticket+' ')
            self.view.show_a_ticket(ticket)
            self.view.show_ticket_midder()
            self.view.show_ticket_footer()
        else:
            if ticket == None:
                self.view.error('El ticket no existe')
            else:
                self.view.error('Problema al leer el ticket. Verifica')
            return
        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual): ')
        whole_vals = self.ask_ticket()
        fields, vals = self.update_lists(['t_date', 't_schedule', 't_seat'], whole_vals)
        vals.append(ID_ticket)
        vals = tuple(vals)
        out = self.model.update_ticket(fields, vals)
        if out == True:
            self.view.ok(ID_ticket, 'Actualizó')
        else:
            self.view.error('No se pudo actualizar el ticket. Verifica')
        return

    def delete_ticket(self):
        self.view.ask('ID del ticket a borrar: ')
        ID_ticket = input()
        count = self.model.delete_ticket(ID_ticket)
        if count !=0:
            self.view.ok(ID_ticket, 'borró')
        else:
            if count == 0:
                self.view.error('El ticket no existe')
            else:
                self.view.error('Problema al borrar el ticket. Verifica')
        return