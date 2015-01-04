class bunch(dict):
    def __init__(self, *args, **kwds):
        super(bunch, self).__init__(*args, **kwds)
        self.__dict__ = self
if __name__ == '__main__':
    t = bunch(a=1, b=2)
    print repr(t)
