from unittest import TestCase
from pass_checker import validate_password

class TestPasswordTestCase(TestCase):
    def setUp(self):
        # data preparation
        self.pass_short_len = "icode"
        self.pass_long_len = "Qwerty123@@fafdcjsdfcaj"
        self.pass_lower    =  "QWE123@"
        self.pass_num = "Qwe@WEdr"
        self.pass_upper = "qwetw1@"
        self.pass_special = "Qwe1233"
        self.pass_whitespace = "Qwe@ 1234"
        self.pass_correct = "QwertY123@"

    def test_short_pass_len(self):
        self.assertEqual(
             validate_password(self.pass_short_len),
             "Your Password {} is Invalid it should have a minumum of 6 characters & a maximum of 12 characters".format(self.pass_short_len)
        )    
 
    def test_pass_max_len(self):
        self.assertEqual(
            validate_password(self.pass_long_len),
             "Your Password {} is Invalid it should have a minumum of 6 characters & a maximum of 12 characters".format(self.pass_long_len))

    def test_pass_lowercase_char(self):
        self.assertEqual(
            validate_password(self.pass_lower),
             "Your Password {} is Invalid it should contain at least a lowercase character".format(self.pass_lower))

    def test_pass_should_contain_num(self):
        self.assertEqual(
            validate_password(self.pass_num),
             "Your Password {} is Invalid it should contain at least a number".format(self.pass_num))

    def test_pass_should_contain_uppercase_char(self):
        self.assertEqual(
            validate_password(self.pass_upper),
             "Your Password {} is Invalid it should contain at least a capital character".format(self.pass_upper))

    def test_pass_should_contain_special_char(self):
        self.assertEqual(
            validate_password(self.pass_special),
             "Your Password {} is Invalid it should contain at least a special character".format(self.pass_special))

    def test_pass_no_whitespace(self):
        self.assertEqual(
            validate_password(self.pass_whitespace),
             "Your Password {} is Invalid it should not contain white spaces".format(self.pass_whitespace))

    def test_valid_pass(self):
        self.assertEqual(
            validate_password(self.pass_correct), "Your password {} is Valid".format(self.pass_correct))
