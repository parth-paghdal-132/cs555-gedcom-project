import unittest
import project_4_sprints

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
        self.assertEqual(len(project_4_sprints.us03_birth_before_death()), len(usO3Data), "This test case will pass since assertEqual method is used and both array has same length")

    # This test case will check content of expected and actual output by in order
    # This test case will pass since assertEqual is used to check content of both array and that content is same
    def test_us_03_same_content(self):
        usO3Data = [
            "Error: INDIVIDUAL US03 I7: named: John /Chapmen/ Died: 1929-03-19 before born at 1930-03-16",
            "Error: INDIVIDUAL US03 I8: named: Adrian /Chapmen/ Died: 1925-05-19 before born at 1930-03-16"
        ]
        data = project_4_sprints.us03_birth_before_death()
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
        self.assertNotEqual(len(project_4_sprints.us03_birth_before_death()), len(usO3Data), "This test case will pass since assertNotEqual is used and both array has different length")
    
    # This test case will check content of expected and actual output by in order
    # This test case will pass since assertNotEqual is used to check content both array and that content is different
    def test_us_03_different_content(self):
        usO3Data = [
            "Error: INDIVIDUAL US03 I8: named: Adrian /Chapmen/ Died: 1925-05-19 before born at 1930-03-16",
            "Error: INDIVIDUAL US03 I7: named: John /Chapmen/ Died: 1929-03-19 before born at 1930-03-16"
        ]
        data = project_4_sprints.us03_birth_before_death()
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
        self.assertEqual(len(project_4_sprints.us30_list_living_married()), len(us30Data), "This test case will pass since assertEqual method is used and both array has same length")

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
        data = project_4_sprints.us30_list_living_married()
        for index, value in enumerate(data):
            self.assertEqual(value, us30Data[index], "This test case will pass since assertEqual is used to check content of both array and that content is same")

    # This test case will check length of expected and actual output
    # This test case will pass since assertNotEqual is used and both array has different length
    def test_us_30_different_length(self):
        us30Data = [
            "Error: Family US30 Family id F3 husband name: Joanne /Chapmen/ and wife name: Sebastian /Chapmen/ both are still living married couple.",
            "Error: Family US30 Family id F8 husband name: Neil /Chapmen/ and wife name: Victoria /Chapmen/ both are still living married couple."
        ]
        self.assertNotEqual(len(project_4_sprints.us30_list_living_married()), len(us30Data), "This test case will pass since assertNotEqual is used and both array has different length")
    
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
        data = project_4_sprints.us30_list_living_married()
        for index, value in enumerate(data):
            self.assertNotEqual(value, us30Data[index], "This test case will pass since assertNotEqual is used to check content both array and that contentis different")

    # Name:- SAI KRISHNA MIRIYALA
    #CWID:- 20010913
    #User Story-29
    # This test case will check the length of the expected and actual output
    # This test case will pass since assertEqual is used and both arrays have the same length
    def test_us_29_same_length(self):
        us29Data = [
            "Error: Individual US29 I1 : named: Edward /Chapmen/ died on: 2010-03-15",
            "Error: Individual US29 I2 : named: Wanda /Chapmen/ died on: 2005-06-19",
            "Error: Individual US29 I3 : named: Sam /Chapmen/ died on: 2015-04-16",
            "Error: Individual US29 I6 : named: John /Chapmen/ died on: 2012-02-18",
            "Error: Individual US29 I7 : named: John /Chapmen/ died on: 1929-03-19",
            "Error: Individual US29 I8 : named: Adrian /Chapmen/ died on: 1925-05-19",
            "Error: Individual US29 I9 : named: Karen /Chapmen/ died on: 1990-05-18",
            "Error: Individual US29 I11 : named: Carol /Chapmen/ died on: 2015-10-30",
            "Error: Individual US29 I13 : named: Maria /Chapmen/ died on: 1999-05-16"
        ]
        self.assertEqual(len(project_4_sprints.us_29_List_deceased()), len(us29Data),
                         "This test case will pass since assertEqual method is used and both arrays have the same length")

    # This test case will check the content of the expected and actual output by order
    # This test case will pass since assertEqual is used to check content of both arrays and that content is the same
    def test_us_29_same_content(self):
        us29Data = [
            "Error: Individual US29 I1 : named: Edward /Chapmen/ died on: 2010-03-15",
            "Error: Individual US29 I2 : named: Wanda /Chapmen/ died on: 2005-06-19",
            "Error: Individual US29 I3 : named: Sam /Chapmen/ died on: 2015-04-16",
            "Error: Individual US29 I6 : named: John /Chapmen/ died on: 2012-02-18",
            "Error: Individual US29 I7 : named: John /Chapmen/ died on: 1929-03-19",
            "Error: Individual US29 I8 : named: Adrian /Chapmen/ died on: 1925-05-19",
            "Error: Individual US29 I9 : named: Karen /Chapmen/ died on: 1990-05-18",
            "Error: Individual US29 I11 : named: Carol /Chapmen/ died on: 2015-10-30",
            "Error: Individual US29 I13 : named: Maria /Chapmen/ died on: 1999-05-16"
        ]
        data = project_4_sprints.us_29_List_deceased()
        for index, value in enumerate(data):
            self.assertEqual(value, us29Data[index],
                             "This test case will pass since assertEqual is used to check content of both arrays and that content is the same")

    # This test case will check the length of the expected and actual output
    # This test case will pass since assertNotEqual is used and both arrays have different length
    def test_us_29_different_length(self):
        us29Data = [
            "Error: Individual US29 I1 : named: Edward /Chapmen/ died on: 2010-03-15",
            "Error: Individual US29 I2 : named: Wanda /Chapmen/ died on: 2005-06-19",
            "Error: Individual US29 I3 : named: Sam /Chapmen/ died on: 2015-04-16",
            "Error: Individual US29 I6 : named: John /Chapmen/ died on: 2012-02-18",
            "Error: Individual US29 I7 : named: John /Chapmen/ died on: 1929-03-19",
            "Error: Individual US29 I8 : named: Adrian /Chapmen/ died on: 1925-05-19",
            "Error: Individual US29 I9 : named: Karen /Chapmen/ died on: 1990-05-18",
            "Error: Individual US29 I11 : named: Carol /Chapmen/ died on: 2015-10-30",
            "Error: Individual US29 I13 : named: Maria /Chapmen/ died on: 1999-05-16",
            "Some random string to check test case"
        ]
        self.assertNotEqual(len(project_4_sprints.us_29_List_deceased()),len(us29Data),"This test case will pass since assertNotEqual is used and both arrays have different length")

    # This test case will check the content of the expected and actual output by order
    # This test case will pass since assertNotEqual is used to check content of both arrays and that content is different
    def test_us_29_different_content(self):
        us29Data = [
            "Error: Individual US29 I13 : named: Maria /Chapmen/ died on: 1999-05-16",
            "Error: Individual US29 I1 : named: Edward /Chapmen/ died on: 2010-03-15",
            "Error: Individual US29 I2 : named: Wanda /Chapmen/ died on: 2005-06-19",
            "Error: Individual US29 I3 : named: Sam /Chapmen/ died on: 2015-04-16",
            "Error: Individual US29 I6 : named: John /Chapmen/ died on: 2012-02-18",
            "Error: Individual US29 I7 : named: John /Chapmen/ died on: 1929-03-19",
            "Error: Individual US29 I8 : named: Adrian /Chapmen/ died on: 1925-05-19",
            "Error: Individual US29 I9 : named: Karen /Chapmen/ died on: 1990-05-18",
            "Error: Individual US29 I11 : named: Carol /Chapmen/ died on: 2015-10-30"
        ]
        data = project_4_sprints.us_29_List_deceased()
        for index, value in enumerate(data):
            self.assertNotEqual(value, us29Data[index],
                                "This test case will pass since assertNotEqual is used to check content of both arrays and that content is different")


    # Name:- MANOJ PATEL D
    #CWID:- 20012221
    def test_us_05_same_length(self):
        usO5Data = [
            "ERROR: US05 Family: F5 husband died on 2012-02-18 before his marriage date 2016-07-06",
            "ERROR: US05 Family: F6 husband died on 1929-03-19 before his marriage date 1959-05-10",
            "ERROR: US05 Family: F7 husband died on 1925-05-19 before his marriage date 1954-06-15"
        ]
        self.assertEqual(len(project_4_sprints.us05_marriage_before_death()), len(usO5Data), "This test case will pass since assertEqual method is used and both arrays have the same length")

    def test_us_05_same_content(self):
        usO5Data = [
            "ERROR: US05 Family: F5 husband died on 2012-02-18 before his marriage date 2016-07-06",
            "ERROR: US05 Family: F6 husband died on 1929-03-19 before his marriage date 1959-05-10",
            "ERROR: US05 Family: F7 husband died on 1925-05-19 before his marriage date 1954-06-15"
        ]
        data = project_4_sprints.us05_marriage_before_death()
        for index, value in enumerate(data):
            self.assertEqual(value, usO5Data[index], "This test case will pass since assertEqual is used to check the content of both arrays and the content is the same")

    def test_us_05_different_length(self):
        usO5Data = [
            "ERROR: US05 Family: F5 husband died on 2012-02-18 before his marriage date 2016-07-06",
            "ERROR: US05 Family: F6 husband died on 1929-03-19 before his marriage date 1959-05-10",
            "ERROR: US05 Family: F7 husband died on 1925-05-19 before his marriage date 1954-06-15",
            "ERROR: US05 Family: F5 husband died on 2012-02-18 before his marriage date 2016-07-06",
            "ERROR: US05 Family: F6 husband died on 1929-03-19 before his marriage date 1959-05-10",
            "ERROR: US05 Family: F7 husband died on 1925-05-19 before his marriage date 1954-06-15"
        ]
        self.assertNotEqual(len(project_4_sprints.us05_marriage_before_death()), len(usO5Data), "This test case will pass since assertNotEqual is used and both arrays have different lengths")

    def test_us_05_different_content(self):
        usO5Data = [
            "ERROR: US05 Family: F7 husband died on 1925-05-19 before his marriage date 1954-06-15",
            "ERROR: US05 Family: F5 husband died on 2012-02-18 before his marriage date 2016-07-06",
            "ERROR: US05 Family: F6 husband died on 1929-03-19 before his marriage date 1959-05-10"
        ]
        data = project_4_sprints.us05_marriage_before_death()
        for index, value in enumerate(data):
            self.assertNotEqual(value, usO5Data[index], "This test case will pass since assertNotEqual is used and both arrays have differetn content.")


    # This test case will check the length of the expected and actual output
    # This test case will pass since assertEqual is used and both arrays have the same length
    def test_us_31_same_length(self):
        us31Data = [
            "Error: INDIVIDUAL US31 I26 named: Sonia /Chapmen/ is alive, over 30 year old and never married"
        ]
        self.assertEqual(len(project_4_sprints.us31_list_living_single()), len(us31Data),
                         "This test case will pass since assertEqual method is used and both arrays have the same length")

    def test_us_31_same_content(self):
        us31Data = [
            "Error: INDIVIDUAL US31 I26 named: Sonia /Chapmen/ is alive, over 30 year old and never married"
        ]
        data = project_4_sprints.us31_list_living_single()
        for index, value in enumerate(data):
            self.assertEqual(value, us31Data[index], "This test case will pass since data is same in both array.")  
    
    # This test case will check the length of the expected and actual output
    # This test case will pass since assertNotEqual is used and both arrays have different length
    def test_us_31_different_length(self):
        us31Data = [
            "Error: INDIVIDUAL US31 I26 named: Sonia /Chapmen/ is alive, over 30 year old and never married",
            "Error: INDIVIDUAL US31 I26 named: Sonia /Chapmen/ is alive, over 30 year old and never married"
        ]
        self.assertNotEqual(len(project_4_sprints.us31_list_living_single()), len(us31Data),
                            "This test case will pass since assertNotEqual is used and both arrays have different length")

    # This test case will check the content of the expected and actual output by order
    # This test case will pass since assertNotEqual is used to check content of both arrays and that content is different
    def test_us_31_different_content(self):
        us31Data = [
            "Error: INDIVIDUAL US31 I26 named: Andrew /Chapmen/ is alive, over 30 year old and never married"
        ]
        data = project_4_sprints.us31_list_living_single()
        for index, value in enumerate(data):
            self.assertNotEqual(value, us31Data[index],
                                "This test case will pass since assertNotEqual is used to check content of both arrays and that content is different")

    #Name:- SAHITHYA AMBATI
    #CWID:- 20012050
    # Test case for us16_male_last_names()

    # This test case will check length of expected and actual output
    # This test case will pass since assertEqual is used and both array has same length
    def test_us_16_same_length(self):
        us16Data = []
        self.assertEqual(len(project_4_sprints.us16_male_last_names()), len(us16Data),
                         "This test case will pass since assertEqual method is used and both array has same length")

    # This test case will check content of expected and actual output by in order
    # This test case will pass since assertEqual is used to check content of both array and that content is same
    def test_us_16_same_content(self):
        us16Data = []
        data = project_4_sprints.us16_male_last_names()
        for index, value in enumerate(data):
            self.assertEqual(value, us16Data[index],
                             "This test case will pass since assertEqual is used to check content of both array and that content is same")

    # This test case will check length of expected and actual output
    # This test case will pass since assertNotEqual is used and both array has different length
    def test_us_16_different_length(self):
        us16Data = [
            "Some random string just for mock purpose."
        ]
        self.assertNotEqual(len(project_4_sprints.us16_male_last_names()), len(us16Data),
                            "This test case will pass since assertNotEqual is used and both array has different length")

    # This test case will check content of expected and actual output by in order
    # This test case will pass since assertNotEqual is used to check content both array and that content is different
    def test_us_16_different_content(self):
        us16Data = [
            "Some random string just for mock purpose."
        ]
        data = project_4_sprints.us16_male_last_names()
        for index, value in enumerate(data):
            self.assertNotEqual(value, us16Data[index],
                                "This test case will pass since assertNotEqual is used to check content both array and that content is different")

    #Name:- SAHITHYA AMBATI
    #CWID:- 20012050
    # Test case for us28_order_siblings_by_age()
    def test_us_28_same_length(self):
        us28Data = [
            "ERROR: US28 FAMILY: F1 sorted siblings (oldest first): ID:I4 Age: 92 |-| ID:I5 Age: 92 |-| ID:I3 Age: 85 |-| ID:I6 Age: 81 |-| ID:I7 Age: 0 |-| ID:I8 Age: -4",
            "ERROR: US28 FAMILY: F2 sorted siblings (oldest first): ID:I16 Age: 69 |-| ID:I15 Age: 65",
            "ERROR: US28 FAMILY: F3 sorted siblings (oldest first): ID:I20 Age: 80 |-| ID:I21 Age: 76 |-| ID:I22 Age: 11",
            "ERROR: US28 FAMILY: F11 sorted siblings (oldest first): ID:I24 Age: 52",
            "ERROR: US28 FAMILY: F12 sorted siblings (oldest first): ID:I26 Age: 47"
        ]
        self.assertEqual(len(project_4_sprints.us28_order_siblings_by_age()), len(us28Data),
                         "This test case will pass since assertEqual method is used and both array has same length")

    def test_us_28_same_content(self):
        us28Data = [
            "ERROR: US28 FAMILY: F1 sorted siblings (oldest first): ID:I4 Age: 92 |-| ID:I5 Age: 92 |-| ID:I3 Age: 85 |-| ID:I6 Age: 81 |-| ID:I7 Age: 0 |-| ID:I8 Age: -4",
            "ERROR: US28 FAMILY: F2 sorted siblings (oldest first): ID:I16 Age: 69 |-| ID:I15 Age: 65",
            "ERROR: US28 FAMILY: F3 sorted siblings (oldest first): ID:I20 Age: 80 |-| ID:I21 Age: 76 |-| ID:I22 Age: 11",
            "ERROR: US28 FAMILY: F11 sorted siblings (oldest first): ID:I24 Age: 52",
            "ERROR: US28 FAMILY: F12 sorted siblings (oldest first): ID:I26 Age: 47"
        ]
        data = project_4_sprints.us28_order_siblings_by_age()
        for index, value in enumerate(data):
            self.assertEqual(value, data[index],
                             "This test case will pass since assertEqual is used to check content of both array and that content is same")

    def test_us_28_different_length(self):
        us28Data = [
            "ERROR: US28 FAMILY: F2 sorted siblings (oldest first): ID:I16 Age: 69 |-| ID:I15 Age: 65",
            "ERROR: US28 FAMILY: F3 sorted siblings (oldest first): ID:I20 Age: 80 |-| ID:I21 Age: 76 |-| ID:I22 Age: 11",
            "ERROR: US28 FAMILY: F11 sorted siblings (oldest first): ID:I24 Age: 52",
            "ERROR: US28 FAMILY: F12 sorted siblings (oldest first): ID:I26 Age: 47"
        ]
        self.assertNotEqual(len(project_4_sprints.us28_order_siblings_by_age()), len(us28Data),
                            "This test case will pass since assertNotEqual is used and both array has different length")

    def test_us_28_different_content(self):
        us28Data = [
            "ERROR: US28 FAMILY: F2 sorted siblings (oldest first): ID:I16 Age: 69 |-| ID:I15 Age: 65",
            "ERROR: US28 FAMILY: F1 sorted siblings (oldest first): ID:I4 Age: 92 |-| ID:I5 Age: 92 |-| ID:I3 Age: 85 |-| ID:I6 Age: 81 |-| ID:I7 Age: 0 |-| ID:I8 Age: -4",
            "ERROR: US28 FAMILY: F12 sorted siblings (oldest first): ID:I26 Age: 47",
            "ERROR: US28 FAMILY: F3 sorted siblings (oldest first): ID:I20 Age: 80 |-| ID:I21 Age: 76 |-| ID:I22 Age: 11",
            "ERROR: US28 FAMILY: F11 sorted siblings (oldest first): ID:I24 Age: 52"
        ]
        data = project_4_sprints.us28_order_siblings_by_age()
        for index, value in enumerate(data):
            self.assertNotEqual(value, us28Data[index],
                                "This test case will pass since assertNotEqual is used to check content both array and that content is different")
            
    # Test case for US12 - Parents not too old
    # Test cases written by Sai Krishna (km) and Parth Paghdal (pp)
    # This test case are written using pair programming
    # There is total 4 test cases for this user story where two test cases for good data and two for bad data

    # This test case will check length of expected and actual output
    # This test case will pass since assertEqual is used and both array has same length
    def test_us_12_same_length(self):
        us12Data = [
            "ERROR: US12 Family: F1 mother named: Wanda /Chapmen/ and age:94 more than 60 year than her child named: John /Chapmen/ with age 0",
            "ERROR: US12 Family: F1 father named: Edward /Chapmen/ and age:99 more than 80 year than his child named: John /Chapmen/ with age 0",
            "ERROR: US12 Family: F1 mother named: Wanda /Chapmen/ and age:94 more than 60 year than her child named: Adrian /Chapmen/ with age -4",
            "ERROR: US12 Family: F1 father named: Edward /Chapmen/ and age:99 more than 80 year than his child named: Adrian /Chapmen/ with age -4",
            "ERROR: US12 Family: F3 mother named: Sebastian /Chapmen/ and age:92 more than 60 year than her child named: Kimberely /Chapmen/ with age 11",
            "ERROR: US12 Family: F3 father named: Joanne /Chapmen/ and age:92 more than 80 year than his child named: Kimberely /Chapmen/ with age 11"
        ]
        self.assertEqual(len(us12Data), len(project_4_sprints.us12_parents_not_too_old()), "This test case will pass since assertEqual method is used and both array has same length")

    # This test case will check content of expected and actual output by in order
    # This test case will pass since assertEqual is used to check content of both array and that content is same
    def test_us_12_same_content(self):
        us12Data = [
            "ERROR: US12 Family: F1 mother named: Wanda /Chapmen/ and age:94 more than 60 year than her child named: John /Chapmen/ with age 0",
            "ERROR: US12 Family: F1 father named: Edward /Chapmen/ and age:99 more than 80 year than his child named: John /Chapmen/ with age 0",
            "ERROR: US12 Family: F1 mother named: Wanda /Chapmen/ and age:94 more than 60 year than her child named: Adrian /Chapmen/ with age -4",
            "ERROR: US12 Family: F1 father named: Edward /Chapmen/ and age:99 more than 80 year than his child named: Adrian /Chapmen/ with age -4",
            "ERROR: US12 Family: F3 mother named: Sebastian /Chapmen/ and age:93 more than 60 year than her child named: Kimberely /Chapmen/ with age 11",
            "ERROR: US12 Family: F3 father named: Joanne /Chapmen/ and age:92 more than 80 year than his child named: Kimberely /Chapmen/ with age 11"

        ]
        data = project_4_sprints.us12_parents_not_too_old()
        for index, value in enumerate(data):
            self.assertEqual(value, us12Data[index], "This test case will pass since assertEqual is used to check content of both array and that content is same")

    # This test case will check length of expected and actual output
    # This test case will pass since assertNotEqual is used and both array has different length
    def test_us_12_different_length(self):
        us12Data = [
            "ERROR: US12 Family: F1 father named: Edward /Chapmen/ and age:99 more than 80 year than his child named: John /Chapmen/ with age 0",
            "ERROR: US12 Family: F1 father named: Edward /Chapmen/ and age:99 more than 80 year than his child named: Adrian /Chapmen/ with age -4",
            "ERROR: US12 Family: F3 father named: Joanne /Chapmen/ and age:92 more than 80 year than his child named: Kimberely /Chapmen/ with age 11",
            "ERROR: US12 Family: F3 father named: Joanne /Chapmen/ and age:92 more than 80 year than his child named: Kimberely /Chapmen/ with age 11"
        ]
        self.assertNotEqual(len(us12Data), len(project_4_sprints.us12_parents_not_too_old()), "This test case will pass since assertNotEqual is used and both array has different length")


    # This test case will check content of expected and actual output by in order
    # This test case will pass since assertNotEqual is used to check content both array and that content is different
    def test_us_12_different_content(self):
        us12Data = [
            "ERROR: US12 Family: F1 father named: Edward /Chapmen/ and age:99 more than 80 year than his child named: John /Chapmen/ with age 0",
            "ERROR: US12 Family: F1 mother named: Wanda /Chapmen/ and age:94 more than 60 year than her child named: Adrian /Chapmen/ with age -4",
            "ERROR: US12 Family: F1 father named: Edward /Chapmen/ and age:99 more than 80 year than his child named: Adrian /Chapmen/ with age -4",
            "ERROR: US12 Family: F3 mother named: Sebastian /Chapmen/ and age:92 more than 60 year than her child named: Kimberely /Chapmen/ with age 11",
            "ERROR: US12 Family: F3 father named: Joanne /Chapmen/ and age:92 more than 80 year than his child named: Kimberely /Chapmen/ with age 11",
            "ERROR: US12 Family: F1 mother named: Wanda /Chapmen/ and age:94 more than 60 year than her child named: John /Chapmen/ with age 0"
        ]
        data = project_4_sprints.us12_parents_not_too_old()
        for index, value in enumerate(data):
            self.assertNotEqual(value, us12Data[index], "This test case will pass since assertNotEqual is used to check content of both array and that content is different")

    # Test case for US01 - Dates before current date
    # Test cases written by Parth Paghdal (pp)
    # This test case are written individually for finding difference between pair programming and individually
    # There is total 4 test cases for this user story where two test cases for good data and two for bad data
    # This test case will check length of expected and actual output
    # This test case will pass since assertEqual is used and both array has same length
    def test_us_01_same_length(self):
        us01Data = []
        self.assertEqual(len(us01Data), len(project_4_sprints.us01_dates_before_current_date()), "This test case will pass since assertEqual method is used and both array has same length")
    
    # This test case will check content of expected and actual output by in order
    # This test case will pass since assertEqual is used to check content of both array and that content is same
    def test_us_01_same_content(self):
        us01Data = []
        data = project_4_sprints.us01_dates_before_current_date()
        for index, value in enumerate(data):
            self.assertEqual(value, us01Data[index], "This test case will pass since assertEqual is used to check content of both array and that content is same")

    # This test case will check length of expected and actual output
    # This test case will pass since assertNotEqual is used and both array has different length
    def test_us_01_different_length(self):
        us01Data = ["It has some random value to check test case"]
        self.assertNotEqual(len(us01Data), project_4_sprints.us01_dates_before_current_date(), "This test case will pass since assertNotEqual method is used and both array has different length")

    # This test case will check content of expected and actual output by in order
    # This test case will pass since assertNotEqual is used to check content both array and that content is different
    def test_us_01_different_content(self):
        us01Data = ["It has some random value to check test case"]
        data = project_4_sprints.us01_dates_before_current_date()
        for index, value in enumerate(data):
            self.assertNotEqual(value, us01Data[index], "This test case will pass since assertNotEqual is used to check content of both array and that content is different")

    # Test case for US02 - Birth before marriage
    # Test cases written by Parth Paghdal (pp)
    # There is total 4 test cases for this user story where two test cases for good data and two for bad data

    # This test case will check length of expected and actual output
    # This test case will pass since assertEqual is used and both array has same length
    def test_us_02_same_length(self):
        us02Data = [
            "ERROR: US02 Individual: I22 wife named Kimberely /Chapmen/ has future birthdate 2011-08-16 in regards to her marriage date 2002-05-07"
        ]
        self.assertEqual(len(us02Data), len(project_4_sprints.us02_birth_before_marriage()), "This test case will pass since assertEqual method is used and both array has same length")

    # This test case will check content of expected and actual output by in order
    # This test case will pass since assertEqual is used to check content of both array and that content is same
    def test_us_02_same_content(self):
        us02Data = [
            "ERROR: US02 Individual: I22 wife named Kimberely /Chapmen/ has future birthdate 2011-08-16 in regards to her marriage date 2002-05-07"
        ]
        data = project_4_sprints.us02_birth_before_marriage()
        for index, value in enumerate(data):
            self.assertEqual(value, us02Data[index], "This test case will pass since assertEqual is used to check content of both array and that content is same")

    # This test case will check length of expected and actual output
    # This test case will pass since assertNotEqual is used and both array has different length
    def test_us_02_different_length(self):
        us02Data = [
            "ERROR: US02 Individual: I22 wife named Kimberely /Chapmen/ has future birthdate 2011-08-16 in regards to her marriage date 2002-05-07",
            "ERROR: US02 Individual: I22 wife named Kimberely /Chapmen/ has future birthdate 2011-08-16 in regards to her marriage date 2002-05-07"
        ]
        self.assertNotEqual(len(us02Data), len(project_4_sprints.us02_birth_before_marriage()), "This test case will pass since assertNotEqual method is used and both array has different length")

    # This test case will check content of expected and actual output by in order
    # This test case will pass since assertNotEqual is used to check content of both array and that content is different
    def test_us_02_different_content(self):
        us02Data = [
            "ERROR: US02 Individual: I22 wife named Andrew /Chapmen/ has future birthdate 2011-08-16 in regards to her marriage date 2002-05-07"
        ]
        data = project_4_sprints.us02_birth_before_marriage()
        for index, value in enumerate(data):
            self.assertNotEqual(value, us02Data[index], "This test case will pass since assertNotEqual is used to check content of both array and that content is different")
    
    
    # Test case for US25 - Unique first names in families
    # Test cases written by Sai Krishna (km)
    # There is total 4 test cases for this user story where two test cases for good data and two for bad data
    # This test case will check length of expected and actual output
    # This test case will pass since assertEqual is used and both array has same length
    def test_us_25_same_length(self):
        us25Data = [
            "ERROR: US25 FAMILY: F1 is having 2 children with same name: John /Chapmen/ and same birthdate: 1930-03-16"
        ]
        self.assertEqual(len(us25Data), len(project_4_sprints.us_25_unique_first_names_in_families()), "This test case will pass since assertEqual method is used and both array has same length")

    # This test case will check content of expected and actual output by in order
    # This test case will pass since assertEqual is used to check content of both array and that content is same
    def test_us_25_same_content(self):
        us25Data = [
            "ERROR: US25 FAMILY: F1 is having 2 children with same name: John /Chapmen/ and same birthdate: 1930-03-16"
        ]
        data = project_4_sprints.us_25_unique_first_names_in_families()
        for index, value in enumerate(data):
            self.assertEqual(value, us25Data[index], "This test case will pass since assertEqual is used to check content of both array and that content is same")

    # This test case will check length of expected and actual output
    # This test case will pass since assertNotEqual is used and both array has different length
    def test_us_25_different_length(self):
        us25Data = [
            "ERROR: US25 FAMILY: F1 is having 2 children with same name: John /Chapmen/ and same birthdate: 1930-03-16",
            "ERROR: US25 FAMILY: F1 is having 2 children with same name: John /Chapmen/ and same birthdate: 1930-03-16"
        ]
        self.assertNotEqual(len(us25Data), len(project_4_sprints.us_25_unique_first_names_in_families()), "This test case will pass since assertNotEqual method is used and both array has different length")

    # This test case will check content of expected and actual output by in order
    # This test case will pass since assertNotEqual is used to check content of both array and that content is different
    def test_us_25_different_content(self):
        us25Data = [
            "ERROR: US25 FAMILY: F1 is having 250 children with same name: John /Chapmen/ and same birthdate: 1930-03-16"
        ]
        data = project_4_sprints.us_25_unique_first_names_in_families()
        for index, value in enumerate(data):
            self.assertNotEqual(value, us25Data[index], "This test case will pass since assertNotEqual is used to check content of both array and that content is different")

     # Test case for US10 - Marriage after 14
    # Test cases written by Sai Krishna (km)
    # There is total 4 test cases for this user story where two test cases for good data and two for bad data
    # This test case will check length of expected and actual output
    # This test case will pass since assertEqual is used and both array has same length
    def test_us_10_same_length(self):
        us10Data = [
            "ERROR: US10 FAMILY: F3 has wife named: Sebastian /Chapmen/ born on 1930-03-16 and got married on 1941-10-03 and this time difference is less than 14 years",
            "ERROR: US10 FAMILY: F3 has husband named: Joanne /Chapmen/ born on 1931-02-17 and got married on 1941-10-03 and this time difference is less than 14 years",
            "ERROR: US10 FAMILY: F4 has husband named: Dominic /Chapmen/ born on 1930-03-16 and got married on 1942-04-06 and this time difference is less than 14 years",
            "ERROR: US10 FAMILY: F4 has wife named: Carol /Chapmen/ born on 1932-08-23 and got married on 1942-04-06 and this time difference is less than 14 years",
            "ERROR: US10 FAMILY: F14 has wife named: Kimberely /Chapmen/ born on 2011-08-16 and got married on 2002-05-07 and this time difference is less than 14 years",
        ]
        self.assertEqual(len(us10Data), len(project_4_sprints.us_10_marriage_after_14()), "This test case will pass since assertEqual method is used and both array has same length")

    # This test case will check content of expected and actual output by in order
    # This test case will pass since assertEqual is used to check content of both array and that content is same
    def test_us_10_same_content(self):
        us10Data = [
            "ERROR: US10 FAMILY: F3 has wife named: Sebastian /Chapmen/ born on 1930-03-16 and got married on 1941-10-03 and this time difference is less than 14 years",
            "ERROR: US10 FAMILY: F3 has husband named: Joanne /Chapmen/ born on 1931-02-17 and got married on 1941-10-03 and this time difference is less than 14 years",
            "ERROR: US10 FAMILY: F4 has husband named: Dominic /Chapmen/ born on 1930-03-16 and got married on 1942-04-06 and this time difference is less than 14 years",
            "ERROR: US10 FAMILY: F4 has wife named: Carol /Chapmen/ born on 1932-08-23 and got married on 1942-04-06 and this time difference is less than 14 years",
            "ERROR: US10 FAMILY: F14 has wife named: Kimberely /Chapmen/ born on 2011-08-16 and got married on 2002-05-07 and this time difference is less than 14 years",
        ]
        data = project_4_sprints.us_10_marriage_after_14()
        for index, value in enumerate(data):
            self.assertEqual(value, us10Data[index], "This test case will pass since assertEqual is used to check content of both array and that content is same")

    # This test case will check length of expected and actual output
    # This test case will pass since assertNotEqual is used and both array has different length
    def test_us_10_different_length(self):
        us10Data = [
            "ERROR: US10 FAMILY: F3 has wife named: Sebastian /Chapmen/ born on 1930-03-16 and got married on 1941-10-03 and this time difference is less than 14 years",
            "ERROR: US10 FAMILY: F3 has husband named: Joanne /Chapmen/ born on 1931-02-17 and got married on 1941-10-03 and this time difference is less than 14 years",
            "ERROR: US10 FAMILY: F4 has husband named: Dominic /Chapmen/ born on 1930-03-16 and got married on 1942-04-06 and this time difference is less than 14 years",
            "ERROR: US10 FAMILY: F4 has wife named: Carol /Chapmen/ born on 1932-08-23 and got married on 1942-04-06 and this time difference is less than 14 years",
            "ERROR: US10 FAMILY: F14 has wife named: Kimberely /Chapmen/ born on 2011-08-16 and got married on 2002-05-07 and this time difference is less than 14 years",
            "ERROR: US10 FAMILY: F3 has wife named: Sebastian /Chapmen/ born on 1930-03-16 and got married on 1941-10-03 and this time difference is less than 14 years",   
        ]
        self.assertNotEqual(len(us10Data), len(project_4_sprints.us_10_marriage_after_14()), "This test case will pass since assertNotEqual method is used and both array has different length")

    # This test case will check content of expected and actual output by in order
    # This test case will pass since assertNotEqual is used to check content of both array and that content is different
    def test_us_10_different_content(self):
        us10Data = [
            "ERROR: US10 FAMILY: F14 has wife named: Kimberely /Chapmen/ born on 2011-08-16 and got married on 2002-05-07 and this time difference is less than 14 years",
            "ERROR: US10 FAMILY: F3 has wife named: Sebastian /Chapmen/ born on 1930-03-16 and got married on 1941-10-03 and this time difference is less than 14 years",
            "ERROR: US10 FAMILY: F3 has husband named: Joanne /Chapmen/ born on 1931-02-17 and got married on 1941-10-03 and this time difference is less than 14 years",
            "ERROR: US10 FAMILY: F4 has husband named: Dominic /Chapmen/ born on 1930-03-16 and got married on 1942-04-06 and this time difference is less than 14 years",
            "ERROR: US10 FAMILY: F4 has wife named: Carol /Chapmen/ born on 1932-08-23 and got married on 1942-04-06 and this time difference is less than 14 years"
        ]
        data = project_4_sprints.us_10_marriage_after_14()
        for index, value in enumerate(data):
            self.assertNotEqual(value, us10Data[index], "This test case will pass since assertNotEqual is used to check content of both array and that content is different")
            
            
    # Name:- AMBATI BABY NAGA SAHITHYA
    # CWID:- 20012050
    # Test case for us_04_marriage_before_divorce()
    # There is total 4 test cases for this user story where two test cases for good data and two for bad data
    # This test case will check length of expected and actual output
    # This test case will pass since assertEqual is used and both array has same length
    def test_us_04_same_length(self):
        us04Data = [
            "ERROR: US04 FAMILY: F6 is having future marriage date 1959-05-10 in reagrds to divorce date 1951-08-17"
        ]
        self.assertEqual(len(us04Data), len(project_4_sprints.us_04_marriage_before_divorce()),
                            "This test case will pass since assertEqual method is used and both array has same length")

    # This test case will check content of expected and actual output by in order
    # This test case will pass since assertEqual is used to check content of both array and that content is same
    def test_us_04_same_content(self):
        us04Data = [
            "ERROR: US04 FAMILY: F6 is having future marriage date 1959-05-10 in reagrds to divorce date 1951-08-17"
        ]
        data = project_4_sprints.us_04_marriage_before_divorce()
        for index, value in enumerate(data):
            self.assertEqual(value, us04Data[index],
                                "This test case will pass since assertEqual is used to check content of both array and that content is same")

    # This test case will check length of expected and actual output
    # This test case will pass since assertNotEqual is used and both array has different length
    def test_us_04_different_length(self):
        us04Data = [
            "ERROR: US04 FAMILY: F6 is having future marriage date 1959-05-10 in reagrds to divorce date 1951-08-17",
            "ERROR: US04 FAMILY: F6 is having future marriage date 1959-05-10 in reagrds to divorce date 1951-08-17"
        ]
        self.assertNotEqual(len(us04Data), len(project_4_sprints.us_04_marriage_before_divorce()),
                            "This test case will pass since assertNotEqual method is used and both array has different length")

    # This test case will check content of expected and actual output by in order
    # This test case will pass since assertNotEqual is used to check content of both array and that content is different
    def test_us_04_different_content(self):
        us04Data = [
            "ERROR: US04 FAMILY: F1526 is having future marriage date 2052-05-10 in reagrds to divorce date 1950-08-17"
        ]
        data = project_4_sprints.us_04_marriage_before_divorce()
        for index, value in enumerate(data):
            self.assertNotEqual(value, us04Data[index],
                                "This test case will pass since assertNotEqual is used to check content of both array and that content is different")
                
                
    # Name:- AMBATI BABY NAGA SAHITHYA
    # CWID:- 20012050
    # Test case for us_06_divorce_before_death()
    # There is total 4 test cases for this user story where two test cases for good data and two for bad data
    # This test case will check length of expected and actual output
    # This test case will pass since assertEqual is used and both array has same length
    def test_us_06_same_length(self):
        us06Data = [
            "ERROR: US06 FAMILY: F6 divorce happened at 1951-08-17 which is after the death of husband on 1929-03-19"
        ]
        self.assertEqual(len(us06Data), len(project_4_sprints.us_06_divorce_before_death()),
                            "This test case will pass since assertEqual method is used and both array has same length")

    # This test case will check content of expected and actual output by in order
    # This test case will pass since assertEqual is used to check content of both array and that content is same
    def test_us_06_same_content(self):
        us06Data = [
            "ERROR: US06 FAMILY: F6 divorce happened at 1951-08-17 which is after the death of husband on 1929-03-19"
        ]
        data = project_4_sprints.us_06_divorce_before_death()
        for index, value in enumerate(data):
            self.assertEqual(value, us06Data[index],
                                "This test case will pass since assertEqual is used to check content of both array and that content is same")

    # This test case will check length of expected and actual output
    # This test case will pass since assertNotEqual is used and both array has different length
    def test_us_06_different_length(self):
        us06Data = [
            "ERROR: US06 FAMILY: F6 divorce happened at 1951-08-17 which is after the death of husband on 1929-03-19",
            "ERROR: US06 FAMILY: F6 divorce happened at 1951-08-17 which is after the death of husband on 1929-03-19"
        ]
        self.assertNotEqual(len(us06Data), len(project_4_sprints.us_06_divorce_before_death()),
                            "This test case will pass since assertEqual method is used and both array has same length")

    # This test case will check content of expected and actual output by in order
    # This test case will pass since assertNotEqual is used to check content of both array and that content is different
    def test_us_06_different_content(self):
        us06Data = [
            "ERROR: US06 FAMILY: F6410 divorce happened at 3521-08-17 which is after the death of husband on 1129-03-19"
        ]
        data = project_4_sprints.us_06_divorce_before_death()
        for index, value in enumerate(data):
            self.assertNotEqual(value, us06Data[index],
                                "This test case will pass since assertEqual is used to check content of both array and that content is same")
    
