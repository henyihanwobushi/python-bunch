from bunch import bunch

if __name__ == '__main__':
    d = bunch(a=1, b=2)
    print d.a, d.b, d['a']
