import math


def nature_boost(nature, name):
	val1 = 0
	val2 = 0
	gen_stat = {'hp': 1, 'attack': 1, 'defense': 1, 'spatk': 1, 'spdef': 1, 'speed': 1}
	nat_matrix = [['Hardy', 'Lonely', 'Adamant', 'Naughty', 'Brave'],
				  ['Bold', 'Docile', 'Impish', 'Lax', 'Relaxed'],
				  ['Modest', 'Mild', 'Bashful', 'Rash', 'Quiet'],
				  ['Calm', 'Gentle', 'Careful', 'Quirky', 'Sassy'],
				  ['Timid', 'Hasty', 'Jolly', 'Naive', 'Serious']]
	for i in range(5):
		for j in range(5):
			if nat_matrix == nature:
				val1 = i
				val2 = j
	if val1 != val2:
		gen_stat[list(gen_stat.keys())[val1]] = 1.1
		gen_stat[list(gen_stat.keys())[val2]] = 0.9
	return gen_stat[name]


def calculate_stat(stat,level,nature):
	stat_name = stat.name
	evs = stat.EVs
	ivs = stat.IVs
	base = stat.Base

	def formula(name):
		if name == "hp":
			a, b = 100, 10
			return ()
		else:
			a, b = 0, 5
			return

	if stat_name == 'hp':
		value = formula(stat_name)*nature_boost(nature, stat_name)
		return math.floor(value)
	elif stat_name == 'attack':
		pass
	elif stat_name == 'defense':
		pass
	elif stat_name == 'spatk':
		pass
	elif stat_name == 'spdef':
		pass
	elif stat_name == 'speed':
		pass


def total_stats(self):
	return {
		'Base': self.hp['Base']+self.attack['Base']+self.defense['Base']+self.spatk['Base']+self.spdef['Base']+self.speed['Base'],
		'IVs': self.hp['IVs']+self.attack['IVs']+self.defense['IVs']+self.spatk['Base']+self.spdef['IVs']+self.speed['IVs'],
		'EVs': self.hp['EVs']+self.attack['EVs']+self.defense['EVs']+self.spatk['EVs']+self.spdef['EVs']+self.speed['EVs']
	}


class Description:
	def __init__(self):
		self.origin_game = None
		self.battle_version = None
		self.met_location = None
		self.ball = None
		self.met_level = None
		self.met_date = None
		self.fateful_encounter = None
		self.as_egg = None
class Pokemon_Stats:
	from random import random
	def __init__(self):
		self.lvl = 0
		self.exp = 0
		self.nature = None
		self.hp = {'name':'hp','Base':0,'IVs':0,'EVs':0}
		self.attack = {'name':'attack','Base':0,'IVs':0,'EVs':0}
		self.defense = {'name':'defense','Base':0,'IVs':0,'EVs':0}
		self.spatk = {'name':'spatk','Base':0,'IVs':0,'EVs':0}
		self.spdef = {'name':'spdef','Base':0,'IVs':0,'EVs':0}
		self.speed = {'name':'speed','Base':0,'IVs':0,'EVs':0}
		self.hp['Stats']=self.calculate_stat(self.hp,self.lvl,self.nature)
		self.attack['Stats']=self.calculate_stat(self.attack,self.lvl,self.nature)
		self.defense['Stats']=self.calculate_stat(self.defense,self.lvl,self.nature)
		self.spatk['Stats']=self.calculate_stat(self.spatk,self.lvl,self.nature)
		self.spdef['Stats']=self.calculate_stat(self.spdef,self.lvl,self.nature)
		self.speed['Stats']=self.calculate_stat(self.speed,self.lvl,self.nature)
		self.total = self.total()
	#Editar
	def random_ivs(self):
		self.hp['IVs'] = 0
		self.attack['IVs'] = 0
		self.defense['IVs'] = 0
		self.spatk['IVs'] = 0
		self.spdef['IVs'] = 0
		self.speed['IVs'] = 0
		self.hp['Stats']=self.calculate_stat(self.hp,self.lvl,self.nature)
		self.attack['Stats']=self.calculate_stat(self.attack,self.lvl,self.nature)
		self.defense['Stats']=self.calculate_stat(self.defense,self.lvl,self.nature)
		self.spatk['Stats']=self.calculate_stat(self.spatk,self.lvl,self.nature)
		self.spdef['Stats']=self.calculate_stat(self.spdef,self.lvl,self.nature)
		self.speed['Stats']=self.calculate_stat(self.speed,self.lvl,self.nature)
		self.total = self.total()
	# Editar
	def random_evs(self):
		self.hp['IVs'] = 0
		self.attack['IVs'] = 0
		self.defense['IVs'] = 0
		self.spatk['IVs'] = 0
		self.spdef['IVs'] = 0
		self.speed['IVs'] = 0
		self.hp['Stats']=self.calculate_stat(self.hp,self.lvl,self.nature)
		self.attack['Stats']=self.calculate_stat(self.attack,self.lvl,self.nature)
		self.defense['Stats']=self.calculate_stat(self.defense,self.lvl,self.nature)
		self.spatk['Stats']=self.calculate_stat(self.spatk,self.lvl,self.nature)
		self.spdef['Stats']=self.calculate_stat(self.spdef,self.lvl,self.nature)
		self.speed['Stats']=self.calculate_stat(self.speed,self.lvl,self.nature)
		self.total = self.total()


class Pokemon(Description,Pokemon_Stats):
	def __init__(self):
		self.gender = None
		self.pid = None
		self.specie = None
		self.nickname = None
		self.form = None
		self.item = None
		self.ability = None
		self.friendship = None
		self.lang = None
		self.is_egg = None
		self.infected = None
		self.cured = None
		self.height = None
		self.weight = None
		self.desc = Description()

