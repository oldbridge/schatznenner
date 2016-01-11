from schatznenner import get_random_compliment  # SUT


def test_schatznenner_returns_a_string():
    assert type(get_random_compliment()) == str
