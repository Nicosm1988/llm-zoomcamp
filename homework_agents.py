import random

# --- Preparation ---
known_weather_data = {
    'berlin': 20.0
}

def get_weather(city: str) -> float:
    """Genera datos de clima falsos para una ciudad."""
    city = city.strip().lower()
    if city in known_weather_data:
        return known_weather_data[city]
    return round(random.uniform(-5, 35), 1)

# --- Q1. Define function description ---
# Esta es la "receta" que el LLM leerá.
get_weather_tool = {
    "type": "function",
    "function": {
        "name": "get_weather",  # TODO1: El nombre exacto de nuestra función en Python.
        "description": "Obtiene el clima actual para una ciudad específica.", # TODO2: Una descripción clara y concisa de lo que hace la función.
        "parameters": {
            "type": "object",
            "properties": {
                "city": { # TODO3: El nombre exacto del parámetro que espera la función.
                    "type": "string",
                    "description": "El nombre de la ciudad para la cual se quiere obtener el clima, por ejemplo, Berlín." # TODO4: Una descripción de qué es este parámetro.
                }
            },
            "required": ["city"] # TODO5: Una lista de los parámetros que son obligatorios.
        }
    }
}