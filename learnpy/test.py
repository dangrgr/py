#!/c/Python27/python

class NetworkDevice(object):
	def __init__(self, ip, username, password):
		self.ip = ip
		self.username = username
		self.password = password

	def connect_to_device(self):
		...

	def enter_enable_mode(self):
		...

	def show_version(self):
		...