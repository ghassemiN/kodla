# Spell Turkish word
A web application for spelling or codding Turkish words. 

[kodla.link](http://kodla.link)

## Installation

- python3 -m pip install --user virtualenv
- python3 -m venv venv
- source venv/bin/activate
- pip install -r requirements.txt

### Delete old audio file
Define a cronjob - run every 5 min - to delete files older than 5 min in the static folder: 
```
*/5 * * * find PATH/kodla/static/* -type f -mmin +5 -exec rm -f {} +
```
Replace "PATH" with the path of your folder.

