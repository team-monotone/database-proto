
class ArgumentException(Exception):

    def __init__(self, pattern):
        message = f'argument "{pattern[0]}/{pattern[1]}" does not satisfied within "{pattern[2]}".'
        super().__init__(message)

class SelfObject(object):

    def __init__(self):
        pass

def _is_satisfied_strongly(pttn, args, kwargs):
    index, keyword, types = pttn
    
    if index >= len(args) and keyword not in kwargs.keys():
        return True
    
    else:
        conditions = []

        for type_ in types:
            if type_ is SelfObject:
                condition = isinstance(args[index], args[0].__class__)
            
            else:
                condition = isinstance(args[index], type_)

            conditions.append(condition)

    return any(conditions)
      
def is_satisfied_strongly(pttns):
    def decorator(method):
        def decorated(*args, **kwargs):
            for pttn in pttns:
                if not _is_satisfied_strongly(pttn, args, kwargs):
                    raise ArgumentException(pttn)

            return method(*args, **kwargs)
        return decorated
    return decorator