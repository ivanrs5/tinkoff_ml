import argparse
import pickle
import random


class Model:
    def __init__(self):
        self.cnt = None
        self.dct = None

    def fit(self, model):
        file = open(model, 'rb')
        dct = pickle.load(file)
        file.close()

        for x in dct.keys():
            dct[x] = list(dct[x].items())

        self.dct = dict()
        for key in dct.keys():
            self.dct[key] = [x[0] for x in dct[key]]

        self.cnt = dict()
        for key in dct.keys():
            self.cnt[key] = [x[1] for x in dct[key]]

    def generate(self, prefix, length):
        seq = prefix.copy()
        if prefix == [] or prefix[-1] not in self.dct:
            seq.append(random.choice(list(self.dct.keys())))

        while len(seq) < length:
            prev = seq[-1]
            seq += random.choices(self.dct[prev], weights=self.cnt[prev], k=1)

        return seq


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--model', nargs=1)
    parser.add_argument('--prefix', nargs=1, default=None)
    parser.add_argument('--length', nargs=1)

    args = parser.parse_args()

    m = Model()
    m.fit(args.model[0])
    print(*m.generate(args.prefix, int(args.length[0])))


if __name__ == "__main__":
    main()
    