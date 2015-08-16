import random

from django.test import SimpleTestCase

from backend.util.fieldgenerator.generator import generator


class TestGenerator(SimpleTestCase):
    
    def test_integer(self):
        """
        Tests for generator.integer
        """
        for i in xrange(1000):
            ma = random.randint(0, 1000)
            mi = random.randint(0, 1000)
            if(ma < mi):
                mi,ma = ma,mi
            val = generator().integer(max_value= ma, min_value = mi)
            self.assertEqual(True, mi <= val and val <= ma)
        self.assertEqual(None,generator().integer(max_value= 0, min_value = 1))
    def test_float(self):
        """
        Tests for generator.float
        """
        for i in xrange(1000):
            ma = random.uniform(0, 1000)
            mi = random.uniform(0, 1000)
            if(ma < mi):
                mi,ma = ma,mi
            val = generator().float(max_value= ma, min_value = mi)
            self.assertEqual(True, mi <= val and val <= ma)
        self.assertEqual(None,generator().float(max_value= 0, min_value = 1))
        
    def test_string(self):
        """
        Tests for generator.string
        """
        for i in xrange(1000):
            ma = random.randint(10, 20)
            mi = random.randint(0, 10)
            if(ma < mi):
                mi,ma = ma,mi
            str = generator().string(max_length= ma, min_length = mi)
            self.assertEqual(True, str != None)
            self.assertEqual(True, mi <= len(str) and len(str) <= ma)
        self.assertEqual(None,generator().string(max_length= 0, min_length = 1))
        self.assertEqual(None,generator().string(max_length= -1, min_length = -1))
        self.assertEqual("",generator().string(max_length= 0, min_length = -1))
        self.assertEqual(None,generator().string(max_length= 0, min_length = -1,posiblechars=""))
    
    def test_date(self):
        """
        tests for  generator.date
        """
        for _ in xrange(100):
            self.assertEqual(True, generator().date() != None)
    
    def test_none(self):
        """
        tests for generator.none
        """
        for _ in xrange(100):
            opt = generator().none(2)
            self.assertEqual(True, opt == None or opt == 2)
    
    def test_boolean(self):
        """
        tests for generator.boolean
        """
        for _ in xrange(100):
            val = generator().boolean()
            self.assertEqual(True, val == True or val == False)
    
    def test_choices(self):
        """
        tests for generator.boolean
        """
        for _ in xrange(100):
            list = range(100)
            val = generator().choices(list)
            self.assertEqual(True, val in list)
        