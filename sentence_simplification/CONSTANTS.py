SIMPLE_CONNECTIVES = ['और', 'एवं', 'इसलिए', 'क्योंकि', 'जबकि', 'तथा', 'ताकि', 'मगर', 'लेकिन', 'किंतु', 'परंतु', 'फिर', 'या', 'तथापि',
                      'नहीं तो', 'पर', 'व', 'चूंकि', 'चूँकि', 'वरना','अन्यथा', 'बशर्तें', 'हालाँकि', 'इसीलिये', 'इसीलिए' , 'इसलिए', 'अथवा', 'अतः']

COMPLEX_CONNECTIVES = {'चूँकि' : ['अतः'],
                       'जब' : ['तब', 'तो'],
                       'अगर' : ['तो', 'तब'],
                       'यदि' : ['तो'],
                       'यद्यपि' : ['फिर भी'],
                       }

INPUT_FILE = "sentence_input.txt"
PARSER_INPUT = "p_parser_input.txt"
PARSER_OUTPUT = "p_parser_output.txt"
OUTPUT_FILE = "sentence_output.txt"
