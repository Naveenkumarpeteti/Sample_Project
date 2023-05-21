import unittest
import calc 
################################################
class TestCalc(unittest.TestCase):
	
	def test_add(self):
		self.assertEqual(calc.add(3,5),8)
		self.assertEqual(calc.add(-1,1),0)
		self.assertEqual(calc.add(-1,-1),-2)

	def test_substract(self):
		self.assertEqual(calc.substract(10,5),5) haii
		self.assertEqual(calc.substract(-1,-1),0)	

	def test_multiply(self):
		self.assertEqual(calc.multiply(5,6),30) #######
		self.assertEqual(calc.multiply(10,5),50)

	def test_divide(self):
		self.assertEqual(calc.divide(10,5),2) ##
		self.assertEqual(calc.divide(6,3),2)

if __name__ == '__main__':
	unittest.main()


commit1


commit2


commit2

commit3


commit3

commit4


commit4

commit 5


commit 5

commit 6

commit 7


cimmit 8

commit 9

commit 10

