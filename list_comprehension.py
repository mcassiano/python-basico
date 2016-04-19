class Event:

	def __init__(self, name, price):
		self.name = name
		self.price = price

	def __str__(self):
		return "{} ({})".format(self.name, self.price)

events = []

cbsoft = Event('CB Soft', 100.00)
thedevconf = Event('The Developers Conference', 150.00)
marksbirthday = Event('Aniversário do Zuck', 0.00)

events.append(cbsoft)
events.append(thedevconf)
events.append(marksbirthday)

print(thedevconf)
print(marksbirthday)

prices = [event.price for event in events]
print(prices)

less_than_20 = [event.name for event in events if event.price < 20]
print(less_than_20)