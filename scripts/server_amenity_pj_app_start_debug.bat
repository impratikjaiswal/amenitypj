call activate_vir_env.bat
echo Starting Flask Server
cd ..
flask --app amenity_pj_app/app.py --debug run
cd scripts
call deactivate_vir_env.bat
