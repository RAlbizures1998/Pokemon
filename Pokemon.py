import math
import random


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


class Met:
	def __init__(self, og_game: str = "Sword", met_loc: str = "Route 1", ball: str = "Poke bal", met_lvl: int = 5, met_date: str = "01-01-1998", fate_enc: bool = False, as_egg: bool = False):
		self.origin_game = og_game
		self.met_location = met_loc
		self.ball = ball
		self.met_level = met_lvl
		self.met_date = met_date
		self.fateful_encounter = fate_enc
		self.as_egg = as_egg


# Base Points, gender prob and learned moves
class Specie:
	def __init__(self, name: str = "Bulbasaur"):
		self.name = name
		self.ability_index = 0
		self.gender_index = 0
		self.gender = ["male", "female", "none"]
		self.base = {'hp': 0, 'attack': 0, 'defense': 0, 'spatk': 0, 'spdef': 0, 'speed': 0}

		if name == "Bulbasaur":
			self.type = ["Grass", "Poison"]
			self.ability = ["Overgrow", "Overgrow", "Chlorophyll"]
			self.base = {'hp': 45, 'attack': 49, 'defense': 49, 'spatk': 65, 'spdef': 65, 'speed': 45}
		elif name == "Ivysaur":
			self.type = ["Grass", "Poison"]
			self.ability = ["Overgrow", "Overgrow", "Chlorophyll"]
		elif name == "Venusaur":
			self.type = ["Grass", "Poison"]
			self.ability = ["Overgrow", "Overgrow", "Chlorophyll"]
		elif name == "Charmander":
			self.type = ["Fire"]
			self.ability = ["Blaze", "Blaze", "Solar Power"]
		elif name == "Charmeleon":
			self.type = ["Fire"]
			self.ability = ["Blaze", "Blaze", "Solar Power"]
		elif name == "Charizard":
			self.type = ["Fire", "Flying"]
			self.ability = ["Blaze", "Blaze", "Solar Power"]
		elif name == "Squirtle":
			self.type = ["Water"]
			self.ability = ["Torrent", "Torrent", "Rain Dish"]
		elif name == "Wartortle":
			self.type = ["Water"]
			self.ability = ["Torrent", "Torrent", "Rain Dish"]
		elif name == "Blastoise":
			self.type = ["Water"]
			self.ability = ["Torrent", "Torrent", "Rain Dish"]
		elif name == "Caterpie":
			self.type = ["Bug"]
			self.ability = ["Shield Dust", "Shield Dust", "Run Away"]
		elif name == "Metapod":
			self.type = ["Bug"]
			self.ability = ["Shed Skin", "Shed Skin", "Shed Skin"]
		elif name == "Butterfree":
			self.type = ["Bug", "Flying"]
			self.ability = ["Compound Eyes", "Compound Eyes", "Tinted Lens"]
		elif name == "Weedle":
			self.type = ["Bug", "Poison"]
			self.ability = ["Shield Dust", "Shield Dust", "Run Away"]
		elif name == "Kakuna":
			self.type = ["Bug", "Poison"]
			self.ability = ["Shed Skin", "Shed Skin", "Shed Skin"]
		elif name == "Beedrill":
			self.type = ["Bug", "Poison"]
			self.ability = ["Swarm", "Swarm", "Sniper"]
		elif name == "Pdigey":
			self.type = ["Normal", "Flying"]
			self.ability = ["Keen Eye", "Tangled Feet", "Big Pecks"]
		elif name == "Pidgeotto":
			self.type = ["Normal", "Flying"]
			self.ability = ["Keen Eye", "Tangled Feet", "Big Pecks"]
		elif name == "Pidgeot":
			self.type = ["Normal", "Flying"]
			self.ability = ["Keen Eye", "Tangled Feet", "Big Pecks"]
		elif name == "Rattata":
			self.type = ["Normal"]
			self.ability = ["Run Away", "Guts", "Hustle"]
		elif name == "Raticate":
			self.type = ["Normal"]
			self.ability = ["Run Away", "Guts", "Hustle"]
		elif name == "Separow":
			self.type = ["Normal", "Flying"]
			self.ability = ["Keen Eye", "Keen Eye", "Sniper"]
		elif name == "Fearow":
			self.type = ["Normal", "Flying"]
			self.ability = ["Keen Eye", "Keen Eye", "Sniper"]
		elif name == "Eakans":
			self.type = ["Poison"]
			self.ability = ["Intimidate", "Shed Skin", "Unnerve"]
		elif name == "Arbok":
			self.type = ["Poison"]
			self.ability = ["Intimidate", "Shed Skin", "Unnerve"]
		elif name == "Pikachu":
			self.type = ["Electric"]
			self.ability = ["Static", "Static", "Lightning Rod"]
		elif name == "Raichu":
			self.type = ["Electric"]
			self.ability = ["Static", "Static", "Lightning Rod"]
		elif name == "Sandshrew":
			self.type = ["Ground"]
			self.ability = ["Sand Veil", "Sand Veil", "Sand Rush"]
		elif name == "Sandslash":
			self.type = ["Ground"]
			self.ability = ["Sand Veil", "Sand Veil", "Sand Rush"]
		elif name == "Nidoran f":
			self.type = ["Poison"]
			self.ability = ["Poison Point", "Rivalry", "Hustle"]
		elif name == "Nidorina":
			self.type = ["Poison"]
			self.ability = ["Poison Point", "Rivalry", "Hustle"]
		elif name == "Nidoqueen":
			self.type = ["Poison", "Earth"]
			self.ability = ["Poison Point", "Rivalry", "Sheer Force"]
		elif name == "Nidoran m":
			self.type = ["Poison"]
			self.ability = ["Poison Point", "Rivalry", "Hustle"]
		elif name == "Nidorino":
			self.type = ["Poison"]
			self.ability = ["Poison Point", "Rivalry", "Hustle"]
		elif name == "Nidoking":
			self.type = ["Poison", "Earth"]
			self.ability = ["Poison Point", "Rivalry", "Sheer Force"]
		elif name == "Clefairy":
			self.type = ["Fairy"]
			self.ability = ["Cute Charm", "Magic Guard", "Friend Guard"]
		elif name == "Clefable":
			self.type = ["Fairy"]
			self.ability = ["Cute Charm", "Magic Guard", "Unaware"]
		elif name == "Vulpix":
			self.type = ["Fire"]
			self.ability = ["Flash Fire", "Flash Fire", "Drought"]
		elif name == "Ninetales":
			self.type = ["Fire"]
			self.ability = ["Flash Fire", "Flash Fire", "Drought"]
		elif name == "Jigglypuff":
			self.type = ["Normal", "Fairy"]
			self.ability = ["Cute Charm", "Competitive", "Friend Guard"]
		elif name == "Wigglytuff":
			self.type = ["Normal", "Fairy"]
			self.ability = ["Cute Charm", "Competitive", "Frisk"]
		elif name == "Zubat":
			self.type = ["Posion", "Flying"]
			self.ability = ["Inner Focus", "Inner Focus", "Infiltrator"]
		elif name == "Crobat":
			self.type = ["Posion", "Flying"]
			self.ability = ["Inner Focus", "Inner Focus", "Infiltrator"]
		elif name == "Oddish":
			self.type = ["Grass", "Poison"]
			self.ability = ["Chlorophyll", "Chlorophyll", "Run Away"]
		elif name == "Gloom":
			self.type = ["Grass", "Poison"]
			self.ability = ["Chlorophyll", "Chlorophyll", "Stench"]
		elif name == "Vileplume":
			self.type = ["Grass", "Poison"]
			self.ability = ["Chlorophyll", "Chlorophyll", "Effect Spore"]
		elif name == "Paras":
			self.type = ["Bug", "Grass"]
			self.ability = ["Effect Spore", "Dry Skin", "Damp"]
		elif name == "Parasect":
			self.type = ["Bug", "Grass"]
			self.ability = ["Effect Spore", "Dry Skin", "Damp"]
		elif name == "Venonat":
			self.type = ["Bug", "Poison"]
			self.ability = ["Compound Eyes", "Tinted Lens", "Run Away"]
		elif name == "Venomoth":
			self.type = ["Bug", "Poison"]
			self.ability = ["Shield Dust", "Tinted Lens", "Wonder Skin"]
		elif name == "Digglet":
			self.type = ["Ground"]
			self.ability = ["Sand Veil", "Arena Trap", "Sand Force"]
		elif name == "Dugtrio":
			self.type = ["Ground"]
			self.ability = ["Sand Veil", "Arena Trap", "Sand Force"]
		elif name == "Meowth":
			self.type = ["Normal"]
			self.ability = ["Pickup", "Technician", "Unnerve"]
		elif name == "Persian":
			self.type = ["Normal"]
			self.ability = ["Persian Limber", "Technician", "Unnerve"]
		elif name == "Psyduck":
			self.type = ["Water"]
			self.ability = ["Damp", "Cloud Nine", "Swift Swim"]
		elif name == "Golduck":
			self.type = ["Water"]
			self.ability = ["Damp", "Cloud Nine", "Swift Swim"]
		elif name == "Mankey":
			self.type = ["Fighting"]
			self.ability = ["Vital Spirit", "Anger Point", "Defiant"]
		elif name == "Primeape":
			self.type = ["Fighting"]
			self.ability = ["Vital Spirit", "Anger Point", "Defiant"]
		elif name == "Growlithe":
			self.type = ["Fire"]
			self.ability = ["Intimidate", "Flash Fire", "Justified"]
		elif name == "Arcanine":
			self.type = ["Fire"]
			self.ability = ["Intimidate", "Flash Fire", "Justified"]
		elif name == "Poliwag":
			self.type = ["Water"]
			self.ability = ["Water Absorb", "Damp", "Swift Swim"]
		elif name == "Poliwhirl":
			self.type = ["Water"]
			self.ability = ["Water Absorb", "Damp", "Swift Swim"]
		elif name == "Poliwrath":
			self.type = ["Water", "Fighting"]
			self.ability = ["Water Absorb", "Damp", "Swift Swim"]
		elif name == "Abra":
			self.type = ["Psychic"]
			self.ability = ["Synchronize", "Inner Focus", "Magic Guard"]
		elif name == "Kadabra":
			self.type = ["Psychic"]
			self.ability = ["Synchronize", "Inner Focus", "Magic Guard"]
		elif name == "Alakazam":
			self.ability = ["Synchronize", "Inner Focus", "Magic Guard"]
		elif name == "Machop":
			self.type = ["Fighting"]
			self.ability = ["Guts", "No Guard", "Steadfast"]
		elif name == "Machoke":
			self.type = ["Fighting"]
			self.ability = ["Guts", "No Guard", "Steadfast"]
		elif name == "Machamp":
			self.type = ["Fighting"]
			self.ability = ["Guts", "No Guard", "Steadfast"]
		elif name == "Bellsprout":
			self.type = ["Grass", "Poison"]
			self.ability = ["Chlorophyll", "Chlorophyll", "Gluttony"]
		elif name == "Weepinbell":
			self.type = ["Grass", "Poison"]
			self.ability = ["Chlorophyll", "Chlorophyll", "Gluttony"]
		elif name == "Victreebel":
			self.type = ["Grass", "Poison"]
			self.ability = ["Chlorophyll", "Chlorophyll", "Gluttony"]
		elif name == "Tentacool":
			self.type = ["Water", "Poison"]
			self.ability = ["Clear Body", "Liquid Ooze", "Rain Dish"]
		elif name == "Tentacruel":
			self.type = ["Water", "Poison"]
			self.ability = ["Clear Body", "Liquid Ooze", "Rain Dish"]
		elif name == "Geodude":
			self.type = ["Rock", "Ground"]
			self.ability = ["Rock Head", "Sturdy", "Sand Veil"]
		elif name == "Graveler":
			self.type = ["Rock", "Ground"]
			self.ability = ["Rock Head", "Sturdy", "Sand Veil"]
		elif name == "Golem":
			self.type = ["Rock", "Ground"]
			self.ability = ["Rock Head", "Sturdy", "Sand Veil"]
		elif name == "Ponyta":
			self.type = ["Fire"]
			self.ability = ["Run Away", "Flash Fire", "Flame Body"]
		elif name == "Rapidash":
			self.type = ["Fire"]
			self.ability = ["Run Away", "Flash Fire", "Flame Body"]
		elif name == "Slowpoke":
			self.type = ["Water", "Psychic"]
			self.ability = ["Oblivious", "Own Tempo", "Regenerator"]
		elif name == "Slowbro":
			self.type = ["Water", "Psychic"]
			self.ability = ["Oblivious", "Own Tempo", "Regenerator"]
		elif name == "Magnemite":
			self.type = ["Electric", "Steel"]
			self.ability = ["Magnet Pull", "Sturdy", "Analytic"]
		elif name == "Magneton":
			self.type = ["Electric", "Steel"]
			self.ability = ["Magnet Pull", "Sturdy", "Analytic"]
		elif name == "Farfetch'd":
			self.type = ["Normal", "Flying"]
			self.ability = ["Keen Eye", "Inner Focus", "Defiant"]
		elif name == "Doduo":
			self.type = ["Normal", "Flying"]
			self.ability = ["Run Away", "Early Bird", "Tangled Feet"]
		elif name == "Dodrio":
			self.type = ["Normal", "Flying"]
			self.ability = ["Run Away", "Early Bird", "Tangled Feet"]
		elif name == "Seel":
			self.type = ["Water"]
			self.ability = ["Thick Fat", "Hydration", "Ice Body"]
		elif name == "Dewgong":
			self.type = ["Water", "Ice"]
			self.ability = ["Thick Fat", "Hydration", "Ice Body"]
		elif name == "Grimer":
			self.type = ["Poison"]
			self.ability = ["Stench", "Sticky Hold", "Poison Touch"]
		elif name == "Muk":
			self.type = ["Poison"]
			self.ability = ["Stench", "Sticky Hold", "Poison Touch"]
		elif name == "Shellder":
			self.type = ["Water"]
			self.ability = ["Shell Armor", "Skill Link", "Overcoat"]
		elif name == "Cloyster":
			self.type = ["Water", "Ice"]
			self.ability = ["Shell Armor", "Skill Link", "Overcoat"]
		elif name == "Gastly":
			self.type = ["Ghost", "Poison"]
			self.ability = ["Levitate", "Levitate", "Levitate"]
		elif name == "Haunter":
			self.type = ["Ghost", "Poison"]
			self.ability = ["Levitate", "Levitate", "Levitate"]
		elif name == "Gengar":
			self.type = ["Ghost", "Poison"]
			self.ability = ["Cursed Body", "Cursed Body", "Cursed Body"]
		elif name == "Onix":
			self.type = ["Rock", "Ground"]
			self.ability = ["Rock Head", "Sturdy", "Weak Armor"]
		elif name == "Drowzee":
			self.type = ["Psychic"]
			self.ability = ["Insomnia", "Forewarn", "Inner Focus"]
		elif name == "Hypno":
			self.type = ["Psychic"]
			self.ability = ["Insomnia", "Forewarn", "Inner Focus"]
		elif name == "Krabby":
			self.type = ["Water"]
			self.ability = ["Hyper Cutter", "Shell Armor", "Sheer Force"]
		elif name == "Kingler":
			self.type = ["Water"]
			self.ability = ["Hyper Cutter", "Shell Armor", "Sheer Force"]
		elif name == "Voltrob":
			self.type = ["Electric"]
			self.ability = ["Soundproof", "Static", "Aftermath"]
		elif name == "Electrode":
			self.type = ["Electric"]
			self.ability = ["Soundproof", "Static", "Aftermath"]
		elif name == "Exeggcute":
			self.type = ["Grass", "Psychic"]
			self.ability = ["Chlorophyll", "Chlorophyll", "Harvest"]
		elif name == "Exeggutor":
			self.type = ["Grass", "Psychic"]
			self.ability = ["Chlorophyll", "Chlorophyll", "Harvest"]
		elif name == "Cubone":
			self.type = ["Ground"]
			self.ability = ["Rock Head", "Lightning Rod", "Battle Armor"]
		elif name == "Marowak":
			self.type = ["Ground"]
			self.ability = ["Rock Head", "Lightning Rod", "Battle Armor"]
		elif name == "Hitmonlee":
			self.type = ["Fighting"]
			self.ability = ["Limber", "Reckless", "Unburden"]
		elif name == "Hitmonchan":
			self.type = ["Fighting"]
			self.ability = ["Keen Eye", "Iron Fist", "Inner Focus"]
		elif name == "Lickitung":
			self.type = ["Normal"]
			self.ability = ["Own Tempo", "Oblivious", "Cloud Nine"]
		elif name == "Koffing":
			self.type = ["Poison"]
			self.ability = ["Levitate", "Neutralizing Gas", "Stench"]
		elif name == "Weezing":
			self.type = ["Poison"]
			self.ability = ["Levitate", "Neutralizing Gas", "Stench"]
		elif name == "Rhyhorn":
			self.type = ["Ground", "Rock"]
			self.ability = ["Lightning Rod", "Rock Head", "Reckless"]
		elif name == "Rhydon":
			self.type = ["Ground", "Rock"]
			self.ability = ["Lightning Rod", "Rock Head", "Reckless"]
		elif name == "Chansey":
			self.type = ["Normal"]
			self.ability = ["Natural Cure", "Serene Grace", "Healer"]
		elif name == "Tangela":
			self.type = ["Grass"]
			self.ability = ["Chlorophyll", "Leaf Guard", "Regenerator"]
		elif name == "Kangaskhan":
			self.type = ["Grass"]
			self.ability = ["Early Bird", "Scrappy", "Inner Focus"]
		elif name == "Horsea":
			self.type = ["Water"]
			self.ability = ["Swift Swim", "Sniper", "Damp"]
		elif name == "Seadra":
			self.type = ["Water"]
			self.ability = ["Poison Point", "Sniper", "Damp"]
		elif name == "Goldeen":
			self.type = ["Water"]
			self.ability = ["Swift Swim", "Water Veil", "Lightning Rod"]
		elif name == "Seaking":
			self.type = ["Water"]
			self.ability = ["Swift Swim", "Water Veil", "Lightning Rod"]
		elif name == "Staryu":
			self.type = ["Water"]
			self.ability = ["Illuminate", "Natural Cure", "Analytic"]
		elif name == "Starmie":
			self.type = ["Water", "Psychic"]
			self.ability = ["Illuminate", "Natural Cure", "Analytic"]
		elif name == "Mr. Mime":
			self.type = ["Psychic", "Fairy"]
			self.ability = ["Soundproof", "Filter", "Technician"]
		elif name == "Scyther":
			self.type = ["Bug", "Flying"]
			self.ability = ["Swarm", "Technician", "Steadfast"]
		elif name == "Jynx":
			self.type = ["Ice", "Psychic"]
			self.ability = ["Oblivious", "Forewarn", "Dry Skin"]
		elif name == "Electabuzz":
			self.type = ["Electric"]
			self.ability = ["Static", "Static", "Vital Spirit"]
		elif name == "Magmar":
			self.type = ["Fire"]
			self.ability = ["Flame Body", "Flame Body", "Vital Spirit"]
		elif name == "Pinsir":
			self.type = ["Bug"]
			self.ability = ["Hyper Cutter", "Mold Breaker", "Moxie"]
		elif name == "Tauros":
			self.type = ["Normal"]
			self.ability = ["Anger Point", "Anger Point", "Sheer Force"]
		elif name == "Magikarp":
			self.type = ["Water"]
			self.ability = ["Swift Swim", "Swift Swim", "Rattled"]
		elif name == "Gyarados":
			self.type = ["Water", "Flying"]
			self.ability = ["Intimidate", "Intimidate", "Moxie"]
		elif name == "Lapras":
			self.type = ["Water", "Ice"]
			self.ability = ["Water Absorb", "Shell Armor", "Hydration"]
		elif name == "Ditto":
			self.type = ["Normal"]
			self.ability = ["Limber", "Limber", "Imposter"]
		elif name == "Eevee":
			self.type = ["Normal"]
			self.ability = ["Run Away", "Adaptability", "Anticipation"]
		elif name == "Vaporeon":
			self.type = ["Water"]
			self.ability = ["Water Absorb", "Water Absorb", "Hydration"]
		elif name == "Jolteon":
			self.type = ["Electric"]
			self.ability = ["Volt Absorb", "Volt Absorb", "Quick Feet"]
		elif name == "Flareon":
			self.type = ["Fire"]
			self.ability = ["Flash Fire", "Flash Fire", "Guts"]
		elif name == "Proygon":
			self.type = ["Normal"]
			self.ability = ["Trace", "Download", "Analytic"]
		elif name == "Omanyte":
			self.type = ["Rock", "Water"]
			self.ability = ["Swift Swim", "Shell Armor", "Weak Armor"]
		elif name == "Omastar":
			self.type = ["Rock", "Water"]
			self.ability = ["Swift Swim", "Shell Armor", "Weak Armor"]
		elif name == "Kabuto":
			self.type = ["Rock", "Water"]
			self.ability = ["Swift Swim", "Battle Armor", "Weak Armor"]
		elif name == "Kabutops":
			self.type = ["Rock", "Water"]
			self.ability = ["Swift Swim", "Battle Armor", "Weak Armor"]
		elif name == "Aerodactyl":
			self.type = ["Rock", "Flying"]
			self.ability = ["Rock Head", "Pressure", "Unnerve"]
		elif name == "Snorlax":
			self.type = ["Normal"]
			self.ability = ["Immunity", "Thick Fat", "Gluttony"]
		elif name == "Articuno":
			self.type = ["Ice", "Flying"]
			self.ability = ["Pressure", "Pressure", "Snow Cloak"]
		elif name == "Zapdos":
			self.type = ["Electric", "Electric", "Flying"]
			self.ability = ["Pressure", "Pressure", "Static"]
		elif name == "Moltres":
			self.type = ["Fire", "Flying"]
			self.ability = ["Pressure", "Pressure", "Flame Body"]
		elif name == "Dratini":
			self.type = ["Dragon"]
			self.ability = ["Shed Skin", "Shed Skin", "Marvel Scale"]
		elif name == "Dragonair":
			self.type = ["Dragon"]
			self.ability = ["Shed Skin", "Shed Skin", "Marvel Scale"]
		elif name == "Dragonite":
			self.type = ["Dragon", "Flying"]
			self.ability = ["Inner Focus", "Inner Focus", "Multiscale"]
		elif name == "Mewtwo":
			self.type = ["Psychic"]
			self.ability = ["Pressure", "Pressure", "Unnerve"]
		elif name == "Mew":
			self.type = ["Psychic"]
			self.ability = ["Synchronize", "Synchronize", "Synchronize"]


