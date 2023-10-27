# Ayulla
#Clone the repository to your local machine:
git clone https://github.com/Zamokuhle23/hospital_management_api.git
#Create a virtual environment:
 python3 -m venv venv
#Activate the virtual environment:
source venv/bin/activate
#Install the project's dependencies:
pip install -r requirements.txt
#Migrate the database:
python manage.py migrate
#Start the development server:
python manage.py runserver
#Open a web browser and navigate to the following URL:
http://localhost:8000/
