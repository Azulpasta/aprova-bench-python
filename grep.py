def grep(pattern, flags, files):
    flag_set = set(flags.split())
    multiple_files = len(files) > 1

    result = []
    for filename in files:
        with open(filename) as f:
            lines = f.readlines()

        file_matched = False
        for i, line in enumerate(lines, start=1):
            line = line.rstrip("\n")

            if "-x" in flag_set:
                if "-i" in flag_set:
                    matches = line.lower() == pattern.lower()
                else:
                    matches = line == pattern
            else:
                if "-i" in flag_set:
                    matches = pattern.lower() in line.lower()
                else:
                    matches = pattern in line

            if "-v" in flag_set:
                matches = not matches

            if matches:
                file_matched = True
                if "-l" in flag_set:
                    break

                prefix = ""
                if multiple_files:
                    prefix += filename + ":"
                if "-n" in flag_set:
                    prefix += str(i) + ":"
                result.append(prefix + line + "\n")

        if "-l" in flag_set and file_matched:
            result.append(filename + "\n")

    return "".join(result)
