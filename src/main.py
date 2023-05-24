import numpy as np
#from fastapi import FastAPI, Response
from dataclasses import dataclass, field



#app = FastAPI()
#
#@app.get("/")
#def read_root() -> Response:
#    return Response("The server is running.")
#
#
#@app.get("/calc")
#def read_root() -> Response:
#    a = np.array([1, 1])
#    b = np.array([2, 2])
#    return Response(str(np.linalg.norm(a, b)))