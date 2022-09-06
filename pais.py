from mysqlconnection import connectToMySQL

class Pais:
    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

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
        query = f"SELECT * FROM paises where id = %(id)s;"
        data = { 'id' : id }
        results = connectToMySQL('cd_primera_base').query_db(query, data)
        #if len(results) > 0:
        #    return cls(results[0])
        #else:
        #    return None
        return cls(results[0]) if len(results) > 0 else None

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