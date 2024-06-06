import csv
from sys import argv
from random import random
from os.path import isfile


def main():
    if command_line() != 0:
        return

    csv_file_name = argv[1]
    output_file_name = argv[2]

    # Add ".xml" to file name
    if output_file_name[-4:] != ".xml":
        output_file_name = output_file_name + ".xml"

    if check_file(csv_file_name, output_file_name) != 0:
        return

    timestamp_title = load_file(csv_file_name)
    timestamp_title = remove_illegal_xml_chars(timestamp_title)

    write_chapters(timestamp_title, output_file_name)


def command_line():

    # Check for command-line usage
    if len(argv) != 3:
        print("Usage: python app.py file.csv output.xml")
        return 1

    return 0


def check_file(csv_file_name, output_file_name):
    """ CHECK INPUT FILE NAME"""

    # Check if input csv file exist or not
    if not (isfile(csv_file_name)):
        print(f"File '{csv_file_name}' doesn't exist")
        return 1

    """ CHECK OUTPUT FILE NAME """

    # Check if output xml file exist or not
    if isfile(output_file_name):

        print(f"File '{output_file_name}' is in your directory")

        # Confirm to overwrite output file?
        confirm = input("Do you want to overwrite it? (y/n) ")

        if confirm != 'y':
            print("Canceled")
            return 1

    return 0


def load_file(csv_file):
    timestamp_title = []

    # Open and read file
    open_csv_file = open(csv_file)
    lines = csv.reader(open_csv_file)

    # Store it into list
    for line in lines:
        timestamp_title.append(tuple(line))

    timestamp_title = sorted(timestamp_title, key=lambda data: data[0])

    return timestamp_title


def remove_illegal_xml_chars(timestamp_title):
    entity_ref = {
        "<": "&lt;",
        ">": "&gt;",
        "&": "&amp;",
        "'": "&apos;",
        "\"": "&quot;"
    }

    def replace_invalid(text):
        for key in entity_ref.keys():
            text = text.replace(key, entity_ref[key])
        return text

    new_timestamp_title = list(
        map(lambda e: (e[0], replace_invalid(e[1])), timestamp_title))

    return new_timestamp_title


# File.csv -> File.xml
# Start writing video chapters
def write_chapters(timestamp_title, output_file_name):

    # Write chapters to xml file
    with open(output_file_name, "w") as output:

        # Write header
        output.write('<?xml version="1.0"?>')
        output.write('<!-- <!DOCTYPE Chapters SYSTEM "matroskachapters.dtd"> -->')
        output.write('<Chapters>')
        output.write('  <EditionEntry>')
        output.write('    <EditionFlagDefault>1</EditionFlagDefault>')
        output.write('    <EditionUID>')
        output.write(str(int(random()*10**18)))
        output.write('</EditionUID>\n')

        # Write ChapterAtom
        chapter_uid = 3000000000

        for line in timestamp_title:
            print(line)
            # Opening
            output.write('    <ChapterAtom>\n')

            # ChapterUID and ChapterTimeStart
            chapter_uid += 1
            output.write(f'      <ChapterUID>{chapter_uid}</ChapterUID>\n')
            output.write(f'      <ChapterTimeStart>{line[0]}.000000000</ChapterTimeStart>\n')

            # ChapterDisplay
            output.write('      <ChapterDisplay>\n')
            output.write(f'        <ChapterString>{line[1]}</ChapterString>\n')
            output.write('        <ChapterLanguage>und</ChapterLanguage>')
            output.write('        <ChapLanguageIETF>und</ChapLanguageIETF>')
            output.write('      </ChapterDisplay>\n')

            # Ending
            output.write('    </ChapterAtom>\n')

        # Write footer
        output.write('  </EditionEntry>')
        output.write('</Chapters>\n')

    # Exit
    print("DONE")
    return


if __name__ == '__main__':
    main()
