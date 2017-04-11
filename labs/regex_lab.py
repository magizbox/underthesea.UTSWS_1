# -*- coding: utf-8 -*-
import re

# digit_pattern = "\b\d+([\.,]\d+)*\b"
# print re.match(digit_pattern, "9000b") is not None
# print re.match(digit_pattern, "a\n9000b", re.MULTILINE) is None
#
# # digit_pattern doesn't match "9000b"
# print re.match("\b\d+([\.,]\d+)\b$", "9000b") is None

# digit_pattern = r"\b\d+([\.,]\d+)*\w+\b"
# digit_pattern = r"\b[0-9\.]+[0-9]+\b"
digit_pattern = r"\b\d+([\.,]\d+)+\d\b"
# expect matched
print re.match(digit_pattern, "300", re.UNICODE) is not None
print re.match(digit_pattern, "300.000", re.UNICODE) is not None

# expect not match
matched = re.match(digit_pattern, "300.000b", re.UNICODE)
print matched is None
print re.match(digit_pattern, u"300.000đ", re.UNICODE) is None
matched = re.match(digit_pattern, u"300.000.000đ", re.UNICODE)
print matched is None

# matched_1 = re.match(digit_pattern, "300.000b", re.UNICODE)
# print matched_1
