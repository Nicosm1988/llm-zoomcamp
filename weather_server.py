# Importamos las librerías necesarias
from fastmcp import FastMCP
import random

# Definimos nuestra "base de datos" inicial
known_weather_data = {
    'berlin': 20.0
}

# Creamos una instancia del servidor MCP. Le damos un nombre descriptivo.
mcp = FastMCP("Weather Service 🌦️")

# El decorador '@mcp.tool' le dice a FastMCP que esta función es una herramienta disponible.
# FastMCP leerá el docstring (el texto entre """...""") para generar la descripción JSON automáticamente.
@mcp.tool
def get_weather(city: str) -> float:
    """
    Retrieves the temperature for a specified city.
    Parameters:
        city (str): The name of the city for which to retrieve weather data.
    Returns:
        float: The temperature associated with the city.
    """
    city = city.strip().lower()
    if city in known_weather_data:
        return known_weather_data[city]
    return round(random.uniform(-5, 35), 1)

# Hacemos lo mismo para nuestra segunda función.
@mcp.tool
def set_weather(city: str, temp: float) -> str:
    """
    Sets the temperature for a specified city.
    Parameters:
        city (str): The name of the city for which to set the weather data.
        temp (float): The temperature to associate with the city.
    Returns:
        str: A confirmation string 'OK' indicating successful update.
    """
    city = city.strip().lower()
    known_weather_data[city] = temp
    return 'OK'

# Este bloque asegura que el servidor solo se ejecute cuando corremos este archivo directamente.
if __name__ == "__main__":
    mcp.run()