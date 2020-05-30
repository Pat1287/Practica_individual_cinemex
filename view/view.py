class View:
    def start(self):
        print('===============  Bienvenido  ===============')

    def end(self):
        print('===============  Adios  ===============')

    def main_menu(self):
        print('===============  Menu Principal  ===============')
        print('1. Admin')
        print('2. Cliente')
        print('3. Salir')

    def option(self, last):
        print('Selecciona una opción (1-'+last+'): ', end = '')

    def not_valid_option(self):
        print('¡Opción no válida!\nIntenta de nuevo')

    def ask(self, output):
        print(output, end = '')

    def msg(self, output):
        print(output)

    def ok(self, id, op):
        print('+'*(len(str(id))+len(op)+24))
        print('+ ¡'+str(id)+' se '+op+' correctamente! +')
        print('+'*(len(str(id))+len(op)+24))

    def error(self, err):
        print(' ¡ERROR! '.center(len(err)+4, '-'))
        print('- '+err+' -')
        print('-'*(len(err)+4))

    "Menu 1"
    
    def main_menu_admin(self):
        print('===============  Submenu Cine  ===============')
        print('1. Peliculas')
        print('2. Salas')
        print('3. Horarios')
        print('4. Asientos')
        print('5. Tickets')
        print('6. Administradores')
        print('7. Regresar')

    def main_menu_client(self):
        print('===============  Submenu Cine  ===============')
        print('1. Peliculas')
        print('2. Salas')
        print('3. Horarios')
        print('4. Asientos')
        print('5. Tickets')
        print('6. Regresar')


    """Views for admins"""

    def admins_menu_admin(self):
        print('===============  Submenu Admin  ===============')
        print('1. Crear')
        print('2. Mostrar administrador ')
        print('3. Mostrar todos')
        print('4. Actualizar')
        print('5. Borrar')
        print('6. Salir')

    def show_a_admin(self, record):
        print('ID: ', record[0])
        print('Nombre: ', record[1])
        print('Primer apellido: ', record[2])
        print('Segundo apellido: ', record[3])
        print('Nombre de usuario: ', record[4])
        print('Correo electronico: ', record[5])
        print('Contrasenia: ', record[6])

    def fail_to_login(self):
        print('Usuario o Contraseña incorrecta')

    def show_admin_header(self, header):
        print(header.center(75,'*'))
        print('-'*75)

    def show_admin_midder(self):
        print('-'*75)

    def show_admin_footer(self):
        print('*'*75)

    "Vista peliculas"

    def movies_menu_admin(self):
        print('===============  Submenu Peliculas  ===============')
        print('1. Crear')
        print('1. Agregar pelicula')
        print('2. Ver pelicula')
        print('3. Ver todas las peliculas')
        print('4. Ver peliculas por idioma')
        print('5. Ver peliculas por formato')
        print('6. Ver peliculas por hora')
        print('7. Ver peliculas por clasificacion')
        print('8. Actualizar pelicula')
        print('9. Borrar pelicula')
        print('10. Regresar')

    def movies_menu_client(self):
        print('===============  Submenu Pelicualas  ===============')
        print('1. Ver pelicula')
        print('2. Ver todas las peliculas')
        print('3. Ver peliculas por idioma')
        print('4. Ver peliculas por formato')
        print('5. Ver peliculas por hora')
        print('6. Ver peliculas por clasificacion')
        print('7. Regresar')

    def show_a_movie(self, record):
        print('ID: ', record[0])
        print('Titulo: ', record[1])
        print('Genero: ', record[2])
        print('Clasificacion: ', record[3])
        print('Director: ', record[4])
        print('Actores: ', record[5])
        print('Sinopsis: ', record[6])
        print('Fecha de Estreno: ', record[7])
        print('Idioma: ', record[8])
        print('Subtitulos: ', record[9])
        print('Formato: ', record[10])

    def show_movies_hour(self, record):
        print('Titulo: ', record[0])
        print('Clasificacion: ', record[1])
        print('ID horario: ', record[2])
        print('ID pelicula: ', record[3])
        print('Sala ', record[4])
        print('Hora: ', record[5])

    def show_movie_header(self, header):
        print(header.center(100,'*'))
        print('-'*100)

    def show_movie_midder(self):
        print('-'*100)

    def show_movie_footer(self):
        print('*'*100)

    "Vista de salas"

    def halls_menu_admin(self):
        print('===============  Submenu sala  ===============')
        print('1. Crear')
        print('1. Ver sala')
        print('2. Ver todas las salas')
        print('3. Ver salas por asientos')
        print('4. Ver salas por formato')
        print('5. Actualizar sala')
        print('6. Regresar')

    def halls_menu_client(self):
        print('===============  Submenu sala  ===============')
        print('1. Ver sala')
        print('2. Ver todas las salas')
        #print('3. Ver salas por asientos')
        #print('4. Ver salas por formato')
        print('3. Regresar')

    def show_a_hall(self, record):
        print('Sala ', record[0])
        print('Numero de asientos: ', record[1])
        print('Formato: ', record[2])
        print('Precio: ', record[3])

    def show_hall_header(self, header):
        print(header.center(48,'*'))
        print('-'*48)

    def show_hall_midder(self):
        print('-'*48)

    def show_hall_footer(self):
        print('*'*48)

    "Vista Horarios"

    def schedule_menu_admin(self):
        print('===============  Submenu horario  ===============')
        print('1. Agregar horario')
        print('2. Ver horario')
        print('3. Ver todos los horarios')
        print('4. Ver horarios por sala')
        print('5. Ver horarios por pelicula')
        print('6. Actualizar horario')
        print('7. Borrar horario')
        print('8. Regresar')

    def schedule_menu_client(self):
        print('===============  Submenu horario  ===============')
        print('1. Ver horario')
        print('2. Ver todos los horarios')
        print('3. Ver horarios por sala')
        print('4. Ver horarios por pelicula')
        print('5. Regresar')

    def show_a_schedule(self, record):
        print('Horario ', record[0])
        print('ID de la pelicula: ', record[1])
        print('Sala ', record[2])
        print('Hora: ', record[3])
        print('Pelicula: ', record[4])

    def show_schedule_header(self, header):
        print(header.center(48,'*'))
        print('-'*48)

    def show_schedule_midder(self):
        print('-'*48)

    def show_schedule_footer(self):
        print('*'*48)

    "Vista Lugares"

    def seats_menu_admin(self):
        print('===============  Submenu lugares  ===============')
        print('1. Ver todos los Lugares')
        print('2. Ver lugar por sala')
        print('3. Regresar')

    def seats_menu_client(self):
        print('===============  Submenu lugares  ===============')
        print('1. Verer lugares por sala')
        print('2. Regresar')

    def show_a_seat(self, record):
        print('Asiento ', record[0])
        print('Sala ', record[1])

    def show_seats_hall(self, record):
        print(f'{record[0]:<3}')
    
    def show_seats_hall_header(self, header):
        print(header.center(11, '*'))
        print('Asiento'.ljust(11))
        print('-'*11)

    def seats_taken(self):
        print('Asientos ocupados')

    def show_seat_header(self, header):
        print(header.center(11,'*'))
        print('-'*11)

    def show_seat_midder(self):
        print('-'*11)

    def show_seat_footer(self):
        print('*'*11)

    """Views for Tickets"""

    def ticket_menu_admin(self):
        print('===============  Submenu boletos  ===============')
        print('1. Comprar boleto')
        print('2. Ver boleto')
        print('3. Ver todos los boletos')
        print('4. Ver boletos por horario')
        print('5. Ver boletos por fecha')
        print('6. Ver boletos por pelicula')
        print('7. Ver boletos por sala')
        print('8. Actualizar boleto')
        print('9. Borrar boleto')
        print('10. Regresar')

    def ticket_menu_client(self):
        print('===============  Submenu boletos  ===============')
        print('1. Comprar boleto')
        print('2. Ver ticket')
        print('3. Regresar')

    def show_a_ticket(self, record):
        print('ID: ', record[0])
        print('Asiento: ', record[1])
        print('Fecha: ', record[2])
        print('Sala ', record[3])
        print('Hora: ', record[4])
        print('Formato de la Sala: ', record[5])
        print('Precio: ', record[6])
        print('Pelicula: ', record[7])
        print('Clasificacion ', record[8])
        print('lenguaje: ', record[9])
        print('Subtitulos: ', record[10])
        print('Formato de la pelicula: ', record[11])

    def show_ticket_header(self, header):
        print(header.center(48,'*'))
        print('-'*48)

    def show_ticket_midder(self):
        print('-'*48)

    def show_ticket_footer(self):
        print('*'*48)