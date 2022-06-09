#!/usr/local/bin/python3
import atheris
import sys
from normality import normalize, slugify, collapse_spaces, ascii_text, latinize_text, stringify, predict_encoding, guess_encoding

@atheris.instrument_func
def TestOneInput(data):
    fdp = atheris.FuzzedDataProvider(data)
    if len(data) < 1:
        return

    option = fdp.ConsumeBytes(1)[0]
    in_string = fdp.ConsumeUnicodeNoSurrogates(len(data))

    if option % 8 == 0:
        normalize(in_string)
    elif option % 8 == 1:
        slugify(in_string)
    elif option % 8 == 2:
        collapse_spaces(in_string)
    elif option % 8 == 3:
        ascii_text(in_string)
    elif option % 8 == 4:
        latinize_text(in_string)
    elif option % 8 == 5:
        stringify(in_string)
    elif option % 8 == 6:
        predict_encoding(bytes(in_string, 'utf-8'))
    elif option % 8 == 7:
        guess_encoding(bytes(in_string, 'utf-8'))


atheris.instrument_all()
atheris.Setup(sys.argv, TestOneInput)
atheris.Fuzz()