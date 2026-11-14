ANIMALS = [
    "fly",
    "spider",
    "bird",
    "cat",
    "dog",
    "goat",
    "cow",
    "horse",
]

COMMENTS = {
    "fly": None,
    "spider": "It wriggled and jiggled and tickled inside her.",
    "bird": "How absurd to swallow a bird!",
    "cat": "Imagine that, to swallow a cat!",
    "dog": "What a hog, to swallow a dog!",
    "goat": "Just opened her throat and swallowed a goat!",
    "cow": "I don't know how she swallowed a cow!",
    "horse": "She's dead, of course!",
}


def verse(n):
    animal = ANIMALS[n - 1]
    lines = [f"I know an old lady who swallowed a {animal}."]

    if animal == "horse":
        lines.append(COMMENTS["horse"])
        return lines

    comment = COMMENTS[animal]
    if comment:
        lines.append(comment)

    for i in range(n, 1, -1):
        predator = ANIMALS[i - 1]
        prey = ANIMALS[i - 2]
        line = f"She swallowed the {predator} to catch the {prey}"
        if prey == "spider":
            line += " that wriggled and jiggled and tickled inside her"
        lines.append(line + ".")

    lines.append(
        "I don't know why she swallowed the fly. Perhaps she'll die."
    )
    return lines


def recite(start_verse, end_verse):
    lines = []
    for n in range(start_verse, end_verse + 1):
        if lines:
            lines.append("")
        lines.extend(verse(n))
    return lines
