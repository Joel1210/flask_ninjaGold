from flask import Flask, render_template, request, redirect, session
import random
import datetime

app = Flask(__name__)
app.secret_key = 'This is a secret'

@app.route('/')
def index():
    if 'gold' not in session:
        session['gold'] = 0
    return render_template('index.html')
     

@app.route('/process_money', methods= ['POST'])
def process_money():
    time = datetime.datetime.now()
    if 'activitylog' not in session:
        session['activitylog'] = []


    building = request.form['building']
    if building == 'farm':
        gold = random.randint(10,20)
        session['gold'] += gold
        activity = {
            "textcolor": 'gain',
            "msg": f"You've earned {gold} gold from the {building} on        {time}"
        }
        session['activitylog'].insert(0, activity)

    if building == 'cave':
        gold = random.randint(5,10)
        session['gold'] += gold
        activity = {
            "textcolor": 'gain',
            "msg": f"You've earned {gold} gold from the {building} on        {time}"
        }
        session['activitylog'].insert(0, activity)

    if building == 'house':
        gold = random.randint(2,5)
        session['gold'] += gold
        activity = {
            "textcolor": 'gain',
            "msg": f"You've earned {gold} gold from the {building} on        {time}"
        }
        session['activitylog'].insert(0, activity)

    if building == 'casino':
        gold = random.randint(-50,50)
        earnlose = 'won' if gold >0 else 'lost'
        lifesucks = ' ' if gold>0 else '...fml' 
        session['gold'] += gold
        activity = {
            "textcolor": 'gain' if gold >= 0 else 'loss',
            "msg": f"You've {earnlose} {abs(gold)} gold from the {building} {lifesucks} on        {time}"
        }
        session['activitylog'].insert(0, activity)
   
    return redirect('/')


@app.route('/destroy_session', methods=['POST'])
def clear():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)