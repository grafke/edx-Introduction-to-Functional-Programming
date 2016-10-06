from abc import ABCMeta, abstractmethod


class Action:
    __metaclass__ = ABCMeta


class Atom(Action, object):
    def Atom(self, atom):
        self.atom = atom

    def get_atom(self):
        return self.atom

    def __str__(self):
        return "atom"


class Form(Action, object):
    def fork(self, a1, a2):
        self.a1 = a1
        self.a2 = a2

    def get_a1(self):
        return self.a1

    def get_a2(self):
        return self.a2

    def __str__(self):
        return 'fork' + str(self.a1) + ' ' + str(self.a2)


class Stop(Action, object):
    def __str__(self):
        return 'stop'


class Concurrent(object):
    def Concurrent(self, func):
        self.func = func

    def of(self, A, a):
        return NotImplemented

    def flat_map(self, mapper):
        return

    def and_then(self, after):
        return

    def action(self):
        return

    def stop(self):
        return

    def atom(self, ioA):
        return

    def fork(self):
        return

    def par(self, c1, c2):
        return

    def run(self):
        return self.round_robin([self.action()])

    def round_robin(self, xs):
        return
