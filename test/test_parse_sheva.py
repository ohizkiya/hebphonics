#!/usr/bin/python
"""`sheva-`"""

# pkg
from hebphonics.grammar import Parser

DEFAULT_DISABLE = ["qamats-qatan-closed-unaccented"]


def test_not_real_sheva():
    """an unknown kind of sheva"""
    word = r"זרְע"
    parts = ["zayin", "resh", "sheva", "ayin"]
    assert parts == Parser().parse(word).flat()


def test_sheva_gaya():
    """`sheva` with a `meteg` is a `sheva-gaya`"""
    word = r"וְֽנָשׁ֔וּבָה"
    parts = [
        "vav",
        "sheva-gaya",
        "nun",
        "qamats-gadol",
        "shin",
        "shuruq",
        "vet",
        "qamats-male-he",
        "he",
    ]
    assert parts == Parser().parse(word).flat()


def test_sheva_na_start():
    """`sheva` at word start is `sheva-na` (sheva-na-start)"""
    word = r"וְאֵת"  # ve-et
    parts = ["vav", "sheva-na", "alef", "tsere", "sav"]
    assert parts == Parser().parse(word).flat()

    word = r"קְדוֹשׁ"  # ke-dosh
    parts = ["qof", "sheva-na-mute", "dalet", "holam-male-vav", "shin"]
    assert parts == Parser().parse(word).flat()

    word = r"בְּלִי"  # be-li
    parts = ["bet", "dagesh-qal", "sheva-na", "lamed", "hiriq-male-yod", "yod"]
    assert parts == Parser().parse(word).flat()


def test_sheva_nah_end():
    """`sheva` at word end is `sheva-nah` (sheva-nah-end)"""
    word = r"לָךְ"  # lach
    parts = ["lamed", "qamats", "khaf-sofit", "sheva-nah"]
    assert parts == Parser().parse(word).flat()


def test_sheva_nah_alef_end():
    """`sheva` before last bare `alef` is `sheva-nah` (sheva-nah-alef-end)"""
    word = "חֵטְא"  # cheit
    parts = ["het", "tsere", "tet", "sheva-nah", "alef"]
    assert parts == Parser().parse(word).flat()


def test_sheva_double_end():
    """two `sheva` at word end are `sheva-nah`, `sheva-nah` (sheva-double-end)"""
    word = r"אַנְתְּ"  # ahnt
    parts = ["alef", "patah", "nun", "sheva-nah", "tav", "dagesh-qal", "sheva-nah"]
    assert parts == Parser().parse(word).flat()


def test_double_sheva_middle():
    """two `sheva` midword are `sheva-nah`, `sheva-na` (sheva-double-middle)"""
    word = r"יִמְשְׁלוּ"  # yim-she-lu
    parts = ["yod", "hiriq", "mem", "sheva-nah", "shin", "sheva-na", "lamed", "shuruq"]
    assert parts == Parser().parse(word).flat()


def test_sheva_na_double_letter():
    """`sheva` before same letter is `sheva-na` (sheva-na-double-letter)"""
    word = r"הַלְלוּ"  # ha-le-lu
    parts = ["he", "patah", "lamed", "sheva-na", "lamed", "shuruq"]
    assert parts == Parser().parse(word).flat()

    word = r"הִנְנִי"  # hi-ne-ni (has vowel under second letter)
    parts = ["he", "hiriq", "nun", "sheva-na", "nun", "hiriq-male-yod", "yod"]
    assert parts == Parser().parse(word).flat()


def test_sheva_na_under_dagesh_hazaq():
    """`sheva` under `dagesh-hazaq` is `sheva-na` (sheva-na-dagesh-hazaq)"""
    word = r"הַבְּאֵר"  # ha-be-eir
    parts = ["he", "patah", "bet", "dagesh-hazaq", "sheva-na", "alef", "tsere", "resh"]
    assert parts == Parser().parse(word).flat()


def test_sheva_nah_after_shuruq_start():
    """`sheva` after shuruq at word start in non-dagesh letter is `sheva-nah`"""
    word = r"וּרְבוּ"
    parts = ["shuruq", "resh", "sheva-nah", "vet", "shuruq"]
    assert parts == Parser().parse(word).flat()


def test_sheva_na_after_long_vowel():
    """`sheva` after long vowel is `sheva-na` (sheva-na-after-long-vowel)"""
    word = r"יֵשְׁבוּ"  # yei-she-vu
    parts = ["yod", "tsere", "shin", "sheva-na", "vet", "shuruq"]
    assert parts == Parser().parse(word).flat()


def test_sheva_na_after_holam_alef():
    """holam + alef is a long vowel (sheva-na-after-long-vowel)"""
    word = r"יֹאמְרוּ"  # yo-me-ru (Exodus 4:1)
    parts = ["yod", "holam-male-alef", "alef", "mem", "sheva-na", "resh", "shuruq"]
    assert parts == Parser().parse(word).flat()


