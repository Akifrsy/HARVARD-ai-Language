import nltk

grammar = nltk.CFG.fromstring("""
    S -> NP VP
    
    AP -> A | A AP
    NP -> N | D NP | AP NP | N PP
    PP -> P NP
    VP -> V | V NP | V NP PP
                              
    A -> "big" | "blue"     | "small"  | "dry"    | "wide" |              |
    D -> "the" | "a" | "an" |          |          |        |              |
    N -> "she" | "city"     | "car"    | "street" | "dog"  | "binoculars" |
    P -> "on"  | "over"     | "before" | "below"  | "with" |              |
    V -> "saw" | "walked"   |          |          |        |              |
""")

parser = nltk.ChartParser(grammar)