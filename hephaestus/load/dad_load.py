def load(*args):
    """Placeholder, change, rename, remove... """
    for arg in args:
        className = arg.__class__.__name__
        if className == 'str':
            print(arg)
        else:
            print(className)