def test_sheva_nah_after_short_vowel():
    """`sheva` after short vowel is `sheva-nah` (sheva-nah-after-short-vowel)"""
    word = r"יִשְׁלַח"  # yish-lach
    parts = ["yod", "hiriq", "shin", "sheva-nah", "lamed", "patah", "het"]
    assert parts == Parser().parse(word).flat()


def test_sheva_nah_after_initial_vav_with_patah():
    """`sheva` after initial `vav` with `patah` is `sheva-nah` (sheva-nah-after-short-vowel)"""
    word = r"וַיְהִי"  # vay-he (feels weird)
    parts = ["vav", "patah", "yod", "sheva-nah", "he", "hiriq-male-yod", "yod"]
    assert parts == Parser().parse(word).flat()


def test_sheva_na_wikipedia():
    """examples from <https://en.wikipedia.org/wiki/Shva#Shva_Na>"""

    # first letter of a word
    word = r"מְרַחֵף‎"  # me-ra-chef
    parts = ["mem", "sheva-na", "resh", "patah", "het", "tsere", "fe-sofit"]
    assert parts == Parser().parse(word).flat()

    word = r"לְפָנָי‎"  # le-fa-nai
    parts = ["lamed", "sheva-na", "fe", "qamats-gadol", "nun", "qamats", "yod"]
    assert parts == Parser(disabled=DEFAULT_DISABLE).parse(word).flat()

    word = r"שְׁמַע‎"  # she-ma
    parts = ["shin", "sheva-na-mute", "mem", "patah", "ayin"]
    assert parts == Parser().parse(word).flat()

    # first of two identical letters
    # no example given

    # second of two shevas under two consecutive letter (except when marked under
    # the last letter of a word)
    word = r"רַעְמְסֵס‎"
    parts = [
        "resh",
        "patah",
        "ayin",
        "sheva-nah",
        "mem",
        "sheva-na",
        "samekh",
        "tsere",
        "samekh",
    ]
    assert parts == Parser().parse(word).flat()

    word = r"וַיִּשְׁמְעוּ"
    parts = [
        "vav",
        "patah",
        "yod",
        "dagesh-hazaq",
        "hiriq",
        "shin",
        "sheva-nah",
        "mem",
        "sheva-na",
        "ayin",
        "shuruq",
    ]
    assert parts == Parser().parse(word).flat()

    # when the letter before the one under which it is marked is marked with a
    # "long" niqqud-variant
    word = r"יְחִֽידְֿךָ‎"  # ye-chi-de-cha
    parts = [
        "yod",
        "sheva-na",
        "het",
        "hiriq-male-yod",
        "yod",
        "dalet",
        "sheva-na",
        "khaf-sofit",
        "qamats-gadol",
    ]
    assert parts == Parser().parse(word).flat()

    word = r"הוֹלְכִֿים‎"
    parts = [
        "he",
        "holam-male-vav",
        "lamed",
        "sheva-na",
        "khaf",
        "hiriq-male-yod",
        "yod",
        "mem-sofit",
    ]
    assert parts == Parser().parse(word).flat()

    word = r"יוֹדְֿעִים‎"
    parts = [
        "yod",
        "holam-male-vav",
        "dalet",
        "sheva-na",
        "ayin",
        "hiriq-male-yod",
        "yod",
        "mem-sofit",
    ]
    assert parts == Parser().parse(word).flat()

    word = r"מוֹכְֿרִים‎"
    parts = [
        "mem",
        "holam-male-vav",
        "khaf",
        "sheva-na",
        "resh",
        "hiriq-male-yod",
        "yod",
        "mem-sofit",
    ]
    assert parts == Parser().parse(word).flat()

    # when marked under a letter with a dagesh ḥazaq
    word = r"מִפְּנֵיכֶם‎"
    parts = [
        "mem",
        "hiriq",
        "pe",
        "dagesh-hazaq",
        "sheva-na",
        "nun",
        "tsere-male-yod",
        "yod",
        "khaf",
        "segol",
        "mem-sofit",
    ]
    assert parts == Parser().parse(word).flat()

    word = r"מִקְּדָֿשׁ‎"  # mi-ke-dash
    parts = [
        "mem",
        "hiriq",
        "qof",
        "dagesh-hazaq",
        "sheva-na",
        "dalet",
        "qamats",
        "shin",
    ]
    assert parts == Parser(disabled=DEFAULT_DISABLE).parse(word).flat()


# Modern Hebrew Sheva <https://en.wikipedia.org/wiki/Shva>
# NOTE: In modern Hebrew, whether a `sheva` is voiced or not does not depend on
# the traditional distinction between `sheva-na` vs `sheva-nah`


