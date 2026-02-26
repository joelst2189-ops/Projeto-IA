@echo off
REM Cultura LAB.ia - Launcher
REM Este script abre a aplicação Streamlit automaticamente

setlocal enabledelayedexpansion

REM Obter o diretório do script
set "SCRIPT_DIR=%~dp0"
cd /d "%SCRIPT_DIR%"

REM Verificar se o Python está instalado
python --version >nul 2>&1
if errorlevel 1 (
    echo.
    echo ========================================
    echo ERRO: Python nao encontrado!
    echo ========================================
    echo.
    echo Instale Python 3.8+ de: https://www.python.org/
    echo.
    pause
    exit /b 1
)

REM Verificar se os requirements estão instalados
echo Verificando dependências...
python -m pip install -q -r requirements.txt

REM Abrir a aplicação Streamlit
echo.
echo ========================================
echo Iniciando Cultura LAB.ia...
echo ========================================
echo.
echo A aplicação será aberta em: http://localhost:8501
echo.
echo Pressione Ctrl+C para encerrar
echo.

python -m streamlit run app.py --logger.level=warning

pause
