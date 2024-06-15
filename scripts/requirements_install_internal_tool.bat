call activate_vir_env.bat
echo Installing Internal tools requirements
pip install -r ..\requirements_internal_tool.yml
call deactivate_vir_env.bat
