# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(6,1,9),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(9,8,7),'Right','5,3,4 is a Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(5,5,5),'Equilateral','1,1,1 should be equilateral')

    def test_triangle(self):
        self.assertEqual(classify_triangle(3, 3, 4), "Isosceles")
        self.assertEqual(classify_triangle(8, 14, 17), "Scalene")
        self.assertEqual(classify_triangle(30, 30, 30), "Equilateral")


if __name__ == "__main__":
    classify_triangle(2,5,9)
    classify_triangle(3,3,3)
    unittest.main()

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

