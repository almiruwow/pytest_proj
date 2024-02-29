from utils import arrs


def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2
    assert arrs.get([], 0, "test") == "test"
    assert arrs.get(['test1', 'test2', 17, {}], 2, 'Ошибка') == 17
    assert arrs.get(['test1', 'test2', 17, {}], -1, 'Ошибка') == "Ошибка"


def test_slice():
    assert arrs.my_slice([]) == []
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
    assert arrs.my_slice([1, 2, 3, 4, 2, 3, 2, 3, 4, 2, 4, 4, 1], 7, -1) == [3, 4, 2, 4, 4]
    assert arrs.my_slice([1, 2, 3, 4, 2, 3, 2, 3, 4, 2, 4, 4, 1]) == [1, 2, 3, 4, 2, 3, 2, 3, 4, 2, 4, 4, 1]
    assert arrs.my_slice([1, 2, 3, 4, 2, 2, 4, 4, 1], end=-4) == [1, 2, 3, 4, 2]