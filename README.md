# THE PITCH
#### This is a web application where a user can add,comment on,upvote and downvote a pitch,Current version:25 february 2019

### By **TUYISENGE Anabella**
## Description
The pitch is a web app where a user can add a one minute pitch and other users can comment on it and upvote or downvote it.These pitches are divided in different categories such as pickup lines ,interview pitches and so on.A user has to create an account and they have to be logged in to post,vote on or comment on a pitch

##Setup/Installations
### Prerequisites
* Python3.6
* Pip

### Cloning
* In your terminal<br>
   $ git clone https://github.com/Anabella1109/THE-PITCH.git
   $ cd THE-PITCH

### Install postgres
[Postgres]()
  
### Create virtual environment
sudo apt-get install python3.6-venv<br>
python3.6 -m venv virtual<br>
source virtual/bin/activate<br>

### Install dependencies
pip3 install -r requirements<br>

### Exporting environment variables
export DATABASE_URL='postgresql+psycopg2://username:password@localhost/thepitch'<br>
export SECRET_KEY='Your secret key'

## Run database migrations
python manage.py db init<br>
python manage.py db migrate -m "initial migration"<br>
python manage.py db upgrade

### Running
 * In your terminal<br>

     $ chmod +x start.sh<br>
     $ ./start.sh


