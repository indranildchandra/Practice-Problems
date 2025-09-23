# Design push and pull APIs for a producer consumer system with N producers and M consumers conforming to the following definitions:

# Push(Key, Payload);
# Push need not have consecutive keys. But keys pushed are monotonically increasing.

# Payload Pull(Key);
# Pull can be for any seq/key number.
# If the seq number is not found, return the payload for the immediate next higher sequence number.
# If there is no next higher seq num, return null.

# Container has a fixed amount of memory.
# When the container is full, you can delete the lowest sequence number.
# Once an item is pulled, it is unavailable for other pulls and can be discarded by the container

## capacity = 3
## push (1, "value1")

## push (3, "value3")

## push (5, "value5")

## pull (2) => "value3"

## push (10, "value10")

## push (15, "value15")  => deletion of (1, "value")

import traceback
from collections import OrderedDict

class PubSub():
	
	def __init__(self, container_size):
		self.capacity = container_size
		self.message_stack = OrderedDict()
		
	def find_cross_over(self, arr, low, high, x):
		if (arr[high] <= x): 
			return high 
		if (arr[low] > x):
			return low   
		mid = (low + high) // 2 
		if (arr[mid] <= x and arr[mid + 1] > x): 
			return mid  
		if(arr[mid] < x): 
			return self.find_cross_over(arr, mid + 1, high, x) 
		return self.find_cross_over(arr, low, mid - 1, x) 
	
	def get_K_closest(self, arr, x, k, n): 
		l = self.find_cross_over(arr, 0, n - 1, x) 
		r = l + 1 
		count = 0
		candidate_elements = list()
		if (arr[l] == x) : 
			l -= 1
		while (l >= 0 and r < n and count < k) :    
			if (x - arr[l] < arr[r] - x):
				# print(arr[l], end = " ")
				candidate_elements.append(arr[l])
				l -= 1
			else: 
				# print(arr[r], end = " ")
				candidate_elements.append(arr[r])
				r += 1
			count += 1
		while (count < k and l >= 0): 
			# print(arr[l], end = " ")
			candidate_elements.append(arr[l])
			l -= 1
			count += 1
		while (count < k and r < n):  
			# print(arr[r], end = " ")
			candidate_elements.append(arr[r])
			r += 1
			count += 1
		return candidate_elements
	
	
	def push(self, key, payload):
		try:
			if len(self.message_stack) < self.capacity:
				self.message_stack[key] = payload
			else:
				self.message_stack.pop(0)
				self.message_stack[key] = payload
			return 1
		except:
			print(traceback.format_exc())
			return 0
	
	
	def pull(self, lookup_key):
		try:
			# payload = self.message_stack.get(lookup_key) or self.message_stack[min(self.message_stack.keys(), key = lambda key: abs(lookup_key-key))]
			if lookup_key in self.message_stack.keys():
				payload = self.message_stack.get(lookup_key)
				del self.message_stack[lookup_key]
			elif lookup_key > max(self.message_stack.keys()):
				payload = None
			elif lookup_key < min(self.message_stack.keys()):
				nearest_key = min(self.message_stack.keys())
				payload = self.message_stack.get(nearest_key)
				del self.message_stack[nearest_key]
			else:
				nearest_key = max(self.get_K_closest(list(self.message_stack.keys()), lookup_key, 2, len(self.message_stack.keys())))
				payload = self.message_stack.get(nearest_key)
				del self.message_stack[nearest_key]
			return payload, True
		except:
			print(traceback.format_exc())
			return None, False