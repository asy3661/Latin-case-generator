# from extract_from_corpus import scour_corpus
import clean_data
from pathlib import Path
from data import read_lines, all_letters, n_letters
from rnn import RNN
from lstm import LSTM
import torch.nn as nn
from train import train
from evaluate import complete_word

home = Path.home()
source_dir = home / 'cltk_data' / 'lat' / \
    'text' / 'lat_text_tesserae' / 'texts'
language = 'lat'
output_path = Path.cwd()
data = output_path / 'data.txt'
hidden_layer_size = 128

if __name__ == "__main__":

    # if not data.exists():
    #     scour_corpus(source_dir, output_path, language)
    #     clean_data()

    rnn = RNN(n_letters, 128, n_letters)

    lines = read_lines(data)
    train(rnn, lines)

    print(complete_word(rnn, 'in memori'))
    print(complete_word(rnn, 'ab insul'))
    print(complete_word(rnn, 'sub insul'))
    print(complete_word(rnn, 'ad insul'))
