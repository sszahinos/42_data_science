import time
import os

def log(func):
	def write_log(text):
		f = open("machine.log", "a")
		f.write(text)
		f.close()

	def log_register(*args, **kwargs):
		start_time = time.time()
		result = func(*args, **kwargs)
		total_time = time.time() - start_time
		if total_time % 10 == 0:
			total_time = "{:.3f} ms".format(float(total_time))
		else:
			total_time = "{:.3f} s ".format(float(total_time))
		write_log("({})Running: {:<18} [exec-time = {} ]\n".format(
			os.getlogin(), func.__name__, total_time))
		return result

	return log_register

class CoffeeMachine():
	water_level = 100
	
	@log
	def start_machine(self):
		if self.water_level > 20:
			return True
		else:
			print("Please add water!")
		return False
	
	@log
	def boil_water(self):
		return "boiling..."
	
	@log
	def make_coffee(self):
		if self.start_machine():
			for _ in range(20):
				time.sleep(0.1)
				self.water_level -= 1
			print(self.boil_water())
			print("Coffee is ready!")

	@log
	def add_water(self, water_level):
		time.sleep(1)
		self.water_level += water_level
		print("Blub blub blub...")

if __name__ == "__main__":
	machine = CoffeeMachine()
	for i in range(0, 5):
		machine.make_coffee()
	machine.make_coffee()
	machine.add_water(70)
