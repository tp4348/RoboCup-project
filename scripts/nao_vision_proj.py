from controller import Robot, Motion
import math
import numpy as np
from math import cos, sin
import time

PICKUP_DISTANCE = 0.24
DROPOFF_DISTANCE =0.198
RED = [1.0, 0.0, 0.0]
GREEN = [0.0, 1.0, 0.0]
BLUE = [0.0, 0.0, 1.0]

class Nao (Robot):

    def findAndEnableDevices(self):
        # get the time step of the current world.
        self.timeStep = int(self.getBasicTimeStep()) # milliseconds

    def __init__(self):
        Robot.__init__(self)

        # initialize stuff
        self.findAndEnableDevices()
        self.load_motions()
        self.load_sensors()

    def load_motions(self):
        self.turn_left_60 = Motion("scripts/motions/TurnLeft60.motion")
        self.turn_right_60 = Motion('scripts/motions/TurnRight60.motion')
        self.forward = Motion("scripts/motions/Forwards.motion")
        self.forward_with_box = Motion("scripts/motions/ForwardWithBox.motion")
        self.backward = Motion("scripts/motions/Backwards.motion")
        self.side_step_left = Motion("scripts/motions/SideStepLeft.motion")
        self.side_step_right = Motion("scripts/motions/SideStepRight.motion")
        self.pickup = Motion('scripts/motions/Pickup.motion')
        self.stand = Motion('scripts/motions/Stand.motion')
        self.drop = Motion('scripts/motions/drop.motion')
        self.stand_with_box = Motion("scripts/motions/standwithbox.motion")
        self.turn_with_box = Motion("scripts/motions/turnwithbox.motion")

    def load_sensors(self):
        # camera
        self.cameraTop = self.getDevice("CameraTop")
        self.cameraBottom = self.getDevice("CameraBottom")
        self.cameraTop.enable(4 * self.timeStep)
        self.cameraBottom.enable(4 * self.timeStep)
        self.cameraTop.recognitionEnable(4 * self.timeStep)
        self.cameraBottom.recognitionEnable(4 * self.timeStep)

        # sonars
        self.sonar_right = self.getDevice('Sonar/Right')
        self.sonar_left = self.getDevice('Sonar/Left')
        self.sonar_right.enable(4 * self.timeStep)
        self.sonar_left.enable(4 * self.timeStep)

        # bumpers
        self.right_foot_right_bumper = self.getDevice('RFoot/Bumper/Right')
        self.right_foot_left_bumper = self.getDevice('RFoot/Bumper/Left')
        self.left_foot_right_bumper = self.getDevice('LFoot/Bumper/Right')
        self.left_foot_left_bumper = self.getDevice('LFoot/Bumper/Left')
        self.right_foot_right_bumper.enable(4 * self.timeStep)
        self.right_foot_left_bumper.enable(4 * self.timeStep)
        self.left_foot_right_bumper.enable(4 * self.timeStep)
        self.left_foot_left_bumper.enable(4 * self.timeStep)
        
        # accelerometer
        self.accel = self.getDevice('accelerometer')
        self.accel.enable(4 * self.timeStep)

        # gyro
        self.gyro = self.getDevice('gyro')
        self.gyro.enable(4 * self.timeStep)

    def get_rot_matrix(self, rot_x, rot_y, rot_z):
        a11 = cos(rot_z)*cos(rot_y)
        a12 = cos(rot_z)*sin(rot_y)*sin(rot_x) - sin(rot_z)*cos(rot_x)
        a13 = cos(rot_z)*sin(rot_y)*cos(rot_x) + sin(rot_z)*sin(rot_x)
        a21 = sin(rot_z)*sin(rot_y)
        a22 = sin(rot_z)*sin(rot_y)*sin(rot_x) + cos(rot_z)*cos(rot_x)
        a23 = sin(rot_z)*sin(rot_y)*cos(rot_x) - cos(rot_z)*cos(rot_x)
        a31 = -sin(rot_y)
        a32 = cos(rot_y)*sin(rot_x)
        a33 = cos(rot_y)*cos(rot_x)
        rot_matrix = np.matrix([[a11, a12, a13],
                                [a21, a22, a23],
                                [a31, a32, a33]])

        return rot_matrix

    def transform_gyro(self, x, y, z):
        rot_x = 0.0
        rot_y = 0.0
        rot_z = 0.0

        rot_matrix = self.get_rot_matrix(rot_x, rot_y, rot_z)
        out = np.dot([x, y, z], rot_matrix)
        out = np.squeeze(np.asarray(out))

        return out[0], out[1], out[2]

    def transform_accel(self, x, y, z):
        rot_x = -3.1415927
        rot_y = 0.0
        rot_z = 0.0

        rot_matrix = self.get_rot_matrix(rot_x, rot_y, rot_z)
        out = np.dot([x, y, z], rot_matrix)
        out = np.squeeze(np.asarray(out))

        return out[0], out[1], out[2]

    def transform_bottom_cam(self, x, y, z):
        '''red := x, green := y, blue := z'''
        # Got by inverse quaternion of the camera orientation such that coordinate frame had x forward and y to the left of the robot(z up) + converted to radians
        rot_x = -0.8779005
        rot_y = 0
        rot_z = 1.5707963

        rot_matrix = self.get_rot_matrix(rot_x, rot_y, rot_z)
        out = np.dot([x, y, z], rot_matrix)
        out = np.squeeze(np.asarray(out))

        return out[0], out[1], out[2]

    def transform_top_cam(self, x, y, z):
        '''red := x, green := y, blue := z'''
        # Got by inverse quaternion of the camera orientation such that coordinate frame had x forward and y to the left of the robot(z up) + converted to radians
        rot_x = -1.5498539
        rot_y = -0.000002
        rot_z = 1.5707983

        rot_matrix = self.get_rot_matrix(rot_x, rot_y, rot_z)
        out = np.dot([x, y, z], rot_matrix)
        out = np.squeeze(np.asarray(out))

        return out[0], out[1], out[2]

    def move(self, motion):
        # Start motion and execute it until done
        motion.play()
        while (not motion.isOver()):
            robot.step(self.timeStep)

    def run(self):
        have_object = False
        blue_have_object = False
        counter = 0
        while True:
            
            #print('sonar left: ', self.sonar_right.getValue())
            #print('sonar right: ', self.sonar_right.getValue())
            #print('bumpers RR: ', self.right_foot_right_bumper.getValue())
            #print('bumpers LL: ', self.left_foot_left_bumper.getValue())
            #('bumpers RL: ', self.right_foot_left_bumper.getValue())
            #print('bumpers LR: ', self.left_foot_right_bumper.getValue())
            #print('gyro: ', self.gyro.getValues())
            #print('accel: ', self.accel.getValues())

            # Rotate until you detect an object
            self.move(self.turn_right_60)
            # Try to detect object with Top camera (more precise if the object is more distant)
            objects = self.cameraTop.getRecognitionObjects()
            if len(objects) == 0 and have_object == False:
                
                # If Top camera doesnt detect anything try to detect with Bottom camera
                objects = self.cameraBottom.getRecognitionObjects()

            if objects:
                colors = objects[0].get_colors()

                # Drop off location is BLUE
                if colors == BLUE and have_object:
                    print('Have an object and moving towards to the drop off location')
                    blue_have_object = True
                elif colors == BLUE and not have_object:
                    print('We dont have yet the object to drop it off')
                    continue 
                elif colors == RED and not have_object:
                    print('Lets go pick up the object')
                elif colors == RED and have_object:
                    print('We are already carrying the object')
                    continue

                if objects:

                    first_loop = True
                    x = objects[0].get_position()[0]
                    y = objects[0].get_position()[1]
                    distance = math.sqrt(math.pow(x,2)+math.pow(y,2))
                    print('distance: ', distance)
                    while ((distance > PICKUP_DISTANCE and blue_have_object== False )or counter==0) or (distance > DROPOFF_DISTANCE and blue_have_object== True ):
                        # Update objects all the time since we are moving
                        if not first_loop:
                            objects = self.cameraTop.getRecognitionObjects()
                            if len(objects) == 0:
                                # If Top camera doesnt detect anything try to detect with Bottom camera
                                objects = self.cameraBottom.getRecognitionObjects()
                        first_loop = False
                        if objects:
                            first_object = objects[0]
                            x = first_object.get_position()[0]
                            y = first_object.get_position()[1]
                            z = first_object.get_position()[2]
                            x, y, z = self.transform_bottom_cam(x, y, z)
                            #print('x: ', x)
                            #print('y: ', y)
                            #print('z: ', z)

                            distance = math.sqrt(math.pow(x,2)+math.pow(y,2))
                            print('distance: ', distance)
                            angle = math.atan2(x,y)
                            print('angle: ', angle)

                            # First turn towards the box
                            # TODO: Need smaller angle turns!

                            # Go to the box
                            # TODO: Need smaller steps forward!
                            print(colors)
                            if have_object and colors == BLUE:
                                self.move(self.forward)

                            elif not have_object:
                                self.move(self.forward)
                                counter+=1
                            elif have_object and not colors == BLUE:
                                print("lost sight of dropoff box")
                                continue
                            
                        else:
                            print('Lost sight ob object. Back to searching...')
                            distance = PICKUP_DISTANCE - 1  # Break out of loop 

                    if colors == BLUE: 
                        print('Dropping of the object')
                        self.move(self.drop)
                        self.move(self.backward)
                        self.move(self.backward)
                        counter =0
                        blue_have_object = False
                        have_object = False
                    elif colors == RED:
                        self.move(self.stand)
                        self.move(self.pickup)
                        print('Picking up the object')    
                        have_object = True
            else:
                print('No Object detected')

# create the Robot instance and run main loop
robot = Nao()
robot.run()
