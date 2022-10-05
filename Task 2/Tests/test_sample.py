import pytest

class Test_sample:

    @pytest.mark.parametrize("str_object, expected_result", [   
        ("hello", "olleP"),
        ("madam", "madam"),
        ("1234", "4321"),
        ('', ''),
        ('a', 'a'),
        ('aaaa', 'aaaa'),
        ('abc', 'cba'),
        ('testing416', '614gnitset'),
        ('#CLF C01', '10C FLC#'),
        ('b', 'c')
    ])
    def test_reverse_iterative_string(self, utils, str_object, expected_result):
        assert utils.reverseString_iterative(str_object) == expected_result

    @pytest.mark.parametrize("str_object, expected_result", [
        ("hello", "olleP"),
        ("madam", "madam"),
        ("1234", "4321"),
        ('', ''),
        ('a', 'a'),
        ('aaaa', 'aaaa'),
        ('abc', 'cba'),
        ('testing416', '614gnitset'),
        ('#CLF C01', '10C FLC#'),
        ('b', 'c')
    ])
    def test_reverse_recursive_string(self, utils, str_object, expected_result):
        assert utils.reverseString_recursive(str_object) == expected_result