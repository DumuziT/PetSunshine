from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/procesar_formulario', methods=['POST'])
def procesar_formulario():
    # Obtener los datos del formulario
    fila_materiales = request.form.getlist('FilaMateriales[]')
    materiales = request.form.getlist('Materiales[]')
    cantidad_materiales = request.form.getlist('CantidadMateriales[]')
    precio_unitario_materiales = request.form.getlist('PrecioUnitarioMateriales[]')
    precio_total_materiales = request.form.getlist('PrecioTotalMateriales[]')
    total_neto_materiales = request.form.get('TotalNetoMateriales')

    fila_trabajo = request.form.getlist('FilaTrabajo[]')
    trabajo = request.form.getlist('Trabajo[]')
    cantidad_trabajo = request.form.getlist('CantidadTrabajo[]')
    precio_unitario_trabajo = request.form.getlist('PrecioUnitarioTrabajo[]')
    precio_total_trabajo = request.form.getlist('PrecioTotalTrabajo[]')
    total_neto_trabajo = request.form.get('TotalNetoTrabajo')

    # Imprimir datos en la terminal
    print("Datos de Materiales:")
    for i in range(len(materiales)):
        print(f"{fila_materiales[i]}, {materiales[i]}, {cantidad_materiales[i]}, {precio_unitario_materiales[i]}, {precio_total_materiales[i]}")

    print(f"Total Neto Materiales: {total_neto_materiales}")

    print("\nDatos de Trabajo:")
    for i in range(len(trabajo)):
        print(f"{fila_trabajo[i]}, {trabajo[i]}, {cantidad_trabajo[i]}, {precio_unitario_trabajo[i]}, {precio_total_trabajo[i]}")

    print(f"Total Neto Trabajo: {total_neto_trabajo}")

    return 'Datos recibidos correctamente'


if __name__ == '__main__':
    app.run(debug=True)
