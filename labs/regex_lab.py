# -*- coding: utf-8 -*-
import re

digit_pattern = r"\b.*đ\B"

# expect matched
print re.match(digit_pattern, "300", re.UNICODE) is not None

print re.match(digit_pattern, "300.000", re.UNICODE) is not None

print re.match(digit_pattern, "300.000.000", re.UNICODE) is not None


# expect not match
print re.match(digit_pattern, u"300đ", re.UNICODE) is None

print re.match(digit_pattern, u"300.000đ", re.UNICODE) is None

print re.match(digit_pattern, u"300.000.000đ", re.UNICODE) is None
