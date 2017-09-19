from consts import Vector


class Sterring(object):

    def __init__(self):
        self.linear = Vector(0, 0)
        self.angular = 0

        self.velocity = Vector(0, 0)
        self.rotation = 0

class Kinematic(object):

    def __init__(self, position=None, max_speed=0, max_acceleration=0, weight=0):
        self.position = Vector(0, 0)
        self.direction = 0.0 # orientation
        self.velocity = Vector(0,0)
        self.rotation = 0.0

        self.angularVelocity = 0.0

        # character data
        self.max_speed = max_speed
        self.max_acceleration = max_acceleration
        self.weight = weight
        self.movement = None
        self.sterring = Sterring()

    def apply(self, steer, time):
        # Update the position and direction
        self.position += self.velocity * time
        self.direction += self.rotation * time

        # and velocity and rotation
        self.velocity += steer.linear * time
        self.direction += steer.angular * time

        if self.velocity.get_length() > self.max_speed:
            self.velocity = self.velocity.normalized() * self.max_speed


    def update(self, deltaTime):
        if self.movement:
            steer = self.movement.sterring()
            self.apply(steer, deltaTime)

            # print self.position, self.rotation, self.velocity, deltaTime, self.max_acceleration
