from django.test.testcases import TestCase

from backend.core.user.forms import RegisterForm
from backend.util.fieldgenerator.generator import generator


################ OBJ CREATION #############
def userRandDict():
    gen = generator()
    return {
        "email":gen.email(),
        "password":gen.slug(6,20),
        "first_name":gen.slug(5,10),
        "last_name":gen.slug(5,10),
        }

def userRandObj(data={}):
    dic = userRandDict()
    dic.update(data)
    form = RegisterForm(dic)
    assert(form.is_valid())
    return form.save()
    

################ TESTS OBJ CREATION #############

class AppUserSave(TestCase):
    def test_save(self):
        obj = userRandObj()
        obj.delete()
    

################ TESTS Views ####################

