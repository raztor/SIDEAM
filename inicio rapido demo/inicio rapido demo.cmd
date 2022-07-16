@echo off

:check-git
echo revisando si git esta instalado
echo.
git --version && (
  goto :inicio
) || (
  goto :git-installchoice
)
pause

:git-installchoice
cls
echo Instalar git (solo seleccionar no si no esta instalado)?
echo.
set choice=
set /p choice=Escribe s para SI o n para NO.
if not '%choice%'=='' set choice=%choice:~0,1%
if '%choice%'=='s' goto :git-install
if '%choice%'=='n' goto :inicio


:inicio
cls
echo clonar repositorio?
set choice=
set /p choice=Escribe s para SI o n para NO.
if not '%choice%'=='' set choice=%choice:~0,1%
if '%choice%'=='s' goto :git
if '%choice%'=='n' goto :selecpyt


:git-install
start git-install.exe


:git
echo iniciando clonacion
git clone https://github.com/Raztorr/SIDEAM.git
echo clonacion exitosa
timeout 2
goto :slecpyt


:selecpyt
echo.
echo instalar pytorch?
set choice=
set /p choice=Escribe s para SI o n para NO.
if not '%choice%'=='' set choice=%choice:~0,1%
if '%choice%'=='s' goto :pytorch
if '%choice%'=='n' goto :selecrequ


:pytorch
echo instalando Py Torch Cuda...
echo =========================
echo.
py -m pip install --no-input torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu113
goto :selecrequ

:selecrequ
cls
echo Instalar requirements.txt?
echo.
set choice=
set /p choice=Escribe s para SI o n para NO.
if not '%choice%'=='' set choice=%choice:~0,1%
if '%choice%'=='s' goto :requirements.txt
if '%choice%'=='n' goto :selecinicio

:requirements.txt
echo instalando requirements.txt...
py -m pip install --no-input -r requirements.txt
goto :selecinicio

:selecinicio
cls
echo Iniciar demo?
echo.
set choice=
set /p choice=Escribe s para SI o n para NO.
if not '%choice%'=='' set choice=%choice:~0,1%
if '%choice%'=='s' goto :iniciar
if '%choice%'=='n' goto :end

:iniciar
echo iniciando test2.py
py test2.py
goto :end

:end
cls
echo instalacion finalizada
pause