import heapq
from collections import Counter, namedtuple

class Node(namedtuple("Node", ["left", "right"])):
	def walk(self, code, acc):
		self.left.walk(code, acc +'0')
		self.right.walk(code, acc +'1')


class Leaf(namedtuple("Leaf", ["char"])):
	def walk(self, code, acc):		
		code[self.char] = acc or '0'

def huffman_encode(fileInputPath, fileOutputPath):

	fileInput = open(fileInputPath, 'r')
	s = fileInput.read()
	fileInput.close()
	h=[]
	for ch, freq in Counter(s).items():
		h.append((freq, len(h), Leaf(ch)))
	heapq.heapify(h)

	count = len(h)
	while len(h) > 1:
		# getting two elements with the minimum frequency
		freq1, _count1, left = heapq.heappop(h)
		freq2, _count2, right = heapq.heappop(h)
		heapq.heappush(h, (freq1 + freq2, count, Node(left, right)))
		count += 1

	global code
	code = {}
	if h:
		[(_freq, _count, root)] = h
		root.walk(code, "")

	encoded = "".join(code[ch] for ch in s)

	fileOutput = open(fileOutputPath, 'w')
	fileOutput.write(encoded)
	fileOutput.close()


def huffman_decode(fileInputPath, fileOutputPath):

	fileInput = open(fileInputPath, 'r')
	encodedStr = fileInput.read()
	fileInput.close()

	pointer = 0
	decodedStr = ''
	while pointer < len(encodedStr):
		for ch in code.keys():
			if encodedStr.startswith(code[ch], pointer):
				decodedStr += ch
				pointer += len(code[ch])

	fileOutput = open(fileOutputPath, 'a')
	fileOutput.write('\n' + decodedStr)
	fileOutput.close()

def main():
    try:
        fileInputPath = input('Введите название исходного файла: ')
        fileOutputPath = input('Введите название файла для записи: ')
        huffman_encode(fileInputPath, fileOutputPath)
        huffman_decode(fileOutputPath, fileOutputPath)
        print('True')
    except:
        print('False')
    finally:
        print('Program was completed')

if __name__ == "__main__":
    main()
