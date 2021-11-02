import random
import torch
import torch.nn as nn
import matplotlib.pyplot as plt
from data import *
import time
import math
from rnn import RNN

criterion = nn.NLLLoss()

# rnn = RNN(n_letters, 128, n_letters)


def train(rnn, lines):
    start = time.time()
    n_iters = 100000
    print_every = 5000
    plot_every = 500
    all_losses = []
    total_loss = 0

    print('starting training')
    for iter in range(1, n_iters + 1):
        training_example = random_training_example(lines)
        output, loss = optimize_parameters(rnn, *training_example)
        total_loss += loss

        if iter % print_every == 0:
            print('%s (%d %d%%) %.4f' % (time_since(start), iter, iter / n_iters * 100, loss))

        if iter % plot_every == 0:
            all_losses.append(total_loss / plot_every)
            total_loss = 0
    plt.figure()
    plt.plot(all_losses)
    plt.show()

def optimize_parameters(rnn, input_line_tensor, target_line_tensor):
    learning_rate = 0.0005
    target_line_tensor.unsqueeze_(-1)
    hidden = rnn.initHidden()

    rnn.zero_grad()

    loss = 0

    # print('input tensor', input_line_tensor)
    # print('input tensor size', input_line_tensor.size(0))

    for  i in range(input_line_tensor.size(0)):
        # print('i', i)
        output, hidden = rnn(input_line_tensor[i], hidden)
        # print('output', output)
        # print('target tensor', target_line_tensor)
        # print('i', i)
        l = criterion(output, target_line_tensor[i])
        loss += l

    loss.backward()

    for p in rnn.parameters():
        p.data.add_(p.grad.data, alpha=-learning_rate)

    return output, loss.item() / input_line_tensor.size(0)

def input_tensor(line):
    tensor = torch.zeros(len(line), 1, n_letters)
    for letter_index in range(len(line)):
        letter = line[letter_index]
        tensor[letter_index][0][all_letters.find(letter)] = 1
    return tensor

def target_tensor(line):
    letter_indices = [all_letters.find(line[li]) for li in range(1, len(line))]
    letter_indices.append(n_letters - 1) # End of string
    return torch.LongTensor(letter_indices)

def random_training_example(lines):
    line = random_line(lines)
    # print(line)
    input_line_tensor = input_tensor(line)
    target_line_tensor = target_tensor(line)
    return input_line_tensor, target_line_tensor

def random_line(lines):
    return lines[random.randint(0, len(lines) - 1)]


def time_since(since):
    now = time.time()
    s = now - since
    m = math.floor(s / 60)
    s -= m * 60
    return f'{m}m {s}s'


