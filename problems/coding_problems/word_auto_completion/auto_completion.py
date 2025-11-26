# Problem Statement: 
# - Design and implement the core logic for an auto-complete engine used in a text editor or IDE.
# - The engine should suggest completions as the user types text based on previously stored entries and usage context.
# - Given a prefix (e.g., pri), suggest the top matching words or symbols (e.g., print, private, printf).
# - Return suggestions in sorted order based on frequency of usage.


from simple_trie import Trie

class AutoCompletion:
	def __init__(self, trie: Trie, max_suggestions=5):
		self.trie = trie
		self.max_suggestions = max_suggestions
		self.freq = {}  # store usage frequency for ranking

	def addWord(self, word: str):
		word = word.lower()
		self.trie.insert(word)
		if word not in self.freq:
			self.freq[word] = 0

	def _collectAllWords(self, node, prefix, result):
		"""DFS to collect words under a prefix."""
		if node.isEndOfWord:
			result.append(prefix)

		for i in range(26):
			child = node.children[i]
			if child is not None:
				char = chr(i + ord('a'))
				self._collectAllWords(child, prefix + char, result)

	def suggest(self, prefix: str):
		prefix = prefix.lower()
		trieNode = self.trie.root

		# Traverse to the prefix node
		for ch in prefix:
			idx = ord(ch) - ord('a')
			if trieNode.children[idx] is None:
				return []  # no completions
			trieNode = trieNode.children[idx]

		# Collect all completions under this prefix
		suggestions = []
		self._collectAllWords(trieNode, prefix, suggestions)

		# Sort by frequency (highest first), then alphabetically
		suggestions.sort(key=lambda w: (-self.freq.get(w, 0), w))

		return suggestions[:self.max_suggestions]

	
	def recordUsage(self, word: str):
		"""Increment frequency when user selects a suggestion."""
		word = word.lower()
		self.freq[word] = self.freq.get(word, 0) + 1


if __name__ == '__main__':
	keys = ["the", "a", "there", "ANSWER", "any", "by", "bye", "their", "hero", "heroplane"]
	trieGraph = Trie()
	for i in range(len(keys)):
		trieGraph.insert(keys[i])

	print("========================")
	print("*** Printing the created graph ***")
	trieGraph.printTrie()
	print("*************************")

	print("========================")
	print("*** Testing Autocompletion ***")
	autoCompletion = AutoCompletion(trieGraph, max_suggestions=3)
	# Add the same words to freq table
	for words in keys:
		autoCompletion.addWord(words)

	print(f"Suggestions for he: {autoCompletion.suggest('he')}")   # expected: ['hero', 'heroplane', 'their', ...]
	print(f"Suggestions for an: {autoCompletion.suggest('an')}")   # ['answer', 'any']
	print(f"Suggestions for th: {autoCompletion.suggest('th')}")   # ['the', 'there', 'their']
	print(f"Suggestions for z: {autoCompletion.suggest('z')}")    # []