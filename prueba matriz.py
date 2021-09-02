import matriz as lc
import unittest
class TestCplxoperations(unittest.TestCase):

    def test(self):
        suma = lc.suvectores([(2, 8), (8, 9), (6, 7)],[(7, 0), (9, 10), (2, 3)])
        self.assertAlmostEqual(suma[0],(9,8))
        self.assertAlmostEqual(suma[1],(17,19))
        self.assertAlmostEqual(suma[2], (8, 10))



if __name__ == '__main__':
    unittest.main()
import unittest
class TestCplxoperations(unittest.TestCase):

    def test(self):
        suma = lc.invma([(2, 8), (8, 9), (6, 7)])
        self.assertAlmostEqual(suma[0],(-2,-8))
        self.assertAlmostEqual(suma[1],(-8,-9))
        self.assertAlmostEqual(suma[2], (-6,-7))



if __name__ == '__main__':
    unittest.main()
import unittest
class TestCplxoperations(unittest.TestCase):

    def test(self):
        suma = lc.multesc((1,0),[(2, 8), (8, 9), (6, 7)])
        self.assertAlmostEqual(suma[0],(2,8))
        self.assertAlmostEqual(suma[1],(8,9))
        self.assertAlmostEqual(suma[2], (6, 7))



if __name__ == '__main__':
    unittest.main()
import unittest
class TestCplxoperations(unittest.TestCase):

    def test(self):
        suma = lc.summa([[(2, 3), (3, 4), (3, 2)], [(1, 1), (1, 1), (1, 1)], [(2, 2), (3, 3), (4, 4)]],[[(4, 4), (3, 6), (3, 7)], [(1, 2), (1, 2), (1, 2)], [(1, 1), (2, 2), (3, 3)]])
        self.assertAlmostEqual(suma[0],[(6, 7), (6, 10), (6, 9)])
        self.assertAlmostEqual(suma[1],[(2, 3), (2, 3), (2, 3)])
        self.assertAlmostEqual(suma[2],[(3, 3), (5, 5), (7, 7)])
if __name__ == '__main__':
    unittest.main()
import unittest


class TestCplxoperations(unittest.TestCase):

    def test(self):
        suma = lc.trama([[(2, 3), (3, 4), (3, 2)],
                         [(1, 1), (1, 1), (1, 1)],
                         [(2, 2), (3, 3), (4, 4)]])
        self.assertAlmostEqual(suma[0],[(2, 3), (1, 1), (2, 2)])
        self.assertAlmostEqual(suma[1],[(3, 4), (1, 1), (3, 3)])
        self.assertAlmostEqual(suma[2], [(3, 2), (1, 1), (4, 4)])



if __name__ == '__main__':
    unittest.main()
class TestCplxoperations(unittest.TestCase):

    def test(self):
        suma = lc.invma([[(2, 3), (3, 4), (3, 2)],
                         [(1, 1), (1, 1), (1, 1)],
                         [(2, 2), (3, 3), (4, 4)]])
        self.assertAlmostEqual(suma[0],[(-2, -3), (-3, -4), (-3, -2)])
        self.assertAlmostEqual(suma[1],[(-1, -1), (-1, -1), (-1, -1)])
        self.assertAlmostEqual(suma[2],[(-2, -2), (-3, -3), (-4, -4)])



if __name__ == '__main__':
    unittest.main()
class TestCplxoperations(unittest.TestCase):

    def test(self):
        suma = lc.mulma([[(2, 3), (3, 4), (3, 2)],
                         [(1, 1), (1, 1), (1, 1)],
                         [(2, 2), (3, 3), (4, 4)]])
        self.assertAlmostEqual(suma[0],[(2, 3), (3, 4), (3, 2)])
        self.assertAlmostEqual(suma[1],[(1, 1), (1, 1), (1, 1)])
        self.assertAlmostEqual(suma[2],[(2, 2), (3, 3), (4, 4)])



if __name__ == '__main__':
    unittest.main()