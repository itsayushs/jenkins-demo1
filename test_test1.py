import unittest
# import simple_api
from simple_api import getData
  
class SimpleTest(unittest.TestCase): 
    
    def test_testcase1(self):         
        self.assertTrue(False) 
   
    def test_testcase2(self):
        response_from_api = getData()
        if "data" in response_from_api:
            test_passed = True
        else:
            test_passed = False
        self.assertTrue(test_passed)

if __name__ == '__main__': 
    unittest.main() 