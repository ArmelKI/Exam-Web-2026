from flask import Flask, render_template, url_for, redirect, request

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
    
if __name__== '__main__':
    app.run(debug=True, host='0.0.0.0', port=5454)