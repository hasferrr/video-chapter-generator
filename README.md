# Video Chapter Generator

(Python Script) This script consumes **input.csv** file and produces a video chapter file for the MKV format video **output.xml**

![chapters](example/chapter-file.jpg)

## Usage

```bash
python app.py file.csv output.xml
```

## Description

### Input

The contents of the input file must be exactly as in the file [test.csv](example/test.csv)

- 1st column: timestamp
- 2nd column: chapters name

```c
00:00:00,Introduction
00:00:24,Object-Oriented Programming
00:01:00,Tuples
00:18:39,Dictionaries
00:26:45,Classes and Objects
00:39:18,Instance Methods
00:59:49,Validating Attributes
01:04:25,The String Method
01:11:13,Custom Methods
01:20:43,"Properties, Getters, and Setters"
01:42:33,Types and Classes
01:50:29,Class Methods
02:21:10,Inheritance
02:35:29,Operator Overloading
02:50:03,Conclusion
```

### Process

**input.csv** file will be processed or formatted into an **output.xml** file for the chapter file.

### Output

Example output file: [test-output.xml](example/test-output.xml)

```xml
<?xml version="1.0"?>
<!-- <!DOCTYPE Chapters SYSTEM "matroskachapters.dtd"> -->
<Chapters>
  <EditionEntry>
    <EditionFlagDefault>1</EditionFlagDefault>
    <EditionUID>123456789012345678</EditionUID>
    <ChapterAtom>
      <ChapterUID>3000000001</ChapterUID>
      <ChapterTimeStart>00:00:00.000000000</ChapterTimeStart>
      <ChapterDisplay>
        <ChapterString>Introduction</ChapterString>
        <ChapterLanguage>und</ChapterLanguage>
        <ChapLanguageIETF>und</ChapLanguageIETF>
      </ChapterDisplay>
    </ChapterAtom>

    ...

    <ChapterAtom>
      <ChapterUID>3000000015</ChapterUID>
      <ChapterTimeStart>02:50:03.000000000</ChapterTimeStart>
      <ChapterDisplay>
        <ChapterString>Conclusion</ChapterString>
        <ChapterLanguage>und</ChapterLanguage>
        <ChapLanguageIETF>und</ChapLanguageIETF>
      </ChapterDisplay>
    </ChapterAtom>
  </EditionEntry>
</Chapters>
```

### MKV

The output is in the form of an **output.xml** file that can be embedded/merged into an **MKV** format video file.

See :

- [MKVToolNix GUI](https://mkvtoolnix.download/)
- [mkvmerge documentation](https://mkvtoolnix.download/doc/mkvmerge.html)