class PokemonStats(Specie):

	def calculate_stats(self):
		base = self.base
		ivs = self.ivs
		evs = self.evs
		level = self.lvl
		nature = self.nature

		def formula(stat_name):
			if stat_name == "hp":
				a, b = 100, 10
			else:
				a, b = 0, 5
			return math.floor(math.floor((2 * base[stat_name] + ivs[stat_name] + math.floor(evs[stat_name] / 4) + a) * level / 100)+b)*nature_boost(nature, stat_name)
		return {'hp': formula('hp'), 'attack': formula('attack'), 'defense': formula('defense'), 'spatk': formula('spatk'), 'spdef': formula('spdef'), 'speed': formula('speed')}

	def __init__(self, specie: str = "Bulbasaur", lvl: int = 5, exp: int = 15, nature: str = "Bold"):
		super().__init__()
		self.lvl = lvl
		self.exp = exp
		self.nature = nature
		self.specie = Specie(specie)
		self.base = Specie(specie).base
		self.ivs = {'hp': 0, 'attack': 0, 'defense': 0, 'spatk': 0, 'spdef': 0, 'speed': 0}
		self.evs = {'hp': 0, 'attack': 0, 'defense': 0, 'spatk': 0, 'spdef': 0, 'speed': 0}
		self.stats = self.calculate_stats()

	def random_ivs(self):
		self.ivs = {'hp': random.randint(0, 31), 'attack': random.randint(0, 31), 'defense': random.randint(0, 31), 'spatk': random.randint(0, 31), 'spdef': random.randint(0, 31), 'speed': random.randint(0, 31)}
		self.stats = self.calculate_stats()

	def random_evs(self):
		rand_evs = []
		prechecker = 510
		while prechecker >= 0 and len(rand_evs) < 5:
			rnum = random.randint(0, 252)
			if prechecker - rnum > 0:
				rand_evs.append(rnum)
				prechecker -= rnum
		rand_evs.append(prechecker)
		self.evs = {'hp': rand_evs[0], 'attack': rand_evs[1], 'defense': rand_evs[2], 'spatk': rand_evs[3], 'spdef': rand_evs[4], 'speed': rand_evs[5]}
		self.stats = self.calculate_stats()


# Add Methods and EXP stuff, moves
class Pokemon(Met, PokemonStats):
	def __init__(self, specie: str = "Bulbasaur", nickname: str = None, item: str = None, friendship: int = 0, lang: str = "eng", is_egg: bool = False, infected: bool = False, cured: bool = False, height: int = 0, weight: int = 0, met: Met = Met()):
		super().__init__()
		self.specie = Specie(specie)
		self.nickname = nickname
		self.item = item
		self.friendship = friendship
		self.lang = lang
		self.is_egg = is_egg
		self.infected = infected
		self.cured = cured
		self.height = height
		self.weight = weight
		self.desc = met
		self.stats = PokemonStats(specie)


blastoise = Pokemon("Bulbasaur")
blastoise.stats.random_ivs()
blastoise.stats.random_evs()
print(blastoise.stats.base)
print(blastoise.stats.lvl)
print(blastoise.stats.ivs)
print(blastoise.stats.evs)
print(blastoise.stats.stats)
