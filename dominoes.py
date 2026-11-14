def can_chain(dominoes):
    if not dominoes:
        return []

    def search(chain, remaining):
        if not remaining:
            if chain[0][0] == chain[-1][1]:
                return chain
            return None
        last = chain[-1][1]
        for i, (a, b) in enumerate(remaining):
            rest = remaining[:i] + remaining[i + 1 :]
            if a == last:
                result = search(chain + [(a, b)], rest)
                if result is not None:
                    return result
            if b == last:
                result = search(chain + [(b, a)], rest)
                if result is not None:
                    return result
        return None

    first = dominoes[0]
    rest = dominoes[1:]
    return search([first], rest)
