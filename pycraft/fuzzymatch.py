"""Implement some basic fuzzy-name matching for ease of use"""
class FuzzyNamespace(object):
    def __init__(self, source):
        self.source = source
    def __getattr__(self,key):
        return resolve_name(key, self.source)

def as_constant(name):
    """Convert the name to a python constant"""
    return name.upper().replace(' ','_').replace('-','_')

def similar_names(name, lookup_space,first=False):
    """Look for all names similar to name in namespace"""
    seen = set()
    if name in lookup_space:
        seen.add(name)
        yield name
    for key in lookup_space:
        if name in key:
            if key not in seen:
                seen.add(key)
                yield key

def resolve_name(name,lookup_space):
    """Fuzzy lookup of name in name-space"""
    if hasattr(name,'__call__'):
        return name(lookup_space)
    if hasattr(name,'id'):
        return name
    elif isinstance(name,int):
        return name 
    elif isinstance(name, str):
        test = as_constant(name)
        if test in lookup_space:
            return lookup_space[test]
        else:
            possible = list(similar_names(test,lookup_space))
        if len(possible) == 1:
            return lookup_space[possible[0]]
        elif possible:
            raise NameError(
                name,
                'Possibly you meant: %s'%(
                    ', '.join(sorted(possible))
                )
            )
        else:
            raise NameError(
                name,'Did not find any names like that'
            )
        raise TypeError(
        "Expected an integer, Block/Entity, or string name, got %r"
        %(
            name,
        )
    )
