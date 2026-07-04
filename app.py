from flask import Flask, jsonify
import time
import random

app = Flask(__name__)

@app.route("/")
def inicio():
    return """
    <h1>Comercial Andina S.A.C.</h1>
    <p>Aplicación demo para prueba de escalabilidad y autoescalado.</p>
    <a href="/cotizar">Generar cotizacion</a>
    """
    
@app.route("/cotizar")
def cotizar():
    inicio = time.time()
    
    # Simulación de proceso que consume recursos
    total = 0
    for i in range(300000):
        total += i * random.randint(1, 3)
        
    tiempo = round(time.time() - inicio, 3)
    
    return jsonify({
        "mensaje": "Cotización generada correctamente",
        "tiempo_respuesta": tiempo,
        "resultado": total
    })
    
@app.route("/salud")
def salud():
    return jsonify({"estado": "ok"})
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
