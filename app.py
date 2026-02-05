from flask import Flask, render_template, url_for, redirect, request

app = Flask(__name__)

@app.route('/status')
def status():
    return f"Le mur est prêt !"
    
if __name__== '__main__':
    app.run(debug=True, host='0.0.0.0', port=5454)