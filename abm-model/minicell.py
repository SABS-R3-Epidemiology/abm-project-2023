from numpy import random

class Minicell():

	'''
	A box where all people are tracked:
		variables:
			events: the list of transitions that has to be handled at the end of the time step (shall we call it queue?)
			s_list: the list of susceptible people
			i_list: the list of infectious people
			r_list: the list of recovered people
			all_list: a list containing people ordered by id
			current_time: the current time of the simulation
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

	def __init__(self, N, P, D, initial = [], name = 'test'):
		
		'''
		setting the epistemic parameters
		'''
		
		self.P = P
		self.D = D
		self.current_time = 0

		'''
		initializing each pearson in the minicell as susceptible
		'''

		for id in range(N):
			self.all_list += [person.Person(str(id),'Susceptible')]
			self.s_list += [person.Person(str(id),'Susceptible')]
			
		'''
		specifying the initial events that have to be handled before running the model
		'''
		
		for event in initial:
			self.handle(event)

		'''
		initializing the .csv file
		'''

		file = open('history_'+ self.name + '.csv', 'a')
		file.write('time\\name,')
		for subject in self.all_list:
			file.write(subject.id + ',')
		file.write('\n')
		file.write(str(self.current_time) + ',')
		for subject in self.all_list:
			file.write(subject.current_status + ',')
		file.write('\n')

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

		statuses = {'Susceptible': self.s_list, 'Infected': self.i_list, 'Removed': self.r_list}
		statuses[str(event['person'].current_status)].remove(event['person'])
		event['person'].current_status = event['status']
		statuses[str(event['person'].current_status)].append(event['person'])

	def update(self, dt):

		current_time += dt

		'''
		update each person's status, persons eventually raise events during this process
		'''
		
		for some_list in [s_list, i_list, r_list]:
			for subject in some_list:
				subject.update(self)

		'''
		handle each event raised in the updating loop above
		(e.g. with) cell.events.append({'person':target,'status':Infected})
		ACHTUNG: read achtung0 above
		'''
		
		for event in self.events:
			self.handle(event)

	def write_csv(self, path):
		file = open('history_'+ self.name + '.csv', 'a')
		file.write(str(self.current_time) + ',')
		for subject in self.all_list:
			file.write(subject.current_status + ',')
		file.write('\n')