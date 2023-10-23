

<!-- toc -->

- [Intro](#intro)
- [Code](#code)
  * [Input format](#input-format)
  * [Output format](#output-format)
  * [Required python packages](#required-python-packages)
- [Annotation Schema](#annotation-schema)
  * [Area of interest](#area-of-interest)
  * [Text](#text)
  * [Image](#image)
  * [Participant](#participant)
  * [Relationship: connected metaphor](#relationship-connected-metaphor)
  * [Relationship: contained](#relationship-contained)

<!-- tocstop -->

# Intro

This repository contains code developed for the project "Verbal and visual metaphors for coronavirus at the health crisis onset: 'Emerging styles' of representation in British and Italian front page news".
The study investigates emerging metaphors during the Covid-19 outbreak and was presented at [CIRM 2023](https://cirm.unige.it/node/284) ("Le metafore alla prova dei generi testuali").

The project was developed by researchers [Antonella Luporini](https://www.unibo.it/sitoweb/antonella.luporini) and [Roberta Combei](https://unipv.unifind.cineca.it/resource/person/1213697) with the support of [Laboratorio Sperimentale](https://site.unibo.it/laboratorio-sperimentale/it).

# Code

This code is concerned with the conversion of annotations into a human-readable format.

The annotation was performed through [Labelbox](https://labelbox.com/), a popular tool in AI-research that allows fine grained annotation of custom categories on a variety of multimedia objects, including images (object of this study).

The annotation schema is described below and provided in file `data/ontology.json`.


## Input format

Labelbox provides annotations in `.ndjson` format. Not all of the info exported from Labelbox. An example of Labelbox's output format is provided in `data/labelbox_export.ndjson` (for privacy and copyright issues, some info was pseudoanonymized in the file)

## Output format

The script produces a number of output files in `.tsv` format. These can be easily read through excel-like software or loaded through a script for further processing.

More specifically, the script generates the followind files:

1. `data/export_primepagine.tsv`: containing the list of front pages examined in the study and some basic features of the image (width, height, area)
2. `data/export_annotazioni.tsv`: containing the full list of annotations
3. `data/export_areasofinterest.tsv`: containing the list of identified areas of interest and their coded information
4. `data/export_images.tsv`: containing the list of identified images and their coded information
5. `data/export_texts.tsv`: containing the list of identified text areas and their coded information
6. `data/export_participants.tsv`: containing the list of identified participant areas and their coded information

For each area of interest, text area, image and participant also the dimension of the area covered by the object is reported in the file.


## Required python packages

1. `ndjson`
2. `shapely`


# Annotation Schema

The purpose of the annotation was to identify metaphors (both verbal and visual) present on newspaper's front pages.

The following categories were defined:
## Area of interest

Polygon identifying the area of interest (i.e., article + image) on front page. For each front page, annotators were asked to identify:
1. area containing the main article (area A)
2. in case area A wasn't covid-related or didn't contain any image, a second area of interest for an article/content that instead had those features.

For each area of interest, the following aspects were registered:

### main article
Registering whether the area of interest pertains to the main article on front page.

### dominance of modality
Registering whether the area contains more textual content, more image-like content of a balanced mixture of the two.

### covid related
Registering whether the area contains covid-related content or not.


## Text

Bounding box containing textual content. Annotators were asked to identify only titles, subtitles and image captions.

For each textual content, the following aspects were registered:

### Type

Identifying wheter the textual area contains a `title`, `subtitle`, `caption` or other kind of text.

### Metaphor

Registering whether the text contains a metaphorical expression

### Quotation

Registering the linguistic metaphorical content contained in the text.

### Source Domain

Source domain of the metaphorical expression

### Target Domain

Target domain of the metaphorical expression

### Sentiment

Registering whether the metaphor elicits a `negative`, `positive` or `neutral` sentiment.

### Emotion

Registering whether any of these emotions is triggered by the metaphor: `fear`, `anger`, `trust`, `sadness`, `disgust`, `surprise`, `anticipation`, `joy`.


## Image

Bounding box containing visual content.

For each visual content, the following aspects were registered:

### Closeness

Registering the image modality, i.e. whether it is a close-up (`focus`) or a `landscape` perspective.

### Angle

Registering whether the image is depicted from a `bottom-up`, `top-down` or `eye-level` point of view.

### Cultural Context

Registering any connection to a specific cultural landscape triggered by the image.

### Metaphor

Registering whether the image contains a metaphorical expression

### Quotation

Registering the metaphorical content contained in the image.

### Source Domain

Source domain of the metaphorical expression

### Target Domain

Target domain of the metaphorical expression

### Sentiment

Registering whether the metaphor elicits a `negative`, `positive` or `neutral` sentiment.

### Emotion

Registering whether any of these emotions is triggered by the metaphor: `fear`, `anger`, `trust`, `sadness`, `disgust`, `surprise`, `anticipation`, `joy`.


## Participant

Within each image, the main participant were identified through polygons and tagged with the following features:

### Type

Registering the type of participant (e.g., person, policeman, waiter, animal, object, etc.)

### Gaze

Registering the gaze of the participant


### Gesture

Registering the gesture of the participant


### Posture

Registering the posture of the participant (e.g., standing, sitting, leaning towards sth...)

### Role

Registering whether the participant is an `actor` or `undergoer` in the event depicted in the image.


### Process

Identifying the kind of event (`material`, `mental`, `relational`, `verbal`, `behavioral`).


## Relationship: connected metaphor

In case two or more metaphors were identified in the front page, this node was used to connect the two elements and signal a relationship holding among the metaphors.

## Relationship: contained

As more areas of interests can be identified in the same front page, and similarly multiple images and text areas are possible, this relationship was employed to connect


