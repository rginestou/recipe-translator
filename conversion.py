from fuzzywuzzy import fuzz
import re

conversions = {
    "ounce": (28, "g"),
    "pound": (450, "g")
}

cups = {
    "flour": (120, "g"),
    "sugar": (200, "g"),
    "icing sugar": (100, "g"),
    "brown sugar": (180, "g"),
    "cornflour": (120, "g"),
    "rice": (190, "g"),
    "couscous": (180, "g"),
    "uncooked oats": (90, "g"),
    "salt": (300, "g"),
    "butter": (240, "g"),
    "chopped nuts": (150, "g"),
    "ground nuts": (120, "g"),
    "fresh breadcrumbs": (60, "g"),
    "dry breadcrumbs": (150, "g"),
    "sultanas": (200, "g"),
    "raisins": (200, "g"),

    "vegetable stock": (240, "ml"),
    "vegetable broth": (240, "ml"),
    "vegetable": (190, "g"),
}

def round_portion(p, c):
    return int(p * c / 5) * 5

def convert_cups(p, txt):
    maxi_r = 0
    item = ""
    conv = 240 #ml
    for key in cups:
        r = fuzz.token_set_ratio(txt,key)
        if r > maxi_r:
            maxi_r = r
            item = key
            conv = cups[key]

    rp = str(round_portion(p, conv[0]))
    if maxi_r > 80:
        return rp + ' ' + conv[1]
    return rp + ' ' + 'ml'


pattern = "(\d+)(?:\/(\d+))? (\w+)(?: (\(\d+\ ?(?:ml|g|kg|l)\)))?"
regex = re.compile(pattern, re.IGNORECASE)

def convert(txt):
    f = regex.findall(txt)
    if len(f) > 0:
        match = f[0]
        repl = ""

        unit = match[2].rstrip('s')
        p = float(match[0])
        if match[1]:
            p /= float(match[1])

        if unit in conversions:
            conv = conversions[unit]
            repl = str(int(p * conv[0] / 5) * 5) + ' ' + conv[1]
        if unit == "cup":
            repl = convert_cups(p, txt)

        if repl:
            txt = regex.sub(repl, txt)

    return txt
