import unittest
from app.common.cube import get_volume_cube

class CubeTest(unittest.TestCase):
    ''' Cube Test '''
    def test_smoke(self):
        ''' Smoke test make sure function exist '''
        self.assertIsNotNone(get_volume_cube)

    def test_should_return_volume_when_passing_side(self):
        ''' Should return volume when passing side '''
        self.assertEqual(get_volume_cube(10), 1000)
        self.assertEqual(get_volume_cube(15), 3375)