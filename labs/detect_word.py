# -*- coding: utf-8 -*-
import difflib
from pprint import pprint

sentence1 = "Sở_hữu vòng 1 " + "khủng" + " , Phi_Thanh_Vân thường_xuyên diện những bộ_cánh hở hang khoe triệt_để"
sentence2 = "Sở_hữu vòng 1 " + "khủng" + " , Phi Thanh_Vân thường_xuyên diện những bộ_cánh hở_hang khoe triệt_để"
words1 = [word for word in sentence1.split(' ')]
words2 = [word for word in sentence2.split(' ')]
diff = difflib.ndiff(words2, words1)
delta = ' '.join(x[2:] for x in diff if x.startswith('- '))

print delta
print 0
