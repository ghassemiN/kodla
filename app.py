from flask import Flask, render_template, request, escape
from letters import *
from gtts import gTTS
from playsound import playsound
import random, string



app=Flask(__name__,template_folder='templates', static_folder='static')
app.config["DEBUG"] = True


@app.route('/')
def home():
   return render_template('index.html')

# record the audio file
def play_word(coded_string):
    file_name =''.join(random.choice(string.ascii_lowercase) for i in range(10))
    language = 'tr'
    myobj = gTTS(text=coded_string,lang=language,slow=True)
    myobj.save("static/{}.mp3".format(file_name))
    return file_name


@app.route("/", methods=['POST'])
# Decode turkish words
def coding():
    my_word = request.form['words']
    coded_string = ""

    for i in my_word:
        if i in lower_upper:
            i = lower_upper[i]
        
        if i not in replace_letters:
          return render_template('index.html',err_msg= " Your entry could involve : lower or upper letters/numbers/_/-/space")

    if len(my_word)!= 0 or len(my_word) > 30:
        for i in range(len(my_word)):
            if i == 0:
                coded_string = coded_string + replace_letters[my_word.upper()[i]]
            else:
                coded_string = coded_string + " , " + replace_letters[my_word.upper()[i]]

        file_name = play_word(coded_string)
        return render_template('index.html',coded_string= escape(coded_string) , file_name=file_name,my_word=my_word)
    else: 
        return render_template('index.html',err_msg="Check your entry, it should be between 1-30 letters")





if __name__ == "__main__":
    app.run()