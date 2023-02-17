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
            self.assertNotEqual(value, us30Data[index], "This test case will pass since assertNotEqual is used to check content both array and that contentis different")
# Name:- SAI KRISHNA MIRIYALA
#CWID:- 20010913
#User Story-29
import unittest2
import project_4_sprint_1


class TestListdeceased(unittest2.TestCase):

    # This test case will check the length of the expected and actual output
    # This test case will pass since assertEqual is used and both arrays have the same length
    def test_us_29_same_length(self):
        us29Data = [
           "Error: Individual US29 I1 : named: Edward /Chapmen/ died on: 2010-03-15"
            "Error: Individual US29 I2 : named: Wanda /Chapmen/ died on: 2005-06-19"
            "Error: Individual US29 I3 : named: Sam /Chapmen/ died on: 2015-04-16"
            "Error: Individual US29 I6 : named: John /Chapmen/ died on: 2012-02-18"
            "Error: Individual US29 I7 : named: John /Chapmen/ died on: 1929-03-19"
            "Error: Individual US29 I8 : named: Adrian /Chapmen/ died on: 1925-05-19"
            "Error: Individual US29 I9 : named: Karen /Chapmen/ died on: 1990-05-18"
            "Error: Individual US29 I11 : named: Carol /Chapmen/ died on: 2015-10-30"
            "Error: Individual US29 I13 : named: Maria /Chapmen/ died on: 1999-05-16"
        ]
        self.assertEqual(len(project_4_sprint_1.us_29_List_deceased()), len(us29Data),
                         "This test case will pass since assertEqual method is used and both arrays have the same length")

    # This test case will check the content of the expected and actual output by order
    # This test case will pass since assertEqual is used to check content of both arrays and that content is the same
    def test_us_29_same_content(self):
        us29Data = [
          "Error: Individual US29 I1 : named: Edward /Chapmen/ died on: 2010-03-15"
            "Error: Individual US29 I2 : named: Wanda /Chapmen/ died on: 2005-06-19"
            "Error: Individual US29 I3 : named: Sam /Chapmen/ died on: 2015-04-16"
            "Error: Individual US29 I6 : named: John /Chapmen/ died on: 2012-02-18"
            "Error: Individual US29 I7 : named: John /Chapmen/ died on: 1929-03-19"
            "Error: Individual US29 I8 : named: Adrian /Chapmen/ died on: 1925-05-19"
            "Error: Individual US29 I9 : named: Karen /Chapmen/ died on: 1990-05-18"
            "Error: Individual US29 I11 : named: Carol /Chapmen/ died on: 2015-10-30"
            "Error: Individual US29 I13 : named: Maria /Chapmen/ died on: 1999-05-16"
        ]
        data = project_4_sprint_1.us_29_List_deceased()
        for index, value in enumerate(data):
            self.assertEqual(value, us29Data[index],
                             "This test case will pass since assertEqual is used to check content of both arrays and that content is the same")

    # This test case will check the length of the expected and actual output
    # This test case will pass since assertNotEqual is used and both arrays have different length
    def test_us_29_different_length(self):
        us29Data = [
           "Error: Individual US29 I1 : named: Edward /Chapmen/ died on: 2010-03-15"
            "Error: Individual US29 I2 : named: Wanda /Chapmen/ died on: 2005-06-19"
            "Error: Individual US29 I3 : named: Sam /Chapmen/ died on: 2015-04-16"
            "Error: Individual US29 I6 : named: John /Chapmen/ died on: 2012-02-18"
            "Error: Individual US29 I7 : named: John /Chapmen/ died on: 1929-03-19"
            "Error: Individual US29 I8 : named: Adrian /Chapmen/ died on: 1925-05-19"
            "Error: Individual US29 I9 : named: Karen /Chapmen/ died on: 1990-05-18"
            "Error: Individual US29 I11 : named: Carol /Chapmen/ died on: 2015-10-30"
            "Error: Individual US29 I13 : named: Maria /Chapmen/ died on: 1999-05-16"
        ]
        self.assertNotEqual(len(project_4_sprint_1.us_29_List_deceased()),len(us29Data),"This test case will pass since assertNotEqual is used and both arrays have different length")

    # This test case will check the content of the expected and actual output by order
    # This test case will pass since assertNotEqual is used to check content of both arrays and that content is different
    def test_us_29_different_content(self):
        us29Data = [
            "Error: Individual US29 I1 : named: Edward /Chapmen/ died on: 2010-03-15"
            "Error: Individual US29 I2 : named: Wanda /Chapmen/ died on: 2005-06-19"
            "Error: Individual US29 I3 : named: Sam /Chapmen/ died on: 2015-04-16"
            "Error: Individual US29 I6 : named: John /Chapmen/ died on: 2012-02-18"
            "Error: Individual US29 I7 : named: John /Chapmen/ died on: 1929-03-19"
            "Error: Individual US29 I8 : named: Adrian /Chapmen/ died on: 1925-05-19"
            "Error: Individual US29 I9 : named: Karen /Chapmen/ died on: 1990-05-18"
            "Error: Individual US29 I11 : named: Carol /Chapmen/ died on: 2015-10-30"
            "Error: Individual US29 I13 : named: Maria /Chapmen/ died on: 1999-05-16"
        ]
        data = project_4_sprint_1.us_29_List_deceased()
        for index, value in enumerate(data):
            self.assertNotEqual(value, us29Data[index],
                                "This test case will pass since assertNotEqual is used to check content of both arrays and that content is different")


