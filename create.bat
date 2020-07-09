@echo off 

d:

cd /MyProjects/ProjectAutomation

set project = %1

if "%1"=="" (
echo Project Name is NOT defined
)else python3 create.py %1



