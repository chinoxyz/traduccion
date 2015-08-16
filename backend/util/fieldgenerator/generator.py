

from datetime import datetime
import random
import string

from faker import Faker

class generator:
    def integer(self,min_value = 0,max_value=1<<32):
        if min_value > max_value: return None
        return random.randint(min_value, max_value)
    
    def float(self,min_value = 0,max_value=1<<32):
        if min_value > max_value: return None
        return random.uniform(min_value, max_value)
    
    def string(self, min_length=0, max_length=20,posiblechars = string.printable):
        min_length = max(0,min_length)
        if min_length > max_length or len(posiblechars) <= 0: return None
        length = self.integer(min_length, max_length)
        result = ""
        for i in xrange(length):
            pos = self.integer(0, len(posiblechars)-1)
            result += posiblechars[pos]
        return result
    
    def slug(self, min_length=0,max_length=20):
        return self.string(min_length=min_length, max_length=max_length, posiblechars=string.ascii_letters)
    
    def password(self):
        return self.slug(8,8)
    
    def email(self):
        return (self.slug(6,10)+'@'+self.slug(6, 10)+".com").lower()
    
    def corporative_email(self, domain):
        return (self.slug(6,20)+'@'+domain).lower()
    
    def url(self):
        return "http://cocoonapp.com/"+self.slug(5,10)
    
    def datetime(self):
        year = random.choice(range(2000, 2015))
        month = random.choice(range(1, 13))
        day = random.choice(range(1, 29))
        birthDate = datetime(year, month, day)
        return birthDate
    
    def none(self, value, p=0.1):
        if self.float(0,1) < p:
            return None
        else:
            return value
    
    def date(self):
        return self.datetime().date()
    
    def boolean(self):
        return True if self.integer(0,1) == 0 else False
    
    def choices(self, list):
        return list[self.integer(0,len(list)-1)]
    
    
    def address(self):
        fake = Faker()
        return fake.address()
    def text(self):
        fake = Faker()
        return fake.text()
    
    def name(self):
        fake = Faker();
        return fake.name()