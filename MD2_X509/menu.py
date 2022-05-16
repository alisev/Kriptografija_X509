import typing

from inputfilename import *
from inputoption import *

import x509
import verify
import cipher

_options = [
        {
            'title': "1 - X.509 sertifikāta izveidošana.",
            'function': x509.main
        },
        {
            'title': "2 - Sertifikāta pārbaude.",
            'function': verify.main
        },
        {
            'title': "3 - Ziņojuma iekodēšana/dekodēšana.",
            'function': cipher.main
        }
    ]
_option_count = len(_options)
inputoption = inputOption()
inputfilename = inputFilename()

def show_menu():
    for txt in _options:
        print(txt['title'])
    option = _get_input(inputoption)
    filename = _get_input(inputfilename)
    _run_selected_action(option, filename)

def _get_input(input_module) -> int:
    input_given = False
    while(input_given == False):
        try:
            input = input_module.input()
            if input_module.validity_check(input):
                input_given = True
            else:
                raise ValueError(input_module.error_message)
        except Exception as e:
            print(e)
    return input

def _run_selected_action(action: int, filename: str):
    _options[action - 1]['function'](filename)