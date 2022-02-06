from flask import Flask, render_template, request, escape, jsonify
from letters import *
from gtts import gTTS
from playsound import playsound
import random, string, json

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

# Validates user entry
def validator(a_word):
    print (a_word)
    for i in a_word:
        if i in lower_upper:
            i = lower_upper[i]
        
        if i not in replace_letters:
          return "Your entry could involve : lower or upper letters/numbers/_/-/space"

    if len(a_word) == 0 or len(a_word) > 30:
        return "Your entry should be between 1-30 letters"
    else:
        return 200
        
# Spells the word given to it 
def spelling_alphabet(a_word):
    coded_string = ""
    for i in range(len(a_word)):
        if i == 0:
            coded_string = coded_string + replace_letters[a_word.upper()[i]]
        else:
            coded_string = coded_string + " , " + replace_letters[a_word.upper()[i]]
    return coded_string
    


@app.route("/", methods=['POST'])
# render template
def kodla():
    my_word = request.form['words']
    my_result = validator(my_word)
    if my_result != 200:
        return render_template('index.html',err_msg= my_result )
    
    spelled = spelling_alphabet(my_word)
    file_name = play_word(spelled)
    return render_template('index.html',coded_string= escape(spelled) , file_name=file_name, my_word=my_word)


# take and response json entry
@app.route("/api", methods=['POST']) 
def api_kodla():
    data = json.dumps(request.get_json())
    items = json.loads(data)

    my_word = items["my_word"]

    my_result = validator(my_word)
    if my_result != 200:
        return jsonify({'message' : my_result }),400
    
    spelled = spelling_alphabet(my_word)
    file_name = play_word(spelled)
    result = {
        'coded_string' : spelled,
        'audio_file_path'    : "static/"+file_name+".mp3",
    }
    return jsonify(result),200



if __name__ == "__main__":
    app.run()