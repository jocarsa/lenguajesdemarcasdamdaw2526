En terminal:

sudo apt install apache2

De ahi en adelante, todos los archivos que hagáis tendrán que estar en:
/var/www/html

Liberación de permisos:

cd /var/www
cd = Change directory (Win, Linux, macOS)
sudo chmod 777 -R html

sudo = El super usuario va a hacer algo
chmod = cambiamos permisos de archivo y carpeta
777 = los tres grupos pueden hacer de todo
-R = recursivo (se aplica a todo lo contenido)
html = la carpeta de destino

sudo apt install php