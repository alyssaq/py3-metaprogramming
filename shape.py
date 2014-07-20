from debuggly import debug, debugmethods, debugattr

@debugattr
class Dot(object):
  num_inst = 0

  @classmethod
  def get_num_instances(cls):
    return cls.num_inst

  @staticmethod
  def funny():
    print('static method with no reference to cls or self')

  def __init__(self, x=0, y=0, colour='black'):
    Dot.num_inst += 1
    self.x = x
    self.y = y
    self.colour = colour

  @property
  def size(self):
    return self.x + self.y

  @debug(prefix='**')
  def left(self, i=1):
    self.x += i

  def right(self, i=1):
    self.x -= i

  def __repr__(self):
    return self.__dict__

  def __str__(self):
    return str(self.__repr__())

if __name__ == '__main__':
  s = Dot(2, 3)
  s.left(2)
  print(s)
  print('size is:', s.size)
  s.funny()
  print('Num instances: ', Dot.get_num_instances())