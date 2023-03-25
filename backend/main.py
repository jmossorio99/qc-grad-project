from fastapi import FastAPI
from qplex.examples.portfolio import run

app = FastAPI()


@app.get("/")
async def read_root():
    objective_value = run(20, 200)
    return {"Objective Value": objective_value}