# Test case for US08 - Birth before marriage of parents
    # Test cases written by Manoj Patel (mp)
    # There is total 4 test cases for this user story where two test cases for good data and two for bad data
    # This test case will check length of expected and actual output
    # This test case will pass since assertEqual method is used and both array has same length
    def test_us_08_same_length(self):
        us08Data = [
            "ERROR: US08 FAMILY F2 is having child named Sam /Chapmen/ born on 1953-11-29 which is earlier than parents' marriage date 1954-05-27"
        ]
        self.assertEqual(len(us08Data), len(project_4_sprints.us_08_birth_before_marriage_of_parents()),
                            "This test case will pass since assertEqual method is used and both array has same length")

    # This test case will check content of expected and actual output by in order
    # This test case will pass since assertEqual is used to check content of both array and that content is same
    def test_us_08_same_content(self):
        us08Data = [
            "ERROR: US08 FAMILY F2 is having child named Sam /Chapmen/ born on 1953-11-29 which is earlier than parents' marriage date 1954-05-27"
        ]
        data = project_4_sprints.us_08_birth_before_marriage_of_parents()
        for index, value in enumerate(data):
            self.assertEqual(value, us08Data[index],"This test case will pass since assertEqual is used to check content of both array and that content is same")

    # This test case will check length of expected and actual output
    # This test case will pass since assertNotEqual method is used and both array has different length
    def test_us_08_different_length(self):
        us08Data = [
            "ERROR: US08 FAMILY F2 is having child named Sam /Chapmen/ born on 1953-11-29 which is earlier than parents' marriage date 1954-05-27",
            "ERROR: US08 FAMILY F2 is having child named Sam /Chapmen/ born on 1953-11-29 which is earlier than parents' marriage date 1954-05-27"
        ]
        self.assertNotEqual(len(us08Data), len(project_4_sprints.us_08_birth_before_marriage_of_parents()),
                            "This test case will pass since assertNotEqual method is used and both array has different length")

    # This test case will check content of expected and actual output by in order
    # This test case will pass since assertNotEqual is used to check content of both array and that content is different
    def test_us_08_different_content(self):
        us08Data = [
            "ERROR: US08 FAMILY F215 is having child named Tako /Mannican/ born on 1324-11-29 which is earlier than parents' marriage date 3568-05-27"
        ]
        data = project_4_sprints.us_08_birth_before_marriage_of_parents()
        for index, value in enumerate(data):
            self.assertNotEqual(value, us08Data[index],"This test case will pass since assertNotEqual is used to check content of both array and that content is different")


    # Test case for US09 - Birth before death of parents
    # Test cases written by Manoj Patel (mp)
    # There is total 4 test cases for this user story where two test cases for good data and two for bad data
    # This test case will check length of expected and actual output
    # This test case will pass since assertEqual method is used and both array has same length
    def test_us_09_same_length(self):
        us09Data = []
        self.assertEqual(len(us09Data), len(project_4_sprints.us_09_birth_before_death_of_parents()), "This test case will pass since assertEqual method is used and both array has same length")

    # This test case will check content of expected and actual output by in order
    # This test case will pass since assertEqual is used to check content of both array and that content is same
    def test_us_09_same_content(self):
        us09Data = []
        data = project_4_sprints.us_09_birth_before_death_of_parents()
        for index, value in enumerate(data):
            self.assertEqual(value, us09Data[index], "This test case will pass since assertEqual is used to check content of both array and that content is same")

    # This test case will check length of expected and actual output
    # This test case will pass since assertNotEqual method is used and both array has different length
    def test_us_09_different_length(self):
        us09Data = ["Here is the some random string to check test case"]
        self.assertNotEqual(len(us09Data), len(project_4_sprints.us_09_birth_before_death_of_parents()), "This test case will pass since assertNotEqual method is used and both array has different length")

    # This test case will check content of expected and actual output by in order
    # This test case will pass since assertNotEqual is used to check content of both array and that content is different
    def test_us_09_different_content(self):
        us09Data = ["Here is the some random string to check test case"]
        data = project_4_sprints.us_09_birth_before_death_of_parents()
        for index, value in enumerate(data):
            self.assertNotEqual(value, us09Data[index], "This test case will pass since assertNotEqual is used to check content of both array and that content is different")

    # Test case for US13 - Siblings spacing
    # Test cases written by Parth Paghdal (pp)
    # There is total 4 test cases for this user story where two test cases for good data and two for bad data

    # This test case will check length of expected and actual output
    # This test case will pass since assertEqual is used and both array has same length
    def test_us_13_same_length(self):
        us13Data = [
            "ERROR: US13 Individual I3 named Sam /Chapmen/ born on 1930-03-16 is either born before 8 months or less than 2 days apart his sibling id I4 named Sebastian /Chapmen/ born on 1930-03-16",
            "ERROR: US13 Individual I4 named Sebastian /Chapmen/ born on 1930-03-16 is either born before 8 months or less than 2 days apart his sibling id I5 named Dominic /Chapmen/ born on 1930-03-16",
            "ERROR: US13 Individual I5 named Dominic /Chapmen/ born on 1930-03-16 is either born before 8 months or less than 2 days apart his sibling id I6 named John /Chapmen/ born on 1930-03-16",
            "ERROR: US13 Individual I6 named John /Chapmen/ born on 1930-03-16 is either born before 8 months or less than 2 days apart his sibling id I7 named John /Chapmen/ born on 1930-03-16",
            "ERROR: US13 Individual I7 named John /Chapmen/ born on 1930-03-16 is either born before 8 months or less than 2 days apart his sibling id I8 named Adrian /Chapmen/ born on 1930-03-16",
            "ERROR: US13 Individual I16 named Sam /Chapmen/ born on 1953-11-29 is either born before 8 months or less than 2 days apart his sibling id I15 named Neil /Chapmen/ born on 1957-12-25",
            "ERROR: US13 Individual I20 named Benjamin /Chapmen/ born on 1943-01-12 is either born before 8 months or less than 2 days apart his sibling id I21 named Boris /Chapmen/ born on 1946-05-29",
            "ERROR: US13 Individual I21 named Boris /Chapmen/ born on 1946-05-29 is either born before 8 months or less than 2 days apart his sibling id I22 named Kimberely /Chapmen/ born on 2011-08-16"
        ]
        self.assertEqual(len(us13Data), len(project_4_sprints.us_13_siblings_spacing()), "This test case will pass since assertEqual method is used and both array has same length")

    # This test case will check content of expected and actual output by in order
    # This test case will pass since assertEqual is used to check content of both array and that content is same
    def test_us_13_same_content(self):
        us13Data = [
            "ERROR: US13 Individual I3 named Sam /Chapmen/ born on 1930-03-16 is either born before 8 months or less than 2 days apart his sibling id I4 named Sebastian /Chapmen/ born on 1930-03-16",
            "ERROR: US13 Individual I4 named Sebastian /Chapmen/ born on 1930-03-16 is either born before 8 months or less than 2 days apart his sibling id I5 named Dominic /Chapmen/ born on 1930-03-16",
            "ERROR: US13 Individual I5 named Dominic /Chapmen/ born on 1930-03-16 is either born before 8 months or less than 2 days apart his sibling id I6 named John /Chapmen/ born on 1930-03-16",
            "ERROR: US13 Individual I6 named John /Chapmen/ born on 1930-03-16 is either born before 8 months or less than 2 days apart his sibling id I7 named John /Chapmen/ born on 1930-03-16",
            "ERROR: US13 Individual I7 named John /Chapmen/ born on 1930-03-16 is either born before 8 months or less than 2 days apart his sibling id I8 named Adrian /Chapmen/ born on 1930-03-16",
            "ERROR: US13 Individual I16 named Sam /Chapmen/ born on 1953-11-29 is either born before 8 months or less than 2 days apart his sibling id I15 named Neil /Chapmen/ born on 1957-12-25",
            "ERROR: US13 Individual I20 named Benjamin /Chapmen/ born on 1943-01-12 is either born before 8 months or less than 2 days apart his sibling id I21 named Boris /Chapmen/ born on 1946-05-29",
            "ERROR: US13 Individual I21 named Boris /Chapmen/ born on 1946-05-29 is either born before 8 months or less than 2 days apart his sibling id I22 named Kimberely /Chapmen/ born on 2011-08-16"
        ]
        data = project_4_sprints.us_13_siblings_spacing()
        for index, value in enumerate(data):
            self.assertEqual(value, us13Data[index], "This test case will pass since assertEqual is used to check content of both array and that content is same")

    # This test case will check length of expected and actual output
    # This test case will pass since assertNotEqual method is used and both array has different length
    def test_us_13_different_length(self):
        us13Data = [
            "ERROR: US13 Individual I3 named Sam /Chapmen/ born on 1930-03-16 is either born before 8 months or less than 2 days apart his sibling id I4 named Sebastian /Chapmen/ born on 1930-03-16",
            "ERROR: US13 Individual I4 named Sebastian /Chapmen/ born on 1930-03-16 is either born before 8 months or less than 2 days apart his sibling id I5 named Dominic /Chapmen/ born on 1930-03-16",
            "ERROR: US13 Individual I5 named Dominic /Chapmen/ born on 1930-03-16 is either born before 8 months or less than 2 days apart his sibling id I6 named John /Chapmen/ born on 1930-03-16",
            "ERROR: US13 Individual I6 named John /Chapmen/ born on 1930-03-16 is either born before 8 months or less than 2 days apart his sibling id I7 named John /Chapmen/ born on 1930-03-16",
            "ERROR: US13 Individual I7 named John /Chapmen/ born on 1930-03-16 is either born before 8 months or less than 2 days apart his sibling id I8 named Adrian /Chapmen/ born on 1930-03-16",
            "ERROR: US13 Individual I16 named Sam /Chapmen/ born on 1953-11-29 is either born before 8 months or less than 2 days apart his sibling id I15 named Neil /Chapmen/ born on 1957-12-25",
            "ERROR: US13 Individual I20 named Benjamin /Chapmen/ born on 1943-01-12 is either born before 8 months or less than 2 days apart his sibling id I21 named Boris /Chapmen/ born on 1946-05-29",
            "ERROR: US13 Individual I21 named Boris /Chapmen/ born on 1946-05-29 is either born before 8 months or less than 2 days apart his sibling id I22 named Kimberely /Chapmen/ born on 2011-08-16",
            "some random string to verify test case."
        ]
        self.assertNotEqual(len(us13Data), len(project_4_sprints.us_13_siblings_spacing()), "This test case will pass since assertNotEqual method is used and both array has different length")

    # This test case will check content of expected and actual output by in order
    # This test case will pass since assertNotEqual is used to check content of both array and that content is different
    def test_us_13_different_content(self):
        us13Data = [
            "ERROR: US13 Individual I21 named Boris /Chapmen/ born on 1946-05-29 is either born before 8 months or less than 2 days apart his sibling id I22 named Kimberely /Chapmen/ born on 2011-08-16",
            "ERROR: US13 Individual I3 named Sam /Chapmen/ born on 1930-03-16 is either born before 8 months or less than 2 days apart his sibling id I4 named Sebastian /Chapmen/ born on 1930-03-16",
            "ERROR: US13 Individual I4 named Sebastian /Chapmen/ born on 1930-03-16 is either born before 8 months or less than 2 days apart his sibling id I5 named Dominic /Chapmen/ born on 1930-03-16",
            "ERROR: US13 Individual I5 named Dominic /Chapmen/ born on 1930-03-16 is either born before 8 months or less than 2 days apart his sibling id I6 named John /Chapmen/ born on 1930-03-16",
            "ERROR: US13 Individual I6 named John /Chapmen/ born on 1930-03-16 is either born before 8 months or less than 2 days apart his sibling id I7 named John /Chapmen/ born on 1930-03-16",
            "ERROR: US13 Individual I7 named John /Chapmen/ born on 1930-03-16 is either born before 8 months or less than 2 days apart his sibling id I8 named Adrian /Chapmen/ born on 1930-03-16",
            "ERROR: US13 Individual I16 named Sam /Chapmen/ born on 1953-11-29 is either born before 8 months or less than 2 days apart his sibling id I15 named Neil /Chapmen/ born on 1957-12-25",
            "ERROR: US13 Individual I20 named Benjamin /Chapmen/ born on 1943-01-12 is either born before 8 months or less than 2 days apart his sibling id I21 named Boris /Chapmen/ born on 1946-05-29"
        ]
        data = project_4_sprints.us_13_siblings_spacing()
        for index, value in enumerate(data):
            self.assertNotEqual(value, us13Data[index], "This test case will pass since assertNotEqual is used to check content of both array and that content is different")


    # Test case for US26 - Corresponding entries
    # Test cases written by Parth Paghdal (pp)
    # There is total 4 test cases for this user story where two test cases for good data and two for bad data

    # This test case will check length of expected and actual output
    # This test case will pass since assertEqual is used and both array has same length
    def test_us_26_same_length(self):
        us26Data = []
        self.assertEqual(len(us26Data), len(project_4_sprints.us_26_corresponding_entries()), "This test case will pass since assertEqual method is used and both array has same length")

    # This test case will check content of expected and actual output by in order
    # This test case will pass since assertEqual is used to check content of both array and that content is same
    def test_us_26_same_content(self):
        us26Data = []
        data = project_4_sprints.us_26_corresponding_entries()
        for index, value in enumerate(data):
            self.assertEqual(value, us26Data[index], "This test case will pass since assertEqual is used to check content of both array and that content is same")

    # This test case will check length of expected and actual output
    # This test case will pass since assertNotEqual method is used and both array has different length
    def test_us_26_different_length(self):
        us26Data = ["Some random string to test this function"]
        self.assertNotEqual(len(us26Data), len(project_4_sprints.us_26_corresponding_entries()), "This test case will pass since assertNotEqual method is used and both array has different length")

    # This test case will check content of expected and actual output by in order
    # This test case will pass since assertNotEqual is used to check content of both array and that content is different
    def test_us_26_different_content(self):
        us26Data = ["Some random string to test this function"]
        data = project_4_sprints.us_26_corresponding_entries()
        for index, value in enumerate(data):
            self.assertNotEqual(value, us26Data[index], "This test case will pass since assertNotEqual is used to check content of both array and that content is different")
    
    # Test case for US14 - Multiple births <= 5
    # Test cases written by Sai Krishna (km)
    # There is total 4 test cases for this user story where two test cases for good data and two for bad data
    # This test case will check length of expected and actual output
    # This test case will pass since assertEqual is used and both array has same length
    def test_us_14_same_length(self):
        us14Data = [
            "ERROR: US14 FAMILY F1 is having more than 5 children born on 1930-03-16"
        ]
        self.assertEqual(len(us14Data), len(project_4_sprints.us_14_multiple_births()), "This test case will pass since assertEqual method is used and both array has same length")

    # This test case will check content of expected and actual output by in order
    # This test case will pass since assertEqual is used to check content of both array and that content is same
    def test_us_14_same_content(self):
        us14Data = [
            "ERROR: US14 FAMILY F1 is having more than 5 children born on 1930-03-16"
        ]
        data = project_4_sprints.us_14_multiple_births()
        for index, value in enumerate(data):
            self.assertEqual(value, us14Data[index], "This test case will pass since assertEqual is used to check content of both array and that content is same")

    # This test case will check length of expected and actual output
    # This test case will pass since assertNotEqual method is used and both array has different length
    def test_us_14_different_length(self):
        us14Data = [
            "ERROR: US14 FAMILY F1 is having more than 5 children born on 1930-03-16",
            "ERROR: US14 FAMILY F1 is having more than 5 children born on 1930-03-16"
        ]
        self.assertNotEqual(len(us14Data), len(project_4_sprints.us_14_multiple_births()), "This test case will pass since assertNotEqual method is used and both array has different length")

    # This test case will check content of expected and actual output by in order
    # This test case will pass since assertNotEqual is used to check content of both array and that content is different
    def test_us_14_different_content(self):
        us14Data = [
            "ERROR: US14 FAMILY F2512 is having more than 105 children born on 1930-03-16",
            "ERROR: US14 FAMILY F0132 is having more than 10525 children born on 1930-03-16"
        ]
        data = project_4_sprints.us_14_multiple_births()
        for index, value in enumerate(data):
            self.assertNotEqual(value, us14Data[index], "This test case will pass since assertNotEqual is used to check content of both array and that content is different")

    # Test case for US18 - Siblings should not marry
    # Test cases written by Sai Krishna (km)
    # There is total 4 test cases for this user story where two test cases for good data and two for bad data
    # This test case will check length of expected and actual output
    # This test case will pass since assertEqual is used and both array has same length
    def test_us_18_same_length(self):
        us18Data = []
        self.assertEqual(len(us18Data), len(project_4_sprints.us_18_siblings_should_not_marry()), "This test case will pass since assertEqual method is used and both array has same length")

    # This test case will check content of expected and actual output by in order
    # This test case will pass since assertEqual is used to check content of both array and that content is same
    def test_us_18_same_content(self):
        us18Data = []
        data = project_4_sprints.us_18_siblings_should_not_marry()
        for index, value in enumerate(data):
            self.assertEqual(value, us18Data[index], "This test case will pass since assertEqual is used to check content of both array and that content is same")

    # This test case will check length of expected and actual output
    # This test case will pass since assertNotEqual method is used and both array has different length
    def test_us_18_different_length(self):
        us18Data = [
            "some random string to test this function"
        ]
        self.assertNotEqual(len(us18Data), len(project_4_sprints.us_18_siblings_should_not_marry()), "This test case will pass since assertNotEqual method is used and both array has different length")

    # This test case will check content of expected and actual output by in order
    # This test case will pass since assertNotEqual is used to check content of both array and that content is different
    def test_us_18_different_content(self):
        us18Data = [
            "some random string to test this function"
        ]
        data = project_4_sprints.us_18_siblings_should_not_marry()
        for index, value in enumerate(data):
            self.assertNotEqual(value, us18Data[index], "This test case will pass since assertNotEqual is used to check content of both array and that content is different")


    
    # Name:- AMBATI BABY NAGA SAHITHYA
    # CWID:- 20012050
    # Test case for us_22_unique_ids()
    # There is total 4 test cases for this user story where two test cases for good data and two for bad data
    # This test case will check length of expected and actual output
    # This test case will pass since assertEqual is used and both array has same length
    def test_us_22_same_length(self):
        us22Data = []
        self.assertEqual(len(us22Data), len(project_4_sprints.us_22_unique_ids()), "This test case will pass since assertEqual method is used and both array has same length")

    # This test case will check content of expected and actual output by in order
    # This test case will pass since assertEqual is used to check content of both array and that content is same
    def test_us_22_same_content(self):
        us22Data = []
        data = project_4_sprints.us_22_unique_ids()
        for index, value in enumerate(data):
            self.assertEqual(value, us22Data[index], "This test case will pass since assertEqual is used to check content of both array and that content is same")

    # This test case will check length of expected and actual output
    # This test case will pass since assertNotEqual method is used and both array has different length
    def test_us_22_different_length(self):
        us22Data = [
            "some random string to test this function"
        ]
        self.assertNotEqual(len(us22Data), len(project_4_sprints.us_22_unique_ids()), "This test case will pass since assertNotEqual method is used and both array has different length")

    # This test case will check content of expected and actual output by in order
    # This test case will pass since assertNotEqual is used to check content of both array and that content is different
    def test_us_22_different_content(self):
        us22Data = [
            "some random string to test this function"
        ]
        data = project_4_sprints.us_22_unique_ids()
        for index, value in enumerate(data):
            self.assertNotEqual(value, us22Data[index], "This test case will pass since assertNotEqual is used to check content of both array and that content is different")
    
    # Name:- AMBATI BABY NAGA SAHITHYA
    # CWID:- 20012050
    # Test case for us_23_unique_name_and_birth_date()
    # There is total 4 test cases for this user story where two test cases for good data and two for bad data
    # This test case will check length of expected and actual output
    # This test case will pass since assertEqual is used and both array has same length
    def test_us_23_same_length(self):
        us23Data = [
            "ERROR US23 INDIVIDUAL I6 is having duplicate record with same name John /Chapmen/ and same birthdate 1930-03-16",
            "ERROR US23 INDIVIDUAL I7 is having duplicate record with same name John /Chapmen/ and same birthdate 1930-03-16"
        ]
        self.assertEqual(len(us23Data), len(project_4_sprints.us_23_unique_name_and_birth_date()), "This test case will pass since assertEqual method is used and both array has same length")

    # This test case will check content of expected and actual output by in order
    # This test case will pass since assertEqual is used to check content of both array and that content is same
    def test_us_23_same_content(self):
        us23Data = [
            "ERROR US23 INDIVIDUAL I6 is having duplicate record with same name John /Chapmen/ and same birthdate 1930-03-16",
            "ERROR US23 INDIVIDUAL I7 is having duplicate record with same name John /Chapmen/ and same birthdate 1930-03-16"
        ]
        data = project_4_sprints.us_23_unique_name_and_birth_date()
        for index, value in enumerate(data):
            self.assertEqual(value, us23Data[index], "This test case will pass since assertEqual is used to check content of both array and that content is same")

    # This test case will check length of expected and actual output
    # This test case will pass since assertNotEqual method is used and both array has different length
    def test_us_23_different_length(self):
        us23Data = [
            "ERROR US23 INDIVIDUAL I6 is having duplicate record with same name John /Chapmen/ and same birthdate 1930-03-16",
            "ERROR US23 INDIVIDUAL I7 is having duplicate record with same name John /Chapmen/ and same birthdate 1930-03-16",
            "ERROR US23 INDIVIDUAL I6 is having duplicate record with same name John /Chapmen/ and same birthdate 1930-03-16",
            "ERROR US23 INDIVIDUAL I7 is having duplicate record with same name John /Chapmen/ and same birthdate 1930-03-16"
        ]
        self.assertNotEqual(len(us23Data), len(project_4_sprints.us_23_unique_name_and_birth_date()), "This test case will pass since assertNotEqual method is used and both array has different length")

    # This test case will check content of expected and actual output by in order
    # This test case will pass since assertNotEqual is used to check content of both array and that content is different
    def test_us_23_different_content(self):
        us23Data = [
            "ERROR US23 INDIVIDUAL I7 is having duplicate record with same name John /Chapmen/ and same birthdate 1930-03-16",
            "ERROR US23 INDIVIDUAL I6 is having duplicate record with same name John /Chapmen/ and same birthdate 1930-03-16",
        ]
        data = project_4_sprints.us_23_unique_name_and_birth_date()
        for index, value in enumerate(data):
            self.assertNotEqual(value, us23Data[index], "This test case will pass since assertNotEqual is used to check content of both array and that content is different")

            
    # Test case for US15 - Fewer than 15 siblings
    # Test cases written by Manoj Patel (mp)
    # There is total 4 test cases for this user story where two test cases for good data and two for bad data
    # This test case will check length of expected and actual output
    # This test case will pass since assertEqual method is used and both array has same length
    def test_us_15_same_length(self):
        us15Data = []
        self.assertEqual(len(us15Data), len(project_4_sprints.us_15_fewer_then_15_siblings()), "This test case will pass since assertEqual method is used and both array has same length")

    # This test case will check content of expected and actual output by in order
    # This test case will pass since assertEqual is used to check content of both array and that content is same
    def test_us_15_same_content(self):
        us15Data = []
        data = project_4_sprints.us_15_fewer_then_15_siblings()
        for index, value in enumerate(data):
            self.assertEqual(value, us15Data[index], "This test case will pass since assertEqual is used to check content of both array and that content is same")

    # This test case will check length of expected and actual output
    # This test case will pass since assertNotEqual method is used and both array has different length
    def test_us_15_different_length(self):
        us15Data = [
            "some random string to test this function"
        ]
        self.assertNotEqual(len(us15Data), len(project_4_sprints.us_15_fewer_then_15_siblings()), "This test case will pass since assertNotEqual method is used and both array has different length")

    # This test case will check content of expected and actual output by in order
    # This test case will pass since assertNotEqual is used to check content of both array and that content is different
    def test_us_15_different_content(self):
        us15Data = [
            "some random string to test this function"
        ]
        data = project_4_sprints.us_15_fewer_then_15_siblings()
        for index, value in enumerate(data):
            self.assertNotEqual(value, us15Data[index], "This test case will pass since assertNotEqual is used to check content of both array and that content is different")

    # Test case for US20 - Aunts and uncles
    # Test cases written by Manoj Patel (mp)
    # There is total 4 test cases for this user story where two test cases for good data and two for bad data
    # This test case will check length of expected and actual output
    # This test case will pass since assertEqual method is used and both array has same length
    def test_us_20_same_length(self):
        us20Data = [
            "ERROR US20 FAMILY F14 husband I24 is married to his aunt I22"
        ]
        self.assertEqual(len(us20Data), len(project_4_sprints.us_20_aunts_and_uncles()), "This test case will pass since assertEqual method is used and both array has same length")

    # This test case will check content of expected and actual output by in order
    # This test case will pass since assertEqual is used to check content of both array and that content is same
    def test_us_20_same_content(self):
        us20Data = [
            "ERROR US20 FAMILY F14 husband I24 is married to his aunt I22"
        ]
        data = project_4_sprints.us_20_aunts_and_uncles()
        for index, value in enumerate(data):
            self.assertEqual(value, us20Data[index], "This test case will pass since assertEqual is used to check content of both array and that content is same")

    # This test case will check length of expected and actual output
    # This test case will pass since assertNotEqual method is used and both array has different length
    def test_us_20_different_length(self):
        us20Data = [
            "ERROR US20 FAMILY F14 husband I24 is married to his aunt I22",
            "ERROR US20 FAMILY F14 husband I24 is married to his aunt I22"
        ]
        self.assertNotEqual(len(us20Data), len(project_4_sprints.us_20_aunts_and_uncles()), "This test case will pass since assertNotEqual method is used and both array has different length")

    # This test case will check content of expected and actual output by in order
    # This test case will pass since assertNotEqual is used to check content of both array and that content is different
    def test_us_20_different_content(self):
        us20Data = [
            "ERROR US20 FAMILY F18451044 husband I245213541 is married to his aunt I256512122"
        ]
        data = project_4_sprints.us_20_aunts_and_uncles()
        for index, value in enumerate(data):
            self.assertNotEqual(value, us20Data[index], "This test case will pass since assertNotEqual is used to check content of both array and that content is different")
    

    # Test case for US07 - Less then 150 years old
    # Test cases written by Parth Paghdal (pp)
    # There is total 4 test cases for this user story where two test cases for good data and two for bad data

    # This test case will check length of expected and actual output
    # This test case will pass since assertEqual is used and both array has same length
    def test_us_07_same_length(self):
        us07Data = []
        self.assertEqual(len(us07Data), len(project_4_sprints.us_07_less_than_150_years()), "This test case will pass since assertEqual method is used and both array has same length")

    # This test case will check content of expected and actual output by in order
    # This test case will pass since assertEqual is used to check content of both array and that content is same
    def test_us_07_same_content(self):
        us07Data = []
        data = project_4_sprints.us_07_less_than_150_years()
        for index, value in enumerate(data):
            self.assertEqual(value, us07Data[index], "This test case will pass since assertEqual is used to check content of both array and that content is same")

    # This test case will check length of expected and actual output
    # This test case will pass since assertNotEqual method is used and both array has different length
    def test_us_07_different_length(self):
        us07Data = ["Some random string to test this function"]
        self.assertNotEqual(len(us07Data), len(project_4_sprints.us_07_less_than_150_years()), "This test case will pass since assertNotEqual method is used and both array has different length")

    # This test case will check content of expected and actual output by in order
    # This test case will pass since assertNotEqual is used to check content of both array and that content is different
    def test_us_07_different_content(self):
        us07Data = ["Some random string to test this function"]
        data = project_4_sprints.us_07_less_than_150_years()
        for index, value in enumerate(data):
            self.assertNotEqual(value, us07Data[index], "This test case will pass since assertNotEqual is used to check content of both array and that content is different")

    # Test case for US21 - Correct gender for role
    # Test cases written by Parth Paghdal (pp)
    # There is total 4 test cases for this user story where two test cases for good data and two for bad data

    # This test case will check length of expected and actual output
    # This test case will pass since assertEqual is used and both array has same length
    def test_us_21_same_length(self):
        us21Data = ["ERROR: US21 FAMILY F3 is having incorrect gender role for wife with id I4 named Sebastian /Chapmen/"]
        self.assertEqual(len(us21Data), len(project_4_sprints.us_21_correct_gender_for_role()), "This test case will pass since assertEqual method is used and both array has same length")

    # This test case will check content of expected and actual output by in order
    # This test case will pass since assertEqual is used to check content of both array and that content is same
    def test_us_21_same_content(self):
        us21Data = ["ERROR: US21 FAMILY F3 is having incorrect gender role for wife with id I4 named Sebastian /Chapmen/"]
        data = project_4_sprints.us_21_correct_gender_for_role()
        for index, value in enumerate(data):
            self.assertEqual(value, us21Data[index], "This test case will pass since assertEqual is used to check content of both array and that content is same")

    # This test case will check length of expected and actual output
    # This test case will pass since assertNotEqual method is used and both array has different length
    def test_us_21_different_length(self):
        us21Data = [
            "ERROR: US21 FAMILY F3 is having incorrect gender role for wife with id I4 named Sebastian /Chapmen/",
            "Some random string to test this function"
            ]
        self.assertNotEqual(len(us21Data), len(project_4_sprints.us_21_correct_gender_for_role()), "This test case will pass since assertNotEqual method is used and both array has different length")

    # This test case will check content of expected and actual output by in order
    # This test case will pass since assertNotEqual is used to check content of both array and that content is different
    def test_us_21_different_content(self):
        us21Data = [
            "Some random string to test this function",
            "ERROR: US21 FAMILY F3 is having incorrect gender role for wife with id I4 named Sebastian /Chapmen/"
        ]
        data = project_4_sprints.us_21_correct_gender_for_role()
        for index, value in enumerate(data):
            self.assertNotEqual(value, us21Data[index], "This test case will pass since assertNotEqual is used to check content of both array and that content is different")

     # Test case for US24 - Unique families by spouses
    # Test cases written by Sai Krishna (km) and Parth Paghdal (pp)
    # This test case are written using pair programming
    # There is total 4 test cases for this user story where two test cases for good data and two for bad data

    # This test case will check length of expected and actual output
    # This test case will pass since assertEqual is used and both array has same length
    def test_us_24_same_length(self):
        us24Data = []
        self.assertEqual(len(us24Data), len(project_4_sprints.us_24_unique_families_by_spouces()), "This test case will pass since assertEqual method is used and both array has same length")

    # This test case will check content of expected and actual output by in order
    # This test case will pass since assertEqual is used to check content of both array and that content is same
    def test_us_24_same_content(self):
        us24Data = []
        data = project_4_sprints.us_24_unique_families_by_spouces()
        for index, value in enumerate(data):
            self.assertEqual(value, us24Data[index], "This test case will pass since assertEqual is used to check content of both array and that content is same")

    # This test case will check length of expected and actual output
    # This test case will pass since assertNotEqual is used and both array has different length
    def test_us_24_different_length(self):
        us24Data = ["Some random string to test this function"]
        self.assertNotEqual(len(us24Data), len(project_4_sprints.us_24_unique_families_by_spouces()), "This test case will pass since assertNotEqual is used and both array has different length")


    # This test case will check content of expected and actual output by in order
    # This test case will pass since assertNotEqual is used to check content both array and that content is different
    def test_us_24_different_content(self):
        us24Data = ["Some random string to test this function"]
        data = project_4_sprints.us_24_unique_families_by_spouces()
        for index, value in enumerate(data):
            self.assertNotEqual(value, us24Data[index], "This test case will pass since assertNotEqual is used to check content of both array and that content is different")

    # Test case for US27 - Include individual ages
    # Test cases written by Sai Krishna (km)
    # There is total 4 test cases for this user story where two test cases for good data and two for bad data
    # This test case will check length of expected and actual output
    # This test case will pass since assertEqual is used and both array has same length
    def test_us_27_same_length(self):
        us27Data = [
            "ERROR: US27 INDIVIDUAL I1 named Edward /Chapmen/ is 99 years old.",
            "ERROR: US27 INDIVIDUAL I2 named Wanda /Chapmen/ is 94 years old.",
            "ERROR: US27 INDIVIDUAL I3 named Sam /Chapmen/ is 85 years old.",
            "ERROR: US27 INDIVIDUAL I4 named Sebastian /Chapmen/ is 93 years old.",
            "ERROR: US27 INDIVIDUAL I5 named Dominic /Chapmen/ is 93 years old.",
            "ERROR: US27 INDIVIDUAL I6 named John /Chapmen/ is 81 years old.",
            "ERROR: US27 INDIVIDUAL I7 named John /Chapmen/ is 0 years old.",
            "ERROR: US27 INDIVIDUAL I8 named Adrian /Chapmen/ is -4 years old.",
            "ERROR: US27 INDIVIDUAL I9 named Karen /Chapmen/ is 60 years old.",
            "ERROR: US27 INDIVIDUAL I10 named Joanne /Chapmen/ is 92 years old.",
            "ERROR: US27 INDIVIDUAL I11 named Carol /Chapmen/ is 83 years old.",
            "ERROR: US27 INDIVIDUAL I12 named Leah /Chapmen/ is 94 years old.",
            "ERROR: US27 INDIVIDUAL I13 named Maria /Chapmen/ is 70 years old.",
            "ERROR: US27 INDIVIDUAL I14 named Jennifer /Chapmen/ is 92 years old.",
            "ERROR: US27 INDIVIDUAL I15 named Neil /Chapmen/ is 65 years old.",
            "ERROR: US27 INDIVIDUAL I16 named Sam /Chapmen/ is 69 years old.",
            "ERROR: US27 INDIVIDUAL I17 named Victoria /Chapmen/ is 63 years old.",
            "ERROR: US27 INDIVIDUAL I18 named Abigail /Black/ is 63 years old.",
            "ERROR: US27 INDIVIDUAL I19 named Felicity /Chapmen/ is 62 years old.",
            "ERROR: US27 INDIVIDUAL I20 named Benjamin /Chapmen/ is 80 years old.",
            "ERROR: US27 INDIVIDUAL I21 named Boris /Chapmen/ is 76 years old.",
            "ERROR: US27 INDIVIDUAL I22 named Kimberely /Chapmen/ is 11 years old.",
            "ERROR: US27 INDIVIDUAL I23 named Nicola /Chapmen/ is 77 years old.",
            "ERROR: US27 INDIVIDUAL I24 named Andrew /Chapmen/ is 52 years old.",
            "ERROR: US27 INDIVIDUAL I25 named Penelope /Chapmen/ is 75 years old.",
            "ERROR: US27 INDIVIDUAL I26 named Sonia /Chapmen/ is 47 years old.",
        ]
        self.assertEqual(len(us27Data), len(project_4_sprints.us_27_include_individual_ages()), "This test case will pass since assertEqual method is used and both array has same length")

    # This test case will check content of expected and actual output by in order
    # This test case will pass since assertEqual is used to check content of both array and that content is same
    def test_us_27_same_content(self):
        us27Data = [
            "ERROR: US27 INDIVIDUAL I1 named Edward /Chapmen/ is 99 years old.",
            "ERROR: US27 INDIVIDUAL I2 named Wanda /Chapmen/ is 94 years old.",
            "ERROR: US27 INDIVIDUAL I3 named Sam /Chapmen/ is 85 years old.",
            "ERROR: US27 INDIVIDUAL I4 named Sebastian /Chapmen/ is 93 years old.",
            "ERROR: US27 INDIVIDUAL I5 named Dominic /Chapmen/ is 93 years old.",
            "ERROR: US27 INDIVIDUAL I6 named John /Chapmen/ is 81 years old.",
            "ERROR: US27 INDIVIDUAL I7 named John /Chapmen/ is 0 years old.",
            "ERROR: US27 INDIVIDUAL I8 named Adrian /Chapmen/ is -4 years old.",
            "ERROR: US27 INDIVIDUAL I9 named Karen /Chapmen/ is 60 years old.",
            "ERROR: US27 INDIVIDUAL I10 named Joanne /Chapmen/ is 92 years old.",
            "ERROR: US27 INDIVIDUAL I11 named Carol /Chapmen/ is 83 years old.",
            "ERROR: US27 INDIVIDUAL I12 named Leah /Chapmen/ is 94 years old.",
            "ERROR: US27 INDIVIDUAL I13 named Maria /Chapmen/ is 70 years old.",
            "ERROR: US27 INDIVIDUAL I14 named Jennifer /Chapmen/ is 92 years old.",
            "ERROR: US27 INDIVIDUAL I15 named Neil /Chapmen/ is 65 years old.",
            "ERROR: US27 INDIVIDUAL I16 named Sam /Chapmen/ is 69 years old.",
            "ERROR: US27 INDIVIDUAL I17 named Victoria /Chapmen/ is 63 years old.",
            "ERROR: US27 INDIVIDUAL I18 named Abigail /Black/ is 63 years old.",
            "ERROR: US27 INDIVIDUAL I19 named Felicity /Chapmen/ is 62 years old.",
            "ERROR: US27 INDIVIDUAL I20 named Benjamin /Chapmen/ is 80 years old.",
            "ERROR: US27 INDIVIDUAL I21 named Boris /Chapmen/ is 76 years old.",
            "ERROR: US27 INDIVIDUAL I22 named Kimberely /Chapmen/ is 11 years old.",
            "ERROR: US27 INDIVIDUAL I23 named Nicola /Chapmen/ is 77 years old.",
            "ERROR: US27 INDIVIDUAL I24 named Andrew /Chapmen/ is 52 years old.",
            "ERROR: US27 INDIVIDUAL I25 named Penelope /Chapmen/ is 75 years old.",
            "ERROR: US27 INDIVIDUAL I26 named Sonia /Chapmen/ is 47 years old.",
        ]
        data = project_4_sprints.us_27_include_individual_ages()
        for index, value in enumerate(data):
            self.assertEqual(value, us27Data[index], "This test case will pass since assertEqual is used to check content of both array and that content is same")

    # This test case will check length of expected and actual output
    # This test case will pass since assertNotEqual method is used and both array has different length
    def test_us_27_different_length(self):
        us27Data = [
            "some random string to test this function"
        ]
        self.assertNotEqual(len(us27Data), len(project_4_sprints.us_27_include_individual_ages()), "This test case will pass since assertNotEqual method is used and both array has different length")

    # This test case will check content of expected and actual output by in order
    # This test case will pass since assertNotEqual is used to check content of both array and that content is different
    def test_us_27_different_content(self):
        us27Data = [
            "ERROR: US27 INDIVIDUAL I26 named Sonia /Chapmen/ is 47 years old.",
            "ERROR: US27 INDIVIDUAL I1 named Edward /Chapmen/ is 99 years old.",
            "ERROR: US27 INDIVIDUAL I2 named Wanda /Chapmen/ is 94 years old.",
            "ERROR: US27 INDIVIDUAL I3 named Sam /Chapmen/ is 85 years old.",
            "ERROR: US27 INDIVIDUAL I4 named Sebastian /Chapmen/ is 93 years old.",
            "ERROR: US27 INDIVIDUAL I5 named Dominic /Chapmen/ is 93 years old.",
            "ERROR: US27 INDIVIDUAL I6 named John /Chapmen/ is 81 years old.",
            "ERROR: US27 INDIVIDUAL I7 named John /Chapmen/ is 0 years old.",
            "ERROR: US27 INDIVIDUAL I8 named Adrian /Chapmen/ is -4 years old.",
            "ERROR: US27 INDIVIDUAL I9 named Karen /Chapmen/ is 60 years old.",
            "ERROR: US27 INDIVIDUAL I10 named Joanne /Chapmen/ is 92 years old.",
            "ERROR: US27 INDIVIDUAL I11 named Carol /Chapmen/ is 83 years old.",
            "ERROR: US27 INDIVIDUAL I12 named Leah /Chapmen/ is 94 years old.",
            "ERROR: US27 INDIVIDUAL I13 named Maria /Chapmen/ is 70 years old.",
            "ERROR: US27 INDIVIDUAL I14 named Jennifer /Chapmen/ is 92 years old.",
            "ERROR: US27 INDIVIDUAL I15 named Neil /Chapmen/ is 65 years old.",
            "ERROR: US27 INDIVIDUAL I16 named Sam /Chapmen/ is 69 years old.",
            "ERROR: US27 INDIVIDUAL I17 named Victoria /Chapmen/ is 63 years old.",
            "ERROR: US27 INDIVIDUAL I18 named Abigail /Black/ is 63 years old.",
            "ERROR: US27 INDIVIDUAL I19 named Felicity /Chapmen/ is 62 years old.",
            "ERROR: US27 INDIVIDUAL I20 named Benjamin /Chapmen/ is 80 years old.",
            "ERROR: US27 INDIVIDUAL I21 named Boris /Chapmen/ is 76 years old.",
            "ERROR: US27 INDIVIDUAL I22 named Kimberely /Chapmen/ is 11 years old.",
            "ERROR: US27 INDIVIDUAL I23 named Nicola /Chapmen/ is 77 years old.",
            "ERROR: US27 INDIVIDUAL I24 named Andrew /Chapmen/ is 52 years old.",
            "ERROR: US27 INDIVIDUAL I25 named Penelope /Chapmen/ is 75 years old."
        ]
        data = project_4_sprints.us_27_include_individual_ages()
        for index, value in enumerate(data):
            self.assertNotEqual(value, us27Data[index], "This test case will pass since assertNotEqual is used to check content of both array and that content is different")
  # Test case for US36 - List recent deaths
    # Test cases written by Manoj Patel (mp)
    # There is total 4 test cases for this user story where two test cases for good data and two for bad data
    # This test case will check length of expected and actual output
    # This test case will pass since assertEqual method is used and both array has same length
    def test_us_36_same_length(self):
        us36Data = []
        self.assertEqual(len(us36Data), len(project_4_sprints.us_36_list_recent_deaths()), "This test case will pass since assertEqual method is used and both array has same length")

    # This test case will check content of expected and actual output by in order
    # This test case will pass since assertEqual is used to check content of both array and that content is same
    def test_us_36_same_content(self):
        us36Data = []
        data = project_4_sprints.us_36_list_recent_deaths()
        for index, value in enumerate(data):
            self.assertEqual(value, us36Data[index], "This test case will pass since assertEqual is used to check content of both array and that content is same")

    # This test case will check length of expected and actual output
    # This test case will pass since assertNotEqual method is used and both array has different length
    def test_us_36_different_length(self):
        us36Data = ["Some random string to test this function"]
        self.assertNotEqual(len(us36Data), len(project_4_sprints.us_36_list_recent_deaths()), "This test case will pass since assertNotEqual method is used and both array has different length")

    # This test case will check content of expected and actual output by in order
    # This test case will pass since assertNotEqual is used to check content of both array and that content is different
    def test_us_36_different_content(self):
        us36Data = ["Some random string to test this function"]
        data = project_4_sprints.us_36_list_recent_deaths()
        for index, value in enumerate(data):
            self.assertNotEqual(value, us36Data[index], "This test case will pass since assertNotEqual is used to check content of both array and that content is different")

    # Test case for US38 - List upcoming birthdays
    # Test cases written by Manoj Patel (mp)
    # There is total 4 test cases for this user story where two test cases for good data and two for bad data
    # This test case will check length of expected and actual output
    # This test case will pass since assertEqual method is used and both array has same length
    def test_us_38_same_length(self):
        us38Data = []
        self.assertEqual(len(us38Data), len(project_4_sprints.us_38_list_upcoming_birthdays()), "This test case will pass since assertEqual method is used and both array has same length")

    # This test case will check content of expected and actual output by in order
    # This test case will pass since assertEqual is used to check content of both array and that content is same
    def test_us_38_same_content(self):
        us38Data = []
        data = project_4_sprints.us_38_list_upcoming_birthdays()
        for index, value in enumerate(data):
            self.assertEqual(value, us38Data[index], "This test case will pass since assertEqual is used to check content of both array and that content is same")

    # This test case will check length of expected and actual output
    # This test case will pass since assertNotEqual method is used and both array has different length
    def test_us_38_different_length(self):
        us38Data = ["Some random string to test this function"]
        self.assertNotEqual(len(us38Data), len(project_4_sprints.us_38_list_upcoming_birthdays()), "This test case will pass since assertNotEqual method is used and both array has different length")

    # This test case will check content of expected and actual output by in order
    # This test case will pass since assertNotEqual is used to check content of both array and that content is different
    def test_us_38_different_content(self):
        us38Data = ["Some random string to test this function"]
        data = project_4_sprints.us_38_list_upcoming_birthdays()
        for index, value in enumerate(data):
            self.assertNotEqual(value, us38Data[index], "This test case will pass since assertNotEqual is used to check content of both array and that content is different")
           
