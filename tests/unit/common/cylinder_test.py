import unittest
from app.common.cylinder import get_volume_cylinder

class CylinderTest(unittest.TestCase):
    '''  Cylinder Test '''
    def test_smoke(self):
        ''' Smoke test make sure function exist '''
        self.assertIsNotNone(get_volume_cylinder)

    def test_should_return_volume_when_passing_radius(self):
        ''' Should return volume when passing side '''
        self.assertEqual(get_volume_cylinder(5), 78.5398)
        self.assertEqual(get_volume_cylinder(25), 1963.4950000000001)