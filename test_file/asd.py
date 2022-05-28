import argparse



class FooAction(argparse.Action):
    def __init__(self, option_strings, dest, nargs=None, **kwargs):
        if nargs is not None:
            raise ValueError("nargs not allowed")
        super().__init__(option_strings, dest, **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):
        print('%r %r %r' % (namespace, values, option_string))
        setattr(namespace, self.dest, values)
        print("hasdsa")

parser = argparse.ArgumentParser()
parser.add_argument('--foo', action=FooAction)
parser.add_argument('bar', action=FooAction)





#args = parser.parse_args('1 --foo 2'.split())
#args = parser.parse_args('bar')
#args








