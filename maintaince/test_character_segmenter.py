# -*- coding: utf-8 -*-
from unittest import TestCase

from maintaince.tokenize import tokenize


class Test_TokenizeSentence(TestCase):
    def test_tokenize(self):
        text = "300.000.000.000"
        actual = tokenize(text)
        expected = "300.000.000.000"
        self.assertEqual(actual, expected)

    def test_tokenize_2(self):
        text = u"Vụ “hot girl xứ Thanh” has 400.000 (USD)"
        actual = tokenize(text)
        expected = u'Vụ “ hot girl xứ Thanh ” has 400.000 ( USD )'
        self.assertEqual(actual, expected)

    def test_tokenize_3(self):
        text = "abc@gmail.com"
        actual = tokenize(text)
        expected = "abc@gmail.com"
        self.assertEqual(actual, expected)

    def test_tokenize_4(self):
        text = u"giá chỉ từ 800.000đ - 3.000.000đ/1 vòng vàng charm. Một số xu hướng"
        actual = tokenize(text)
        expected = u"giá chỉ từ 800.000 đ - 3.000.000 đ / 1 vòng vàng charm . Một số xu hướng"
        self.assertEqual(actual, expected)

    def test_tokenize_42(self):
        text = u"800.000VNĐ"
        actual = tokenize(text)
        expected = u"800.000 VNĐ"
        self.assertEqual(actual, expected)

    def test_tokenize_41(self):
        text = u"chỉ số 800.000VNĐ"
        actual = tokenize(text)
        expected = u"chỉ số 800.000 VNĐ"
        self.assertEqual(actual, expected)

    def test_tokenize_5(self):
        text = u"tăng tốc từ 0-100 km/h trong 3,2 giây và tốc độ tối đa 330 km/h. Tại Việt Nam "
        actual = tokenize(text)
        expected = u"tăng tốc từ 0 - 100 km / h trong 3,2 giây và tốc độ tối đa 330 km / h . Tại Việt Nam"
        self.assertEqual(actual, expected)

    def test_tokenize_6(self):
        text = u"ngày 6/2/2017: Kết quả xổ số điện toán 123 là 2 26 733; "
        actual = tokenize(text)
        expected = u"ngày 6 / 2 / 2017 : Kết quả xổ số điện toán 123 là 2 26 733 ;"
        self.assertEqual(actual, expected)

    def test_tokenize_7(self):
        text = u"https://github.com/JackNhat/underthesea.UTSWS_1"
        actual = tokenize(text)
        expected = u"https://github.com/JackNhat/underthesea.UTSWS_1"
        self.assertEqual(actual, expected)

        text = u"abcdajkflajflajflajlfajlfjsal.com.edu.vn"
        actual = tokenize(text)
        expected = u"abcdajkflajflajflajlfajlfjsal.com.edu.vn"
        self.assertEqual(actual, expected)

    def test_tokenize_8(self):
        text = u'cơ. “Tôi đã bớt ngây thơ hơn trong cách nhìn nhận về thế giới, nhưng điều này vẫn cần học hỏi thêm”, anh nói. Mtexth Hải'
        actual = tokenize(text)
        expected = u"cơ . “ Tôi đã bớt ngây thơ hơn trong cách nhìn nhận về thế giới , nhưng điều này vẫn cần học hỏi thêm ” , anh nói . Mtexth Hải"
        self.assertEqual(actual, expected)

    def test_tokenize_9(self):
        text = u"Sen Vàng (P.Mtexth Khai, Q.Hai Bà Trưng, Hà Nội), "
        actual = tokenize(text)
        expected = u'Sen Vàng ( P . Mtexth Khai , Q . Hai Bà Trưng , Hà Nội ) ,'
        self.assertEqual(actual, expected)

    def test_tokenize_10(self):
        text = u"->"
        actual = tokenize(text)
        expected = u"->"
        self.assertEqual(actual, expected)

    def test_tokenize_11(self):
        text = u"3,4"
        actual = tokenize(text)
        expected = u"3,4"
        self.assertEqual(actual, expected)

    def test_tokenize_12(self):
        text = u"google.com"
        actual = tokenize(text)
        expected = u"google.com"
        self.assertEqual(actual, expected)

    def test_tokenize_13(self):
        text = u"..."
        actual = tokenize(text)
        expected = u"..."
        self.assertEqual(actual, expected)

    def test_tokenize_14(self):
        text = u"máy bay F-111"
        actual = tokenize(text)
        expected = u"máy bay F-111"
        self.assertEqual(actual, expected)

    def test_tokenize_15(self):
        text = u"xem tại đây >>"
        actual = tokenize(text)
        expected = u"xem tại đây >>"
        self.assertEqual(actual, expected)

    def test_tokenize_16(self):
        text = u"mô-men vô-lăng la-zăng"
        actual = tokenize(text)
        expected = u"mô-men vô-lăng la-zăng"
        self.assertEqual(actual, expected)


    def test_tokenize_17(self):
        text = u"'1.729"
        actual = tokenize(text)
        expected = u"' 1.729"
        self.assertEqual(actual, expected)

    def test_tokenize_18(self):
        text = u"' '000001"
        actual = tokenize(text)
        expected = u"' 000001"
        self.assertEqual(actual, expected)