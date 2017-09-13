class Counter:

    def __init__(self, name):
        self.name = name
        self.count = 0

    def increment(self):
        self.count += 1

    def tally(self):
        return self.count

    def __repr__(self):
        return self.name + " " + str(self.count)


def main():
    heads = Counter("heads")
    tails = Counter("tails")

    heads.increment()
    heads.increment()
    tails.increment()
    print(str(heads) + " " + str(tails))
    print(heads.tally() + tails.tally())


if __name__ == "__main__":
    main()
