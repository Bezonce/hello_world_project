import numpy as np
from fastapi import FastAPI, HTTPException, Response

app = FastAPI()


def my_sum(a, b):
    return a + b


def vec_diff_length(a, b):
    return np.linalg.norm(a - b)


@app.get("/")
def read_root() -> Response:
    return Response("The hello world project server is running.")


@app.get("/calculate/")
def run_calculation() -> Response:
    return Response(str(vec_diff_length(np.array([1, 1]), np.array([2, 2]))))
