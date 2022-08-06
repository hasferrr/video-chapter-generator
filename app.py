import csv
from sys import argv
from random import random


def main():

    # Check for command-line usage
    if len(argv) != 2:
        exit("Usage: python app.py file.csv ")

    # Open file
    csv_file = open(argv[1])
    lines = csv.reader(csv_file)

    # Open file xml
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
        output.write("</EditionUID>\n")

        # Write ChapterAtom
        chapter_uid = 3000000000
        for line in lines:

            # Opening
            output.write("    <ChapterAtom>\n")

            # ChapterUID and ChapterTimeStart
            chapter_uid += 1
            output.write(f"      <ChapterUID>{chapter_uid}</ChapterUID>\n")
            output.write(f"      <ChapterTimeStart>{line[0]}.000000000</ChapterTimeStart>\n")

            # ChapterDisplay
            output.write("      <ChapterDisplay>\n")
            output.write(f"        <ChapterString>{line[1]}</ChapterString>\n")
            output.write(
"""        <ChapterLanguage>und</ChapterLanguage>
        <ChapLanguageIETF>und</ChapLanguageIETF>
      </ChapterDisplay>\n""")

            # Ending
            output.write("    </ChapterAtom>\n")

        # Write footer
        output.write(
"""  </EditionEntry>
</Chapters>\n""")


    # Close file
    csv_file.close()


if __name__ == '__main__':
    main()
