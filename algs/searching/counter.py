class FrequencyCounter:

    def __init__(self, ST, textdir, minlen):
        self.ST = ST
        self.textdir = textdir
        self.minlen = minlen

    def count_words(self):
        st = self.ST()

        with open(self.textdir, 'r') as reader:
            for word in reader:
                if len(word) < self.minlen:
                    continue

                count = st.get(word)
                if count is None:
                    st.put(word, 1)
                else:
                    st.put(word, count+1)

        max_word = ""
        st.put(max_word, 0)

        for word in st.keys():
            if st.get(word) > st.get(max_word):
                max_word = word

        print(max_word + " => " + str(st.get(max_word)))
