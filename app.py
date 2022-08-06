import csv
from random import random


def main():
    # Check validity file .csv

    # Open file
    csv_file = open("test.csv")

    lines = csv.reader(csv_file)
    for line in lines:
        print(line)

    # Write file xml
    with open("output.xml", "w") as output:

        # Write header
        output.write(
"""<?xml version="1.0"?>
<!-- <!DOCTYPE Chapters SYSTEM "matroskachapters.dtd"> -->
<Chapters>
  <EditionEntry>
    <EditionFlagDefault>1</EditionFlagDefault>
    <EditionUID>""")
        output.write(str(int(random()*10**18)))
        output.write("</EditionUID>")


    # Close file
    csv_file.close()


if __name__ == '__main__':
    main()
