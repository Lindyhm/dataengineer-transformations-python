from data_transformations.citibike import ingest


def test_should_sanitize_nothing():
    no_whitespace_columns = ['foo']

    actual = ingest.sanitize_columns(no_whitespace_columns)
    expected = no_whitespace_columns

    assert expected == actual


def test_should_sanitize_whitespace_outside():
    no_whitespace_columns = [' foo ']

    actual = ingest.sanitize_columns(no_whitespace_columns)
    expected = ['_foo_']

    assert expected == actual


def test_should_sanitize_whitespace_in_between():
    no_whitespace_columns = ['foo bar']

    actual = ingest.sanitize_columns(no_whitespace_columns)
    expected = ['foo_bar']

    assert expected == actual
