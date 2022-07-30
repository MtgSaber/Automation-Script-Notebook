# This script should take as args: [--lex_permute|--lex_align] parameterized_regex [lexicons] files
#   parameterized_regex: This is a standard regex, but with support for special meta-characters of {\0, \1, ... , \9}.
#                        these meta-characters will be substituted with lexicon contents, in the order the lexicons are
#                        provided. These meta-characters can occur more than once in a given parameterized_regex.
#                        However, the set containing usages of these meta-characters should not "skip" a number,
#                        and should either be empty or should always contain \0.
#   [lexicons]: This optional parameter is a whitespace-separated list of lexicons to supply terms to substitute
#               the aforementioned meta-characters with. The number of lexicons should equal the cardinality
#               of the set containing usages of the aforementioned meta-characters.
#   files:
