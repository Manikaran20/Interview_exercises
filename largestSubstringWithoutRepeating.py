/*
Given a string, 
find the length of the longest substring without repeating characters.
Example:
The longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3.
For "bbbbb" the longest substring is "b", with the length of 1.
*/


def longest_substring_length(string):
	l= len(string)
	list1=[]
	for i in string:
		s=''
		s+=i
		#list1=[]
		for j in range(0,l):
			j+=1
			if(string[j] in s):
				break
			else:
				s+=string[j]
		list1.append(s)

	longest_substring= (max(list1, key=len))
	length= len(longest_substring)
	print ("longest substring is " + longest_substring +" and it's length is " + str(length) )

longest_substring_length("abcdefghiijklmhbhncjdskbfksfjdnvbiyufgu")
