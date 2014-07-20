import inspect

def make_signature(names):
  return inspect.Signature(
      [inspect.Parameter(name, inspect.Parameter.POSITIONAL_OR_KEYWORD)
          for name in names])

class StructMeta(type):
  def __new__(cls, clsname, bases, clsdict):
    clsobj = super().__new__(cls, clsname, bases, clsdict)
    sig = make_signature(clsobj._fields)
    setattr(clsobj, '__signature__', sig)
    return clsobj

class Structure(metaclass=StructMeta):
  __signature__ = make_signature([])
  _fields = []

  def __init__(self, *args, **kwargs):
    bound = self.__signature__.bind(*args, **kwargs)
    for name, val in zip(self._fields, args):
      setattr(self, name, val)

  def __repr__(self):
    return str(self.__dict__)

  def __str__(self):
    return str(self.__dict__)

class Stock(Structure):
  _fields = ['name', 'shares', 'price']

class Points(Structure):
  _fields = ['x', 'y']

class Address(Structure):
  _fields = ['hostname', 'port', 'protocol']

if __name__ == '__main__':
  p = Points(2, 3)
  s = Stock('AGG', 102, 23.43)
  print(p)
  print(s)
