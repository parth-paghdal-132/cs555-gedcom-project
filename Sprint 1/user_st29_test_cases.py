import unittest2
import user_st1
def test_us_29_same_length(self):
        us29Data = [
                "Error Individual List Deceased us29:name:Edward Chapmen",

                "Error Individual List Deceased us29:name:Wanda Chapmen"

                "Error Individual List Deceased us29:name:Sam Chapmen"

                "Error Individual List Deceased us29:name:John Chapmen"

                "Error Individual List Deceased us29:name:John Chapmen"

                "Error Individual List Deceased us29:name:Adrian Chapmen"

                "Error Individual List Deceased us29:name:Karen Chapmen"

                "Error Individual List Deceased us29:name:Carol Chapmen"

                "Error Individual List Deceased us29:name:Maria Chapmen"
        ]
        self.assertEqual(len(user_st1.us_29_List_deceased()), len(us29Data), "This test case will pass since assertEqual method is used and both array has same length")

     # This test case will compare the expected and actual outputs' content in the following sequence.
    # As assertEqual is used to verify that the contents of both arrays are identical, this test case will pass.
def test_us_29_same_content(self):
        us29Data = [
                "Error Individual List Deceased us29:name:Edward Chapmen",

                "Error Individual List Deceased us29:name:Wanda Chapmen"

                "Error Individual List Deceased us29:name:Sam Chapmen"

                "Error Individual List Deceased us29:name:John Chapmen"

                "Error Individual List Deceased us29:name:John Chapmen"

                "Error Individual List Deceased us29:name:Adrian Chapmen"

                "Error Individual List Deceased us29:name:Karen Chapmen"

                "Error Individual List Deceased us29:name:Carol Chapmen"

                "Error Individual List Deceased us29:name:Maria Chapmen"
        ]
        data = user_st1.us_29_List_deceased()
        for index, value in enumerate(data):
            self.assertEqual(value, us29Data[index], "This test case will pass since assertEqual is used to check content of both array and that content is same")
    
    # The length of the expected and actual output will be compared in this test scenario.
def test_us_29_different_length(self):
        us29Data = [
                "Error Individual List Deceased us29:name:Edward Chapmen",

                "Error Individual List Deceased us29:name:Wanda Chapmen"

                "Error Individual List Deceased us29:name:Sam Chapmen"

                "Error Individual List Deceased us29:name:John Chapmen"

                "Error Individual List Deceased us29:name:John Chapmen"

                "Error Individual List Deceased us29:name:Adrian Chapmen"

                "Error Individual List Deceased us29:name:Karen Chapmen"

                "Error Individual List Deceased us29:name:Carol Chapmen"

                "Error Individual List Deceased us29:name:Maria Chapmen"
        ]
        self.assertNotEqual(len(user_st1.us_29_List_deceased()), len(us29Data), "This test case will pass since assertNotEqual is used and both array has different length")
    
    # This test case will compare the predicted and actual outputs' content in the following sequence.
    # Since assertNotEqual is used to verify that the contents of an array are distinct, this test case will pass.
def test_us_29_different_content(self):
        us29Data = [
                "Error Individual List Deceased us29:name:Edward Chapmen",

                "Error Individual List Deceased us29:name:Wanda Chapmen"

                "Error Individual List Deceased us29:name:Sam Chapmen"

                "Error Individual List Deceased us29:name:John Chapmen"

                "Error Individual List Deceased us29:name:John Chapmen"

                "Error Individual List Deceased us29:name:Adrian Chapmen"

                "Error Individual List Deceased us29:name:Karen Chapmen"

                "Error Individual List Deceased us29:name:Carol Chapmen"

                "Error Individual List Deceased us29:name:Maria Chapmen"
        ]
        data = user_st1.us_29_List_deceased()
        for index, value in enumerate(data):
            self.assertNotEqual(value, us29Data[index], "This test case will pass since assertNotEqual is used to check content both array and that content is different")

if __name__ == '__main__':
    unittest2.main()
