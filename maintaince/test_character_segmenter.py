# -*- coding: utf-8 -*-
from unittest import TestCase

from maintaince.script import character_segmenter


class TestCharacter_segmenter(TestCase):

    def test_character_segmenter(self):
        input = (u"tố “làm luật”: Bộ._trưởng ")
        actual = character_segmenter(input)
        expected = u'tố “làm luật”:Bộ._trưởng'
        self.assertEqual(actual,expected)
        # return actual

    def test_character_segmenter_2(self):
        input = ("300.000 VND")
        actual = character_segmenter(input)
        expected = ("300.000 VND")
        self.assertEqual(actual,expected)

    def test_character_segmenter_3(self):
        input = (u"A._Ferrari (VND)")
        actual = character_segmenter(input)
        expected = (u"A._Ferrari ( VND )")
        self.assertEqual(actual,expected)

