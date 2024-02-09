from parsimonious.grammar import Grammar

grammar = Grammar(
    '''
    code = (node / edge / delimiter)*

    node = label command
    command = number / builtin

    number = ~r"[0-9]+"
    builtin = ~r"[`~!@#$%^&*()_=+\[{\]}\|;:'\\",<.>/?]"

    edge = label '-' label
    
    label = ~r"[A-Z]"i
    delimiter = ~r"(\s+|$)"
    '''
)