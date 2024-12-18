from antlr4 import *
import copy

if "." in __name__:
    from .RegexParser import RegexParser
else:
    from RegexParser import RegexParser


class RegexVisitor(ParseTreeVisitor):

    def __init__(self):
        super().__init__()
        self.stack = []

    def visitRegex(self, ctx: RegexParser.RegexContext):
        return self.visitChildren(ctx)

    def visitAlternation(self, ctx: RegexParser.AlternationContext):
        b = []
        cnt = 0
        for child in ctx.concatenation():
            cnt += 1
            old_ind = len(self.stack)
            self.visit(child)
            b.append(self.stack[old_ind:])
        current_stack = []
        if cnt > 1:
            i, count_split_and_jump  = 0, 0
            for branch in b:
                for p in branch:
                    p_copy = copy.deepcopy(p)
                    if i != 0:
                        if p[0] == "split":
                            p_copy[1] += count_split_and_jump
                            p_copy[2] += count_split_and_jump
                        elif p[0] == "jmp" and p[1] != "end":
                            p_copy[1] += count_split_and_jump
                    current_stack.append(p_copy)
                copy_stack = []
                if i != cnt - 1:
                    copy_stack.append(["split", 1, len(current_stack) + 2])
                    for p in current_stack:
                        p_copy = copy.deepcopy(p)
                        if p[0] == "split":
                            p_copy[1] += 1
                            p_copy[2] += 1
                        elif p[0] == "jmp" and p[1] != "end":
                            p_copy[1] += 1
                        copy_stack.append(p_copy)
                    copy_stack.append(["jmp", "end"])
                    count_split_and_jump += 2
                    current_stack = copy_stack
                i += 1
            self.stack = current_stack
        else:
            current_stack = b
        return current_stack

    def visitConcatenation(self, ctx: RegexParser.ConcatenationContext):
        return self.visitChildren(ctx)

    def visitRepetition(self, ctx: RegexParser.RepetitionContext):
        stack = self.visit(ctx.primary())
        if stack is None:
            stack = []
        count = len(stack)
        current_stack = stack
        if ctx.QUESTION():
            self.stack = self.stack[:-count]
            current_stack = [["split", len(self.stack) + 1, len(self.stack) + len(stack) + 1]] + stack
            self.stack += current_stack
        elif ctx.STAR():
            self.stack = self.stack[:-count]
            current_stack = [["split", len(self.stack) + 1, len(self.stack) + len(stack) + 2]] + stack
            current_stack.append(["jmp", len(self.stack)])
            self.stack += current_stack
        elif ctx.PLUS():
            tmp_stack = [["split", len(self.stack) - 1, len(self.stack) + len(stack)]]
            self.stack += tmp_stack
            current_stack = stack + tmp_stack
        return current_stack
    def visitSymbol(self, ctx: RegexParser.SymbolContext):
        current_stack = []
        current_stack += [["char", ctx.getText()]]
        self.stack += current_stack
        return current_stack
    def visitPrimary(self, ctx: RegexParser.PrimaryContext):
        if ctx.group():
            return self.visit(ctx.group())
        elif ctx.symbol():
            return self.visit(ctx.symbol())
    def visitGroup(self, ctx: RegexParser.GroupContext):
        return self.visit(ctx.alternation())
del RegexParser
