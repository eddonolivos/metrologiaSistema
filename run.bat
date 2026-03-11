@echo off
setlocal

:: Obtener la ruta donde está el .bat
set PROJECT_DIR=%~dp0

:: Ir a la raíz del proyecto
cd /d "%PROJECT_DIR%"

:: Verificar que exista el entorno virtual
if not exist ".venv\Scripts\activate.bat" (
    echo ERROR: No se encontró el entorno virtual .venv
    pause
    exit /b 1
)

:: Activar entorno virtual
call ".venv\Scripts\activate.bat"

:: Ejecutar el proyecto
python main.py

pause