if __name__ == '__main__':
    unittest.main()
    
    # Name:- AMBATI BABY NAGA SAHITHYA
    # CWID:- 20012050
    # Test case for us_32_list_multiple_births()
    # There is total 4 test cases for this user story where two test cases for good data and two for bad data
    # This test case will check length of expected and actual output
    # This test case will pass since assertEqual is used and both array has same length
    def test_us_32_same_length(self):
        us32Data = [
            "ERROR: US32 INDIVIDUAL I1 named Edward /Chapmen/ born on 1910-08-15",
            "ERROR: US32 INDIVIDUAL I2 named Wanda /Chapmen/ born on 1911-02-16",
            "ERROR: US32 INDIVIDUAL I3 named Sam /Chapmen/ born on 1930-03-16",
            "ERROR: US32 INDIVIDUAL I4 named Sebastian /Chapmen/ born on 1930-03-16",
            "ERROR: US32 INDIVIDUAL I5 named Dominic /Chapmen/ born on 1930-03-16",
            "ERROR: US32 INDIVIDUAL I6 named John /Chapmen/ born on 1930-03-16",
            "ERROR: US32 INDIVIDUAL I7 named John /Chapmen/ born on 1930-03-16",
            "ERROR: US32 INDIVIDUAL I8 named Adrian /Chapmen/ born on 1930-03-16",
            "ERROR: US32 INDIVIDUAL I9 named Karen /Chapmen/ born on 1929-06-17",
            "ERROR: US32 INDIVIDUAL I10 named Joanne /Chapmen/ born on 1931-02-17",
            "ERROR: US32 INDIVIDUAL I11 named Carol /Chapmen/ born on 1932-08-23",
            "ERROR: US32 INDIVIDUAL I12 named Leah /Chapmen/ born on 1928-05-13",
            "ERROR: US32 INDIVIDUAL I13 named Maria /Chapmen/ born on 1928-08-15",
            "ERROR: US32 INDIVIDUAL I14 named Jennifer /Chapmen/ born on 1930-06-14",
            "ERROR: US32 INDIVIDUAL I15 named Neil /Chapmen/ born on 1957-12-25",
            "ERROR: US32 INDIVIDUAL I16 named Sam /Chapmen/ born on 1953-11-29",
            "ERROR: US32 INDIVIDUAL I17 named Victoria /Chapmen/ born on 1959-09-29",
            "ERROR: US32 INDIVIDUAL I18 named Abigail /Black/ born on 1959-04-19",
            "ERROR: US32 INDIVIDUAL I19 named Felicity /Chapmen/ born on 1960-08-18",
            "ERROR: US32 INDIVIDUAL I20 named Benjamin /Chapmen/ born on 1943-01-12",
            "ERROR: US32 INDIVIDUAL I21 named Boris /Chapmen/ born on 1946-05-29",
            "ERROR: US32 INDIVIDUAL I22 named Kimberely /Chapmen/ born on 2011-08-16",
            "ERROR: US32 INDIVIDUAL I23 named Nicola /Chapmen/ born on 1945-04-14",
            "ERROR: US32 INDIVIDUAL I24 named Andrew /Chapmen/ born on 1970-05-15",
            "ERROR: US32 INDIVIDUAL I25 named Penelope /Chapmen/ born on 1947-09-16",
            "ERROR: US32 INDIVIDUAL I26 named Sonia /Chapmen/ born on 1975-06-17",
        ]
        self.assertEqual(len(us32Data), len(project_4_sprints.us_32_list_multiple_births()), "This test case will pass since assertEqual method is used and both array has same length")

    # This test case will check content of expected and actual output by in order
    # This test case will pass since assertEqual is used to check content of both array and that content is same
    def test_us_32_same_content(self):
        us32Data = [
            "ERROR: US32 INDIVIDUAL I1 named Edward /Chapmen/ born on 1910-08-15",
            "ERROR: US32 INDIVIDUAL I2 named Wanda /Chapmen/ born on 1911-02-16",
            "ERROR: US32 INDIVIDUAL I3 named Sam /Chapmen/ born on 1930-03-16",
            "ERROR: US32 INDIVIDUAL I4 named Sebastian /Chapmen/ born on 1930-03-16",
            "ERROR: US32 INDIVIDUAL I5 named Dominic /Chapmen/ born on 1930-03-16",
            "ERROR: US32 INDIVIDUAL I6 named John /Chapmen/ born on 1930-03-16",
            "ERROR: US32 INDIVIDUAL I7 named John /Chapmen/ born on 1930-03-16",
            "ERROR: US32 INDIVIDUAL I8 named Adrian /Chapmen/ born on 1930-03-16",
            "ERROR: US32 INDIVIDUAL I9 named Karen /Chapmen/ born on 1929-06-17",
            "ERROR: US32 INDIVIDUAL I10 named Joanne /Chapmen/ born on 1931-02-17",
            "ERROR: US32 INDIVIDUAL I11 named Carol /Chapmen/ born on 1932-08-23",
            "ERROR: US32 INDIVIDUAL I12 named Leah /Chapmen/ born on 1928-05-13",
            "ERROR: US32 INDIVIDUAL I13 named Maria /Chapmen/ born on 1928-08-15",
            "ERROR: US32 INDIVIDUAL I14 named Jennifer /Chapmen/ born on 1930-06-14",
            "ERROR: US32 INDIVIDUAL I15 named Neil /Chapmen/ born on 1957-12-25",
            "ERROR: US32 INDIVIDUAL I16 named Sam /Chapmen/ born on 1953-11-29",
            "ERROR: US32 INDIVIDUAL I17 named Victoria /Chapmen/ born on 1959-09-29",
            "ERROR: US32 INDIVIDUAL I18 named Abigail /Black/ born on 1959-04-19",
            "ERROR: US32 INDIVIDUAL I19 named Felicity /Chapmen/ born on 1960-08-18",
            "ERROR: US32 INDIVIDUAL I20 named Benjamin /Chapmen/ born on 1943-01-12",
            "ERROR: US32 INDIVIDUAL I21 named Boris /Chapmen/ born on 1946-05-29",
            "ERROR: US32 INDIVIDUAL I22 named Kimberely /Chapmen/ born on 2011-08-16",
            "ERROR: US32 INDIVIDUAL I23 named Nicola /Chapmen/ born on 1945-04-14",
            "ERROR: US32 INDIVIDUAL I24 named Andrew /Chapmen/ born on 1970-05-15",
            "ERROR: US32 INDIVIDUAL I25 named Penelope /Chapmen/ born on 1947-09-16",
            "ERROR: US32 INDIVIDUAL I26 named Sonia /Chapmen/ born on 1975-06-17",
        ]
        data = project_4_sprints.us_32_list_multiple_births()
        for index, value in enumerate(data):
            self.assertEqual(value, us32Data[index], "This test case will pass since assertEqual is used to check content of both array and that content is same")

    # This test case will check length of expected and actual output
    # This test case will pass since assertNotEqual method is used and both array has different length
    def test_us_32_different_length(self):
        us32Data = [
            "Some random string to test this function.",
            "ERROR: US32 INDIVIDUAL I1 named Edward /Chapmen/ born on 1910-08-15",
            "ERROR: US32 INDIVIDUAL I2 named Wanda /Chapmen/ born on 1911-02-16",
            "ERROR: US32 INDIVIDUAL I3 named Sam /Chapmen/ born on 1930-03-16",
            "ERROR: US32 INDIVIDUAL I4 named Sebastian /Chapmen/ born on 1930-03-16",
            "ERROR: US32 INDIVIDUAL I5 named Dominic /Chapmen/ born on 1930-03-16",
            "ERROR: US32 INDIVIDUAL I6 named John /Chapmen/ born on 1930-03-16",
            "ERROR: US32 INDIVIDUAL I7 named John /Chapmen/ born on 1930-03-16",
            "ERROR: US32 INDIVIDUAL I8 named Adrian /Chapmen/ born on 1930-03-16",
            "ERROR: US32 INDIVIDUAL I9 named Karen /Chapmen/ born on 1929-06-17",
            "ERROR: US32 INDIVIDUAL I10 named Joanne /Chapmen/ born on 1931-02-17",
            "ERROR: US32 INDIVIDUAL I11 named Carol /Chapmen/ born on 1932-08-23",
            "ERROR: US32 INDIVIDUAL I12 named Leah /Chapmen/ born on 1928-05-13",
            "ERROR: US32 INDIVIDUAL I13 named Maria /Chapmen/ born on 1928-08-15",
            "ERROR: US32 INDIVIDUAL I14 named Jennifer /Chapmen/ born on 1930-06-14",
            "ERROR: US32 INDIVIDUAL I15 named Neil /Chapmen/ born on 1957-12-25",
            "ERROR: US32 INDIVIDUAL I16 named Sam /Chapmen/ born on 1953-11-29",
            "ERROR: US32 INDIVIDUAL I17 named Victoria /Chapmen/ born on 1959-09-29",
            "ERROR: US32 INDIVIDUAL I18 named Abigail /Black/ born on 1959-04-19",
            "ERROR: US32 INDIVIDUAL I19 named Felicity /Chapmen/ born on 1960-08-18",
            "ERROR: US32 INDIVIDUAL I20 named Benjamin /Chapmen/ born on 1943-01-12",
            "ERROR: US32 INDIVIDUAL I21 named Boris /Chapmen/ born on 1946-05-29",
            "ERROR: US32 INDIVIDUAL I22 named Kimberely /Chapmen/ born on 2011-08-16",
            "ERROR: US32 INDIVIDUAL I23 named Nicola /Chapmen/ born on 1945-04-14",
            "ERROR: US32 INDIVIDUAL I24 named Andrew /Chapmen/ born on 1970-05-15",
            "ERROR: US32 INDIVIDUAL I25 named Penelope /Chapmen/ born on 1947-09-16",
            "ERROR: US32 INDIVIDUAL I26 named Sonia /Chapmen/ born on 1975-06-17",
        ]

        self.assertNotEqual(len(us32Data), len(project_4_sprints.us_32_list_multiple_births()), "This test case will pass since assertNotEqual method is used and both array has different length")

    # This test case will check content of expected and actual output by in order
    # This test case will pass since assertNotEqual is used to check content of both array and that content is different
    def test_us_32_different_content(self):
        us32Data = [
            "ERROR: US32 INDIVIDUAL I26 named Sonia /Chapmen/ born on 1975-06-17",
            "ERROR: US32 INDIVIDUAL I1 named Edward /Chapmen/ born on 1910-08-15",
            "ERROR: US32 INDIVIDUAL I2 named Wanda /Chapmen/ born on 1911-02-16",
            "ERROR: US32 INDIVIDUAL I3 named Sam /Chapmen/ born on 1930-03-16",
            "ERROR: US32 INDIVIDUAL I4 named Sebastian /Chapmen/ born on 1930-03-16",
            "ERROR: US32 INDIVIDUAL I5 named Dominic /Chapmen/ born on 1930-03-16",
            "ERROR: US32 INDIVIDUAL I6 named John /Chapmen/ born on 1930-03-16",
            "ERROR: US32 INDIVIDUAL I7 named John /Chapmen/ born on 1930-03-16",
            "ERROR: US32 INDIVIDUAL I8 named Adrian /Chapmen/ born on 1930-03-16",
            "ERROR: US32 INDIVIDUAL I9 named Karen /Chapmen/ born on 1929-06-17",
            "ERROR: US32 INDIVIDUAL I10 named Joanne /Chapmen/ born on 1931-02-17",
            "ERROR: US32 INDIVIDUAL I11 named Carol /Chapmen/ born on 1932-08-23",
            "ERROR: US32 INDIVIDUAL I12 named Leah /Chapmen/ born on 1928-05-13",
            "ERROR: US32 INDIVIDUAL I13 named Maria /Chapmen/ born on 1928-08-15",
            "ERROR: US32 INDIVIDUAL I14 named Jennifer /Chapmen/ born on 1930-06-14",
            "ERROR: US32 INDIVIDUAL I15 named Neil /Chapmen/ born on 1957-12-25",
            "ERROR: US32 INDIVIDUAL I16 named Sam /Chapmen/ born on 1953-11-29",
            "ERROR: US32 INDIVIDUAL I17 named Victoria /Chapmen/ born on 1959-09-29",
            "ERROR: US32 INDIVIDUAL I18 named Abigail /Black/ born on 1959-04-19",
            "ERROR: US32 INDIVIDUAL I19 named Felicity /Chapmen/ born on 1960-08-18",
            "ERROR: US32 INDIVIDUAL I20 named Benjamin /Chapmen/ born on 1943-01-12",
            "ERROR: US32 INDIVIDUAL I21 named Boris /Chapmen/ born on 1946-05-29",
            "ERROR: US32 INDIVIDUAL I22 named Kimberely /Chapmen/ born on 2011-08-16",
            "ERROR: US32 INDIVIDUAL I23 named Nicola /Chapmen/ born on 1945-04-14",
            "ERROR: US32 INDIVIDUAL I24 named Andrew /Chapmen/ born on 1970-05-15",
            "ERROR: US32 INDIVIDUAL I25 named Penelope /Chapmen/ born on 1947-09-16"
        ]

        data = project_4_sprints.us_32_list_multiple_births()
        for index, value in enumerate(data):
            self.assertNotEqual(value, us32Data[index], "This test case will pass since assertNotEqual is used to check content of both array and that content is different")

    # Name:- AMBATI BABY NAGA SAHITHYA
    # CWID:- 20012050
    # Test case for us_35_list_recent_births()
    # There is total 4 test cases for this user story where two test cases for good data and two for bad data
    # This test case will check length of expected and actual output
    # This test case will pass since assertEqual method is used and both array has same length
    def test_us_35_same_length(self):
        us35Data = []
        self.assertEqual(len(us35Data), len(project_4_sprints.us_35_list_recent_births()), "This test case will pass since assertEqual method is used and both array has same length")

    # This test case will check content of expected and actual output by in order
    # This test case will pass since assertEqual is used to check content of both array and that content is same
    def test_us_35_same_content(self):
        us35Data = []
        data = project_4_sprints.us_35_list_recent_births()
        for index, value in enumerate(data):
            self.assertEqual(value, us35Data[index], "This test case will pass since assertEqual is used to check content of both array and that content is same")

    # This test case will check length of expected and actual output
    # This test case will pass since assertNotEqual method is used and both array has different length
    def test_us_35_different_length(self):
        us35Data = ["Some random string to test this function"]
        self.assertNotEqual(len(us35Data), len(project_4_sprints.us_35_list_recent_births()), "This test case will pass since assertNotEqual method is used and both array has different length")

    # This test case will check content of expected and actual output by in order
    # This test case will pass since assertNotEqual is used to check content of both array and that content is different
    def test_us_35_different_content(self):
        us35Data = ["Some random string to test this function"]
        data = project_4_sprints.us_35_list_recent_births()
        for index, value in enumerate(data):
            self.assertNotEqual(value, us35Data[index], "This test case will pass since assertNotEqual is used to check content of both array and that content is different")

if __name__ == '__main__':
    unittest.main()



