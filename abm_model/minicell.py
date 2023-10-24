from abm_model.status import *
from abm_model.person import *

class Minicell():

	'''
	A box where all people are tracked:
		attributes:
			events: the list of transitions that has to be handled at the end of the time step (shall we call it queue?)
			s_list: the list of susceptible people
			i_list: the list of infectious people
			r_list: the list of recovered people
			all_list: a list containing people ordered by id
			current_time: the current time of the simulation
			name: the name of the minicell
			path: the path where dats are stored
		methods:
			update(dt): changes the status of each pearson into the minicell coherently with the model
				inputs: dt: the time lenght of the step to update
				output: None
			write_csv(path): upload the hystory on the file path.csv
				inputs: path: the path of the file where the hystory is being transcribed
				output: None
			handle(event): update the evets that are to be handled at the end of the time step
				inputs: event: the event to handle
				output: None
	'''

	def __init__(self, N: int = 100, P: float = 0.01, D: float = 1, initial = {}, name = 'test', path: str = 'data'):
	
		'''
		setting the epistemic parameters
		'''
		
		self.P = P
		self.D = D
		self.current_time = 0
		self.events = []
		self.s_list = []
		self.i_list = []
		self.r_list = []
		self.all_list = []
		self.name = name
		self.path = path

		'''
		initializing each pearson in the minicell as susceptible
		'''

		statuses = {'Susceptible': self.s_list, 'Infected': self.i_list, 'Recovered': self.r_list}
		for id in range(N):
			if id in initial:
				my_person = Person(str(id), initial[id])
				statuses[str(initial[id])].append(my_person)
			else:
				my_person = Person(str(id), Susceptible())
				self.s_list.append(my_person)
			self.all_list.append(my_person)

		'''
		initializing the .csv files
		'''

		file = open(self.path + '/plot_data_'+ self.name + '.csv', 'w')
		file.write('time\\stat,')
		for some_stat in ['Susceptible', 'Infected', 'Recovered']:
			file.write(some_stat[0] + ',')
		file.write('\n')
		file.write(str(self.current_time) + ',')
		for some_list in [self.s_list, self.i_list, self.r_list]:
			file.write(str(len(some_list)) + ',')
		file.write('\n')
		file.close()
		

	def handle(self, event):

		'''
		an event is a dictionary with keys:
			'person': the target of the event
			'status': the new status specified
		ACHTUNG0:
			THIS MAY CAUSE COLLISIONS IF ONE PERSON IS INFECTED
			WE SUGGEST ADDING AN HANDLE METHOD TO THE STATUS CLASS THAT TO BE CALLED BY A MINICELL
			(e.g. with) event['person'].status.handle(event['status'])
			WE SUGGEST ADDING A RAISING METHOD TO THE MINICELL CLASS THAT CAN BE CALLED BY A PERSON
			(e.g. with) cell.rising(event)
			IN THIS WAY COLLISIONS CAN BE HANDLED TOGETHER
		'''

		statuses = {'Susceptible': self.s_list, 'Infected': self.i_list, 'Recovered': self.r_list}
		statuses[str(event['person'].status)].remove(event['person'])
		event['person'].status = event['status']
		statuses[str(event['person'].status)].append(event['person'])

	def write_csv(self):

		'''
		ACHTUNG1: if self.all_list is modified, the .csv file will not be reliable
		'''
		
		file = open(self.path + '/plot_data_'+ self.name + '.csv', 'a')
		file.write(str(self.current_time) + ',')
		for some_list in [self.s_list, self.i_list, self.r_list]:
			file.write(str(len(some_list)) + ',')
		file.write('\n')
		file.close()

	def update(self, dt: float = 1):

		self.current_time += dt

		'''
		update each person's status, persons eventually raise events during this process
		'''
		
		for some_list in [self.s_list, self.i_list, self.r_list]:
			for subject in some_list:
				subject.update(self, dt)

		'''
		handle each event raised in the updating loop above
		(e.g. with) cell.events.append({'person':target,'status':Infected})
		ACHTUNG2: read achtung0 above
		'''
		
		for event in self.events:
			self.handle(event)
		self.events = []
		self.write_csv()

