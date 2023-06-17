import pyarrow
import pyarrow.flight
import pyarrow.csv as csv
import numpy as np
import random, string


def random_word(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


def create_data(num_rows):
    cols = []
    vals = []
    np.random.seed(12)

    for i in range(0, 100):
        cols.append("col" + str(i))
        if i == 0:
            vals.append(np.random.randint(low=1000000, high=2000000, size=num_rows))
        elif i <= 10:
            word1 = random_word(14)
            word2 = random_word(14)
            word3 = random_word(8)
            words = [word1, word2, word3]
            list_words = []
            for i in range(0,num_rows):
                list_words.append(random.choice(words))
            vals.append(list_words)
        else:
            vals.append(np.random.normal(-10000.0, 10000.0, size=num_rows))

        #    data_table = pyarrow.table(
    #        [["IBM", "GS", "APPL", "IBM", "GS", "APPL", "IBM", "GS", "APPL", "IBM"], qty],
    #        names=["Stock", "Qty"]
    #    )

    data_table = pyarrow.table(
        vals,
        names=cols
    )

    csv.write_csv(data_table, "../../../orders" + str(num_rows) + ".csv")


if __name__ == '__main__':
    create_data(1000)