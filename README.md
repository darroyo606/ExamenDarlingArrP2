# ExamenDarlingArrP2
Crear un servicio web (usando Python + Flask o Django) que acceda a esa base de datos y haga algo (puede ser simplemente un print) o algo más elaborado como un buscador web

Creamos el archivo requirements.txt 
Aqui colocaremos
requests==2.31.0
pymongo==4.5.0
python-dotenv==1.0.0
flask
# Creamos nuestro archivo mongodb.py 
Para tener la conexion de la Base de Datos, es importante mencionar que tenermos un archivo
.env en el cual tenemos nuestro usuario y contraseña que nos permitirán acceder a nuestra data de la BDD

El formato del mismo es el siguiente:
MONGO_USER=tu usuario
MONGO_PASSWORD=tu password
# La Base de Datos se visualiza asi:
![image](https://github.com/darroyo606/ExamenDarlingArrP2/assets/55005126/fb376cc5-59de-4a7c-adfa-0446b7a68808)

Lo que quiere decir que se encuentra grabando los campos de forma adecuada.

# Creamos nuestro archivo DePrati.py
Aqui realizaremos la obtención de los datos que se encuentran el la base de datos:
El enlace para ver los datos es:http://127.0.0.1:5000/get-productos
![image](https://github.com/darroyo606/ExamenDarlingArrP2/assets/55005126/a6a4c224-7a1c-42fe-a030-ef14ff92f494)

Hemos eliminado uno de los campos del producto que es el stock status ya que al momento de extraer la variable
se encontraba en null indistintamente por lo que la hemos comentado por no ser un dato relevante.

