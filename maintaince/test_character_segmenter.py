# -*- coding: utf-8 -*-
from unittest import TestCase

from maintaince.tokenize_sentence import tokenize_sentence


class Test_TokenizeSentence(TestCase):

    def test_tokenize_sentence(self):
        input = "300.000.000.000"
        actual = tokenize_sentence(input)
        expected = "300.000.000.000"
        self.assertEqual(actual, expected)

    def test_tokenize_sentence_2(self):
        input = u"Vụ “hot girl xứ Thanh” has 400.000 (USD) "
        actual = tokenize_sentence(input)
        expected = u'Vụ “ hot girl xứ Thanh ” has 400.000 ( USD ) '
        self.assertEqual(actual, expected)

    def test_tokenize_sentence_3(self):
        input = ("abc@gmail.com")
        actual = tokenize_sentence(input)
        expected = ("abc@gmail.com")
        self.assertEqual(actual, expected)

    def test_tokenize_sentence_4(self):
        input = u"giá chỉ từ 800.000đ - 3.000.000đ/1 vòng vàng charm. Một số xu hướng"
        actual = tokenize_sentence(input)
        expected = u"giá chỉ từ 800.000 đ - 3.000.000 đ / 1 vòng vàng charm . Một số xu hướng"
        self.assertEqual(actual, expected)

    def test_tokenize_sentence_42(self):
        input = u"800.000VNĐ"
        actual = tokenize_sentence(input)
        expected = u"800.000 VNĐ"
        self.assertEqual(actual, expected)

    def test_tokenize_sentence_41(self):
        input = u"chỉ số 800.000VNĐ"
        actual = tokenize_sentence(input)
        expected = u"chỉ số 800.000 VNĐ"
        self.assertEqual(actual, expected)

    def test_tokenize_sentence_5(self):
        input = u"tăng tốc từ 0-100 km/h trong 3,2 giây và tốc độ tối đa 330 km/h. Tại Việt Nam "
        actual = tokenize_sentence(input)
        expected = u"tăng tốc từ 0 - 100 km / h trong 3,2 giây và tốc độ tối đa 330 km / h . Tại Việt Nam "
        self.assertEqual(actual, expected)

    def test_tokenize_sentence_6(self):
        input = u"ngày 6/2/2017: Kết quả xổ số điện toán 123 là 2 26 733; "
        actual = tokenize_sentence(input)
        expected = u"ngày 6 / 2 / 2017 : Kết quả xổ số điện toán 123 là 2 26 733 ; "
        self.assertEqual(actual, expected)


    def test_tokenize_sentence_7(self):
        input = u"https://github.com/JackNhat/underthesea.UTSWS_1"
        actual = tokenize_sentence(input)
        expected = u"https://github.com/JackNhat/underthesea.UTSWS_1"
        self.assertEqual(actual, expected)



    def test_tokenize_sentence_8(self):
        input = u"cơ. “Tôi đã bớt ngây thơ hơn trong cách nhìn nhận về thế giới, nhưng điều này vẫn cần học hỏi thêm”, anh nói. Minh Hải"
        actual = tokenize_sentence(input)
        expected = u"cơ . “ Tôi đã bớt ngây thơ hơn trong cách nhìn nhận về thế giới , nhưng điều này vẫn cần học hỏi thêm ” , anh nói . Minh Hải"
        self.assertEqual(actual, expected)

    def test_tokenize_sentence_9(self):
        input = u"Sen Vàng (P.Minh Khai, Q.Hai Bà Trưng, Hà Nội), "
        actual = tokenize_sentence(input)
        expected = u'Sen Vàng ( P . Minh Khai , Q . Hai Bà Trưng , Hà Nội ) , '
        self.assertEqual(actual, expected)

    def test_tokenize_sentence_10(self):
        input = u"->"
        actual = tokenize_sentence(input)
        expected = u"->"
        self.assertEqual(actual, expected)

    def test_tokenize_sentence_11(self):
        input = u"3,4"
        actual = tokenize_sentence(input)
        expected = u"3,4"
        self.assertEqual(actual, expected)

    def test_tokenize_sentence_12(self):
        input = u"google.com"
        actual = tokenize_sentence(input)
        expected = u"google.com"
        self.assertEqual(actual, expected)

