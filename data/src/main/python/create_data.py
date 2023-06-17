import pyarrow
import pyarrow.flight
import pyarrow.csv as csv
import numpy as np


def create_data(num_rows):
    cols = []
    vals = []
    np.random.seed(12)

    for i in range(0, 100):
        cols.append("col" + str(i))
        vals.append(np.random.normal(0.0, 1.0, size=1000))

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