python copy_work.py

@echo off
set curpath=%~dp0

@rem cd ..
@rem set KBE_ROOT=%cd%
::已经预设 KBE_ROOT 环境变量
@rem set KBE_ROOT=F:\kbengine\kbengine
set KBE_RES_PATH=%KBE_ROOT%/kbe/res/;%curpath%/;%curpath%/scripts/;%curpath%/res/
set KBE_BIN_PATH=%KBE_ROOT%/kbe/bin/server/

if defined uid (echo UID = %uid%)

cd %curpath%
call "kill_server.bat"

echo KBE_ROOT = %KBE_ROOT%
echo KBE_RES_PATH = %KBE_RES_PATH%
echo KBE_BIN_PATH = %KBE_BIN_PATH%

set /p name= ma log inter db bm cm ba ca login:  

if "%name%" == "ma" ( start "machine" "%KBE_BIN_PATH%/machine.exe" --cid=1000 --gus=1 )
if "%name%" == "log" ( start "logger" "%KBE_BIN_PATH%/logger.exe" --cid=2000 --gus=2 )
if "%name%" == "inter" ( start "interfaces" "%KBE_BIN_PATH%/interfaces.exe" --cid=3000 --gus=3 )
if "%name%" == "db" ( start "dbmgr" "%KBE_BIN_PATH%/dbmgr.exe" --cid=4000 --gus=4 )
if "%name%" == "bm" ( start "baseappmgr" "%KBE_BIN_PATH%/baseappmgr.exe" --cid=5000 --gus=5 )
if "%name%" == "cm" ( start "cellappmgr" "%KBE_BIN_PATH%/cellappmgr.exe" --cid=6000 --gus=6 )
if "%name%" == "ba" ( start "baseapp" "%KBE_BIN_PATH%/baseapp.exe" --cid=7001 --gus=7 )
if "%name%" == "ca" ( start "cellapp" "%KBE_BIN_PATH%/cellapp.exe" --cid=8001 --gus=9 )
if "%name%" == "login" ( start "loginapp" "%KBE_BIN_PATH%/loginapp.exe" --cid=9000 --gus=11 )
if "%name%" == "" ( 
start "machine" "%KBE_BIN_PATH%/machine.exe" --cid=1000 --gus=1
start "logger" "%KBE_BIN_PATH%/logger.exe" --cid=2000 --gus=2
start "interfaces" "%KBE_BIN_PATH%/interfaces.exe" --cid=3000 --gus=3
start "dbmgr" "%KBE_BIN_PATH%/dbmgr.exe" --cid=4000 --gus=4
start "baseappmgr" "%KBE_BIN_PATH%/baseappmgr.exe" --cid=5000 --gus=5
start "cellappmgr" "%KBE_BIN_PATH%/cellappmgr.exe" --cid=6000 --gus=6
start "baseapp" "%KBE_BIN_PATH%/baseapp.exe" --cid=7001 --gus=7
@rem start "" "%KBE_BIN_PATH%/baseapp.exe" --cid=7002 --gus=8 --hide=1
start "cellapp" "%KBE_BIN_PATH%/cellapp.exe" --cid=8001 --gus=9
@rem start "" "%KBE_BIN_PATH%/cellapp.exe" --cid=8002  --gus=10 --hide=1
start "loginapp" "%KBE_BIN_PATH%/loginapp.exe" --cid=9000 --gus=11
)