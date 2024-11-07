# Moselsagen

## Project description

"Moselsagen" is an endeavour to digitize tales and stories from 19th century tale books. These books contain stories from all around the Moselle region in Germany, Luxembourg and France. So far eight
books have been digitized. These are:

- "Sagen des Moseltals"
- "Sagen und Erzählungen aus Trier und Umgebung"
- "Sagen des Oberelsass"
- "Sagen des Unterelsass"
- "Pfälzisches Sagenbuch"
- "Lothringen"
- "Luxembourg 1"
- "Luxembourg 2"

The main goals are to localize the tales and show them on a map, create XML-TEI versions of each book and make them readable on a website. To reach these goals several steps had to be taken:

- OCR
- Parsing
- Localization
- XML creation
- Database + Website

## OCR

The first step was to extract the text from the books. To achieve this we needed scans of the physical book. These were available for each of the books. To create the OCR version we used preexisting 
transcriptions from the libraries we got the scans from and the tool OCR-4all.

## Parsing

The goal of parsing was to divide the books into tales. We used the titles of the tales for splitting. The title list was generated from the index of the books.

## Localization

The localization was performed in two diffrent ways. Some books already had an index of the locations from each tale that we could used. For the other books we performed Named Entity Recognition to find
mentions of locations.

## XML creation

The XML files were created from the parsed tales. Additionally a JSON file is created and used for all the metadata in the TEI header.\
The following is a schematic structure of the JSON file and its contents

```json
{
  "fileDesc": {
    "title": "Title",
    "subtitle": "Subtitle",
    "author": "Author",
    "publisher": "Publisher",
    "address": "Address",
    "date": "1850-01-01",
    "sourceDesc": "Description of source",
    "editor": [
      "Editor 1",
      "Editor 2",
      "Editor 3"
    ]
  },
  "encodingDesc": {
    "projectDesc": "Description of project",
    "samplingDecl": "Description of methods used for selecting text",
    "editorialDecl": {
      "correction": "Corrections applied to text",
      "normalization": "Normalization applied to text",
      "segmentation": "Segments"
    }
  },
  "profileDesc": {
    "abstract": "Abstract",
    "langUsage": [
      {
        "ident": "de-DE",
        "name": "Deutsch"
      }
    ],
    "classCode": "Classcode"
  },
  "division": [
    "NaN",
    "cat",
    "group"
  ]
}
```

## Database + Website

All the generated files and informations were put into a database to create a website. There you can download all the XML-TEI files and a CSV of our complete database, find a map that shows the locations 
of the tales and read all tales from the books.

Website: https://www.mosel-sagen.de

License: CC-BY-SA 4.0
