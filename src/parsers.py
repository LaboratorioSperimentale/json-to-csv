"""Set of utilities to select info from json"""

import collections
import shapely


def AOI (annotation_object):
    ret = collections.defaultdict(str)

    classifications = annotation_object["classifications"]
    for classification in classifications:
        name = classification["name"]
        label = classification["radio_answer"]["name"]

        ret[name] = label

    polygon = annotation_object["polygon"]
    coordinates = []

    for coord in polygon:
        x = coord["x"]
        y = coord["y"]
        coordinates.append((x, y))

    # ret["coordinates"] = coordinates

    ret["area"] = shapely.geometry.Polygon(coordinates).area

    return ret


def TESTO (annotation_object):
    ret = collections.defaultdict(str)

    classifications = annotation_object["classifications"]

    for classification in classifications:
        name = classification["name"]
        label = ""

        if name in ["tipo", "metafora", "sentiment"]:
           label = classification["radio_answer"]["name"]

        elif name in ["metafora_quot", "target domain", "source domain", "metonimia"]:
            label = classification["text_answer"]["content"]

        elif name in ["emotion"]:
            label = [x["name"] for x in classification["checklist_answers"]]
            label = ", ".join(label)

        ret[name] = label


    bounding_box = annotation_object["bounding_box"]
    top = bounding_box["top"]
    left = bounding_box["left"]
    width = bounding_box["width"]
    heigth = bounding_box["height"]

    # ret["coordinates"] = [(top, left), (top, left+width), (top-heigth, left), (top-heigth, left+width)]

    ret["area"] = width*heigth

    return ret


def IMMAGINE (annotation_object):
    ret = collections.defaultdict(str)

    classifications = annotation_object["classifications"]

    for classification in classifications:
        name = classification["name"]
        label = ""

        if name in ["metafora", "sentiment", "closeness", "angle"]:
           label = classification["radio_answer"]["name"]

        elif name in ["target domain", "source domain", "cultural context", "metafora_exp", "metonimia"]:
            label = classification["text_answer"]["content"]

        elif name in ["emotion"]:
            label = [x["name"] for x in classification["checklist_answers"]]
            label = ", ".join(label)

        ret[name] = label


    bounding_box = annotation_object["bounding_box"]
    top = bounding_box["top"]
    left = bounding_box["left"]
    width = bounding_box["width"]
    heigth = bounding_box["height"]

    # ret["coordinates"] = [(top, left), (top, left+width), (top-heigth, left), (top-heigth, left+width)]

    ret["area"] = width*heigth

    return ret



def PARTECIPANTE (annotation_object):
    ret = collections.defaultdict(str)

    classifications = annotation_object["classifications"]

    for classification in classifications:
        name = classification["name"]

        if name in ["role"]:
            label = classification["radio_answer"]["name"]

        if name in ["type", "gaze", "gesture", "posture"]:
            label = classification["text_answer"]["content"]

        if name in ["processo"]:
            label = [x["name"] for x in classification["checklist_answers"]]
            label = ", ".join(label)

        ret[name] = label

    polygon = annotation_object["polygon"]
    coordinates = []

    for coord in polygon:
        x = coord["x"]
        y = coord["y"]
        coordinates.append((x, y))

    # ret["coordinates"] = coordinates

    ret["area"] = shapely.geometry.Polygon(coordinates).area


    return ret