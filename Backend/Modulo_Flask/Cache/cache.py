import redis


class CacheManager:
    def __init__(self, host, port, password, *args, **kwargs):
        self.redis_client = redis.Redis(
            host=host,
            port=port,
            password=password,
            *args,
            **kwargs,
        )

        try:
            if self.redis_client.ping():
                print("Conexión creada de manera exitosa")
        except redis.RedisError as error:
            print(f"No se pudo conectar a Redis: {error}")

    def store_data(self, key, value, time_to_live=None):
        try:
            if time_to_live is None:
                self.redis_client.set(key, value)
            else:
                self.redis_client.setex(key, time_to_live, value)
        except redis.RedisError as error:
            print(f"Ah ocurrido un error al almacenar los datos: {error}")

    def get_data(self, key):
        try:
            output = self.redis_client.get(key)
            if output is not None:
                return output.decode("utf-8")
            return None
        except redis.RedisError as error:
            print(f"Ah ocurrido un error al traer la información: {error}")
            return None

    def delete_data(self, key):
        try:
            output = self.redis_client.delete(key)
            return output == 1
        except redis.RedisError as error:
            print(f"A ocurrido un error mientras se borra la información almacenada en Cache: {error}")
            return False


class EntityCache:
    # Cachea listas y detalles de una entidad bajo un prefijo común (ej. "products", "clients"), sin repetir el esquema de keys/invalidación por cada entidad que se quiera cachear.
    def __init__(self, cache_manager, prefix):
        self.cache_manager = cache_manager
        self.prefix = prefix

    def list_key(self):
        return f"{self.prefix}:list"

    def detail_key(self, entity_id):
        return f"{self.prefix}:{entity_id}"

    def get_list(self):
        return self.cache_manager.get_data(self.list_key())

    def store_list(self, body, time_to_live=None):
        self.cache_manager.store_data(self.list_key(), body, time_to_live)

    def get_detail(self, entity_id):
        return self.cache_manager.get_data(self.detail_key(entity_id))

    def store_detail(self, entity_id, body, time_to_live=None):
        self.cache_manager.store_data(
            self.detail_key(entity_id), body, time_to_live)

    def invalidate_list(self):
        self.cache_manager.delete_data(self.list_key())

    def invalidate_many(self, entity_ids):
        for entity_id in entity_ids:
            self.cache_manager.delete_data(self.detail_key(entity_id))
        self.invalidate_list()

    def invalidate(self, entity_id):
        self.invalidate_many([entity_id])
