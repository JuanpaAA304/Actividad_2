# API de Biblioteca (FastAPI)

API simple para gestionar libros usando **solo estructuras en memoria** (listas/diccionarios), sin Pydantic ni bases de datos.

## Ejecutar

```bash
uvicorn main:app --reload
```

Servirá en `http://127.0.0.1:8000` y documentación en `http://127.0.0.1:8000/docs`.

## Datos de ejemplo en memoria
Al iniciar se cargan:
- `{"id": 1, "titulo": "Cien años de soledad", "autor": "Gabriel García Márquez"}`
- `{"id": 2, "titulo": "Don Quijote de la Mancha", "autor": "Miguel de Cervantes"}`

## Endpoints

- `GET /`  
  Mensaje de bienvenida.

- `GET /books`  
  Lista todos los libros.

- `GET /books/{book_id}`  
  Obtiene un libro por ID.

- `POST /books`  
  Crea un libro. Cuerpo JSON:
  ```json
  {
    "id": 3,
    "titulo": "El principito",
    "autor": "Antoine de Saint-Exupéry"
  }
  ```

- `PUT /books/{book_id}`  
  Actualiza un libro existente. Cuerpo JSON (campos opcionales `titulo`, `autor`):
  ```json
  {
    "titulo": "Título actualizado",
    "autor": "Autor actualizado"
  }
  ```
  Puedes enviar uno o ambos campos para actualizaciones parciales.

- `DELETE /books/{book_id}`  
  Elimina un libro por ID.

## Notas
- Datos simulados en memoria; se pierden al reiniciar.
- Sin modelos Pydantic ni conexiones a BD, siguiendo el tutorial de rutas y operaciones HTTP.