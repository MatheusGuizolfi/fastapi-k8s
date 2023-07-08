from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {"message": "Hello Matheus"}

@app.get("/hello/{name}")
def hello_person(name):
    return {"message": "Hello {}".format(name)}
