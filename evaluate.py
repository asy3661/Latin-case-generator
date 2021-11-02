from train import input_tensor, n_letters, all_letters
import torch

max_length = 20

def sample(rnn, start_letter='a'):
    with torch.no_grad():
        input = input_tensor(start_letter)
        hidden = rnn.initHidden()

        output_name = start_letter

        for i in range(max_length):
            output, hidden = rnn(input[0], hidden)
            topv, topi = output.topk(1)
            topi = topi[0][0]
            if topi == n_letters - 1:
                break
            else:
                letter = all_letters[topi]
                output_name += letter
            input = input_tensor(letter)

        return output_name

def complete_word(rnn, input_string):
    with torch.no_grad():
        input = input_tensor(input_string)
        hidden = rnn.initHidden()

        output_name = input_string

        for i in range(max_length):
            output, hidden = rnn(input[0], hidden)
            topv, topi = output.topk(1)
            topi = topi[0][0]
            if topi == n_letters - 1:
                break
            else:
                letter = all_letters[topi]
                if letter == ' ':
                    break
                output_name += letter
            input = input_tensor(letter)

        return output_name


