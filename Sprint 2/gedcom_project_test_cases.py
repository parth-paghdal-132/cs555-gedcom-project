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
        self.assertNotEqual(len(project_4_sprints.us_29_List_deceased()), len(us29Data),
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
        data = project_4_sprints.us_29_List_deceased()
        for index, value in enumerate(data):
            self.assertEqual(value, data[index],
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
        self.assertNotEqual(len(project_4_sprints.us_29_List_deceased()),len(us29Data),"This test case will pass since assertNotEqual is used and both arrays have different length")

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
        data = project_4_sprints.us_29_List_deceased()
        for index, value in enumerate(data):
            self.assertEqual(value, data[index],
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
            "ERROR: US12 Family: F1 father named: Edward /Chapmen/ and age:99 more than 80 year than his child named: John /Chapmen/ with age 0",
            "ERROR: US12 Family: F1 father named: Edward /Chapmen/ and age:99 more than 80 year than his child named: Adrian /Chapmen/ with age -4",
            "ERROR: US12 Family: F3 father named: Joanne /Chapmen/ and age:92 more than 80 year than his child named: Kimberely /Chapmen/ with age 11"
        ]
        self.assertEqual(len(us12Data), len(project_4_sprints.us12_parents_not_too_old()), "This test case will pass since assertEqual method is used and both array has same length")

    # This test case will check content of expected and actual output by in order
    # This test case will pass since assertEqual is used to check content of both array and that content is same
    def test_us_12_same_content(self):
        us12Data = [
            "ERROR: US12 Family: F1 father named: Edward /Chapmen/ and age:99 more than 80 year than his child named: John /Chapmen/ with age 0",
            "ERROR: US12 Family: F1 father named: Edward /Chapmen/ and age:99 more than 80 year than his child named: Adrian /Chapmen/ with age -4",
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
            "ERROR: US12 Family: F3 father named: Joanne /Chapmen/ and age:92 more than 80 year than his child named: Kimberely /Chapmen/ with age 11",
            "ERROR: US12 Family: F1 father named: Edward /Chapmen/ and age:99 more than 80 year than his child named: John /Chapmen/ with age 0",
            "ERROR: US12 Family: F1 father named: Edward /Chapmen/ and age:99 more than 80 year than his child named: Adrian /Chapmen/ with age -4"
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


            
            
       
    

if __name__ == '__main__':
    unittest.main()

