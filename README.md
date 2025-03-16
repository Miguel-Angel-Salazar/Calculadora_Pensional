# Calculadora de Pensiones

Este proyecto permite calcular la pensión con base en los salarios de los últimos 10 años, la edad, las semanas cotizadas y el número de hijos. Además, maneja excepciones personalizadas para validar las condiciones de edad y semanas cotizadas.

## Requisitos previos

- Python 3.10 o superior
- Tener instalado `venv` (entorno virtual de Python recomendado)
- Instalar las dependencias necesarias (si las hay)

## Instalación

1. Clonar este repositorio:
   ```bash
   git clone https://github.com/David2421b/Calculadora_Pensional.git
   ```
2. Crear y activar un entorno virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Linux/Mac
   venv\Scripts\activate  # En Windows
   ```

## Ejecución del programa

Para ejecutar la calculadora de pensiones, usa el siguiente comando:

```bash
src/view/console.py
```

El programa solicitará los siguientes datos:

- Género (1 para Masculino, 2 para Femenino)
- Edad
- Semanas cotizadas
- Número de hijos
- Salarios de los últimos 10 años

Si los datos ingresados no cumplen con los requisitos mínimos para la pensión, se generará una excepción con el mensaje correspondiente.

## Ejecutar pruebas

El proyecto incluye pruebas unitarias para validar la lógica de cálculo de la pensión. Para ejecutar las pruebas, usa el siguiente comando:

```bash
python -m unittest discover -s tests
```

Esto ejecutará todas las pruebas ubicadas en la carpeta `tests`.

## Consola interactiva

Si deseas probar funciones específicas en la consola de Python, sigue estos pasos:

1. Abre la terminal y activa el entorno virtual (si no está activado).

2. Ingresa al modo interactivo de Python:
   ```bash
   python
   ```
3. Importa el módulo `pylogic`:
   ```python
   from src.model import pylogic
   ```
4. Ejecuta pruebas personalizadas, por ejemplo:
   ```python
   print(pylogic.pension_total([2000000, 2500000, 2700000, 3000000], "Masculino", 63, 1400, 2))
   ```

## Manejo de errores

El programa maneja los siguientes errores:

- `NegativeNum`: Se lanza cuando se ingresa un salario negativo.
- `InvalidAgeError`: Se lanza si la edad es menor a la requerida.
- `InvalidWeeksError`: Se lanza si las semanas cotizadas son menores a las requeridas.
- `InvalidDatesError`: Se lanza si no se cumplen los requisitos de edad y semanas cotizadas.

---

## Uso

   1. Para ejecutar las pruebas unitarias, ejecute el siguiente comando desde la raiz:
      ```bash
      py test/test_1.py
      ```
   
   2. Para ejecutar el programa, corra el siguiente comando desde la raiz:
      ```bash
      py src/view/console.py
      ```
   
      

---
**Autores: Simon Correa Bravo, David Hernández Mejía**\
**Repositorio:** [GitHub](https://github.com/tu-usuario/tu-repositorio)


## Entrevista  
📺 [Ver en YouTube](https://youtu.be/5jBNKtJzQe4?si=5xQrhLlG16mk0w0V)  

## Documento de Excel  
📂 [Abrir en Google Sheets](https://docs.google.com/spreadsheets/d/1kuuWBAFq2SusGgKoASq2CQfCwAenW69s/edit?usp=sharing&ouid=114415268604794066439&rtpof=true&sd=true)  
