import queue

class DFA:
    def __init__(self, n: int, m: int):
        self.n = n
        self.m = m
        self.accepted = [False for i in range(n)]
        self.transitions = [[-1 for j in range(m)] for i in range(n)]
        self.start = -1

    def add_transition(self, _from: int, _to: int, symbol: int) -> None:
        assert 0 <= _from < self.n and 0 <= _to < self.n and 0 <= symbol < self.m
        self.transitions[_from][symbol] = _to

    def set_accepted(self, accepted_list):
        for vertex in accepted_list:
            assert 0 <= vertex < self.n
            self.accepted[vertex] = True

    def set_start(self, _start: int) -> None:
        self.start = _start

    def execute(self, array):
        assert self.start != -1
        current: int = self.start
        for val in array:
            if self.transitions[current][val] == -1:
                return False
            current = self.transitions[current][val]
        return self.accepted[current]

def MinimizeDFA(dfa: DFA) -> DFA:
    classes = []
    if sum(dfa.accepted) > 0:
        classes.append([i for i in range(dfa.n) if dfa.accepted[i]])
    if sum(dfa.accepted) != dfa.n:
        classes.append([i for i in range(dfa.n) if not dfa.accepted[i]])
    def update():
        for r_class in classes:
            for _symbol in range(dfa.m):
                st = set()
                for _el in r_class:
                    st.add(dfa.transitions[_el][_symbol])
                if len(st) != 1:
                    classes.remove(r_class)
                    to = [[] for i in range(dfa.n)]
                    dead = []
                    for _el in r_class:
                        if dfa.transitions[_el][_symbol] != -1:
                            to[dfa.transitions[_el][_symbol]].append(_el)
                        else:
                            dead.append(_el)
                    for new_possible_class in to:
                        if len(new_possible_class) > 0:
                            classes.append(new_possible_class)
                    if len(dead) > 0:
                        classes.append(dead)
                    return True

        return False
    while True:
        if not update():
            break
    n = len(classes)
    m = dfa.m
    result: DFA = DFA(n, m)
    accepted = [False for i in range(n)]
    for i in range(n):
        flag: bool = True
        for el in classes[i]:
            if not el in dfa.accepted:
                flag = False
        if flag:
            accepted[i] = True
    result.set_accepted(accepted)
    start: int = -1
    for i in range(n):
        if dfa.start in classes[i]:
            start = i
    result.set_start(start)

    def find_class_by_el(a: int):
        for j in range(n):
            if a in classes[j]:
                return j

    for i in range(n):
        for symbol in range(m):
            q_0 = classes[i][0]
            if (dfa.transitions[q_0][symbol]) != -1:
                result.add_transition(i, find_class_by_el(dfa.transitions[q_0][symbol]), symbol)
    return result


def EqualDfa(dfa1: DFA, dfa2: DFA):
    if dfa1.n != dfa2.n or dfa1.m != dfa2.m:
        return False
    q = queue.Queue()
    q.put((dfa1.start, dfa2.start))
    used = [[False for i in range(dfa1.n)] for j in range(dfa1.n)]
    while not q.empty():
        u, v = q.get()
        if dfa1.accepted[u] != dfa2.accepted[v]:
            return False
        used[u][v] = True
        for sym in range(dfa1.m):
            if (dfa1.transitions[u][sym], dfa2.transitions[v][sym]) == (-1, -1):
                continue
            elif dfa1.transitions[u][sym] == -1 or dfa2.transitions[v][sym] == -1:
                return False
            else:
                q.put((dfa1.transitions[u][sym], dfa2.transitions[v][sym]))
    return True

def CheckFullLanguage(dfa: DFA):
    min_dfa = MinimizeDFA(dfa)
    if min_dfa.n > 1:
        return False
    for i in range(min_dfa.m):
        if min_dfa.transitions[0][i] == -1:
            return False
    if not dfa.accepted[0]:
        return False
    return True

def Test1():
    # 6 состояний, бьются на три группы по 2 так, что из одной группы в другую переходы одинаковые. Тогда каждую
    # группу можно отождествить с одной вершиной. Итого 3 вершины.
    dfa_x = DFA(6, 3)
    l_groups = [[0, 1], [2, 3], [4, 5]]
    for i in range(3):
        for j in range(3):
            if i == j:
                continue

            for a in l_groups[i]:
                for b in l_groups[j]:
                    dfa_x.add_transition(a, b, (i + j) % 3)
    dfa_y = MinimizeDFA(dfa_x)

    if dfa_y.n != 3:
        raise Exception("Test 1 failed")



def TestFullLanguage():
    dfa_x = DFA(6, 3)
    for i in range(6):
        for j in range(6):
            for p in range(3):
                dfa_x.add_transition(i, j, p)
    dfa_x.start = 0
    dfa_x.accepted = [True for i in range(6)]
    min_dfa = MinimizeDFA(dfa_x)
    if not CheckFullLanguage(min_dfa):
        raise Exception("Test 2 failed")

def TestEqualDfa():
    dfa_x = DFA(6, 3)
    dfa_y = DFA(6, 3)
    if not EqualDfa(dfa_x, dfa_y):
        raise Exception("Test 3 failed")

def Create_dfa(n: int, m: int, start: int, accepted: [bool], list_transitions):
    # list_transitions = [(from, to, symbol)]
    dfa = DFA(n, m)
    dfa.accepted = accepted
    dfa.start = start
    for (u, v, w) in list_transitions:
        dfa.add_transition(u, v, w)
    return dfa

#Example
example_dfa = Create_dfa(3, 2, 0, [False, False, True], [(0, 1, 1), (0, 2, 0), (1, 2, 1)])


def CustomTest():
    pass


Test1()
TestFullLanguage()
TestEqualDfa()
CustomTest()


