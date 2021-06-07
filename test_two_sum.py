import two_sum


class TestTwoSum:
    def test_1(self):
        assert two_sum.two_sum([5, 6, 2, 9], 11) == [5, 6]

    def test_2(self):
        assert two_sum.two_sum([7, 12, 5, 9], 16) == [7, 9]