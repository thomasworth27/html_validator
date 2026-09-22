#!/bin/python3


def validate_html(html):
    '''
    This function performs a limited version of html validation by checking whether every opening tag has a corresponding closing tag.

    >>> validate_html('<strong>example</strong>')
    True
    >>> validate_html('<strong>example')
    False
    '''

    # HINT:
    # use the _extract_tags function below to generate a list of html tags without any extra text;
    # then process these html tags using the balanced parentheses algorithm from the stack.py file.
    # The main difference between your code and the code from class will be that you will have to keep track of not just the 3 types of parentheses,
    # but arbitrary text located between the html tags.

    try:
        tags = _extract_tags(html)
    except ValueError:
        return False

    stack = []
    for tag in tags:
        if tag.startswith('</'):
            if not stack or stack[-1] != tag[2:-1]:
                return False
            stack.pop()
        else:
            stack.append(tag[1:-1])
    return len(stack) == 0


def _extract_tags(html):
    '''
    This is a helper function for `validate_html`.
    By convention in Python, helper functions that are not meant to be used directly by the user are prefixed with an underscore.

    This function returns a list of all the html tags contained in the input string,
    stripping out all text not contained within angle brackets.

    >>> _extract_tags('Python <strong>rocks</strong>!')
    ['<strong>', '</strong>']
    '''
    tags = []
    i = 0
    while True:
        start = html.find('<', i)
        if start == -1:
            break
        end = html.find('>', start + 1)
        next_open = html.find('<', start + 1)
        if end == -1 or (next_open != -1 and next_open < end):
            raise ValueError('found < without matching >')
        inner = html[start + 1:end].split()
        name = inner[0] if inner else ''
        tags.append('<' + name + '>')
        i = end + 1
    return tags
