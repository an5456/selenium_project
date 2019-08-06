import requests

import random


class Test01:
    def test_2(self, test_1):
        print(test_1)
        assert random.randrange(1, 4) == test_1

    def test_3(self, test_1):
        print(test_1)
        assert random.randrange(1, 4) == test_1

# test_1class Test02:
#     def test_2(self,test_1):
#         print(test_1)
#         assert random.randrange(1,4) == test_1
