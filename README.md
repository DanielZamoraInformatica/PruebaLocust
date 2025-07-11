# Petstore API Testing with Python

El proyecto realiza pruebas funcionales y de carga sobre el endpoint POST `/pet` del API Swagger Petstore.

## Tecnologías usadas

- Python
- `requests` para peticiones HTTP
- `unittest` para validaciones funcionales
- `locust` para pruebas de carga

## Estructura del proyecto

```
petstore_post_api_test/
├── services/           # Logica de conexion al endpoint
├── tests/              # Casos de prueba funcional
├── utils/              # Generacion de datos/payloads
├── locustfiles/        # Configuración para prueba de carga
```

## Cómo ejecutar

### 1. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 2. Ejecutar pruebas funcionales

```bash
python -m unittest tests/test_add_pet.py
```

### 3. Ejecutar pruebas de carga con Locust

```bash
python -m locust -f locustfiles/locustfile.py
```

Y abre `http://localhost:8089` para configurar y lanzar la carga.
