## Calculadora de Pensiones 📈

Una herramienta para calcular pensiones basada en historial salarial, datos demográficos y cotizaciones. Desarrollada en Python con manejo de excepciones y pruebas unitarias.
Python 3.10+
Licencia

Características principales ✨

- Cálculo pensional con base en 10 años de historial salarial

- Validación de requisitos de edad y semanas cotizadas

- Manejo de excepciones personalizadas

- Interfaz gráfica y de consola

- Pruebas unitarias integradas

## Estructura del proyecto 🗂️
```bash
Calculadora_Pensional/
├── README.md
├── src/
│   ├── controller/          
│   ├── model/
│   │   └── pylogic.py      # Lógica de cálculo principal
│   └── view/
│       ├── console.py       # Interfaz de línea de comandos
│       └── interfaz.py      # Interfaz gráfica (Kivy)
└── test/
    └── test_1.py           # Pruebas unitarias
```
## Requisitos previos ⚙️

- Python 3.10 o superior
- Gestor de paquetes pip
- Entorno virtual recomendado (venv)
- Dependencias:
  ```
  pip install kivy
  ```
## Instalación y configuración 🔧

1. Clonar este repositorio:
   ```bash
   git clone https://github.com/David2421b/Calculadora_Pensional.git
   cd Calculadora_Pensional
   ```
2. Crear y activar un entorno virtual:
   ```bash
      # Windows
    python -m venv venv
    venv\Scripts\activate
    # Linux/Mac
    python3 -m venv venv
    source venv/bin/activate
   ```
3. Instalar dependencias
   ```
   pip install -r requirements.txt  # Si existe el archivo
   pip install kivy                # Instalación directa
   ```
   
## Modos de ejecución 🚀

Interfaz de consola

```bash
src/view/console.py
```

## Datos requeridos:

- Género (1: Masculino, 2: Femenino)
- Edad actual
- Semanas cotizadas
- Número de hijos
- Salarios últimos 10 años (valores separados por comas)

Si los datos ingresados no cumplen con los requisitos mínimos para la pensión, se generará una excepción con el mensaje correspondiente.

## Interfaz gráfica
```
src/view/interfaz.py

```
## Ejecutar pruebas

El proyecto incluye pruebas unitarias para validar la lógica de cálculo de la pensión. Para ejecutar las pruebas, usa el siguiente comando:

```bash
python -m unittest discover -s tests
```

Esto ejecutará todas las pruebas ubicadas en la carpeta `tests`.

## Desarrollo y contribución 💻
Consola interactiva
Para experimentar con la lógica directamente:
```
>>> from src.model import pylogic
>>> pylogic.pension_total([2000000, 2500000, 2700000, 3000000], "Masculino", 63, 1400, 2)
```

Estructura del cálculo
```
def calcular_pension(salarios, genero, edad, semanas, hijos):
    # 1. Validar requisitos mínimos
    # 2. Calcular promedio salarial
    # 3. Aplicar factores de ajuste
    # 4. Retornar valor pensional
```

## 🛠️ Creación del APK

"⚙️ Configuración inicial en Google Colab"

- Crea un nuevo archivo en Google Colab.
- Sube los siguientes archivos al entorno:
- 📄 main.py (Interfaz gráfica desarrollada con Kivy)
- 📦 pylogic.py (Lógica del programa)
- 🖼️ logo.png (Icono de la aplicación)

"🚀 Ejecución de comandos"

- Ejecuta los siguientes comandos en orden y en celdas separadas:
  
```
>>> !pip3 install --user --upgrade buildozer
>>> !sudo apt update
>>> !sudo apt install -y git zip unzip openjdk-17-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev
>>> !pip3 install --user --upgrade Cython==0.29.33 virtualenv
>>> !/root/.local/bin/buildozer init
```
"🔧 Configuración del archivo buildozer.spec"

Tras ejecutar buildozer init, se generará el archivo buildozer.spec

Realiza las siguientes modificaciones clave:

- 🏷️ Establece el nombre de la aplicación (title).
- 📌 Especifica la ruta del icono (logo = logo.png).
- 📋 En la sección requirements, agrega: python3, kivy, kivymd.

Guarda los cambios y cierra el archivo.

"📤 Generación del APK"
Ejecuta el comando final para iniciar la compilación:

```
!/root/.local/bin/buildozer android debug
```
- ⏳ Durante el proceso (20-25 minutos aprox.),
- ✅ se solicitará confirmación interactiva. Presiona y cuando sea necesario.
- 📁 Al finalizar, se generará la carpeta bin/ con el APK listo para descargar e instalar.
  
## Manejo de excepciones 🛡️

El sistema incluye validaciones específicas para garantizar datos correctos:


Excepción -> Condición de error
NegativeNum	 -> Salarios negativos detectados
InvalidAgeError	 -> Edad inferior al mínimo requerido
InvalidWeeksError	-> Semanas cotizadas insuficientes
InvalidDatesError  -> Combinación edad/semanas no válida


## Autores 👥

- Simón Correa Bravo 
- David Hernández Mejía 
- Miguel Ángel Guarnizo 
- Tomás Mercado

## ¿Problemas o sugerencias?

- ✉️ Abre un issue en el repositorio.

## Entrevista  
📺 [Ver en YouTube](https://youtu.be/5jBNKtJzQe4?si=5xQrhLlG16mk0w0V)  

## Documento de Excel  
📂 [Abrir en Google Sheets](https://docs.google.com/spreadsheets/d/1kuuWBAFq2SusGgKoASq2CQfCwAenW69s/edit?usp=sharing&ouid=114415268604794066439&rtpof=true&sd=true)  
