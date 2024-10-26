class RegexVM:
    def __init__(self, regex):
        self.instructions = RegexVM.build(regex)

    @staticmethod
    def build(regex: str):
        instructions = []
        index = 0
        while index < len(regex):
            if index + 1 < len(regex) and regex[index] in "ab" and regex[index + 1] == "*":
                instructions.append(('split', len(instructions) + 1, len(instructions) + 3))
                instructions.append(('char', regex[index]))
                instructions.append(('jmp', len(instructions) - 2))
                index += 2

            elif index + 1 < len(regex) and regex[index] in "ab" and regex[index + 1] == "+":
                instructions.append(('char', regex[index]))
                instructions.append(('split', len(instructions) - 1, len(instructions) + 1))
                index += 2
            elif index + 1 < len(regex) and regex[index] in "ab" and regex[index + 1] == "?":
                instructions.append(('split', len(instructions) + 1, len(instructions) + 2))
                instructions.append(('char', regex[index]))
                index += 2
            ###TODO он пока не работает, тестов на него нету.
            elif index + 1 < len(regex) and regex[index] == "|" and regex[index + 1] in "ab":
                split_instr = ('split', len(instructions) + 1, len(instructions) + 3)
                instructions.append(split_instr)
                index += 1
                instructions.append(('char', regex[index]))
                jmp_instr = ('jmp', len(instructions) + 2)
                instructions.append(jmp_instr)
                index += 1
                instructions.append(('char', regex[index]))

            elif regex[index] in "ab":
                instructions.append(('char', regex[index]))
                index += 1

        instructions.append(('match',))
        return instructions

    def match(self, string):
        pc = 0
        index = 0
        stack = []
        visited_states = set()

        while True:
            instr = self.instructions[pc]
            if instr[0] == 'char':
                if index >= len(string) or string[index] != instr[1]:
                    if stack:
                        pc, index = stack.pop()
                        continue
                    else:
                        return False
                index += 1
                pc += 1

            elif instr[0] == 'match':
                return index == len(string)

            elif instr[0] == 'split':
                x, y = instr[1], instr[2]
                if (pc, index) not in visited_states:
                    stack.append((y, index))
                    visited_states.add((pc, index))
                pc = x

            elif instr[0] == 'jmp':
                if (pc, index) not in visited_states:
                    visited_states.add((pc, index))  #
                pc = instr[1]


TESTS = [
    ("a+b+", "aaabb", True),
    ("a+b+", "aabba", False),
    ("a+b+", "aa", False),
    ("a*b*", "aabbbb", True),
    ("a*b*", "ab", True),
    ("a*b*", "b", True),
    ("aaa?ba", "abba", False),
    ("aaa?ba", "aaba", True),
    ("a+bb*", "aa", False),
    ("a+bb+a*", "aaabb", True),
    ("aa*", "aa", True),
    ("babb*b?b+", "babbbbbbbb", True),
    ("a+", "aaaa", True),
    ("a+", "b", False),
    ("a*b", "aab", True),
    ("a*b", "b", True),
    ("a*b", "aabb", False),
    ("a?b", "b", True),
    ("a?b", "ab", True),
    ("a?b", "aa", False),
    ("a*b+", "b", True),
    ("a*b+", "bb", True),
    ("a*b+", "aab", True),
    ("a*b+", "a", False),
    ("a*b+", "aaabbb", True),
    ("ab+", "ab", True),
    ("ab+", "a", False),
    ("ab+", "abb", True),
    ("a*b?", "a", True),
    ("a*b?", "ab", True),
    ("a*b?", "aabb", False),
    ("a+bb*", "abb", True),
    ("a+bb*", "abbb", True),
    ("a+bb*", "a", False),
    ("ab?a", "aa", True),
    ("ab?a", "aba", True),
    ("ab?a", "ababa", False),
    ("a*bb+", "bb", True),
    ("a*bb+", "abbb", True),
    ("a*bb+", "aab", False),
    ("a+ba?", "aa", False),
    ("a+ba?", "aab", True),
    ("a+ba?", "aaba", True),
    ("ab*a", "a", False),
    ("ab*a", "aba", True),
    ("ab*a", "abbaa", False),
    ("a?b?a?", "a", True),
    ("a?b?a?", "b", True),
    ("a?b?a?", "ab", True),
    ("a?b?a?", "ba", True),
    ("a?b?a?", "aa", True),
    ("a?b?a?", "abb", False),
    ("a*b*b*", "aabbb", True),
    ("a*b*b*", "ab", True),
    ("a*b*b*", "bbbb", True),
    ("a*b*b*", "aabbbba", False),
]


cnt = 0
for (a, b, c) in TESTS:
    cnt += 1
    X = RegexVM(a)
    if X.match(b) != c:
        print(a, b, c)
        raise Exception(f'WA test {cnt}')
