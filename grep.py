def grep(pattern, flags, files):
    flag_list = flags.split() if flags else []
    has_n = '-n' in flag_list
    has_l = '-l' in flag_list
    has_i = '-i' in flag_list
    has_v = '-v' in flag_list
    has_x = '-x' in flag_list

    matches = []
    files_with_matches = []

    for filename in files:
        with open(filename) as f:
            lines = f.readlines()

        file_has_match = False

        for line_num, line in enumerate(lines, 1):
            line_content = line.rstrip('\n')

            search_pattern = pattern.lower() if has_i else pattern
            search_line = line_content.lower() if has_i else line_content

            if has_x:
                matches_pattern = search_pattern == search_line
            else:
                matches_pattern = search_pattern in search_line

            if has_v:
                matches_pattern = not matches_pattern

            if matches_pattern:
                matches.append((filename, line_num, line_content))
                if not file_has_match:
                    files_with_matches.append(filename)
                    file_has_match = True

    if has_l:
        result = '\n'.join(files_with_matches)
        return result + '\n' if result else ''

    result_lines = []
    for filename, line_num, line_content in matches:
        line_output = ''

        if len(files) > 1:
            line_output += filename + ':'

        if has_n:
            line_output += str(line_num) + ':'

        line_output += line_content
        result_lines.append(line_output)

    return '\n'.join(result_lines) + '\n' if result_lines else ''
