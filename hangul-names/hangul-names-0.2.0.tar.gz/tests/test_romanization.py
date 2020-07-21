import pytest

from hangul_names.dramawiki import DramaWiki, DramaWikiFormatter
from hangul_names.transliterator import Transliterator
from hangul_names.words import SyllableRuleSet

dw_worker = DramaWiki()


class RevisedWithDramawikiFormatter(DramaWikiFormatter, Transliterator):
    pass


rr_worker = RevisedWithDramawikiFormatter()
rr_vanilla = Transliterator()

msg = "{hangul} is expected to become {expected}."

DRAMAWIKI_TESTS = (
    ("김혜은", "Kim Hye Eun"),
    ("박신혜", "Park Shin Hye"),
    ("권화운", "Kwon Hwa Woon"),
    ("신동미", "Shin Dong Mi"),
    ("장나라", "Jang Na Ra"),
    ("최시원", "Choi Shi Won"),
    ("김종결", "Kim Jong Kyul"),
    ("함성민", "Ham Sung Min"),
    ("강이수", "Kang Yi Soo"),
    ("오승현", "Oh Seung Hyun"),
    ("이언정", "Lee Uhn Jung"),
    ("최강희", "Choi Kang Hee"),
    ("이도경", "Lee Do Kyung"),
    ("원빈", "Won Bin"),
    ("왕빛나", "Wang Bit Na"),
    ("서지석", "Suh Ji Suk"),
    ("김형일", "Kim Hyung Il"),
    ("최자혜", "Choi Ja Hye"),
    ("샤를리즈테론", "Sya Reul Ri Jeu Te Ron"),  # Charlize Theron...
)

REVISED_ROMANIZATION_TESTS = (
    ("김혜은", "Gim Hye Eun"),
    ("박신혜", "Bak Sin Hye"),
    ("권화운", "Gwon Hwa Un"),
    ("신동미", "Sin Dong Mi"),
    ("장나라", "Jang Na Ra"),
    ("최시원", "Choe Si Won"),
    ("김종결", "Gim Jong Gyeol"),
    ("함성민", "Ham Seong Min"),
    ("강이수", "Gang I Su"),
    ("오승현", "Oh Seung Hyeon"),
    ("이언정", "Lee Eon Jeong"),
    ("최강희", "Choe Gang Hui"),
    ("이도경", "Lee Do Gyeong"),
    ("원빈", "Won Bin"),
    ("왕빛나", "Wang Bit Na"),
    ("서지석", "Seo Ji Seok"),
    ("김형일", "Gim Hyeong Il"),
    ("최자혜", "Choe Ja Hye"),
)

REVISED_VANILLA_TESTS = (
    ("김혜은", "Gim Hye-eun"),
    ("박신혜", "Bak Sin-hye"),
    ("권화운", "Gwon Hwa-un"),
    ("신동미", "Sin Dong-mi"),
    ("장나라", "Jang Na-ra"),
    ("최시원", "Choe Si-won"),
    ("김종결", "Gim Jong-gyeol"),
    ("함성민", "Ham Seong-min"),
    ("강이수", "Gang I-su"),
    ("오승현", "Oh Seung-hyeon"),
    ("이언정", "Lee Eon-jeong"),
    ("최강희", "Choe Gang-hui"),
    ("이도경", "Lee Do-gyeong"),
    ("원빈", "Won Bin"),
    ("왕빛나", "Wang Bit-na"),
    ("서지석", "Seo Ji-seok"),
    ("김형일", "Gim Hyeong-il"),
    ("최자혜", "Choe Ja-hye"),
)


@pytest.mark.parametrize(("hangul", "expected"), DRAMAWIKI_TESTS)
def test_dramawiki(hangul, expected):
    actual = dw_worker.romanize(hangul)
    assert actual == expected, msg.format(hangul=hangul, expected=expected)


@pytest.mark.parametrize(("hangul", "expected"), REVISED_ROMANIZATION_TESTS)
def test_revised_romanization(hangul, expected):
    actual = rr_worker.romanize(hangul)
    assert actual == expected, msg.format(hangul=hangul, expected=expected)


@pytest.mark.parametrize(("hangul", "expected"), REVISED_VANILLA_TESTS)
def test_revised_romanization_vanilla(hangul, expected):
    actual = rr_vanilla.romanize(hangul)
    assert actual == expected, msg.format(hangul=hangul, expected=expected)


def test_illegal_chars():
    with pytest.raises(ValueError) as e:
        assert SyllableRuleSet()._lookup_letter(" ")
    assert str(e.value) == "32 out of range (< 4352)"

    with pytest.raises(ValueError) as e:
        assert SyllableRuleSet()._lookup_letter("ᇔ")
    assert str(e.value) == "4564 out of range (> 4546)"
