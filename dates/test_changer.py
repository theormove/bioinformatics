import unittest
from time_changer import change_time

class TestChangeTime(unittest.TestCase):
	def test_list(self):
		data = [20,10,10]
		result = change_time(data)
		self.assertEqual(result,'Decimal time: 8:40:39')
	def test_list1(self):
		data = [1,1,1]
		result = change_time(data)
		self.assertEqual(result,'Decimal time: 0:42:37')	
	def test_dummy(self):
		data = 'wdaddd'
		result = change_time(data)
		self.assertEqual(result,'Only numbers allowed')
	def test_list2(self):
		data = [20,100,10]
		result = change_time(data)
		self.assertEqual(result,'Time input is incorrect, values are too big')
	def test_list3(self):
		data = [200,10,10]
		result = change_time(data)
		self.assertEqual(result,'Time input is incorrect, values are too big')
	def test_list4(self):
		data = [20,10,100]
		result = change_time(data)
		self.assertEqual(result,'Time input is incorrect, values are too big')			



if __name__=="__main__":
	unittest.main()		
