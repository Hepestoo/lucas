from flask import Flask, jsonify, request, render_template_string

app = Flask(__name__)


HTML_HOME = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Lucas AI - v1.0.5</title>
    <style>
        body {
            font-family: 'Helvetica Neue', Arial, sans-serif;
            background-color: #f4f6f9;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            color: #333;
        }
        .card {
            background: white;
            padding: 2rem;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            width: 100%;
            max-width: 400px;
            text-align: center;
        }
        h1 {
            color: #2c3e50;
            margin-bottom: 0.5rem;
        }
        .version {
            color: #7f8c8d;
            font-size: 0.9rem;
            margin-bottom: 1.5rem;
            display: block;
        }
        textarea {
            width: 100%;
            padding: 10px;
            margin-bottom: 1rem;
            border: 1px solid #ddd;
            border-radius: 5px;
            box-sizing: border-box; /* Para que el padding no rompa el ancho */
            min-height: 80px;
            font-family: inherit;
        }
        button {
            background-color: #3498db;
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 5px;
            cursor: pointer;
            font-size: 1rem;
            width: 100%;
            transition: background 0.3s;
        }
        button:hover {
            background-color: #2980b9;
        }
        #resultado {
            margin-top: 1.5rem;
            padding: 10px;
            background-color: #eef2f7;
            border-radius: 5px;
            display: none; /* Oculto por defecto */
            font-weight: bold;
        }
    </style>
</head>
<body>

<div class="card">
    <h1>Examen</h1>
    <span class="version">Versión 1.0.5</span>

    <!-- Formulario Simple -->
    <textarea id="textoInput" placeholder="Escribe tu texto aquí..."></textarea>
    <button onclick="analizarTexto()">Analizar</button>

    <div id="resultado"></div>
</div>

<script>
    async function analizarTexto() {
        const texto = document.getElementById('textoInput').value;
        const divResultado = document.getElementById('resultado');

        if (!texto) {
            alert("Por favor escribe algo.");
            return;
        }

        divResultado.style.display = 'block';
        divResultado.innerText = "Procesando...";

        try {
            const respuesta = await fetch('/predict', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ text: texto })
            });

            const datos = await respuesta.json();
            divResultado.innerText = `Puntaje: ${datos.score} | Input: ${datos.input}`;
        } catch (error) {
            divResultado.innerText = "Error al conectar con la API.";
        }
    }
</script>

</body>
</html>
"""

@app.get("/")
def home():
    return render_template_string(HTML_HOME)

@app.get("/predict")
def predict_get():

    text = request.args.get("text", "")
    return jsonify({
        "input": text,
        "score": len(text),
        "version": "1.0.5"
    })

@app.post("/predict")
def predict_post():

    data = request.get_json(silent=True) or {}
    text = data.get("text", "")
    return jsonify({
        "input": text,
        "score": len(text),
        "version": "1.0.5"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)