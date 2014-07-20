import functools

def debug(func=None, *, prefix=''):
  if func is None:
    return functools.partial(debug, prefix=prefix)

  msg = prefix + func.__qualname__

  @functools.wraps(func)
  def wrapper(*args, **kwargs):
    print(msg)
    return func(*args, **kwargs)
  return wrapper

def debugmethods(cls):
  for key, val in vars(cls).items():
    if callable(val):
      setattr(cls, key, debug(val))
  return cls

def debugattr(cls):
  orig_getattr = cls.__getattribute__

  def __getattribute__(self, name):
    print('Get:', name)
    return orig_getattr(self, name)
  cls.__getattribute__ = __getattribute__

  return cls
