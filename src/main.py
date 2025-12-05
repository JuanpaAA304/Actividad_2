from fastapi import FastAPI, HTTPException
from typing import Any, Dict, List

app = FastAPI(title="API de Biblioteca (en memoria)")

books: List[Dict[str, Any]] = [
    {"id": 1, "titulo": "Cien años de soledad", "autor": "Gabriel García Márquez"},
    {"id": 2, "titulo": "Don Quijote de la Mancha", "autor": "Miguel de Cervantes"},
]

def _find_book_index(book_id: int) -> int:
    for idx, book in enumerate(books):
        if book["id"] == book_id:
            return idx
    raise HTTPException(status_code=404, detail="Libro no encontrado")

@app.get("/")
def read_root():
    return {"mensaje": "Bienvenido a la API de Biblioteca"}

@app.get("/books")
def list_books():
    return books

@app.get("/books/{book_id}")
def get_book(book_id: int):
    idx = _find_book_index(book_id)
    return books[idx]

@app.post("/books", status_code=201)
def create_book(book_data: Dict[str, Any]):
    required = {"id", "titulo", "autor"}
    if not required.issubset(book_data):
        raise HTTPException(status_code=400, detail="Faltan campos requeridos: id, titulo, autor")
    if any(existing["id"] == book_data["id"] for existing in books):
        raise HTTPException(status_code=400, detail="Ya existe un libro con ese id")
    books.append({"id": int(book_data["id"]), "titulo": book_data["titulo"], "autor": book_data["autor"]})
    return books[-1]

@app.put("/books/{book_id}")
def update_book(book_id: int, book_data: Dict[str, Any]):
    idx = _find_book_index(book_id)
    if not any(key in book_data for key in ("titulo", "autor")):
        raise HTTPException(status_code=400, detail="Proporcione al menos titulo o autor para actualizar")
    books[idx].update({k: v for k, v in book_data.items() if k in ("titulo", "autor")})
    return books[idx]

@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    idx = _find_book_index(book_id)
    removed = books.pop(idx)
    return {"detalle": "Libro eliminado", "libro": removed}