# Points to remember about static
# Static attributes are created at class level.
# Static attributes are accessed using ClassName.
# Static attributes are object independent. We can access them without creating instance (object) of the class in which they are defined.
# The value stored in static attribute is shared between all instances(objects) of the class in which the static attribute is defined.

class Lion:
  __water_source="well in the circus"

  def __init__(self,name, gender):
      self.__name=name
      self.__gender=gender

  def drinks_water(self):
      print(self.__name,
      "drinks water from the",Lion.__water_source)

  @staticmethod
  def get_water_source():
      return Lion.__water_source

simba=Lion("Simba","Male")
simba.drinks_water()
print( "Water source of lions:",Lion.get_water_source())