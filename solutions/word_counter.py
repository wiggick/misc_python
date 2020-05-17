import re

my_paragraph = '''
Alice in WonderLand First Paragraph
===================================
First Paragraph.  Alice was beginning to get very tired of sitting by her sister on the bank, and of having nothing to do: 
once or twice she had peeped into the book her sister was reading, but it had no pictures or conversations in it, 
`and what is the use of a book,' thought Alice `without pictures or conversation?'

Additional Tests
==================================
It's going to handle contractions.
'''

#a Hundred Foo's
for i in range(100):
	my_paragraph += " foo"

words = my_paragraph.lower()
#handle_contractions
words = re.sub("([A-Za-z]{1})'([A-Za-z]{1})",r"\1_cont_\2",words)

words = re.sub(r'[^\w]', ' ',words)
#get rid of space runs
words = re.sub(r' {2,}', ' ', words)
#put contractions back in
words = words.replace("_cont_","'")

words = words.strip().split(" ")

counts = {}

for word in words:
	if word not in counts:
		counts[word] = words.count(word)

sorted_count = sorted(counts.items(), key=lambda x: x[1],reverse=True)
# equivalent version
# sorted_d = sorted(counts.items(), key=lambda (k,v): v)

max_len = len(str(sorted_count[0][1])) 

for count_tup in sorted_count:
	print(str(count_tup[1]).ljust(max_len,' '),":",count_tup[0])
