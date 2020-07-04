class DoubleLinkedListNode:
	def __init__(self,key,value):
		self.key=key
		self.value=value
		self.next=None
		self.prev=None

class LRUCache:
	def __init__(self,capacity):
		self.size=capacity
		self.dic={}
		self.head=DoubleLinkedListNode(-1,-1) ## It will be the head of LRUCache
		self.tail=DoubleLinkedListNode(-1,-1)
		self.head.next=self.tail
		self.tail.prev=self.head

	def get(self,key):
		if key in self.dic:
			node=self.dic[key]
			self.delete(node)
			self.add(node)
			return node.value
		return -1

			

	def set(self,key,value):
		if key is self.dic:  ## If Key is Already Present then we need to Update it
			self.delete(self.dic[key])

		node=DoubleLinkedListNode(key,value)
		self.add(node)
		self.dic[key]=node
		if len(self.dic)>self.size:
			node=self.head.next
			self.delete(node)
			del self.dic[node.key]


	def add(self,node):
		prev_node=self.tail.prev
		prev_node.next=node
		node.prev=prev_node
		node.next=self.tail
		self.tail.prev=node


		

	def delete(self,node):
		prev_node=node.prev 
		next_node=node.next
		prev_node.next=next_node
		next_node.prev=prev_node

l=LRUCache(2)
print(l.get(1))
l.set(1,"a")
l.set(2,"b")
print(l.get(1))
l.set(3,"c")
print(l.get(2))

## Approach head and tail is Dummy Node The Previous of Tail will be the most recent Node
## The next of head will be least recent Used node
## Whenever get Function is called first we remove it from DLL and then add it as previous of tail so that it will be the most recent
## Dictionary is used to store address of key node




