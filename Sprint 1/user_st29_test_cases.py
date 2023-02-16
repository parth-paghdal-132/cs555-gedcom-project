# Name:- SAI KRISHNA MIRIYALA
#CWID:- 20010913
import unittest2
import user_st1


class TestListdeceased(unittest2.TestCase):

    # This test case will check the length of the expected and actual output
    # This test case will pass since assertEqual is used and both arrays have the same length
    def test_us_29_same_length(self):
        us29Data = [
           "Error Individual List Deceased us29:name:Edward Chapmen",
           "Error Individual List Deceased us29:name:Wanda Chapmen",
           "Error Individual List Deceased us29:name:Sam Chapmen",
           "Error Individual List Deceased us29:name:John Chapmen",
           "Error Individual List Deceased us29:name:John Chapmen",
           "Error Individual List Deceased us29:name:Adrian Chapmen",
           "Error Individual List Deceased us29:name:Karen Chapmen",
           "Error Individual List Deceased us29:name:Carol Chapmen",
           "Error Individual List Deceased us29:name:Maria Chapmen"
        ]
        self.assertEqual(len(user_st1.us_29_List_deceased()), len(us29Data),
                         "This test case will pass since assertEqual method is used and both arrays have the same length")

    # This test case will check the content of the expected and actual output by order
    # This test case will pass since assertEqual is used to check content of both arrays and that content is the same
    def test_us_29_same_content(self):
        us29Data = [
            "Error Individual List Deceased us29:name:Edward Chapmen",
           "Error Individual List Deceased us29:name:Wanda Chapmen",
           "Error Individual List Deceased us29:name:Sam Chapmen",
           "Error Individual List Deceased us29:name:John Chapmen",
           "Error Individual List Deceased us29:name:John Chapmen",
           "Error Individual List Deceased us29:name:Adrian Chapmen",
           "Error Individual List Deceased us29:name:Karen Chapmen",
           "Error Individual List Deceased us29:name:Carol Chapmen",
           "Error Individual List Deceased us29:name:Maria Chapmen"
        ]
        data = user_st1.us_29_List_deceased()
        for index, value in enumerate(data):
            self.assertEqual(value, us29Data[index],
                             "This test case will pass since assertEqual is used to check content of both arrays and that content is the same")

    # This test case will check the length of the expected and actual output
    # This test case will pass since assertNotEqual is used and both arrays have different length
    def test_us_29_different_length(self):
        us29Data = [
            "Error Individual List Deceased us29:name:Edward Chapmen",
           "Error Individual List Deceased us29:name:Wanda Chapmen",
           "Error Individual List Deceased us29:name:Sam Chapmen",
           "Error Individual List Deceased us29:name:John Chapmen",
           "Error Individual List Deceased us29:name:John Chapmen",
           "Error Individual List Deceased us29:name:Adrian Chapmen",
           "Error Individual List Deceased us29:name:Karen Chapmen",
           "Error Individual List Deceased us29:name:Carol Chapmen",
           "Error Individual List Deceased us29:name:Maria Chapmen"
        ]
        self.assertNotEqual(len(user_st1.us_29_List_deceased(),len(us29Data),"This test case will pass since assertNotEqual is used and both arrays have different length"))

    # This test case will check the content of the expected and actual output by order
    # This test case will pass since assertNotEqual is used to check content of both arrays and that content is different
    def test_us_29_different_content(self):
        us29Data = [
            "Error Individual List Deceased us29:name:Edward Chapmen",
           "Error Individual List Deceased us29:name:Wanda Chapmen",
           "Error Individual List Deceased us29:name:Sam Chapmen",
           "Error Individual List Deceased us29:name:John Chapmen",
           "Error Individual List Deceased us29:name:John Chapmen",
           "Error Individual List Deceased us29:name:Adrian Chapmen",
           "Error Individual List Deceased us29:name:Karen Chapmen",
           "Error Individual List Deceased us29:name:Carol Chapmen",
           "Error Individual List Deceased us29:name:Maria Chapmen"
        ]
        data = user_st1.us_29_List_deceased()
        for index, value in enumerate(data):
            self.assertNotEqual(value, us29Data[index],
                                "This test case will pass since assertNotEqual is used to check content of both arrays and that content is different")


if __name__ == '_main_':
    unittest2.main()
