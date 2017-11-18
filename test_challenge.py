#!/usr/bin/env python3
import unittest
from challenge import Turnstile, Customer, TurnstileException


class TestChallenge(unittest.TestCase):

    def test_unlocking_turnstile(self):
        turnstile = Turnstile()
        customer = Customer()
        self.assertTrue(turnstile.is_locked())
        customer.pay(turnstile)
        self.assertFalse(turnstile.is_locked())

    def test_locking_turnstile(self):
        turnstile = Turnstile(False)
        customer = Customer()
        self.assertFalse(turnstile.is_locked())
        customer.pass_(turnstile)
        self.assertTrue(turnstile.is_locked())

    def test_raising_alarm(self):
        turnstile = Turnstile()
        customer = Customer()
        self.assertTrue(turnstile.is_locked())
        with self.assertRaises(TurnstileException):
            customer.pass_(turnstile)
        self.assertTrue(turnstile.is_locked())
        customer.pay(turnstile)
        self.assertFalse(turnstile.is_locked())
        try:
            customer.pass_(turnstile)
        except TurnstileException as e:
            self.fail("Customer should be able to pass!")

    def test_gracefully_eating_money(self):
        turnstile = Turnstile()
        customer = Customer()
        self.assertTrue(turnstile.is_locked())
        customer.pay(turnstile)
        self.assertFalse(turnstile.is_locked())
        customer.pay(turnstile)
        self.assertFalse(turnstile.is_locked())
        customer.pass_(turnstile)
        self.assertTrue(turnstile.is_locked())
