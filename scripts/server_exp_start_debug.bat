call activate_vir_env.bat
echo Starting Flask Server
cd ..
flask --app amenity_pj/helper/flask_exp/app.py --debug run --port 5002
cd scripts
call deactivate_vir_env.bat
