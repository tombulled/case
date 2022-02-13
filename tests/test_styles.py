import case
import pytest


@pytest.fixture
def string() -> str:
    return "MY __mask__ --ofSanityIS.slowly#Slipping"


def test_lower(string) -> None:
    assert case.lower(string) == "my mask of sanity is slowly slipping"


def test_upper(string) -> None:
    assert case.upper(string) == "MY MASK OF SANITY IS SLOWLY SLIPPING"


def test_title(string) -> None:
    assert case.title(string) == "My Mask Of Sanity Is Slowly Slipping"


def test_sentence(string) -> None:
    assert case.sentence(string) == "My mask of sanity is slowly slipping"


def test_snake(string) -> None:
    assert case.snake(string) == "my_mask_of_sanity_is_slowly_slipping"


def test_helter(string) -> None:
    assert case.helter(string) == "My_Mask_Of_Sanity_Is_Slowly_Slipping"


def test_macro(string) -> None:
    assert case.macro(string) == "MY_MASK_OF_SANITY_IS_SLOWLY_SLIPPING"


def test_kebab(string) -> None:
    assert case.kebab(string) == "my-mask-of-sanity-is-slowly-slipping"


def test_train(string) -> None:
    assert case.train(string) == "My-Mask-Of-Sanity-Is-Slowly-Slipping"


def test_cobol(string) -> None:
    assert case.cobol(string) == "MY-MASK-OF-SANITY-IS-SLOWLY-SLIPPING"


def test_flat(string) -> None:
    assert case.flat(string) == "mymaskofsanityisslowlyslipping"


def test_flush(string) -> None:
    assert case.flush(string) == "MYMASKOFSANITYISSLOWLYSLIPPING"


def test_pascal(string) -> None:
    assert case.pascal(string) == "MyMaskOfSanityIsSlowlySlipping"


def test_camel(string) -> None:
    assert case.camel(string) == "myMaskOfSanityIsSlowlySlipping"


def test_dot(string) -> None:
    assert case.dot(string) == "my.mask.of.sanity.is.slowly.slipping"


def test_path(string) -> None:
    assert case.path(string) == "my/mask/of/sanity/is/slowly/slipping"
