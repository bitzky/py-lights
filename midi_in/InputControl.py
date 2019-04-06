
class InputControl:
	def __init__(self, action, type, key, setting, inverse=False):
		self.action = action
		self.type = type
		self.inverse = inverse
		self.key = key
		self.setting = setting

	def trigger(self, params):
		pass

	def toggle(self, params):
		pass

	def hold(self, params, visible):
		pass
	
	def knob(self, params, val):
		self.action.update(self.setting, val)