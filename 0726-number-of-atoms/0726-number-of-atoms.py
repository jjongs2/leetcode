from collections import defaultdict


class Solution:
    def countOfAtoms(self, formula: str) -> str:
        length = len(formula)

        def parse_formula(index):
            counts = defaultdict(int)
            while index < length:
                if formula[index] == ")":
                    return index + 1, counts
                if formula[index] == "(":
                    index, inner_counts = parse_formula(index + 1)
                    index, multiplier = parse_number(index)
                    for name, count in inner_counts.items():
                        counts[name] += count * multiplier
                else:
                    index, name = parse_name(index)
                    index, count = parse_number(index)
                    counts[name] += count
            return index, counts

        def parse_name(start):
            end = start + 1
            while end < length and formula[end].islower():
                end += 1
            return end, formula[start:end]

        def parse_number(start):
            end = start
            while end < length and formula[end].isdigit():
                end += 1
            return end, (int(formula[start:end]) if start < end else 1)

        _, counts = parse_formula(0)
        return "".join(
            name + (str(count) if count > 1 else "")
            for name, count in sorted(counts.items())
        )
