from flask_crud.config.mysqlconnection import connectToMySQL
from flask_crud.models import ciudades

class Pais:
    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        self.ciudades = []

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM paises;"
        results = connectToMySQL('cd_primera_base').query_db(query)
        all_data = []
        for data in results:
            all_data.append(cls(data))
        return all_data

    @classmethod
    def get_by_id(cls, id):
        query = "SELECT * FROM paises JOIN ciudades ON ciudades.pais_id = paises.id WHERE paises.id = %(id)s"
        data = { 'id' : id }
        results = connectToMySQL('cd_primera_base').query_db(query, data)
        #if len(results) > 0:
        #    return cls(results[0])
        #else:
        #    return None
        pais = cls(results[0]) if len(results) > 0 else None
        for fila in results:
            
            ciudad_dato = {
                'id' :fila['ciudades.id'],
                'nombre' :fila['ciudades.nombre'],
                'paises.nombre' :fila['nombre'],
                'paises.id' :fila['id'],
                'created_at' :fila['ciudades.created_at'],
                'updated_at' :fila['ciudades.updated_at'],
            }

            pais.ciudades.append(ciudades.Ciudad(ciudad_dato))

        return pais

    @classmethod
    def save(cls, data):
        query = """
                INSERT INTO paises (id,nombre,created_at,updated_at)
                VALUES (%(id)s, %(nombre)s, NOW(), NOW());
                """
        resultado = connectToMySQL('cd_primera_base').query_db(query, data)
        print("RESULTADO: ", resultado)
        return resultado

    @classmethod
    def update(cls,data):
        query = "UPDATE paises SET nombre = %(nombre)s, updated_at=NOW() WHERE id = %(id)s"
        resultado = connectToMySQL('cd_primera_base').query_db(query, data)
        print("RESULTADO: ", resultado)
        return resultado

    @classmethod
    def delete(cls,id):
        query = "DELETE FROM paises WHERE id = %(id)s"
        data = {
            'id': id
        }
        resultado = connectToMySQL('cd_primera_base').query_db(query, data)
        print("RESULTADO: ", resultado)
        return resultado