
# Recomendación de compras por similitud coseno


## Instalación
Es recomendable ejecutar el proyecto en un entorno virtual. Puedes crear esto haciendo uso de:

```bash
python -m venv env
```

Luego, activa el entorno virtual:

- En Windows:
    ```bash
    .\env\Scripts\activate
    ```
- En macOS y Linux:
    ```bash
    source env/bin/activate
    ```

Después, instala las dependencias del proyecto:

```bash
pip install -r requirements.txt
```

## Ejecución

Una vez hecho, para correr la aplicación utiliza:

```bash
flask --app index run --debug -p 8080
```

### Consideraciones

- La aplicación se ejecuta en modo debugger.
- Se ejecuta en el puerto 8080.
- El servidor no es apto para producción, es solamente un servidor de desarrollo.

## Datos

Los datos originales se encuentran en el archivo: `dataset/electronics.csv`.

Estos son formateados y filtrados mediante el script: `formatData.py`, el cual retorna datos almacenados en: `dataset/dataFormated.csv`.

Este último es utilizado para todo el funcionamiento del sitio web.
