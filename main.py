from fastapi import FastAPI
from typing import Optional

app = FastAPI()


@app.get('/')
def index():
    return {'data': 'blog list'}


@app.get('/blog')
def select(limit: int = 10, published: bool = True, sort: Optional[str] = None):
    if published:
        return {'data': f'{limit} published blogs from the db'}
    else:
        return {'data': f'{limit} blogs from the db'}


@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'all unpublished blogs'}


@app.get('/blog/{id}')
def show(id: int):
    return {'data': {'blog': id}}


@app.get('/blog/{id}/comments')
def show(id: int):
    return {'data': {'blog': [1, 2]}}
