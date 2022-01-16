# winbot/__init__.py

print("Modulo importado exitosamente")

# Le indicamos que al moemnto de importar el modulo winbot, queremos que se importe la clase MouseBot de windows.py
# Esto nos evitara tener que escribir el nombre del archivo "windows.py" cada vez que utilizemos la clase MouseBot
from .windows import MouseBot
