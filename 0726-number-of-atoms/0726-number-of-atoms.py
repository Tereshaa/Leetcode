class Solution:
    def countOfAtoms(self, formula: str) -> str:
        def multiply_counts(counts, factor):
            for element in counts:
                counts[element] *= factor
            return counts

        stack = []
        current_counts = defaultdict(int)
        i = 0
        n = len(formula)

        while i < n:
            if formula[i] == '(':
                stack.append(current_counts)
                current_counts = defaultdict(int)
                i += 1
            elif formula[i] == ')':
                i += 1
                j = i
                while j < n and formula[j].isdigit():
                    j += 1
                factor = int(formula[i:j] or 1)
                current_counts = multiply_counts(current_counts, factor)
                prev_counts = stack.pop()
                for elem, count in current_counts.items():
                    prev_counts[elem] += count
                current_counts = prev_counts
                i = j
            else:
                j = i + 1
                while j < n and formula[j].islower():
                    j += 1
                element = formula[i:j]
                i = j
                while j < n and formula[j].isdigit():
                    j += 1
                count = int(formula[i:j] or 1)
                current_counts[element] += count
                i = j

        result = []
        for elem in sorted(current_counts.keys()):
            result.append(elem)
            if current_counts[elem] > 1:
                result.append(str(current_counts[elem]))

        return ''.join(result)
