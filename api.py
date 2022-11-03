from typing import Union

from fastapi import FastAPI
from fastapi.responses import FileResponse
import dinamo 

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/criandodinamo")
def criando_dinamo():
    dinamo.criando_tabela()

@app.get("/deletandodinamo")
def deletando_dinamo():
    dinamo.deletando_tabela()

@app.put("/escritadinamo/")
async def escrita_dinamo(nome: Union[str, None] = None, matricula: Union[str, None] = None):
    dinamo.escrevendo(nome, matricula)

@app.get("/leituradinamo/")
def leitura_dinamo(nome: Union[str, None] = None):
    return dinamo.lendo(nome)

@app.get("/lendobucket/")
async def lendo_bucket():
    return FileResponse("your_image.jpeg")