from flask_crud.config.mysqlconnection import connectToMySQL

class TipoDireccion:

    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.created_at = data['createt_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM tiposdirecciones;"
        results = connectToMySQL('cd_primera_base').query_db(query)
        all_data = []
        for data in results:
            all_data.append(cls(data))
        return all_data
