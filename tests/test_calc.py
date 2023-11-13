from demolib import Addition

def test_init():
    a = 10
    b = 5

    assert Addition(a,b) == 15
    