"""
Genera el par de llaves RSA (privada + pública)

Este script se corre UNA VEZ manualmente para generar el par de llaves y guardarlas en disco como archivos .pem, que jwt_manager.py luego lee.
"""

from pathlib import Path

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa


KEYS_DIRECTORY = Path(__file__).resolve().parent / "keys"
PRIVATE_KEY_PATH = KEYS_DIRECTORY / "private_key.pem"
PUBLIC_KEY_PATH = KEYS_DIRECTORY / "public_key.pem"


def generate_keys():
    KEYS_DIRECTORY.mkdir(exist_ok=True)

    if PRIVATE_KEY_PATH.exists() or PUBLIC_KEY_PATH.exists():
        raise FileExistsError(
            "Las claves ya existen. Elimínelas manualmente para generar otro par."
        )

    # --- Generar la llave privada ---
    # public_exponent=65537: valor estándar
    # key_size=2048: tamaño mínimo considerado seguro
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )

    # La llave pública se DERIVA matemáticamente de la privada
    public_key = private_key.public_key()

    # PEM es el formato de texto estándar para guardar llaves/certificados
    # PKCS8 es el estándar de estructura interna más común para llaves privadas
    # NoEncryption(): el archivo no lleva contraseña propia
    PRIVATE_KEY_PATH.write_bytes(
        private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption(),
        )
    )

    # SubjectPublicKeyInfo es el formato estándar para llaves públicas
    PUBLIC_KEY_PATH.write_bytes(
        public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo,
        )
    )

    # chmod 0o600 = solo el dueño del archivo puede leer/escribir
    PRIVATE_KEY_PATH.chmod(0o600)
    print("Par de claves RSA generado correctamente en la carpeta keys.")


if __name__ == "__main__":
    generate_keys()