if __name__ == '_main_':
    unittest2.main()
# Name:- MANOJ PATEL D
#CWID:- 20012221
import unittest
import project_4_sprint_1

class Test11(unittest.TestCase):

    def test_us_05_same_length(self):
        usO5Data = [
            "Error: INDIVIDUAL US05 I7: named: John /Chapmen/ Died: 1929-03-19 before married at 1959-05-10 to Maria /Chapmen/",
            "Error: INDIVIDUAL US05 I8: named: Adrian /Chapmen/ Died: 1925-05-19 before married at 1954-06-15 to Jennifer /Chapmen/"
        ]
        self.assertEqual(len(us05_marriage_before_death()), len(usO5Data), "This test case will pass since assertEqual method is used and both arrays have the same length")

    def test_us_05_same_content(self):
        usO5Data = [
            "Error: INDIVIDUAL US05 I7: named: John /Chapmen/ Died: 1929-03-19 before married at 1959-05-10 to Maria /Chapmen/",
            "Error: INDIVIDUAL US05 I8: named: Adrian /Chapmen/ Died: 1925-05-19 before married at 1954-06-15 to Jennifer /Chapmen//"
        ]
        data = us05_marriage_before_death()
        for index, value in enumerate(data):
            self.assertEqual(value, usO5Data[index], "This test case will pass since assertEqual is used to check the content of both arrays and the content is the same")

    def test_us_05_different_length(self):
        usO5Data = [
            "Error: INDIVIDUAL US05 I7: named: John /Chapmen/ Died: 1929-03-19 before married at 1959-05-10 to Maria /Chapmen/",
            "Error: INDIVIDUAL US05 I8: named: Adrian /Chapmen/ Died: 1925-05-19 before married at 1954-06-15 to Jennifer /Chapmen/",
            "Error: INDIVIDUAL US05 I8: named: Nicola /Chapmen/ Died: 1925-05-19 before married at 1930-03-16 to Peter /Chapmen/"
        ]
        self.assertNotEqual(len(us05_marriage_before_death()), len(usO5Data), "This test case will pass since assertNotEqual is used and both arrays have different lengths")

    def test_us_05_different_content(self):
        usO5Data = [
            "Error: INDIVIDUAL US05 I7: named: John /Chapmen/ Died: 1929-03-19 before married at 1959-05-10 to Maria /Chapmen/",
            "Error: INDIVIDUAL US05 I8: named: Adrian /Chapmen/ Died: 1925-05-19 before married at 1954-06-15 to Jennifer /Chapmen/"
        ]
        data = us05_marriage_before_death()
        for index, value in enumerate(data):
            self.assertNotEqual


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
            "Error: Individual US31 Individual id I4, name Sebastian /Chapmen/ is living and single.",
            "Error: Individual US31 Individual id I5, name Dominic /Chapmen/ is living and single.",
            "Error: Individual US31 Individual id I15, name Neil /Chapmen/ is living and single."
        ]
        data = project_4_sprint_1.us31_list_living_single()
        for index, value in enumerate(data):
            self.assertNotEqual(value, us31Data[index],
                                "This test case will pass since assertNotEqual is used to check content of both arrays and that content is different")


if __name__ == '__main__':
    unittest.main()

