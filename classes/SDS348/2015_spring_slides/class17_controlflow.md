# Python II: Control Flow


<br><br>
##FOR is for iterating over values in a list, string, dictionary, etc.
```														
for item in container:
	do this command
	do that command
	#return to for statement and move to next item
```

```
# Loop over a list
for x in [1,2,3,4]:
    print x

# Loop over a string
for x in "abcdefg":
    print x

# Loop over a dictionary (loops over keys!!)
d = {"a":1, "b":2, "c":3, "d":4}
for x in d:
    print x # prints the key
    print d[x] # prints the key x's value
```



Examples
```python
# The range() function is often used when you need to loop a certain number of times. 
for i in range(20):
	print i 
	
# Loop over a list
my_list = ["a", "b", "c", "d", "e"]
for item in my_list:
    print "This item is", item

# Incorporate counters into for loops
i = 0
for item in my_list:
    print "Item", i, "is", item
    i += 1 # Use +=, -=, *=, /= to modify the variable in place!
```

<br><br>
##IF is the basic decision making tool
```
# if can be used on its own
if <logical statement is True>:
	do this command
	do that command
	
# if can be used with an "else". Code in "else" runs when the if condition is False.
if <logical statement is True>:
    do this command
else:
    do that command

# if can be used with "elif" statements to test multiple conditions
# you can have as many elif's as you want!
# Once one condition is true, the rest of the if/elif/else construct will *not be executed*
if <logical statement is True>:
    do this command
elif <some other logical statement is True>:
    do that command
elif <yet another logical statement is True>:
    do those commands
else: 
    do this here command
```

Example: check to see if a certain sequence is within a sequence
```python
# Check if a certain sequence exists in a bigger sequence
sequence='AGGGTGTGTCCTGA'
if 'TGT' in sequence:
	print "AGG is in the sequence!"
if 'ACC' in sequence:
    print "ACC is in the sequence!"

# Test the sequence size
if len(sequence) < 10:
    print "This is a small sequence."
elif len(sequence) > 100:
    print "This is a big sequence."
else:
    print "This sequence is medium-sized."

```
<br><br>
##Examples: Combining if and for
```
# test whether sequence is RNA or DNA by seeing if there is a uracil
seqs=['AUUGAC', 'AGACT', 'CGATAGCA', 'UCCAGAC', 'UGGACU', 'TAGCAGA']
for seq in seqs:
	if 'U' in seq and 'T' not in seq:
		print seq, "is probably RNA"
	elif 'T' in seq and 'U' not in seq:
		print seq, "is probably DNA"
	elif 'T' in seq and 'U' in seq:
	    print seq, "has both T and U. I don't know what it is!"
	elif 'T' not in seq and 'U' not in seq:
	    print seq, "has neither T nor U. I don't know what it is!"
```
