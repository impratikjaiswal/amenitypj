call activate_vir_env.bat
echo Starting Flask Server
cd ..
flask --app amenity_pj_app/helper/flask_demo/app.py --debug run --port 5001
cd scripts
call deactivate_vir_env.bat