def test_modern_sheva_1():
    """`sheva` is voiced when under the first of two letters, both representing the
    same consonant or consonants with identical place and manner of articulation.
    """
    word = r"שָׁכְחוּ"  # sha-che-chu (same sound)
    # TODO: should be qamats-gadol
    parts = ["shin", "qamats", "khaf", "sheva-na", "het", "shuruq"]
    assert parts == Parser().parse(word).flat()

    word = r"מָכְרוּ"  # mach-ru (negative example)
    # TODO: should be sheva-nah (and qamats-gadol)
    parts = ["mem", "qamats", "khaf", "sheva", "resh", "shuruq"]
    assert parts == Parser().parse(word).flat()

    word = r"שָׁדַדְתְּ"  # sha-da-det (same place of articulation)
    parts = [
        "shin",
        "qamats-gadol",
        "dalet",
        "patah",
        "dalet",
        "sheva-nah-voiced",
        "tav",
        "dagesh-qal",
        "sheva-nah",
    ]
    assert parts == Parser().parse(word).flat()

    word = r"שָׁלַלְתְּ"  # sha-lalt (negative example)
    parts = [
        "shin",
        "qamats-gadol",
        "lamed",
        "patah",
        "lamed",
        "sheva-nah",
        "tav",
        "dagesh-qal",
        "sheva-nah",
    ]
    assert parts == Parser().parse(word).flat()


def test_modern_sheva_2():
    """`sheva` is voiced when under the first letter of a word, if this letter
    is a sonorant in modern pronunciation (`yod`, `lamed`, `mem`, `nun`, `resh`).
    """
    word = r"נְמָלִים"  # ne-ma-lim
    parts = [
        "nun",
        "sheva-na",
        "mem",
        "qamats-gadol",
        "lamed",
        "hiriq-male-yod",
        "yod",
        "mem-sofit",
    ]
    assert parts == Parser().parse(word).flat()

    word = r"גְּמָלִים"  # ge-ma-lim (traditional); gma-lim (modern); (negative example)
    parts = [
        "gimel",
        "dagesh-qal",
        "sheva-na-mute",
        "mem",
        "qamats-gadol",
        "lamed",
        "hiriq-male-yod",
        "yod",
        "mem-sofit",
    ]
    assert parts == Parser().parse(word).flat()

    word = r"מְנִיָּה"  # me-ni-ya
    parts = [
        "mem",
        "sheva-na",
        "nun",
        "hiriq",
        "yod",
        "dagesh-hazaq",
        "qamats-male-he",
        "he",
    ]
    assert parts == Parser().parse(word).flat()

    word = r"בְּנִיָּה"  # be-ni-ya (traditional); bni-ya (modern); (negative example)
    parts = [
        "bet",
        "dagesh-qal",
        "sheva-na",  # TODO: sheva-na-mute
        "nun",
        "hiriq",
        "yod",
        "dagesh-hazaq",
        "qamats-male-he",
        "he",
    ]
    assert parts == Parser().parse(word).flat()


def test_modern_sheva_3():
    """`sheva` is voiced when under the first letter of a word, if the second
    letter is a glottal consonant (`alef`, `he`, `ayin`).
    """
    word = r"תְּאָרִים"  # te-a-rim
    parts = [
        "tav",
        "dagesh-qal",
        "sheva-na",
        "alef",
        "qamats-gadol",
        "resh",
        "hiriq-male-yod",
        "yod",
        "mem-sofit",
    ]
    assert parts == Parser().parse(word).flat()

    word = r"תְּמָרִים"  # te-ma-rim (traditional); tma-rim (modern); (negative example)
    parts = [
        "tav",
        "dagesh-qal",
        "sheva-na",  # TODO: sheva-na-mute
        "mem",
        "qamats-gadol",
        "resh",
        "hiriq-male-yod",
        "yod",
        "mem-sofit",
    ]
    assert parts == Parser().parse(word).flat()


def test_modern_sheva_4():
    """`sheva` is voiced when under the first letter of a word, if this letter
    represents one of the prefix-morphemes (`be-`, `ve-`, `ke-`, `le-`, `te-`).
    """

    # TODO: requires knowledge of the root word to determine if the first letter
    # is a prefix or not.

    word = r"בְּרֵיחָהּ"  # be-rei-cha
    parts = [
        "bet",
        "dagesh-qal",
        "sheva-na",
        "resh",
        "tsere-male-yod",
        "yod",
        "het",
        "qamats-male-he",
        "mapiq-he",
        "mapiq",
    ]
    assert parts == Parser(disabled=DEFAULT_DISABLE).parse(word).flat()

    word = r"בְּרֵיכָה"  # brei-cha
    parts = [
        "bet",
        "dagesh-qal",
        "sheva-na",  # TODO: sheva-na-mute
        "resh",
        "tsere-male-yod",
        "yod",
        "khaf",
        "qamats-male-he",
        "he",
    ]
    assert parts == Parser().parse(word).flat()

    # NOTE: requires emphasis information
    word = r"בְּחִישָׁה"  # be-chi-sha
    word = r"בְּחִישָׁה"  # bchi-sha

    word = r"וְרוֹדִים"  # ve-ro-dim
    word = r"וְרוּדִים"  # vru-dim

    # NOTE: requires emphasis information
    word = r"כְּרָזָה"  # ke-ra-za
    word = r"כְּרָזָה"  # kra-za

    word = r"לְפָּרִיז"

    word = r"תְּבַלּוּ"
    word = r"תְּבַלּוּל"
