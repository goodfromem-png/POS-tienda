from flask import Flask, render_template_string, request, jsonify

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Punto de Venta</title>
    <style>
        body { font-family: sans-serif; padding: 20px; background: #f4f6f9; }
        .box { background: white; padding: 20px; border-radius: 8px; max-width: 500px; margin: auto; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }
        input { width: 100%; padding: 10px; font-size: 18px; margin-bottom: 10px; box-sizing: border-box; }
        button { width: 48%; padding: 12px; font-size: 16px; font-weight: bold; border: none; border-radius: 5px; cursor: pointer; color: white; }
        .btn-efectivo { background: #28a745; }
        .btn-tarjeta { background: #007bff; }
        .resumen { margin-top: 20px; padding: 15px; background: #eef2f7; border-radius: 5px; }
    </style>
</head>
<body>
    <div class="box">
        <h2>🛒 Punto de Venta</h2>
        <label>Monto a cobrar:</label>
        <input type="number" id="monto" placeholder="$0.00">
        <div>
            <button class="btn-efectivo" onclick="cobrar('Efectivo')">💵 Efectivo</button>
            <button class="btn-tarjeta" onclick="cobrar('Maquinita')">💳 Maquinita</button>
        </div>
        <div class="resumen">
            <h3>📊 Ventas del Día</h3>
            <p>Efectivo: <b id="totalEfectivo">$0.00</b></p>
            <p>Maquinita: <b id="totalTarjeta">$0.00</b></p>
        </div>
    </div>

    <script>
        let totalEfectivo = 0;
        let totalTarjeta = 0;

        function cobrar(metodo) {
            let val = parseFloat(document.getElementById('monto').value);
            if (!val || val <= 0) return alert('Ingresa un monto válido');

            if (metodo === 'Efectivo') {
                totalEfectivo += val;
                document.getElementById('totalEfectivo').innerText = '$' + totalEfectivo.toFixed(2);
            } else {
                totalTarjeta += val;
                document.getElementById('totalTarjeta').innerText = '$' + totalTarjeta.toFixed(2);
            }

            document.getElementById('monto').value = '';
            alert('Venta registrada en ' + metodo);
        }
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
