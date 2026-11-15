def recite(start_verse, end_verse):
    animals = [
        ("fly", ""),
        ("spider", "It wriggled and jiggled and tickled inside her."),
        ("bird", "How absurd to swallow a bird!"),
        ("cat", "Imagine that, to swallow a cat!"),
        ("dog", "What a hog, to swallow a dog!"),
        ("goat", "Just opened her throat and swallowed a goat!"),
        ("cow", "I don't know how she swallowed a cow!"),
        ("horse", "She's dead, of course!"),
    ]

    result = []

    for verse_num in range(start_verse, end_verse + 1):
        if verse_num > start_verse:
            result.append("")  # Blank line between verses

        index = verse_num - 1
        animal, phrase = animals[index]

        # First line
        result.append(f"I know an old lady who swallowed a {animal}.")

        # For horse, just add the special ending
        if index == len(animals) - 1:  # Horse
            result.append(phrase)
        else:
            # Peculiar phrase
            if phrase:
                result.append(phrase)

            # Cascade
            for i in range(index, 0, -1):
                swallowed_animal, _ = animals[i]
                caught_animal, caught_action = animals[i - 1]

                if caught_action:
                    catch_phrase = caught_action[3:]  # Remove "It "
                    result.append(f"She swallowed the {swallowed_animal} to catch the {caught_animal} that {catch_phrase}")
                else:
                    result.append(f"She swallowed the {swallowed_animal} to catch the {caught_animal}.")

            # Final line
            result.append("I don't know why she swallowed the fly. Perhaps she'll die.")

    return result
