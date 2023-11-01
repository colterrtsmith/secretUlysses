lettersToNumbers = {
	"A": 1,
	"J": 11,
	"Q": 12,
	"K": 13,
}

class Card:
	def __init__(self, number, suit):
		self.number = lettersToNumbers.get(number, number)
		self.suit = suit

class Pair:
	def __init__(self, first: Card, second: Card, good: bool):
		self.first = first
		self.second = second
		self.good = good

class Quality:
	def __init__(self):
		self.name = self.__class__.__name__.lower()

	def check(self, card: Card):
		return False

class Black(Quality):
	def check(self, card):
		return card.suit in ['C', 'S'] 

class Red(Quality):
	def check(self, card):
		return card.suit in ['D', 'H']

class High(Quality):
	def check(self, card):
		return card.number > 7

class Low(Quality):
	def check(self, card):
		return card.number <=7 


class SecretUlyssesSolver:
	def __init__(self):
		self.cards = []
		self.pairs = []
		self.qualities = [Black(), Red(), High(), Low()]

	def separate(self, quality):
		haveGoods = []
		donthaveGoods = []
		haveBads = []
		donthaveBads = []

		for pair in self.pairs:
			if quality.check(pair.first):
				if pair.good:
					haveGoods.append(pair.second)
				else:
					haveBads.append(pair.second)
			else:
				if pair.good:
					donthaveGoods.append(pair.second)
				else:
					donthaveBads.append(pair.second)

		return haveGoods, haveBads, donthaveGoods, donthaveBads

	def nextCard(self, card: Card, good: bool):
		self.cards.append(card)
		if len(self.cards) > 1:
			self.pairs.append(Pair(self.cards[-2], self.cards[-1], good))


		if (len(self.cards) < 3):
			print("Too few cards so far")
			return

		patterns = []
		for firstQuality in self.qualities:
			haveGoods, haveBads, donthaveGoods, donthaveBads = self.separate(firstQuality)
			for secondQuality in self.qualities:
				if all(map(secondQuality.check, haveGoods)) and\
				   not any(map(secondQuality.check, haveBads)) and\
				   not any(map(secondQuality.check, donthaveGoods)) and\
				   all(map(secondQuality.check, donthaveBads)):
				   patterns.append(f"iff {firstQuality.name} then {secondQuality.name}")

		if len(patterns) <= 5:
			print("Possible patterns:")
			for pattern in patterns:
				print(pattern)
		else:
			print("too many possible patterns!")

def test1():
	# pattern: iff high, then red
	print("Test 1")
	cards = [
		(Card("K", "S"), None),
		(Card(8, "H"), True),
		(Card(2, "C"), False),
		(Card(4, "C"), True),
		(Card("A", "S"), True),
		(Card(10, "S"), True),
	]

	s = SecretUlyssesSolver()
	for card, good in cards:
		s.nextCard(card, good)

def test():
	test1()

test()
