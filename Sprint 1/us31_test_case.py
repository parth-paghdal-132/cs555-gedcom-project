import unittest
import project_4_sprint_1


class TestLivingSingle(unittest.TestCase):

    # This test case will check the length of the expected and actual output
    # This test case will pass since assertEqual is used and both arrays have the same length
    def test_us_31_same_length(self):
        us31Data = [
            "Error: Individual US31 Individual id I1, name Emily /Chapman/ is living and single.",
            "Error: Individual US31 Individual id I2, name Rachel /Chapman/ is living and single.",
            "Error: Individual US31 Individual id I3, name Karen /Chapman/ is living and single."
        ]
        self.assertEqual(len(project_4_sprint_1.us31_list_living_single()), len(us31Data),
                         "This test case will pass since assertEqual method is used and both arrays have the same length")

    # This test case will check the content of the expected and actual output by order
    # This test case will pass since assertEqual is used to check content of both arrays and that content is the same
    def test_us_31_same_content(self):
        us31Data = [
            "Error: Individual US31 Individual id I1, name Emily /Chapman/ is living and single.",
            "Error: Individual US31 Individual id I2, name Rachel /Chapman/ is living and single.",
            "Error: Individual US31 Individual id I3, name Karen /Chapman/ is living and single."
        ]
        data = project_4_sprint_1.us31_list_living_single()
        for index, value in enumerate(data):
            self.assertEqual(value, us31Data[index],
                             "This test case will pass since assertEqual is used to check content of both arrays and that content is the same")

    # This test case will check the length of the expected and actual output
    # This test case will pass since assertNotEqual is used and both arrays have different length
    def test_us_31_different_length(self):
        us31Data = [
            "Error: Individual US31 Individual id I1, name Emily /Chapman/ is living and single.",
            "Error: Individual US31 Individual id I2, name Rachel /Chapman/ is living and single."
        ]
        self.assertNotEqual(len(project_4_sprint_1.us31_list_living_single()), len(us31Data),
                            "This test case will pass since assertNotEqual is used and both arrays have different length")

    # This test case will check the content of the expected and actual output by order
    # This test case will pass since assertNotEqual is used to check content of both arrays and that content is different
    def test_us_31_different_content(self):
        us31Data = [
            "Error: Individual US31 Individual id I4, name John /Doe/ is living and single.",
            "Error: Individual US31 Individual id I5, name Jane /Doe/ is living and single.",
            "Error: Individual US31 Individual id I6, name Alex /Doe/ is living and single."
        ]
        data = project_4_sprint_1.us31_list_living_single()
        for index, value in enumerate(data):
            self.assertNotEqual(value, us31Data[index],
                                "This test case will pass since assertNotEqual is used to check content of both arrays and that content is different")


if __name__ == '__main__':
    unittest.main()
