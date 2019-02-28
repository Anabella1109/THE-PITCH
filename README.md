# 60 SECONDS PITCH
#### This is a web application where a user can add,comment on,upvote and downvote a pitch,Current version:25 february 2019

### By **TUYISENGE Anabella**
## Description
The pitch is a web app where a user can add a one minute pitch and other users can comment on it and upvote or downvote it.These pitches are divided in different categories such as pickup lines ,interview pitches and so on.A user has to create an account and they have to be logged in to post,vote on or comment on a pitch

## BDD
| Behavior            | Input                         | Output                        | 
| ------------------- | ----------------------------- | ----------------------------- |
| Signing up | Fill in the form in the signup page | Redirects to the login page |
| Signing in | Fill in the form in the signin page | Redirects to the home page |
| Posting a pitch | In the home page, enter your pitch in text, select a category in the drop down menu and hit Pitch It Button! | Reloads the page with the pitch as the newest pitch |
| Liking a pitch | Press the thumbs up button | Redirects the user to the specific pitch, and the like counter goes to 1 |
| Disliking a pitch | Press the thumbs down button | Redirects the user to the specific pitch, and the dislike counter goes to 1 |
| Leaving feedback on the pitch | Type the feedback on the text area field in the pitch page, and hit post comment | Reloads the page and posts the feedback. The comments will be shown from the most recent |
| Viewing user profile | Click on the users name | Redirects the user to the clicked user profile |
| Uploading a photo | Click on the choose file button and choose file | The page will be refreshed with the profile photo updated |
| Editing the bio | Click on the ```edit bio``` button and enter your bio  | Redirects the page back to the profile page with an updated bio |

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

## Technologies used
* Python3.6
* HTML
* Bootstrap
* CSS
* Postgresql


## Support and contact details

Having any issues?
Email:bellaxbx1109@gmail.com
Slack:TUYISENGE Anabella

### License

[MIT](https://choosealicense.com/licenses/mit/)
Copyright (c) 2019 **TUYISENGE Anabella**

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE


