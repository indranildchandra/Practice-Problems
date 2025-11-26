class TrieNode:
	def __init__(self):
		self.children = [None] * 26
		self.isEndOfWord = False

class Trie:
	def __init__(self):
		self.root = TrieNode()

	def createChildNode(self):
		cNode = TrieNode()
		return cNode

	def insert(self, key):
		trieNode = self.root
		key = key.lower()
		for i in range(len(key)):
			index = ord(key[i]) - ord('a')
			if not trieNode.children[index]:
				trieNode.children[index] = self.createChildNode()
			trieNode = trieNode.children[index]
		trieNode.isEndOfWord = True

	def search(self, key):
		trieNode = self.root
		for i in range(len(key)):
			index = ord(key[i]) - ord('a')
			if not trieNode.children[index]:
				return False
			trieNode = trieNode.children[index]
		return trieNode and trieNode.isEndOfWord
	
	def isPrefix(self, prefix):
		trieNode = self.root
		for char in prefix:
			index = ord(char) - ord('a')
			if trieNode.children[index] is None:
				return False
			trieNode = trieNode.children[index]
		return True

	def isEmpty(self, node):
		for i in range(26):
			if node.children[i] is not None:
				return False
		return True


	def remove(self, key, depth=0, node=None):
		# Initialize node on first call
		if node is None:
			node = self.root

		# Base case: empty trie
		if node is None:
			return None

		# If we reached end of the key
		if depth == len(key):
			if node.isEndOfWord:
				node.isEndOfWord = False  # unmark leaf
			
			# If node has no children, tell parent to delete it
			if self.isEmpty(node):
				return None
			
			return node

		# Recursive case
		index = ord(key[depth]) - ord('a')
		node.children[index] = self.remove(key, depth + 1, node.children[index])

		# If node becomes useless (no children + not end of word), delete it
		if self.isEmpty(node) and not node.isEndOfWord:
			return None

		return node


	def printTrie(self, node=None, level=0, prefix=""):
		if node is None:
			node = self.root
		for i in range(26):
			child = node.children[i]
			if child is not None:
				char = chr(i + ord('a'))
				print("    " * level + f"|--- {char}  (prefix={prefix+char})")
				self.printTrie(child, level + 1, prefix + char)



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
	print("*** Testing search ***")
	print(f"'the' is present? ---> {trieGraph.search('the')}")
	print(f"'these' is present? ---> {trieGraph.search('these')}")
	print("*************************")

	print("========================")
	print("*** Testing deletion ***")
	root = trieGraph.remove("heroplane")
	print(f"'hero' is present after removing 'heroplane'? ---> {trieGraph.search('hero')}")
	print("*************************")
	
	print("========================")
	print("*** Testing prefix search ***")
	prefixKeys = ["th", "dududududu", "an", "lv"]
	for prefix in prefixKeys:
		print(f"'{prefix}' is present? {trieGraph.isPrefix(prefix)}")
	print("*************************")
