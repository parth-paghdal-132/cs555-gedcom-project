import unittest
import project_4_sprint_1

class functionTest(unittest.TestCase):

    # Test case for US03 - Birth before death
    # Test cases written by Parth Paghdal (pp)
    # There is total 4 test cases for this user story where two test cases will pass and two will fail

    # This test case will check length of expected and actual output
    # This test case will pass because expected and actual output has same length
    def test_us_03_same_length_should_pass(self):
        usO3Data = [
            "Error: INDIVIDUAL US03 I7: named: John /Chapmen/ Died: 1929-03-19 before born at 1930-03-16",
            "Error: INDIVIDUAL US03 I8: named: Adrian /Chapmen/ Died: 1925-05-19 before born at 1930-03-16"
        ]
        self.assertEqual(len(project_4_sprint_1.us03_birth_before_death()), len(usO3Data), "This test case will pass because length of both arrays are same.")

    # This test case will check content of expected and actual output by in order
    # This test case will pass because expected and actual output has same content in order.
    def test_us_03_same_content_should_pass(self):
        usO3Data = [
            "Error: INDIVIDUAL US03 I7: named: John /Chapmen/ Died: 1929-03-19 before born at 1930-03-16",
            "Error: INDIVIDUAL US03 I8: named: Adrian /Chapmen/ Died: 1925-05-19 before born at 1930-03-16"
        ]
        data = project_4_sprint_1.us03_birth_before_death()
        for index, value in enumerate(data):
            self.assertEqual(value, usO3Data[index], "This test case will pass because content of both arrays are in same order.")
    
    # This test case will check length of expected and actual output
    # This test case will fail because expected and actual output has different length
    def test_us_03_same_length_should_fail(self):
        usO3Data = [
            "Error: INDIVIDUAL US03 I7: named: John /Chapmen/ Died: 1929-03-19 before born at 1930-03-16",
            "Error: INDIVIDUAL US03 I8: named: Adrian /Chapmen/ Died: 1925-05-19 before born at 1930-03-16",
            "Error: INDIVIDUAL US03 I8: named: Nicola /Chapmen/ Died: 1925-05-19 before born at 1930-03-16"
        ]
        self.assertEqual(len(project_4_sprint_1.us03_birth_before_death()), len(usO3Data), "This test case will fail because length of both arrays are not same.")
    
    # This test case will check content of expected and actual output by in order
    # This test case will fail because expected and actual output has different content in order.
    def test_us_03_same_content_should_fail(self):
        usO3Data = [
            "Error: INDIVIDUAL US03 I8: named: Adrian /Chapmen/ Died: 1925-05-19 before born at 1930-03-16",
            "Error: INDIVIDUAL US03 I7: named: John /Chapmen/ Died: 1929-03-19 before born at 1930-03-16"
        ]
        data = project_4_sprint_1.us03_birth_before_death()
        for index, value in enumerate(data):
            self.assertEqual(value, usO3Data[index], "This test case will fail because content of both arrays are not in same order.")
  
    # Test case for US30 - List living married
    # Test cases written by Parth Paghdal (pp)
    # There is total 4 test cases for this user story where two test cases will pass and two will fail
    
    # This test case will check length of expected and actual output
    # This test case will pass because expected and actual output has same length
    def test_us_30_same_length_should_pass(self):
        us30Data = [
            "Error: Family US30 Family id F3 husband name: Joanne /Chapmen/ and wife name: Sebastian /Chapmen/ both are still living married couple.",
            "Error: Family US30 Family id F8 husband name: Neil /Chapmen/ and wife name: Victoria /Chapmen/ both are still living married couple.",
            "Error: Family US30 Family id F10 husband name: Sam /Chapmen/ and wife name: Felicity /Chapmen/ both are still living married couple.",
            "Error: Family US30 Family id F11 husband name: Benjamin /Chapmen/ and wife name: Nicola /Chapmen/ both are still living married couple.",
            "Error: Family US30 Family id F12 husband name: Boris /Chapmen/ and wife name: Penelope /Chapmen/ both are still living married couple.",
            "Error: Family US30 Family id F14 husband name: Andrew /Chapmen/ and wife name: Kimberely /Chapmen/ both are still living married couple."
        ]
        self.assertEqual(len(project_4_sprint_1.us30_list_living_married()), len(us30Data), "This test case will pass because length of both arrays are same.")

    # This test case will check content of expected and actual output by in order
    # This test case will fail because expected and actual output has different content in order.
    def test_us_30_same_content_should_pass(self):
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
            self.assertEqual(value, us30Data[index], "This test case will fail because content of both arrays are in same order.")

    # This test case will check length of expected and actual output
    # This test case will fail because expected and actual output has different length
    def test_us_30_same_length_should_fail(self):
        us30Data = [
            "Error: Family US30 Family id F3 husband name: Joanne /Chapmen/ and wife name: Sebastian /Chapmen/ both are still living married couple.",
            "Error: Family US30 Family id F8 husband name: Neil /Chapmen/ and wife name: Victoria /Chapmen/ both are still living married couple."
        ]
        self.assertEqual(len(project_4_sprint_1.us30_list_living_married()), len(us30Data), "This test case will fail because length of both arrays are not same.")
    
    # This test case will check content of expected and actual output by in order
    # This test case will fail because expected and actual output has different content in order.
    def test_us_30_same_content_should_fail(self):
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
            self.assertEqual(value, us30Data[index], "This test case will fail because content of both arrays are not in same order.")

if __name__ == '__main__':
    unittest.main()