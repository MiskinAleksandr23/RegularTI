from antlr4 import InputStream, CommonTokenStream
from gen.RegexLexer import RegexLexer
from gen.RegexParser import RegexParser
from gen.RegexVisitor import RegexVisitor
from logging import exception
import copy

class RegexVirtualMachine:
    def __init__(self, regex):
        self.regex = regex
        self.stack = self._build_instructions()

    def _build_instructions(self):
        input_stream = InputStream(self.regex)
        lexer = RegexLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = RegexParser(token_stream)
        tree = parser.regex()
        visitor = RegexVisitor()
        visitor.visit(tree)
        stack = visitor.stack
        stack.append(["match"])
        copy_stack = []
        for l in range(len(stack)):
            l_copy = copy.deepcopy(stack[l])
            if len(stack[l]) > 1 and stack[l][0] == "jmp" and stack[l][1] == "end":
                l_copy[1] = len(stack) - 1
            copy_stack.append(l_copy)
        return copy_stack

    def parse_str(self, string, curr_ind=0, visited=None):
        if visited is None:
            visited = set()

        if (string, curr_ind) in visited:
            return False
        visited.add((string, curr_ind))
        current_instr = self.stack[curr_ind]
        if current_instr[0] == "char" and string != "" and string[0] == current_instr[1]:
            return self.parse_str(string[1:], curr_ind + 1, visited)
        elif current_instr[0] == "char" and (string == "" or string[0] != current_instr[1]):
            return False
        elif current_instr[0] == "jmp":
            return self.parse_str(string, current_instr[1], visited)
        elif current_instr[0] == "split":
            first = current_instr[1]
            second = current_instr[2]
            return self.parse_str(string, first, visited) or self.parse_str(string, second, visited)
        elif current_instr[0] == "match" and string == "":
            return True
        elif current_instr[0] == "match" and string != "":
            return False
        return False

    def matches(self, string):
        return self.parse_str(string)


def test():
    tests = [
        ('a|b', 'abba', False),
        ('(a*)b', 'aab', True),
        ('(ab)', 'ab', True),
        ('(ab)+', 'ab', True),
        ('a(a*)b', 'aaaab', True),
        ('abababab', 'aab', False),
        ('(ab)(a?)(b+)', 'abb', True),
        ('(ab)+', 'ab', True),
        ('(a|b)+', 'a', True),
        ('a*(b+)', 'ab', True),
        ('(a*)(b*)', 'abbbbbbbbbbbbbbbba', False),
        ('(a*)(b*)', 'abbbbbbbbbbbbbbbb', True),
        ('(a)+b+a+', 'aba', True),
        ('(a)+b+a+', 'abab', False),
]

    for ind, (regex, string, expected) in enumerate(tests, 1):
        vm = RegexVirtualMachine(regex)
        if vm.matches(string) != expected:
            raise exception(f"WA test {ind}")


def local_test(regex, string):
    vm = RegexVirtualMachine(regex)
    print(vm.matches(string))


if __name__ == "__main__":
    test()
    local_test("((ab)*)(b*)", "abb")