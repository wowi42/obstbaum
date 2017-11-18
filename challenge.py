#!/usr/bin/env python3


class TurnstileException(Exception):
    pass


class Turnstile:
    def __init__(self, locked=True):
        self._locked = locked

    def put_coin(self):
        self._locked = False

    def pass_through(self):
        if self._locked:
            raise TurnstileException('Turnstil is locked !')
        # reset the turnstile
        self._locked = True

    def is_locked(self):
        return self._locked


class Customer:

    def pay(self, turnstile):
        turnstile.put_coin()

    def pass_(self, turnstile):
        turnstile.pass_through()
