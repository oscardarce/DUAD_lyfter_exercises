# Pasos tomados en cuenta para realizar la normalización:

1. Eliminar los datos duplicados de la tabla, en primer lugar identifique los datos que se repetían, y ya solo con eso se sabe que se debe crear otra tabla nueva por aparte.

2. Se identifican las dependencias de las tablas, para asegurar de que cada fila es única

3. Separar los datos en una tabla independiente, si a la hora de crear una tabla se repiten datos.

4. Validamos que nuestros datos no tengan redundancia, de que cada tabla tiene su id (pk), de que cada una tiene logica y validación de que existe una dependencía directa o transitiva.

5.Creo que se puede llegar a hacer menos tablas, en el segundo ejercicio de automoviles, pero al ejercicio no tener detalles, pienso que son las tablas necesarias. (Pense que VIN se puede cambiar a vehículo y crear una tabla con referencias de FK a make,colors,brand y year) pero al no especificar decidi no hacerlo.


# Cambios solicitados realizados

1. En orders se agregaron las tablas cruz de Special Request y Addres_Per_Client
2. Las tablas Cruz se agregaron a final order

4. En La tabla Cars se agrego year a la tabla Make
5. Se elimino la tabla VIN y se agrego a Car Detail para evitar duplicidad innecesaria
6. Se agrego a la tabla policies id_insurance