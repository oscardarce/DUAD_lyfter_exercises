"""
Encapsula la creación (encode) y verificación (decode) de JSON Web Tokens
firmados con RS256, usando el par de llaves que genera generate_keys.py.
"""

from datetime import datetime, timedelta, timezone
from pathlib import Path

import jwt


class JWT_Manager:
    def __init__(
        self,
        private_key_path,
        public_key_path,
        token_duration_minutes=60,
    ):
        # Leemos el contenido de los .pem UNA VEZ al crear el manager y lo guardamos en memoria con self.private_key / self.public_key
        self.private_key = Path(private_key_path).read_bytes()
        self.public_key = Path(public_key_path).read_bytes()
        self.algorithm = "RS256"
        self.token_duration = timedelta(minutes=token_duration_minutes)

    # Firma un token nuevo. `data` es el dict que va en el payload
    def encode(self, data):
        now = datetime.now(timezone.utc)
        payload = {
            **data,
            # "iat" (issued at) y "exp" (expiration) ESTÁNDAR de JWT timestamps
            "iat": now,
            "exp": now + self.token_duration,
        }

        try:
            # self.private_key firmar (crear un token válido) SOLO se puede hacer con la llave privada. Esta es la razón de fondo por la que encode() y decode() usan llaves distintas.
            return jwt.encode(
                payload,
                self.private_key,
                algorithm=self.algorithm,
            )
        except jwt.PyJWTError as error:
            print(f"No se pudo generar el token: {error}")
            return None

    def decode(self, token):
        """Verifica un token recibido del cliente. Devuelve el payload
        (dict) si es válido, o None si es inválido/expirado/manipulado."""
        try:
            return jwt.decode(
                token,
                # PyJWT lanza una excepción — no hay que comprobarlo a mano.
                self.public_key,
                # algorithms=[self.algorithm] fuerza a PyJWT a aceptar ÚNICAMENTE RS256.
                algorithms=[self.algorithm],
                # Rechaza el token si le faltan estos claims
                options={"require": ["iat", "exp"]},
            )
        except jwt.PyJWTError as error:
            print(f"Token inválido: {error}")
            return None
