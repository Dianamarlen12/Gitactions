# Gitactions

#CREACIÓN DEL CONTENEDOR
docker run -it -p 8080:8080 -v /workspace/Gitactions/pruebas:/pruebas --name webapp1 -h webapp1 webapp1:v1

#CORRER NUESTRO DOCKERFILE
docker build -t webapp1:v1 .