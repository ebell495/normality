#!/usr/local/bin/python3
import atheris
import sys
from normality import normalize, slugify, collapse_spaces, ascii_text, latinize_text, stringify, predict_encoding, guess_encoding

@atheris.instrument_func
def TestOneInput(data):
    barray = bytearray(data)
    if len(barray) > 0:
        if barray[0] % 8 == 0:
            del barray[0]
            normalize(str(barray))
        elif barray[0] % 8 == 1:
            del barray[0]
            slugify(str(barray))
        elif barray[0] % 8 == 2:
            del barray[0]
            collapse_spaces(str(barray))
        elif barray[0] % 8 == 3:
            del barray[0]
            ascii_text(str(barray))
        elif barray[0] % 8 == 4:
            del barray[0]
            latinize_text(str(barray))
        elif barray[0] % 8 == 5:
            del barray[0]
            stringify(str(barray))
        elif barray[0] % 8 == 6:
            del barray[0]
            predict_encoding(bytes(barray))
        elif barray[0] % 8 == 7:
            del barray[0]
            guess_encoding(bytes(barray))
    else:
        pass


atheris.instrument_all()
atheris.Setup(sys.argv, TestOneInput)
atheris.Fuzz()