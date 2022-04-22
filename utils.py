import json

def get_condidates(path):
    with open(path, 'r', encoding='utf-8') as condidates:
        return json.load(condidates)

def format_condidates(condidates_list):
    result = '<pre>'
    for condidate in condidates_list:
        result += (
            f'Имя кандидата - {condidate["name"]}\n'
            f'Позиция кандидата : {condidate["position"]}\n'
            f'Навыки через запятую : {condidate["skills"]}\n\n'
        )

    result += '</pre>'

    return result

def get_condidate_by_id(condidates_list, condidate_id):
    condidate_id = int(condidate_id)
    for condidate in condidates_list:
        if condidate['id'] == condidate_id:
            return condidate


def get_condidates_by_skill(condidates_list, condidate_skill):
    result = []

    for condidate in condidates_list:
        condidate_skills = condidate['skills'].lower().split(', ')

        if condidate_skill.lower() in condidate_skills:
            result.append(condidate)

    return result