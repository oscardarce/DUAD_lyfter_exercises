Paso #1 : El primer paso es crear o generar los archivos .pem privado y publico para eso vamos a correr el archivo de generate_keys.py desde consola.

Para esto es necesario tener instalado cryptography

Paso #2: Se debe de correr el main.py para poner a correr el servidor.

Paso #3: Procedemos a la prueba de crear un administrador enviando un objeto tipo administrador en el body al endpoint http://127.0.0.1:5000/register en una solicitud tipo post

Paso #4: Debe de crearse un cliente para eso vamos a registrar un cliente por medio de http://127.0.0.1:5000/clients/register en una solicitud tipo post

Paso #5: Vamos a hacer pruebas con el administrador para ella vamos a loguearnos con el usuario administrador ya previamente creado http://127.0.0.1:5000/login y esperamos el 200 con el token de autenticación.

Paso #6: Creamos una variable temporal del token para no estar copiando y pegando cada vez que hagamos una solicitud http desde el administrador para esto lo vamos a hacer desde la vista de scripts

Paso #7: Mandamos el el bearer el admin_token y crear un producto desde el usuario de admin http://127.0.0.1:5000/products

Paso #8: Logueamos a nuestro usuario cliente creado previamente, para ello vamos a crear una nueva variable global para guardar el token de la sesión del cliente, y cambiar desde la vista del script donde vamos a setear nuestra variable temporal cambiando el admin_token por la variable que acabamos de crear client_token

Paso #9: Realizamos una venta desde el perfil del cliente para ello enviamos en un POST a http://127.0.0.1:5000/sales id del producto y la cantidad.

Paso #10: Obtenemos el id del cliente por medio de una solicitud GET al endpoint http://127.0.0.1:5000/me de esta manera podemos consultar las facturas activas del cliente por medio de su id.
