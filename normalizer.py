class Normalizer:
    @staticmethod
    def clearing(counter=1, encoding="utf-8"):
        text = open(f"output/output{counter}.txt", "r", encoding=encoding).read().split()
        clear_text = []
        for i in text:
            if (len(i) > 3) and ("-" not in i):
                clear_text.append(i)
        with open(f"clear/clear{counter}.txt", "w+", encoding="utf-8") as out:
            out.write(" ".join(clear_text))

    @staticmethod
    def splitting(file_counter=1,counter=1):
        text = open(f"clear/clear{file_counter}.txt", "r").read().split()
        while text != []:
            if len(text) > 10000:
                with open(f"splitted/splitted{counter}.txt", "w+") as splitted:
                    splitted.write(" ".join(text[:10000]))
                    counter += 1
                    text = text[10000:]
            else:
                with open(f"splitted/splitted{counter}.txt", "w+") as splitted:
                    splitted.write(" ".join(text))
                    return counter+1

    @staticmethod
    def word_normalization(counter):
        import pymorphy2

        def normalize(word):
            morph = pymorphy2.MorphAnalyzer()
            p = morph.parse(word)
            out = []
            for x in p:
                nf = x.inflect({'sing', 'nomn'})
                if nf:
                    out.append(nf)
                else:
                    pass
            try:
                return out[0].normal_form
            except:
                return word

        wordlist = open(f"splitted/splitted{counter}.txt", "r", encoding="utf-8").read().split()
        normalized_words = []
        f = 0
        size = len(wordlist)
        print(size)
        while len(wordlist) != 0:
            normalized_words += normalize(f"{wordlist.pop(0)} {wordlist.pop(0)}").split()
            f += 2
            if f % 1000 == 0:
                print(f)
        with open(f"final/save{counter}.txt", "w") as out:
            out.write(" ".join(normalized_words))
