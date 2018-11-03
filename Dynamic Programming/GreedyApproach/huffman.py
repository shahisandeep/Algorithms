#Sandeep Shahi
import heapq
from operator import itemgetter


def frequency(text):
	frequency = {}
	for character in text:
		if not character in frequency:
			frequency[character] = 0
		frequency[character] += 1

	return frequency


def huffmanEnc(stringOfText):
	swap = []
	for char, tally in stringOfText.items():
		swap.append([tally, [char, '']])
	heapq.heapify(swap)
	while len(swap) > 1:
		leftNode = heapq.heappop(swap)
		rightNode = heapq.heappop(swap)
		for alphabet in leftNode[1:]:
			alphabet[1] = '0' + alphabet[1]
		for alphabet in rightNode[1:]:
			alphabet[1] = '1' + alphabet[1]
		heapq.heappush(swap, [leftNode[0] + rightNode[0]] + leftNode[1:] + rightNode[1:])
	swap = heapq.heappop(swap)
	return swap


if __name__ == "__main__":

	text = raw_input("Ask user for some text: ")

	encodedFormat = huffmanEnc(frequency(text))
	encodedFormat = encodedFormat[1:]

	sorted_encodedFormat = sorted(encodedFormat, key=itemgetter(0))

	print("\t   \t  \t")
	print("Alphabet \t Frequency \t Hufman Code")  # Seperate the alphabet frequency and hufman code

	for x in sorted_encodedFormat:
		tally = frequency(text)[x[0]]
		print(repr(x[0]) + "\t\t\t\t" + str(tally) + "\t\t  " + x[1])






