import csv
from sys import argv
from random import random
from os.path import isfile


def main():
    if command_line() != 0:
        exit()

    if check_file(argv[1], argv[2]) != 0:
        exit()

    write_chapters(argv[1], argv[2])



def command_line():

    # Check for command-line usage
    if len(argv) != 3:
        print("Usage: python app.py file.csv output.xml")
        return 1

    return 0



def check_file(csv_file, output_file_name):


    """ CHECK INPUT FILE NAME"""

    # Check if input csv file exist or not
    if isfile(csv_file) == True:
        pass

    else:
        print(f"File '{csv_file}' doesn't exist")
        return 1


    """ CHECK OUTPUT FILE NAME """

    # Check if output xml file exist or not
    if isfile(output_file_name) == True:

        print(f"File '{output_file_name}' is in your directory")

        # Confirm to overwrite output file?
        confirm = input("Do you want to overwrite it? (y/n) ")

        if confirm == 'y':
            pass

        else:
            print("Canceled")
            return 1

    return 0


# File.csv -> File.xml
# Start writing video chapters
def write_chapters(csv_file, output_file_name):

    # Open and read file
    open_csv_file = open(csv_file)
    lines = csv.reader(open_csv_file)


    # Add ".xml" to file name
    if output_file_name[-4:] != ".xml":
        output_file_name = output_file_name + ".xml"


    # Write chapters to xml file
    with open(output_file_name, "w") as output:

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
            print(line)
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

    # Exit
    open_csv_file.close()
    print("DONE")
    return



if __name__ == '__main__':
    main()
