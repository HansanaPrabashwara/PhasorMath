from src.Phasor.phasor import *
from unittest import TestCase


class phasor_test(TestCase):

    def abstractPhasor_test(self):
        self.assertRaises(ValueError, a = Phasor())

