from googletrans import Translator
from conversion import convert

def recipe_tranlate(data):
    lines = data.split('\n')
    for l in range(len(lines)):
        lines[l] = convert(lines[l])

    txt = '\n'.join(lines)

    translator = Translator()
    out = translator.translate(txt, dest='fr').text

    return out

if __name__ == "__main__":
    txt = """
2 (8-ounce) salmon filets, preferably wild
Kosher salt and freshly ground black pepper
1/3 cup plus 2 tablespoons extra-virgin olive oil, divided
1 medium shallot, thinly sliced
6 ounces pearled couscous
3 cups homemade vegetable stock or store-bought low-sodium vegetable broth
2 tablespoons Dijon mustard
2 tablespoons fresh juice from 1 lemon
1/2 cup picked dill, roughly chopped, plus more for garnish
1 1/2 cups spinach leaves, chopped in half if large, or left whole if baby
"""

    print(recipe_tranlate(txt))
