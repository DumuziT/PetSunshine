import openpyxl
from openpyxl.styles import Border, Side, PatternFill, Font

# Nombre del archivo Excel original
archivo_original = 'aaa.xlsx'

# Nombre del archivo Excel de destino
archivo_destino = 'aaa.xlsx'

# Cargar el libro de trabajo (workbook)
libro_trabajo = openpyxl.load_workbook(archivo_original)

# Seleccionar la hoja de trabajo (worksheet) activa
hoja_trabajo = libro_trabajo.active

# Conseguir Color
colorFondo = hoja_trabajo['A1'].fill.start_color.rgb

Fila = int(input("Inserte fila nueva: "))
Text = str(input("Texto: "))

# Crear una nueva fila en la posición deseada (en este caso, la cuarta fila)
nueva_fila = hoja_trabajo.insert_rows(Fila)

# Realizar las operaciones de edición en la nueva fila, por ejemplo, establecer valores en celdas específicas
hoja_trabajo.cell(row=Fila, column=1, value=Text).font = Font(color='FFFFFF', name='Arial', size=10)

# Definir un fondo amarillo para todas las celdas en la nueva fila
for columna in range(1, hoja_trabajo.max_column + 1):
    celda = hoja_trabajo.cell(row=Fila, column=columna)
    celda.fill = PatternFill(start_color=colorFondo, end_color=colorFondo, fill_type='solid')
    celda.border = Border(left=Side(style='thin', color='FFFFFF'), right=Side(style='thin', color='FFFFFF'), top=Side(style='thin', color='FFFFFF'), bottom=Side(style='thin', color='FFFFFF'))

# Guardar el libro de trabajo modificado con un nuevo nombre
libro_trabajo.save(archivo_destino)

# Cerrar el libro de trabajo
libro_trabajo.close()
