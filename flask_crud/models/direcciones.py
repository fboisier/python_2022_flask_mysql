from flask_crud.config.mysqlconnection import connectToMySQL

class Direccion:

    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.numero = data['numero']
        self.ciudad_id = data['ciudad_id']
        self.tipodireccion_id = data['tipodireccion_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM direcciones;"
        results = connectToMySQL('cd_primera_base').query_db(query)
        all_data = []
        for data in results:
            all_data.append(cls(data))
        return all_data

    @classmethod
    def get_by_id(cls, id):
        query = "SELECT * FROM direcciones WHERE id = %(id)s"
        data = { 'id' : id }
        results = connectToMySQL('cd_primera_base').query_db(query, data)
        
        return cls(results[0]) if len(results) > 0 else None

    @classmethod
    def save(cls, data):
        query = """
                INSERT INTO direcciones (nombre,numero, ciudad_id, tipodireccion_id ,created_at,updated_at)
                VALUES (%(nombre)s,%(numero)s, %(ciudad_id)s, %(tipodireccion_id)s, NOW(), NOW());
                """
        resultado = connectToMySQL('cd_primera_base').query_db(query, data)
        print("RESULTADO: ", resultado)
        return resultado

    @classmethod
    def update(cls,data):
        query = "UPDATE direcciones SET nombre = %(nombre)s, updated_at=NOW(),numero = %(numero)s, ciudad_id=%(ciudad_id)s, tipodireccion_id=%(tipodireccion_id)s  WHERE id = %(id)s"
        resultado = connectToMySQL('cd_primera_base').query_db(query, data)
        print("RESULTADO: ", resultado)
        return resultado

    @classmethod
    def delete(cls,id):
        query = "DELETE FROM direcciones WHERE id = %(id)s"
        data = {
            'id': id
        }
        resultado = connectToMySQL('cd_primera_base').query_db(query, data)
        print("RESULTADO: ", resultado)
        return resultado