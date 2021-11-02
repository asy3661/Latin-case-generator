import string

def read_lines(path):
    '''Takes the data.txt file and splits it into a list of tuples, 
    where the first item is the file the line came from, the second
    item is the lemma form, and the last item is the attested form'''
    with open(path) as fh:
        lines = fh.readlines()
    split_lines = [line.strip().split('\t')[-1] for line in lines]
    return split_lines

# def get_all_letters(lines):
#     all_letters = set()
#     for line in lines:
#         if len(line) > 1:
#             attested_form = line[2]
#         else:
#             attested_form = line
#         all_letters.update(attested_form)
#     return ''.join(sorted(list(all_letters)))

# all_letters = get_all_letters(read_lines('data.txt'))
# n_letters = len(all_letters) + 1

all_letters = string.ascii_lowercase + string.whitespace
n_letters = len(all_letters) + 1
