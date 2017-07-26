def distance(strand_1, strand_2):
    hamming_distance = 0
    if len(strand_1) != len(strand_2):
        raise ValueError('strands are invalid or of different length')
    for h1, h2 in zip(strand_1, strand_2):
        if h1 != h2:
            hamming_distance += 1
    return hamming_distance
