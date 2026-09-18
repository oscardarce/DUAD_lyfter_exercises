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