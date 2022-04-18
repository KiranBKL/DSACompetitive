# Python3 program to find K'th
# character in decrypted string

# Function to find K'th character
# in Encoded String
def encodedChar(string, k):

	n = len(string)

	i = 0
	while i < n:
		j = i
		length = 0
		freq = 0

		# Find length of substring by
		# traversing the string until
		# no digit is found.
		while j < n and string[j].isalpha():
			j += 1
			length += 1

		# Find frequency of preceding substring.
		while j < n and string[j].isdigit():
			freq = freq * 10 + int(string[j])
			j += 1

		# Find the length of the substring
		# when it is repeated.
		num = freq * length

		# If the length of the repeated substring
		# is less than k then required character
		# is present in next substring. Subtract
		# the length of repeated substring from
		# k to keep account of the number
		# of characters required to be visited.
		if k > num:
			k -= num
			i = j

		# If length of repeated substring is
		# more or equal to k then required
		# character lies in current substring.
		else:
			k -= 1
			k %= length
			return string[i + k]

	# This is for the case when there are no
	# repetition in string. e.g. str="abced".
	return string[k - 1]

# Driver Code
if __name__ == "__main__":

	string = "abced"
	k = 4

	print(encodedChar(string, k))

# This code is contributed
# by Rituraj Jain
