def recite(start, take=1):
    number_words = {
        0: "no", 1: "one", 2: "two", 3: "three", 4: "four",
        5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten"
    }

    def pluralize(n):
        return "bottle" if n == 1 else "bottles"

    def verse(n):
        current = number_words[n].capitalize()
        current_plural = pluralize(n)
        next_n = n - 1
        next_word = number_words[next_n]
        next_plural = pluralize(next_n)

        return [
            f"{current} green {current_plural} hanging on the wall,",
            f"{current} green {current_plural} hanging on the wall,",
            "And if one green bottle should accidentally fall,",
            f"There'll be {next_word} green {next_plural} hanging on the wall.",
        ]

    lines = []
    for i in range(take):
        if i > 0:
            lines.append("")
        lines.extend(verse(start - i))

    return lines
