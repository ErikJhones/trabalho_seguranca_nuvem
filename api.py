from typing import Union
import uvicorn
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
import dinamo 
import bucket_s3

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
async def leitura_dinamo(nome: Union[str, None] = None):
    return dinamo.lendo(nome)

@app.get("/criandobucket/")
async def criando_bucket_s3():
    bucket_s3.criando_bucket()

@app.put("/escrevendobucket/")
async def escrevendo_bucket(file: UploadFile):
    bucket_s3.inserindo_bucket(file)

@app.get("/lendobucket/")
async def lendo_bucket():
    return bucket_s3.lendo_bucket()
    # return FileResponse("your_image.jpeg")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)