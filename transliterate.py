# -*- coding: utf-8 -*-
import re


LATIN_TO_CYRILLIC = {
    'a': 'а', 'A': 'А',
    'b': 'б', 'B': 'Б',
    'd': 'д', 'D': 'Д',
    'e': 'е', 'E': 'Е',
    'f': 'ф', 'F': 'Ф',
    'g': 'г', 'G': 'Г',
    'h': 'ҳ', 'H': 'Ҳ',
    'i': 'и', 'I': 'И',
    'j': 'ж', 'J': 'Ж',
    'k': 'к', 'K': 'К',
    'l': 'л', 'L': 'Л',
    'm': 'м', 'M': 'М',
    'n': 'н', 'N': 'Н',
    'o': 'о', 'O': 'О',
    'p': 'п', 'P': 'П',
    'q': 'қ', 'Q': 'Қ',
    'r': 'р', 'R': 'Р',
    's': 'с', 'S': 'С',
    't': 'т', 'T': 'Т',
    'u': 'у', 'U': 'У',
    'v': 'в', 'V': 'В',
    'x': 'х', 'X': 'Х',
    'y': 'й', 'Y': 'Й',
    'z': 'з', 'Z': 'З',
    'o‘': 'ў', 'O‘': 'Ў',
    'oʻ': 'ў', 'Oʻ': 'Ў',
    'g‘': 'ғ', 'G‘': 'Ғ',
    'gʻ': 'ғ', 'Gʻ': 'Ғ',
    'sh': 'ш', 'Sh': 'Ш', 'SH': 'Ш',
    'ch': 'ч', 'Ch': 'Ч', 'CH': 'Ч',
    'yo‘': 'йў', 'Yo‘': 'Йў', 'YO‘': 'ЙЎ',
    'yoʻ': 'йў', 'Yoʻ': 'Йў', 'YOʻ': 'ЙЎ',
    'ts': 'ц', 'Ts': 'Ц', 'TS': 'Ц',
    'yo': 'ё', 'Yo': 'Ё', 'YO': 'Ё',
    'yu': 'ю', 'Yu': 'Ю', 'YU': 'Ю',
    'ya': 'я', 'Ya': 'Я', 'YA': 'Я',
    'ye': 'е', 'Ye': 'Е', 'YE': 'Е',
    'ʼ': 'ъ',  # TODO: case?
}
LATIN_CONSONANTS = (
    'a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U', 'o‘', 'O‘'
)

CYRILLIC_TO_LATIN = {
    'а': 'a', 'А': 'A',
    'б': 'b', 'Б': 'B',
    'в': 'v', 'В': 'V',
    'г': 'g', 'Г': 'G',
    'д': 'd', 'Д': 'D',
    'е': 'e', 'Е': 'E',
    'ё': 'yo', 'Ё': 'Yo',
    'ж': 'j', 'Ж': 'J',
    'з': 'z', 'З': 'Z',
    'и': 'i', 'И': 'I',
    'й': 'y', 'Й': 'Y',
    'к': 'k', 'К': 'K',
    'л': 'l', 'Л': 'L',
    'м': 'm', 'М': 'M',
    'н': 'n', 'Н': 'N',
    'о': 'o', 'О': 'O',
    'п': 'p', 'П': 'P',
    'р': 'r', 'Р': 'R',
    'с': 's', 'С': 'S',
    'т': 't', 'Т': 'T',
    'у': 'u', 'У': 'U',
    'ф': 'f', 'Ф': 'F',
    'х': 'x', 'Х': 'X',
    'ц': 's', 'Ц': 'S',
    'ч': 'ch', 'Ч': 'Ch',
    'ш': 'sh', 'Ш': 'Sh',
    'ъ': 'ʼ', 'Ъ': 'ʼ',
    'ь': '', 'Ь': '',
    'э': 'e', 'Э': 'E',
    'ю': 'yu', 'Ю': 'Yu',
    'я': 'ya', 'Я': 'Ya',
    'ў': 'oʻ', 'Ў': 'Oʻ',
    'қ': 'q', 'Қ': 'Q',
    'ғ': 'gʻ', 'Ғ': 'Gʻ',
    'ҳ': 'h', 'Ҳ': 'H',
}
CYRILLIC_CONSONANTS = (
    'а', 'А', 'е', 'Е', 'ё', 'Ё', 'и', 'И', 'о', 'О', 'у', 'У', 'э', 'Э',
    'ю', 'Ю', 'я', 'Я', 'ў', 'Ў'
)


def to_cyrillic(text):
    """Transliterate latin text to cyrillic  using the following rules:
    """
    return text


def to_latin(text):
    """Transliterate cyrillic text to latin using the following rules:
    1. ц = s at the beginning of a word.
    ц = ts in the middle of a word after a vowel.
    ц = s in the middle of a word after consonant (DEFAULT in CYRILLIC_TO_LATIN)
        цирк = sirk
        цех = sex
        федерация = federatsiya
        функция = funksiya
    2. е = ye at the beginning of a word or after a vowel.
    е = e in the middle of a word after a consonant (DEFAULT).
    3. Сентябр = Sentabr, Октябр = Oktabr
    """
    beginning_rules = {
        'ц': 's', 'Ц': 'S',
        'е': 'ye', 'Е': 'Ye'
    }
    after_vowel_rules = {
        'ц': 'ts', 'Ц': 'Ts',
        'е': 'ye', 'Е': 'Ye'
    }

    text = re.sub('\b([цЦеЕ])', lambda x: beginning_rules[x.group(1)], text)
    text = re.sub(
        '(%s)([цЦеЕ])' % '|'.join(CYRILLIC_CONSONANTS),
        lambda x: '%s%s' % (x.group(1), after_vowel_rules[x.group(2)]),
        text
    )
    text = re.sub(
        '(сент|окт)([яЯ])(бр)',
        lambda x: '%s%s%s' % (x.group(1), 'a' if x.group(2) == 'я' else 'A', x.group(3)),
        text,
        flags=re.IGNORECASE
    )

    return text


def transliterate(text, to_variant):
    if to_variant == 'cyrillic':
        text = to_cyrillic(text)
    elif to_variant == 'latin':
        text = to_latin(text)

    return text
