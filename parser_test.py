import unittest
from parser import parse

class ScannerTest(unittest.TestCase):
  
    # Returns True or False. 
    def test_1(self):        
        self.assertEqual(parse("num"),"Accept")

    def test_2(self):
        self.assertEqual(parse("(+ num num)"),"Accept")

    def test_3(self):
        self.assertEqual(parse("(- num num)"),"Accept")

    def test_4(self):
        self.assertEqual(parse("(* num num)"),"Accept")

    def test_5(self):
        self.assertEqual(parse("(/ num num)"),"Accept")

    def test_6(self):
        self.assertEqual(parse("()"),"Reject")

    def test_7(self):
        self.assertEqual(parse("(+)"),"Reject")

    def test_8(self):
        self.assertEqual(parse(""),"Reject")

    def test_9(self):
        self.assertEqual(parse("(+ num)"),"Reject")

    def test_10(self):
        self.assertEqual(parse("(+ num num"),"Reject")

    def test_11(self):        
        self.assertEqual(parse("(+ (- num num) num)"),"Accept")

    def test_12(self):
        self.assertEqual(parse("(+ num (- num num))"),"Accept")

    def test_13(self):
        self.assertEqual(parse("(+ (- num num) (* num num))"),"Accept")

    def test_14(self):
        self.assertEqual(parse("(+ (- (/ num num) num) (* num num))"),"Accept")

    def test_15(self):
        self.assertEqual(parse("(+ (- (/ num num) num) (* num (+ num num)))"),"Accept")

    def test_16(self):
        self.assertEqual(parse("(+ (- num) num)"),"Reject")

    def test_17(self):
        self.assertEqual(parse("(+ (- num num))"),"Reject")

    def test_18(self):
        self.assertEqual(parse("(+ (- num num"),"Reject")

    def test_19(self):
        self.assertEqual(parse("(+ (- num num) + num num))"),"Reject")

    def test_20(self):
        self.assertEqual(parse("(+ (- num num) (+ num *))"),"Reject")

if __name__ == '__main__':
    unittest.main()