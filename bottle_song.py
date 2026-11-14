NUMBERS = [
    "no",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
    "ten",
]


def bottles(count):
    word = "bottle" if count == 1 else "bottles"
    return f"{NUMBERS[count]} green {word} hanging on the wall"


def verse(count):
    line = bottles(count).capitalize()
    return [
        f"{line},",
        f"{line},",
        "And if one green bottle should accidentally fall,",
        f"There'll be {bottles(count - 1)}.",
    ]


def recite(start, take=1):
    lines = []
    for count in range(start, start - take, -1):
        if lines:
            lines.append("")
        lines.extend(verse(count))
    return lines
