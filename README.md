# ocr_poc
Un repositorio para probar OCR

## Requisitos

- Tesseract: necesitas intalar tesseract-ocr en tu maquina. Esto es lo que esta realmente haciendo el OCR.

  Para instalar siga las [instrucciones para su plataforma](https://github.com/tesseract-ocr/tesseract/wiki#installation).

- Python 3.7
- [Pipenv](https://pipenv.pypa.io/en/latest/install/#installing-pipenv)

  Una vez instalado ejecuta `$ pipenv install` para instalar todas las dependencias de Python.

## Ejecutando el programa

- Necesitas activar el virtual env que creo pipenv en el paso anterior. Para hacer esto ejecuta `$ pipenv shell`
- Luego ejecta `python app.py`
- Para cambiar la foto que se esta procesando necesitas cambiarla dentro del `app.py`