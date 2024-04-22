git Clone https://github.com/RahulSaini3125/Auction.git
cd ./Auction
python -m venv .venv
.venv/scripts/activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
