from consts import Vector
from kinematic import Sterring
from math import atan2, degrees


class Seek(object):

    def __init__(self, origin, target):
        self.origin = origin
        self.target = target

    def sterring(self):
        steer = Sterring()
        steer.linear = self.target.position - self.origin.position
        steer.linear = steer.linear.normalized()

        steer.linear *= self.origin.max_acceleration
        steer.angular = 0

        if self.origin.velocity.get_length() > 0:
            self.origin.direction = degrees(atan2(-self.origin.velocity.x, self.origin.velocity.y)) # - 90

        return steer


class Flee(object):

    def __init__(self, origin, target):
        self.origin = origin
        self.target = target

    def sterring(self):
        steer = Sterring()
        steer.linear = self.origin.position - self.target.position
        steer.linear = steer.linear.normalized()

        steer.linear *= self.origin.max_acceleration
        steer.angular = 0

        return steer


class Arrive(object):

    def __init__(self, origin, target):
        self.origin = origin
        self.target = target
        self.time_to_target = 0.1
        self.target_radius = 6
        self.slow_radius = 4

    def sterring(self):
        steer = Sterring()
        direction = target.position - origin.position
        distance = direction.get_length()

        if distance < target_radius:
            return None
        else:
            target_speed = max_speed * distance / slow_radius

        target_velocity = direction
        target_velocity = target_velocity.normalized()
        target_velocity *= target_speed

        steer.linear = target_velocity - origin.velocity
        steer.linear /= time_to_target

        steer.angular = 0
        return steer


        steer.linear = self.origin.position - self.target.position
        steer.linear = steer.linear.normalized()

        steer.linear *= self.origin.max_acceleration
        steer.angular = 0

        return steer
