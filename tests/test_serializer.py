from unittest import TestCase
from aosoiy.serializers import *

class TestSuvSerializer(TestCase):
    def test_suv(self):
        data = {
            "id": 1,
            "brend": "Pepsi",
            "narx": 6000.0,
            "litr": 0.5,
            "batafsil": "Pepsi!"
        }
        serializer = SuvSerializer(data=data)
        assert serializer.is_valid() == True

class TestMijozSerializer(TestCase):
    def test_mijoz(self):
        data = {
            "id": 1,
            "ism": "Mendirman o'sha",
            "tel": 902324323,
            "manzil": "Farg'ona",
            "qarz": 0,
            "user": 1
        }
        serializer = MijozSerializer(data=data)
        assert serializer.is_valid() == True