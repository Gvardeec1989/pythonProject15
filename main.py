import json

from flask import Flask

from utils import get_condidates, format_condidates, get_condidate_by_id, get_condidates_by_skill

app = Flask(__name__)

@app.route('/')
def main():
    condidates_list = get_condidates('condidates.json')

    return format_condidates(condidates_list)

@app.route('/condidates/<condidate_id>')
def candidate(condidate_id):
    condidates_list = get_condidates('condidates.json')

    condidate = get_condidate_by_id(condidates_list, condidate_id)

    result = f'<img src="{condidate["picture"]}">'

    result += format_condidates([condidate])
    return result

@app.route('/skills/<skill>')
def skils(skill):
    condidates_list = get_condidates('condidates.json')

    return format_condidates(get_condidates_by_skill(condidates_list, skill))

app.run()
