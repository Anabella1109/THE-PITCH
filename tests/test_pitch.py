from app.models import Pitch,User
from app import db
import unittest


class PitchModelTest(unittest.TestCase):
   def setUp(self):
        self.user_James = User(username = 'James',password = 'potato', email = 'james@ms.com')
        self.new_pitch = Pitch(id=12345,content='Pitch for movies',category="hhh",upvotes=12,downvotes=34,user = self.user_James )


   def test_check_instance_variables(self):
        self.assertEquals(self.new_pitch.id,12345)
        self.assertEquals(self.new_pitch.content,'Pitch for movies')
        self.assertEquals(self.new_pitch.category,"hhh")
        self.assertEquals(self.new_pitch.upvotes,12)
        self.assertEquals(self.new_pitch.downvotes,34)
        self.assertEquals(self.new_pitch.user,self.user_James)

   def test_save_pitch(self):
        self.new_pitch.save_pitch()
        self.assertTrue(len(Pitch.query.all())>0)  

   def test_get_pitch_by_id(self):

        self.new_pitch.save_pitch()
        got_pitchs = Pitch.get_pitch(12345)
        self.assertTrue(len(got_pitchs) == 1)      