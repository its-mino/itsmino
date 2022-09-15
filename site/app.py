from flask import Flask, render_template, request, send_file
import sys
import json
sys.path.insert(0, '../projects/api')
import mtg_api
sys.path.insert(0, '../projects/openinghand')
import pick7

app = Flask(__name__)

with open('ddb.json', 'r') as f:
    decks_data = json.load(f)

@app.route('/categories')
def categories():
    with open('categories.txt', 'r') as f:
        data = f.read()
    return data

@app.route('/decks')
def decks():
    with open('ddb_names.txt', 'r') as f:
        data = f.read()
    return data

@app.route('/decks/<name>')
def decks_name(name):
    return json.dumps(decks_data[name], indent=4)

@app.route('/mulligans')
def mulligans():
    chosen_deck, hand = pick7.pick7()
    return render_template('mulligans.html', chosen_deck=chosen_deck, hand=hand)
