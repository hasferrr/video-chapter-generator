import csv
from sys import argv
from random import random
from os.path import isfile


def main():

    # Check for command-line usage
    if len(argv) != 3:
        argv_error()

    if ".csv" not in argv[1]:
        argv_error()

    if ".xml" not in argv[2]:
        argv_error()

    # Open file
    try:
        csv_file = open(argv[1])
    except FileNotFoundError:
        print(f"File '{argv[1]}' doesn't exist")
        return

    lines = csv.reader(csv_file)

    # Check if output xml file exist or not
    if isfile(argv[2]) == True:
        print(f"File '{argv[2]}' is in your directory")
        confirm = input("Do you want to overwrite it? (y/n) ")
        if confirm != 'y':
            print("Canceled")
            csv_file.close()
            return

    # Write chapters to xml file
    with open(argv[2], "w") as output:

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


    # Close file and exit
    csv_file.close()
    print("DONE")
    return


def argv_error():
    exit("Usage: python app.py file.csv output.xml")


if __name__ == '__main__':
    main()
