from itertools import combinations

def yates_order (n):
	#calculate all tcs
	yates=['1']
	letters = ['a','b','c','d','e','f','g','h']
	for i in range(1, len(letters[:n])+1):  
		for j in list(combinations(letters[:n],i)):
			yates.append(j)
	return(yates)
	
def get_effects (n):
	#calculate all effects
	effects=[]
	letters = ['A','B','C','D','E','F','G','H']
	for i in range(1, len(letters[:n])+1):  
		for j in list(combinations(letters[:n],i)):
			effects.append(j)
		
	return(effects)
	
def pretty_print(thelist):
	#prints the effects or list in a more understandable way
	for element in thelist:
		for i in element:
			print(i, end="")
		print(" ", end="\n")
	print()

def pretty_print_alias(alias, cols):
	#pretty print of alias groups
	col=0
	for eff in alias:
		for p in eff:
			print(p, end="")
		col = col +1  
		print("", end="\t")
		if col == cols:
			col = 0
			print("\n")
		
		
def mod2(a, b):
	#performs mod2 multiplication of 2 x tuples
	result=""
	for i in a:
		if not(i in b):
			result = result + i
	for j in b:
		if not(j in a) and not(j in tuple(result)):
			result = result + j
	result = list(result)
	result.sort()
	return(tuple(result))

def other_i (i_effects, total_number=0):
	#calculate the rest of I effects. Multiply all by all.
	len_effects = len(i_effects)
	#get all combinations (subsets) to multiply them
	for L in range(0, len(i_effects)+1):
		for subset in combinations(i_effects, L):
			#multiply subsets with more than two elements
			#print(subset)
			if len(subset) >= 2:
				new_effect = mod2(subset[0],subset[1])
				# if result not in list add it
				if new_effect not in i_effects:
					i_effects.append(new_effect)
			
	#if no new effects were added return
	if len(i_effects) == len_effects:
		return(i_effects)
	else:
		i_effects = other_i(i_effects)
	return(i_effects)
	
	

if __name__ == "__main__":
		
	# ask for number of factors (n) and p
	print("\n\n----------------------------")
	print("FRACTIONAL FACTORIAL DESIGNS\n\n")
	
	#number of factors
	n = int(input("Please enter the number (n) of 2 level factors (2^n): "))
	#number p (effects to lose)
	p = int(input("Please enter p (p is 2^"+str(n)+"-p):"))
	while p > n:
		print("p not valid")
		p = int(input("Please enter p (p is 2^"+str(n)+"-p):"))
	
	#calculate all effects
	effects = get_effects(n)
	print("\n\nHere are all the possible effects of the experiment:\n")
	pretty_print(effects)
	print("--------------------- TOTAL:", str(len(effects)),"EFECTS")
	
	#how many I effects are there? 
	number_i = (2**p) - 1
	print("\nThere are "+str(number_i)+" defining relation effects (I). Introduce them one by one" )
	i_effects = []
	for i in range(number_i):
		ief = input(str(i+1)+":")
		i_effects.append(tuple(ief))
		i_effects = other_i(i_effects)
		if len(i_effects) == number_i:
			print("\nBy multiplication mod 2 you go all the effects!:\n")
			pretty_print(i_effects)
			break
	
	input("\n\n\nPress ENTER to continue ..... \n\n")
	
	# calculate alias groups
	print("\nWe now proceed to calcualte the aliases groups, introduce all the effects by priority. Here is the list:")
	final_effects = []
	effects_left = [x for x in effects if x not in i_effects]
	pretty_print(effects_left)
	print("--------------------- TOTAL:", str(len(effects_left)),"EFECTS")
	
	rows = int(len(effects_left)/(2**p))
	for i in range(rows):
		while True:
			sel_effect = tuple(input("::"))
			if sel_effect not in effects_left:
				print("The effect is already in use, select another one")
			else:
				break
		final_effects.append(sel_effect)
		effects_left.remove(sel_effect)
		for k in i_effects:
			alias_ef = mod2(sel_effect,k)
			final_effects.append(alias_ef)
			effects_left.remove(alias_ef)
		print("Another from:")
		pretty_print(effects_left)	
		print("--------------------- TOTAL:", str(len(effects_left)),"EFECTS")	
	
	print("\n\n")
	pretty_print_alias(final_effects,2**p)			
	
	# get principal block!
	

	# do you want to select dead letters?

	# if ok calculate yates order (with dead letters)

	# do you want to enter the values of observations?

	# calculate results (also calculate signs)