# Spelling Turkish Alphabet
Kodla is a web application for spelling or codding Turkish alphabet. [NATO phonetic alphabet](https://en.wikipedia.org/wiki/NATO_phonetic_alphabet)

[kodla.link](http://kodla.link)
***
## Installation

1. python3 -m pip install --user virtualenv
2. python3 -m venv venv
3. source venv/bin/activate
4. pip install -r requirements.txt
5. export FLASK_APP=app
6. flask run
***
### Delete old audio file
Define a cronjob - run every 5 min - to delete files older than 5 min in the static folder: 
```
*/5 * * * find PATH/kodla/static/* -type f -mmin +5 -exec rm -f {} +
```
Replace **"PATH"** with the path of the Kodla folder.
***
### Kodla API usage
Request:
- endpoint url: 127.0.0.1:5000/api
- method: POST
- body: JSON {"my_word" : "test word"}

Response: 
- 200 status:
```
{
    "audio_file_path": "static/FILE_NAME.mp3",
    "coded_string": "Tokat , Edirne , Sinop , Tokat , BOŞLUK , çift ve , Ordu , Rize , Denizli"
}
```
- error:
If length my_word is 0 or >30:
```
{
    "message": "Your entry could involve : lower or upper letters/numbers/_/-/space"
}
```
If my_word envolve forbidden characters:
```
{
    "message": "Your entry should be between 1-30 letters"
}
```
