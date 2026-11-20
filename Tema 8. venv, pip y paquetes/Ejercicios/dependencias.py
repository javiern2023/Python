'''
Crear un archivo de dependencias y reproducir el entorno.

1.- Crear el archivo requirements.txt.
pip freeze > requirements.txt

2.- Crear un nuevo entorno virtual para comprobar que podemos reproducirlo.
python -m venv nuevo_venv

3.- Activar el nuevo entorno virtual.
nuevo_venv\Scripts\activate  Windows
source nuevo_venv/bin/activate  Linux o Mac

4.- Instalar todas las dependencias del archivo
pip install -r requirements.txt

5.- Comprobar que se ha instalado correctamente
pip list
'''