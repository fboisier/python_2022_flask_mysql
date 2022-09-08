from flask_crud.config.mysqlconnection import connectToMySQL

class Ciudad:
    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.pais = data['paises.nombre']
        self.pais_id = data['paises.id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ciudades JOIN paises ON ciudades.pais_id = paises.id;"
        results = connectToMySQL('cd_primera_base').query_db(query)
        all_data = []
        for data in results:
            all_data.append(cls(data))
        return all_data

    @classmethod
    def get_by_id(cls, id):
        query = f"SELECT * FROM ciudades JOIN paises ON ciudades.pais_id = paises.id where ciudades.id = %(id)s;"
        data = { 'id' : id }
        results = connectToMySQL('cd_primera_base').query_db(query, data)
        return cls(results[0]) if len(results) > 0 else None

    @classmethod
    def save(cls, data):
        query = """
                INSERT INTO ciudades (nombre,created_at,updated_at, pais_id)
                VALUES (%(nombre)s, NOW(), NOW(), %(pais_id)s);
                """
        resultado = connectToMySQL('cd_primera_base').query_db(query, data)
        print("RESULTADO: ", resultado)
        return resultado

    @classmethod
    def update(cls,data):
        query = "UPDATE ciudades SET nombre = %(nombre)s, updated_at=NOW(), pais_id = %(pais_id)s WHERE id = %(id)s"
        resultado = connectToMySQL('cd_primera_base').query_db(query, data)
        print("RESULTADO: ", resultado)
        return resultado

    @classmethod
    def delete(cls,id):
        query = "DELETE FROM ciudades WHERE id = %(id)s"
        data = {
            'id': id
        }
        resultado = connectToMySQL('cd_primera_base').query_db(query, data)
        print("RESULTADO: ", resultado)
        return resultado