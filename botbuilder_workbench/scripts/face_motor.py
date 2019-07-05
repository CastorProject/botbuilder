#!/usr/bin/env python
import rospy
import time
from servo import OnohatServo


class FaceMotor(object):
	def __init__(self):
		rospy.init_node("motor_face_handler")
		self.rate = rospy.Rate(10) # 10hz

		
	def set_servos(self):
		#mouth motors
		self.mouth1 = OnohatServo()
		self.mouth2 = OnohatServo()
		self.mouth3 = OnohatServo()
		#eyeled
		
		#set id's
		self.mouth1.set_motor_id(0)
		self.mouth2.set_motor_id(1)
		self.mouth3.set_motor_id(2)
		
		#set actuation ranges
		self.mouth1.set_actuation_range(min =790, origin =800, max = 1101)
		self.mouth2.set_actuation_range(min =790, origin =1200, max = 1700)  #inverted 1700 is sad, 790 is happy
		self.mouth3.set_actuation_range(min =799, origin =1100, max = 1501) #
	
		#set origin position
		self.mouth1.set_origin_position()
		self.mouth2.set_origin_position()
		self.mouth3.set_origin_position()
	
	def activate_mosfet(self, val):
		#call service to activate onohat 
		pass	
	
	#expressions
	def set_happy(self):
		self.mouth1.set_position(command ={'value':900})
		self.mouth2.set_position(command ={'value':800})
		self.mouth3.set_position(command ={'value':1400})


	def set_sad(self):
		self.mouth1.set_position(command ={'value':800})
		self.mouth2.set_position(command ={'value':1600})
		self.mouth3.set_position(command ={'value':800})
	
	def set_surprise(self):
		self.mouth1.set_position(command ={'value':1100})
		self.mouth2.set_position(command ={'value':1600})
		self.mouth3.set_position(command ={'value':800})

	def talk(self):
		self.mouth2.set_position(command ={'value':1600})
		self.mouth3.set_position(command ={'value':800})
		for i in range(10):
			self.mouth1.set_position(command ={'value':1000})
			time.sleep(0.2)
			self.mouth1.set_position(command ={'value':850})
			time.sleep(0.2)

	
	def loop(self):
		print("face motor node main loop")
		time.sleep(5)
		fm.set_happy()
		time.sleep(5)
		self.mouth1.set_origin_position()
		self.mouth2.set_origin_position()
		self.mouth3.set_origin_position()
		time.sleep(5)
		self.set_sad()
		time.sleep(5)
		self.set_surprise()
		time.sleep(5)
		self.talk()
		self.rate.sleep()

if __name__ == '__main__':

	fm = FaceMotor()

	fm.set_servos()

	while not (rospy.is_shutdown()):
		

		
		
		fm.loop()

