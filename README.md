# EFI Nº 1 
## Python 3 Flask
Esta guía te orientará en la configuración y ejecución de nuestra aplicación Flask utilizando Python, Flask, SQLAlchemy, Flask-Migrate y PyMySQL. También se incluyen los pasos para instalar XAMPP, que nos proporcionará un servidor local con MySQL.

### 1. Clonar el repositorio
Primero, clona el repositorio de la aplicación desde GitHub. Asegúrate de tener git instalado en tu sistema.

### Instalación de git:

Ubuntu: sudo apt install git

Windows: Descarga e instala Git desde su pagina oficial git-scm.com.
Ejecuta el archivo .exe y segui los pasos. Puedes revisar sus opciones. 

### 2. Crear un directorio para el proyecto
Ubuntu: Abre PowerShell o CMD.

Ejecuta los siguientes comandos:
mkdir nombre_del_directorio
cd nombre_del_directorio donde se encuentran tus archivos

Windows:
Abre PowerShell o CMD.

Ejecuta los siguientes comandos:
mkdir nombre_del_directorio
cd nombre_del_directorio donde se encuentran tus archivos

### 3. Clonar el repositorio en el directorio creado
git clone https://github.com/usuario/nombre_del_repositorio.git

Reemplaza usuario y nombre_del_repositorio con los valores correctos de tu repositorio personal. El mismo lo podes obtener desde tu perfil/code/local. 

### 4. Acceder al directorio del proyecto
cd nombre_del_repositorio

Configuración en Linux (Ubuntu)

#### 1. Instalación de Python y Entorno Virtual.

Actualiza el sistema:
sudo apt update

Instala Python 3 y pip:
sudo apt install python3 python3-pip

Crea y activa un entorno virtual:
python3 -m venv env
source env/bin/activate

Instala Flask y las dependencias necesarias:
pip install Flask Flask-SQLAlchemy Flask-Migrate PyMySQL

##### 2. Instalación y Configuración de XAMPP
Descarga XAMPP: Visita la página oficial de XAMPP y descarga la versión para Linux.
Da permisos de ejecución al instalador:
chmod +x xampp-linux-x64-*.run

###### Instala XAMPP:
sudo ./xampp-linux-x64-*.run

###### Inicia XAMPP:
sudo /opt/lampp/lampp start

Configura la base de datos:
Abre http://localhost en tu navegador.
Accede a phpMyAdmin y crea una nueva base de datos gestion_celulares.db

### 3. Ejecuta la Aplicación Flask
Abre el directorio del proyecto en tu editor de código.
Activa el entorno virtual si no lo has hecho:
source env/bin/activate

Inicia la aplicación Flask:
flask run --reload

Configuración en Windows

### 1. Instalación de Python y Entorno Virtual-
Descarga e instala Python 3 desde python.org. Asegúrate de seleccionar la opción para agregar Python al PATH durante la instalación. Debes tildar esta opcion. 
Abre PowerShell y navega al directorio del proyecto.
Crea y activa un entorno virtual:
python -m venv env
.\env\Scripts\Activate

### Instala Flask y las dependencias necesarias:
pip install Flask Flask-SQLAlchemy Flask-Migrate PyMySQL

### 2. Instalación y Configuración de XAMPP

Descarga XAMPP: Visita la página oficial de XAMPP y descarga la versión para Windows.
Instala XAMPP siguiendo las instrucciones del instalador.
Inicia XAMPP a través del Panel de Control de XAMPP.
Configura la base de datos:
Abre http://localhost en tu navegador.
Accede a phpMyAdmin y crea una nueva base de datos llamada gestion_celulares.db .

### 3. Ejecuta la Aplicación Flask
Abre el directorio del proyecto en tu editor de código.
Activa el entorno virtual si no lo has hecho:
.\env\Scripts\Activate

### Inicia la aplicación Flask:
flask run --reload
