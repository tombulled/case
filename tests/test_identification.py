import case


def test_lower() -> None:
    assert set(case.identify("foo bar")) == {case.lower}


def test_upper() -> None:
    assert set(case.identify("FOO BAR")) == {case.upper}


def test_title() -> None:
    assert set(case.identify("Foo Bar")) == {case.title}


def test_sentence() -> None:
    assert set(case.identify("Foo bar")) == {case.sentence}


def test_snake() -> None:
    assert set(case.identify("foo_bar")) == {case.snake}


def test_helter() -> None:
    assert set(case.identify("Foo_Bar")) == {case.helter}


def test_macro() -> None:
    assert set(case.identify("FOO_BAR")) == {case.macro}


def test_kebab() -> None:
    assert set(case.identify("foo-bar")) == {case.kebab}


def test_train() -> None:
    assert set(case.identify("Foo-Bar")) == {case.train}


def test_cobol() -> None:
    assert set(case.identify("FOO-BAR")) == {case.cobol}


def test_flat() -> None:
    assert set(case.identify("foobar")) == {case.camel, case.dot, case.flat, case.kebab, case.lower, case.path, case.snake}


def test_flush() -> None:
    assert set(case.identify("FOOBAR")) == {case.cobol, case.flush, case.macro, case.upper}


def test_pascal() -> None:
    assert set(case.identify("FooBar")) == {case.pascal}


def test_camel() -> None:
    assert set(case.identify("fooBar")) == {case.camel}


def test_dot() -> None:
    assert set(case.identify("foo.bar")) == {case.dot}


def test_path() -> None:
    assert set(case.identify("foo/bar")) == {case.path}
