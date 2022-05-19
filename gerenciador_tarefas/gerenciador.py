# -*- coding: utf-8 -*-
"""
Created on Wed May 18 18:54:01 2022

@author: prumo
"""

from fastapi import FastAPI

app = FastAPI()

TAREFAS = []


@app.get("/tarefas")
def listar():
    return TAREFAS
