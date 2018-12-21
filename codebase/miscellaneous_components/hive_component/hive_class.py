from .hiveconnector_subcomponent import hiveconnector_module as HiveConnector


class DefineHiveInterface:

	def __init__(self):

		self.hiveconnector = HiveConnector.createhiveconnector()

		self.deviceids = self.hiveconnector.getdevices()

		print(self.deviceids)