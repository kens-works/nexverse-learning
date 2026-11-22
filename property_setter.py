class Bullet:
  allowed_engine_cc = ('349cc', '499cc', '648cc')
  def __init__(self, color, engine_cc):
    self._color = color
    self.engine_cc1 = engine_cc
    
  def service_checkup (self):
    print(f"{self.color} bullet of {engine_cc} has be registered for service checkup")

  # Python only triggers a @property or @setter when the exact attribute name matches: engine_cc1 from line 5
  @property
  def engine_cc1(self):
    return self._engine_cc1

  @engine_cc1.setter
  def engine_cc1(self, engine_cc1):
    if engine_cc1 not in self.allowed_engine_cc:
      raise ValueError(f"Select from supported engine capacity: {self.allowed_engine_cc}")
    self._engine_cc1 = engine_cc1
    # Underscore stores the value without re-calling the setter

  @property
  def color(self):
    return self._color
  
red_bullet = Bullet("red", "349cc")
print(red_bullet.color)
print(red_bullet._engine_cc1)

red_bullet.color = "black"
#color become read-only field as there is no setter and check the self._color attribute inside __init__() method
print(red_bullet.color)



# When to use it:

# Validation: Preventing bad data (like negative price, empty color, or fuel_level > 100).

# Read-only fields: Leaving out the setter makes an attribute unchangeable (like a bike's chassis_number or engine_cc after manufacturing).

# Future-proofing: You can start your project with simple self.color today. If your boss adds a rule six months later ("only allow official colors!"), you can wrap color in @property and zero lines of existing code that wrote red_bullet.color = "black" will break.