from django.http import HttpResponse
from djangoProyect.settings import bubbleSort, linearSearch, makeA, bS, lS
import pandas as pd
import time

def main(request, x): # URL: http://127.0.0.1:8000/main/317243489
    A = makeA()
    
    page = f"""
    <!DOCTYPE html>
    <html lang="esp">
        <head>
            <meta charset="UTF-8">
            <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css">
            <link href="style.css" rel="stylesheet">
            <title>BubbleSort & LinearSearch</title>
        </head>

        <body>
            <div class="p-3 mb-2 bg-light text-dark">
                <div>
                    <h1 class="mx-auto" style="width: 50%;">BubbleSort & LinearSearch(Secuencial)</h1>
                </div>
                <br>
                <div class="alert alert-secondary" role="alert">
                    <h4 class="alert-heading">Rosales Herrera Jonathan Adrian</h4>
                    Proyecto desarrollado para la asignatira <strong><em>Computación Concurrente</em></strong> 
                    de la carrera en <strong><i>Ciencia de Datos</i></strong>. Impartida por la <b>UNAM</b>.
                    <hr>
                    No. de Cuenta: <u>317243286</u>
                </div>
                <div>
                    <div class="alert alert-success" role="alert">
                    <b>Números de Cuenta creados</b>
                    </div>
                    <p>{A}</p>
                    <br>
                    <h2>No. de Cuenta a buscar: <span class="badge bg-secondary">{x}</span></h2>
                </div>
                <div>
                    <h5>Ordenando...</h5>
                    <div class="alert alert-success" role="alert">
                        {pd.Series(bubbleSort(A))}
                    </div>

                    <h5>Buscando número de cuenta...</h5><br>
                    <p>Encontrado en la posición: {linearSearch(A, x)}</p>
                </div>
                <div class="alert alert-warning" role="alert">
                    Ve a <a href="#" class="alert-link">http://127.0.0.1:8000/concurrente/X</a> para el paradigma concurrente.
                </div>
            </div>
        </body>
    </html>
    """
    return HttpResponse(page)

def concurrente(request, x):
    A = makeA()

    page = f"""
    <!DOCTYPE html>
    <html lang="esp">
        <head>
            <meta charset="UTF-8">
            <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css">
            <link href="style.css" rel="stylesheet">
            <title>BubbleSort & LinearSearch</title>
        </head>

        <body>
            <div class="p-3 mb-2 bg-light text-dark">
                <div>
                    <h1 class="mx-auto" style="width: 50%;">BubbleSort & LinearSearch(Concurrente)</h1>
                </div>
                <br>
                <div class="alert alert-secondary" role="alert">
                    <h4 class="alert-heading">Rosales Herrera Jonathan Adrian</h4>
                    Proyecto desarrollado para la asignatira <strong><em>Computación Concurrente</em></strong> 
                    de la carrera en <strong><i>Ciencia de Datos</i></strong>. Impartida por la <b>UNAM</b>.
                    <hr>
                    No. de Cuenta: <u>317243286</u>
                </div>
                <div>
                    <div class="alert alert-success" role="alert">
                    <b>Números de Cuenta creados</b>
                    </div>
                    <p>{A}</p>
                    <br>
                    <h2>No. de Cuenta a buscar: <span class="badge bg-secondary">{x}</span></h2>
                </div>
                <div>
                    <h5>Ordenando...</h5>
                    <div class="alert alert-success" role="alert">
                        {pd.Series(bS(A))}
                    </div>
                    <h5>Buscando número de cuenta...</h5><br>
                    <p>Encontrado en la posición: </p>
                    <list>
                        <ul>
                        <li>T1: {lS(A, x, axis=0)}</li>
                        <li>T2: {lS(A, x, axis=1)}</li>
                        </ul>
                    </list>
                </div>
                <div class="alert alert-warning" role="alert">
                    Ve a <a href="#" class="alert-link">http://127.0.0.1:8000/main/X</a> para el paradigma secuencial.
                </div>
            </div>
        </body>
    </html>
    """
    return HttpResponse(page)

