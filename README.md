# Petstore API Testing with Python

El proyecto realiza pruebas funcionales y de carga con locust sobre el endpoint POST `/pet` del API Swagger Petstore.

## Estructura del proyecto

```
petstore_post_api_test/
├── services/           # Logica de conexion al endpoint
├── tests/              # Casos de prueba funcional
├── utils/              # Generacion de datos/payloads
├── locustfiles/        # Configuración para prueba de carga
```

## Cómo ejecutar

### 1. Instalacion de dependencias
Primero se instalan las dependencias indicadas en el requirements con el siguiente comando:
```bash
pip install -r requirements.txt
```

### 2. Para ejecucion de pruebas funcionales se debe ejecutar el siguiente comando:
```bash
python -m unittest tests/test_add_pet.py
```

### 3. Para ejecutar pruebas de carga con Locust se debe ejecutar el siguiente comando
```bash
python -m locust -f locustfiles/locustfile.py
```

### 4. Para para configurar y lanzar la carga:

Abrir en el navegador la siguiente URL `http://localhost:8089`
