import sqlite3 as sql

class Clientes():
    def __init__(self, nombre, apellido, dni):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_apellido(self):
        return self.apellido

    def set_apellido(self, apellido):
        self.apellido = apellido

    def get_dni(self):
        return self.dni

    def set_dni(self, dni):
        self.dni = dni

class Conexion: 
    def __init__(self, nombreBD):
        self.conexion = sql.connect(nombreBD)
        self.cursor = self.conexion.cursor()

    def addVehiculo(self, ano, mod):
        self.cursor.execute('''INSERT INTO vehiculos(anno, modelo) VALUES (?, ?)''', (ano, mod))
        self.conexion.commit()

    def crearTablas(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS clientes(id INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT, apellido TEXT, dni INTEGER)''')
        self.conexion.commit()

    def insert(self, cliente):
        self.cursor.execute('''INSERT INTO clientes(nombre, apellido, dni) VALUES (?, ?, ?)''', (cliente.get_nombre(), cliente.get_apellido(), cliente.get_dni()))
        self.conexion.commit()

    def traerTodo(self):
        self.cursor.execute('''SELECT * FROM clientes''')
        self.resultado = self.cursor.fetchall()
        for res in self.resultado:
            print(res)

    def modificarCliente(self):
        ide = input('''Ingrese el id del cliente: ''')
        nom = input('''Ingrese el nombre del cliente: ''')
        apell = input('''Ingrese el apellido del cliente: ''')
        dn = input('''Ingrese el dni del cliente: ''')
        self.cursor.execute('''UPDATE clientes SET nombre = ?, apellido = ?, dni = ? WHERE id = ?;''', (nom, apell, dn, ide))
        self.conexion.commit()

    def borrarCliente(self):
        id = input('''Ingrese el id del cliente: ''')
        self.cursor.execute('''DELETE FROM clientes WHERE id = ?;''', (id,))
        self.conexion.commit()

    def cerrarConexion(self):
        self.cursor.close()
        self.conexion.close()
