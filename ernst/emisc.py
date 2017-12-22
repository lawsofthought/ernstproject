'''
Miscellaneous utilities

'''

def assertEqual(lhs, rhs):
    '''Assert that one thing is equal to another thing.'''
    assert lhs==rhs, '%s is not %s' % (lhs, rhs)

    return True


def assertTrue(statement):
    '''Assert that something is the case.'''
    assert statement, '%s is not True' % statement

    return True
