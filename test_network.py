from model import Generator
from collections import Counter
import json

prepositions = {'a', 'ab', 'ad', 'apud', 'con', 'contra', 'coram',
        'cum', 'de', 'e', 'ex', 'extra', 'in', 'inter', 'iuxta',
         'ob', 'palam', 'per', 'post', 'prae', 'pro', 'propter',
        'sine', 'sub', 'super', 'trans'}


chosen_prepositions = ['ab', 'ad', 'ex', 'in', 'inter', 'prae']
chosen_stems = ['poen', 'aqu', 'ferr', 'fili', 'flumin', 'fulmin', 
        'senat', 'curs', 'effigi', 'aci']

def main():
    model = Generator()
    model.load_model('case_predictor.pt')
    combs = get_combinations(chosen_prepositions, chosen_stems)
    input_strings = [construct_string(p, n) for (p, n) in combs]

    outputs = {}
    for string in input_strings:
        k, v = process_input_string(string, model)
        outputs[k] = v
    with open('data/samples.json', 'w') as fh:
        json.dump(outputs, fh)


def get_combinations(first_list, second_list):
    combinations = []
    for i in first_list:
        for j in second_list:
            combinations.append((i, j))
    return combinations

def process_input_string(input_string, model):
    counter = dict(model.estimate_prob_dist(input_string))
    formatted_counts = (input_string, counter)
    return formatted_counts

def construct_string(prep, noun):
    return f'{prep} {noun}'

def append_to_file(path, string):
    with open(path, 'a') as fh:
        fh.write(f'{string}\n')


if __name__ == '__main__':
    main()
