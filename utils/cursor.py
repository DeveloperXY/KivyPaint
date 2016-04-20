"""Our custom cursor."""
CURSOR = (
    '       @@@@             ',
    '       @--@             ',
    '       @--@             ',
    '       @--@             ',
    '       @--@             ',
    '       @@@@             ',
    '                        ',
    '@@@@@@ @@@@ @@@@@@      ',
    '@----@ @--@ @----@      ',
    '@----@ @--@ @----@      ',
    '@@@@@@ @@@@ @@@@@@      ',
    '                        ',
    '       @@@@             ',
    '       @--@             ',
    '       @--@             ',
    '       @--@             ',
    '       @--@             ',
    '       @@@@             ',
    '                        ',
    '                        ',
    '                        ',
    '                        ',
    '                        ',
    '                        ',
)


def pygame_compile_cursor(black='@', white='-'):
    """This function translates the Pygame's mouse cursor definition
    into something expected by SDL, Pygame's backend library."""
    aa, bb = [], []
    a = b = 0
    i = 8
    for s in CURSOR:
        for c in s:
            a <<= 1
            b <<= 1
            i -= 1
            if c == black:
                a |= 1
                b |= 1
            elif c == white:
                b |= 1

            if not i:
                aa.append(a)
                bb.append(b)
                a = b = 0
                i = 8

    return tuple(aa), tuple(bb)
