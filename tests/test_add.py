import learning_rust


def test_add():
    assert learning_rust.add(2, 3) == 5
    assert learning_rust.add(0, 0) == 0
    assert learning_rust.add(100, 200) == 300