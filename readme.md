# Spelling Turkish Alphabet
Kodla is a web application for spelling or codding Turkish alphabet. [NATO phonetic alphabet](https://en.wikipedia.org/wiki/NATO_phonetic_alphabet)

[kodla.link](http://kodla.link)

## Installation

- python3 -m pip install --user virtualenv
- python3 -m venv venv
- source venv/bin/activate
- pip install -r requirements.txt
- export FLASK_APP=app
- flask run

### Delete old audio file
Define a cronjob - run every 5 min - to delete files older than 5 min in the static folder: 
```
*/5 * * * find PATH/kodla/static/* -type f -mmin +5 -exec rm -f {} +
```
Replace **"PATH"** with the path of the Kodla folder.

