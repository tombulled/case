import case


def test_lower() -> None:
    assert case.identify("foo bar") == [case.lower]


def test_upper() -> None:
    assert case.identify("FOO BAR") == [case.upper]


def test_title() -> None:
    assert case.identify("Foo Bar") == [case.title]


def test_sentence() -> None:
    assert case.identify("Foo bar") == [case.sentence]


def test_snake() -> None:
    assert case.identify("foo_bar") == [case.snake]


def test_helter() -> None:
    assert case.identify("Foo_Bar") == [case.helter]


def test_macro() -> None:
    assert case.identify("FOO_BAR") == [case.macro]


def test_kebab() -> None:
    assert case.identify("foo-bar") == [case.kebab]


def test_train() -> None:
    assert case.identify("Foo-Bar") == [case.train]


def test_cobol() -> None:
    assert case.identify("FOO-BAR") == [case.cobol]


def test_flat() -> None:
    assert case.flat in case.identify("foobar")


def test_flush() -> None:
    assert case.flush in case.identify("FOOBAR")


def test_pascal() -> None:
    assert case.identify("FooBar") == [case.pascal]


def test_camel() -> None:
    assert case.identify("fooBar") == [case.camel]


def test_dot() -> None:
    assert case.identify("foo.bar") == [case.dot]


def test_path() -> None:
    assert case.identify("foo/bar") == [case.path]
