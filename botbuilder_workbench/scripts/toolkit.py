#!/usr/bin/env python
import rospy
import time
#

from actuator import Actuator
from servo import *
from module import Module



class Toolkit(object):
	def __init__(self):
		self.COMPONENTS = {'base_actuator': Actuator,    #base class for the actuator
	                           'dmx_servo'    : DmxServo,    #custom servo class for dynamixel motor
	                           'onohat_servo' : OnohatServo, #custom servo class for onohat motor controller
	                           'base_module'  : Module       #base class for module
	                           }
	
	def  add_component(self, identifier, custom_class):
		self.COMPONENTS[identifier] = custom_class		


	def get_components(self):
		return self.COMPONENTS

	def delete_component(self, identifier):
		if identifier in self.COMPONENTS:
			del self.COMPONENTS[identifier]
			print "component removed"
		else:
			print "component is not exisiting"



			
