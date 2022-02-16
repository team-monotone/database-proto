
class ArgumentException(Exception):

    def __init__(self, pattern):
        message = f'argument "{pattern[0]}/{pattern[1]}" does not satisfied within "{pattern[2]}".'
        super().__init__(message)

class Itself(object):

    def __init__(self):
        pass

def _is_satisfied_strongly(pttn, args, kwargs):
    index, keyword, types = pttn
    
    if index > len(args) and keyword not in kwargs.keys():
        return True
    
    else:
        condition = [
            isinstance(args[index], args[0].__class__) \
                if type_ is Itself \
                else isinstance(args[index], type_)
            for type_ in types
            ]

    return any(condition)
      
def is_satisfied_strongly(pttns):
    def decorator(method):
        def decorated(*args, **kwargs):
            for pttn in pttns:
                if not _is_satisfied_strongly(pttn, args, kwargs):
                    raise ArgumentException(pttn)

            return method(*args, **kwargs)
        return decorated
    return decorator