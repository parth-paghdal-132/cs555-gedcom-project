import unittest
import project_4_sprint_1

class GedComProjectTestCases(unittest.TestCase):

    # Test case for US03 - Birth before death
    # Test cases written by Parth Paghdal (pp)
    # There is total 4 test cases for this user story where two test cases will pass and two will fail

    # This test case will check length of expected and actual output
    # This test case will pass since assertEqual method is used and both array has same length
    def test_us_03_same_length(self):
        usO3Data = [
            "Error: INDIVIDUAL US03 I7: named: John /Chapmen/ Died: 1929-03-19 before born at 1930-03-16",
            "Error: INDIVIDUAL US03 I8: named: Adrian /Chapmen/ Died: 1925-05-19 before born at 1930-03-16"
        ]
        self.assertEqual(len(project_4_sprint_1.us03_birth_before_death()), len(usO3Data), "This test case will pass since assertEqual method is used and both array has same length")

    # This test case will check content of expected and actual output by in order
    # This test case will pass since assertEqual is used to check content of both array and that content is same
    def test_us_03_same_content(self):
        usO3Data = [
            "Error: INDIVIDUAL US03 I7: named: John /Chapmen/ Died: 1929-03-19 before born at 1930-03-16",
            "Error: INDIVIDUAL US03 I8: named: Adrian /Chapmen/ Died: 1925-05-19 before born at 1930-03-16"
        ]
        data = project_4_sprint_1.us03_birth_before_death()
        for index, value in enumerate(data):
            self.assertEqual(value, usO3Data[index], "This test case will pass since assertEqual is used to check content of both array and that content is same")
    
    # This test case will check length of expected and actual output
    # This test case will pass since assertNotEqual is used and both array has different length
    def test_us_03_different_length(self):
        usO3Data = [
            "Error: INDIVIDUAL US03 I7: named: John /Chapmen/ Died: 1929-03-19 before born at 1930-03-16",
            "Error: INDIVIDUAL US03 I8: named: Adrian /Chapmen/ Died: 1925-05-19 before born at 1930-03-16",
            "Error: INDIVIDUAL US03 I8: named: Nicola /Chapmen/ Died: 1925-05-19 before born at 1930-03-16"
        ]
        self.assertNotEqual(len(project_4_sprint_1.us03_birth_before_death()), len(usO3Data), "This test case will pass since assertNotEqual is used and both array has different length")
    
    # This test case will check content of expected and actual output by in order
    # This test case will pass since assertNotEqual is used to check content both array and that content is different
    def test_us_03_different_content(self):
        usO3Data = [
            "Error: INDIVIDUAL US03 I8: named: Adrian /Chapmen/ Died: 1925-05-19 before born at 1930-03-16",
            "Error: INDIVIDUAL US03 I7: named: John /Chapmen/ Died: 1929-03-19 before born at 1930-03-16"
        ]
        data = project_4_sprint_1.us03_birth_before_death()
        for index, value in enumerate(data):
            self.assertNotEqual(value, usO3Data[index], "This test case will pass since assertNotEqual is used to check content both array and that content is different")
  
    # Test case for US30 - List living married
    # Test cases written by Parth Paghdal (pp)
    # There is total 4 test cases for this user story where two test cases will pass and two will fail
    
    # This test case will check length of expected and actual output
    # This test case will pass since assertEqual method is used and both array has same length
    def test_us_30_same_length(self):
        us30Data = [
            "Error: Family US30 Family id F3 husband name: Joanne /Chapmen/ and wife name: Sebastian /Chapmen/ both are still living married couple.",
            "Error: Family US30 Family id F8 husband name: Neil /Chapmen/ and wife name: Victoria /Chapmen/ both are still living married couple.",
            "Error: Family US30 Family id F10 husband name: Sam /Chapmen/ and wife name: Felicity /Chapmen/ both are still living married couple.",
            "Error: Family US30 Family id F11 husband name: Benjamin /Chapmen/ and wife name: Nicola /Chapmen/ both are still living married couple.",
            "Error: Family US30 Family id F12 husband name: Boris /Chapmen/ and wife name: Penelope /Chapmen/ both are still living married couple.",
            "Error: Family US30 Family id F14 husband name: Andrew /Chapmen/ and wife name: Kimberely /Chapmen/ both are still living married couple."
        ]
        self.assertEqual(len(project_4_sprint_1.us30_list_living_married()), len(us30Data), "This test case will pass since assertEqual method is used and both array has same length")

    # This test case will check content of expected and actual output by in order
    # This test case will pass since assertEqual is used to check content of both array and that content is same
    def test_us_30_same_content(self):
        us30Data = [
            "Error: Family US30 Family id F3 husband name: Joanne /Chapmen/ and wife name: Sebastian /Chapmen/ both are still living married couple.",
            "Error: Family US30 Family id F8 husband name: Neil /Chapmen/ and wife name: Victoria /Chapmen/ both are still living married couple.",
            "Error: Family US30 Family id F10 husband name: Sam /Chapmen/ and wife name: Felicity /Chapmen/ both are still living married couple.",
            "Error: Family US30 Family id F11 husband name: Benjamin /Chapmen/ and wife name: Nicola /Chapmen/ both are still living married couple.",
            "Error: Family US30 Family id F12 husband name: Boris /Chapmen/ and wife name: Penelope /Chapmen/ both are still living married couple.",
            "Error: Family US30 Family id F14 husband name: Andrew /Chapmen/ and wife name: Kimberely /Chapmen/ both are still living married couple."
        ]
        data = project_4_sprint_1.us30_list_living_married()
        for index, value in enumerate(data):
            self.assertEqual(value, us30Data[index], "This test case will pass since assertEqual is used to check content of both array and that content is same")

    # This test case will check length of expected and actual output
    # This test case will pass since assertNotEqual is used and both array has different length
    def test_us_30_different_length(self):
        us30Data = [
            "Error: Family US30 Family id F3 husband name: Joanne /Chapmen/ and wife name: Sebastian /Chapmen/ both are still living married couple.",
            "Error: Family US30 Family id F8 husband name: Neil /Chapmen/ and wife name: Victoria /Chapmen/ both are still living married couple."
        ]
        self.assertNotEqual(len(project_4_sprint_1.us30_list_living_married()), len(us30Data), "This test case will pass since assertNotEqual is used and both array has different length")
    
    # This test case will check content of expected and actual output by in order
    # This test case will pass since assertNotEqual is used to check content both array and that content is different
    def test_us_30_different_content(self):
        us30Data = [
            "Error: Family US30 Family id F11 husband name: Benjamin /Chapmen/ and wife name: Nicola /Chapmen/ both are still living married couple.",
            "Error: Family US30 Family id F12 husband name: Boris /Chapmen/ and wife name: Penelope /Chapmen/ both are still living married couple.",
            "Error: Family US30 Family id F14 husband name: Andrew /Chapmen/ and wife name: Kimberely /Chapmen/ both are still living married couple.",
            "Error: Family US30 Family id F3 husband name: Joanne /Chapmen/ and wife name: Sebastian /Chapmen/ both are still living married couple.",
            "Error: Family US30 Family id F8 husband name: Neil /Chapmen/ and wife name: Victoria /Chapmen/ both are still living married couple.",
            "Error: Family US30 Family id F10 husband name: Sam /Chapmen/ and wife name: Felicity /Chapmen/ both are still living married couple."
        ]
        data = project_4_sprint_1.us30_list_living_married()
        for index, value in enumerate(data):
            self.assertNotEqual(value, us30Data[index], "This test case will pass since assertNotEqual is used to check content both array and that content is different")

if __name__ == '__main__':
    unittest.main()