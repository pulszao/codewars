class VigenereCipher(object):
    def __init__(self, key, alphabet):
        self.key = key
        self.alphabet = alphabet
        self.shift_values = [alphabet.index(a) for a in key]

    def update_shift_values(self, text):
        if len(self.key) < len(text):
            self.key = (self.key * ((len(text) // len(self.key)) + 1))[:len(text) + 2]
            self.shift_values = [self.alphabet.index(a) for a in self.key]

    def encode(self, text):
        self.update_shift_values(text)

        out = ''
        for i, ltr in enumerate(text):
            try:
                new_index = self.alphabet.index(ltr) + self.shift_values[i]
                if new_index >= len(self.alphabet):
                    new_index -= len(self.alphabet)
                out += self.alphabet[new_index]
            except ValueError:
                out += ltr
        return out

    def decode(self, text):
        self.update_shift_values(text)

        out = ''
        for i, ltr in enumerate(text):
            try:
                new_index = self.alphabet.index(ltr) - self.shift_values[i]
                if new_index < 0:
                    new_index += len(self.alphabet)
                out += self.alphabet[new_index]
            except ValueError:
                out += ltr
        return out
