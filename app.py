from flask import Flask, render_template, url_for, redirect, request
from datetime import date
import random

resolutions = [
{
"id": 1,
"pseudo": "G.O.",
"texte": "Rendre ses notes rapidement",
"votes": 3,
"statut": "active",
"created_at": "2025-01-05",
},
{
"id": 2,
"pseudo": "Pierre L.",
"texte": "Faire des examens plus faciles",
"votes": 6,
"statut": "dropped",
"created_at": "2025-01-02",
},
{
"id": 3,
"pseudo": "Mr. Bou",
"texte": "Rire en silence",
"votes": 1,
"statut": "kept",
"created_at": "2025-01-03",
}
]

app = Flask(__name__)

@app.route('/status')
def status():
    return f"Le mur est prêt !"

@app.route('/')
def index():
    return render_template('index.html', resolutions=resolutions)

@app.route('/add', methods=['GET', 'POST'])
def add():
    message = None
    if request.method == 'POST':
        pseudo = request.form.get('pseudo')
        texte = request.form.get('texte')
        new_id = len(resolutions) + 1
        new_res = {
            "id": new_id,
            "pseudo": pseudo,
            "texte": texte,
            "votes": 0,
            "statut": "active",
            "created_at": date.today().isoformat()
        }
        resolutions.append(new_res)
        messages_succes= ["Courage, on y croit !","Bonne chance !", "Go !"]
        message = random.choice(messages_succes)
        
    return render_template('add.html', message=message)
    
if __name__== '__main__':
    app.run(debug=True, host='0.0.0.0', port=5454)