'''
autocomplete.py: Program to implement autocomplete system that,
given string 's' and set of all query strings,
 retrns all strings with 's' as a prefix
'''

# Function args #
#################
# s: query string 
# queries: set of all possible query strings

# return value #
################
# List[str]: list of strings with 's' prefix

from typing import List
import re

def autocomplete(s, queries) -> List[str]:
    pattern = r'^({}).*'.format(s)
    regex = re.compile(pattern)

    res = []

    # match pattern for each element in list
    for q in queries:
        if regex.match(q):
            res.append(q)
    return res

s='de'
queries = ['dog', 'deer', 'deal']

matched_queries = autocomplete(s, queries)
print(matched_queries)