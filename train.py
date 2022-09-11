import argparse
import pickle
import re
import sys


def add_text(text, model):
    file = open(model, 'rb')
    
    try: 
        dct = pickle.load(file)
    except EOFError:
        dct = dict()
    file.close()

    for i in range(len(text) - 1):
        if text[i] not in dct:
            dct[text[i]] = dict()
        if text[i + 1] in dct[text[i]]:
            dct[text[i]][text[i + 1]] += 1
        else:
            dct[text[i]][text[i + 1]] = 1

    file = open(model, 'wb')
    pickle.dump(dct, file)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input-dir', nargs=1, default=None)
    parser.add_argument('--model', nargs=1)

    args = parser.parse_args()

    if not args.input_dir:
        text = sys.stdin.read()
        print(text)
    else:
        file = open(args.input_dir[0])
        text = file.read()
        file.close()

    text = re.findall('[a-zа-яё0-9]+', text, flags=re.IGNORECASE)
    text = list(map(lambda x: x.lower(), text))
    add_text(text, args.model[0])


if __name__ == "__main__":
    main()
    