
#CLASSES 00P PT - 2

from collections import OrderedDict

favorite_laguagens = OrderedDict()

favorite_laguagens['jen'] = 'python'
favorite_laguagens['sarah'] = 'c'
favorite_laguagens['sarah'] = 'ruby'
favorite_laguagens['eadwar'] = 'ruby'
favorite_laguagens['phil'] = 'python'

for name, languages in favorite_laguagens.items():
    print("{}'s favorita linguagem {}".format(name.title(), languages.title()))