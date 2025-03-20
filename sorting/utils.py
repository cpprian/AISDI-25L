from typing import List


def read_words(filename: str, limit: int) -> List[str]:
    output = [None] * limit
    idx = 0
    with open(filename, "r") as file:
        for line in file:
            for word in line.split():
                if idx < limit:
                    output[idx] = word
                    idx += 1
                else:
                    return output
    return output[:idx]
