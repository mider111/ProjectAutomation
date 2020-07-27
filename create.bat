@echo off 

Rem This command changes the path to where the batch file is located
cd /d %~dp0

set folder = %1

if "%1"=="" (
echo Project Name is NOT defined
)else python create.py %1



