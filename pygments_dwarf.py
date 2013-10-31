from pygments.lexer import RegexLexer, bygroups
from pygments.token import *

class DWARFLexer(RegexLexer):
    name = 'DWARF'
    aliases = 'dwarf'

    tokens = {
        'root': [
            (r'\s+', Text),

            # DIE addresses
            (r'(<)((0x)?[0-9a-fA-F]+)(>)',
                bygroups(Operator, Number, None, Operator)),

            # Tags/attributes/opcodes
            (r'DW_TAG_[a-zA-Z_]+', Name.Tag),
            (r'DW_AT_[a-zA-Z_]+', Name.Attribute),
            (r'DW_OP_[a-zA-Z_]+', Name.Function),

            # Common syntax elements: numbers, ...
            (r'0x[0-9a-fA-F]+', Number),
            (r'\d+', Number),

            (r'.', Text),
        ],
    }
