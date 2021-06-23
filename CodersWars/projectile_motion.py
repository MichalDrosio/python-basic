# You must create a class, Projectile, which takes in 3 arguments when initialized:
#
# starting height (0 ≤ h0 < 200)
# starting velocity (0 < v0 < 200)
# angle of the projectile when it is released (0° < a < 90°, measured in degrees).
# All units for distance are feet, and units for time are seconds.
#
# Note: Some solutions were invalidated because I
# added tests for situations where the starting height is 0,
# in which case the equation for height would be in the form h(t) = -16.0t^2 + vt
# where v represents the initial vertical velocity.
#
# ```math \large h = -16t^2 + vt + h_0 ```
# In the above equation, h represents the height of the projectile after t seconds;
# v represents the initial vertical velocity; and h0 represents the starting height.
#
# You need to write the following methods for the Projectile class.
# In Crystal, the arguments passed when the object is initialized will always be of the type Float64,
# and in Java/Scala/Kotlin/Dart/C#, they will be int/Ints.
#
# A height_eq, heightEq, or HeightEq method,
# which returns the equation for height of the projectile as a function of time.
# [takes in nothing, returns a String]
# A horiz_eq, horizEq, or HeightEq method,
# which returns the equation for the horizontal position of the projectile as a function of time.
# [takes in nothing, returns a String]
# A height or Height method,
# which takes in an argument t and calculates the height of the projectile in feet. [
# takes in a double, returns a double]
# A horiz or Horiz method,
# which also takes in an argument t and calculates the horizontal distance that the projectile has traveled.
# [takes in a double, returns a double]
# A landing or Landing method which returns
# the point at which the projectile lands on the ground, in the form [x, y, t].
# (y should always be 0). [takes in nothing, returns an array of doubles]
# EVERYTHING, including values in the equations appearing as coefficients,
# must be rounded to THREE decimal places.
# However, if the value is whole, only show one decimal place
# (for example => -16 becomes -16.0, not -16.000).
# But ensure that you DO NOT use the three-decimal-place rounded values for calculations.
# Otherwise, you will find yourself getting answers CLOSE to the correct one but slightly off.
#
# You also need to define instance variables as needed. These will not be tested.
#
# Examples
# Projectile Motion ExampleThis example shows
# the initial vertical and horizontal velocity when a projectile is fired at 2 ft/s.
#
# p = Projectile(5, 2, 45) #=> a projectile starting at 5 ft above the ground,
# traveling initially at 2 ft/s, and at an angle of 45 degrees with the horizontal (shown in the triangle above)
# p.height_eq() #=> "h(t) = -16.0t^2 + 1.414t + 5.0"
#   # 1.414 = 2sin(45°)
# p.horiz_eq() #=> "x(t) = 1.414t"
#   # 1.414 = 2cos(45°)
# p.height(0.2) #=> 4.643 (Calculation: -16(0.2)^2 + (2sin(45°))(0.2) + 5)
# p.horiz(0.2) #=> 0.283 (Calculation: 2cos(45°) * 0.2)
# p.landing() #=> [0.856, 0, 0.605] (After 0.605 seconds (t = 0.605),
# the particle has landed on the ground (y = 0), and is 0.856 ft horizontally
# (x = 0.856) away from the release point.)
import math


class Projectile:
    def __init__(self, h0, v0, a):
        self.h0 = h0
        self.v0 = v0
        self.a = a
        self.b = self.v0 * math.sin(math.pi * self.a/180.0)
        self.c = self.v0 * math.cos(math.pi * self.a/180.0)

    def height_eq(self):
        if self.h0 == 0:
            return f'h(t) = -16.0t^t + {round(self.b, 3)}t'
        else:
            return f'h(t) = -16.0t^t + {round(self.b, 3)}t + {self.h0:0.1f}'

    def horizon_eq(self):
        return f'x(t) = {round(self.c, 3)}t'

    def height(self, t):
        return round(-16*t**2 + self.b * t + self.h0, 3)

    def horiz(self, t):
        return round(self.c * t, 3)

    def landing(self):
        t = (self.b + (self.b**2 + 64 * self.h0)**0.5)/32
        h = self.c * t
        return [round(h, 3), 0, round(t, 3)]