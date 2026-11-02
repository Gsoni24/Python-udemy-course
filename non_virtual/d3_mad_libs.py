print('Bob\'s adventure!')
adjective1: str = input('Enter an adjective: ')
animal: str = input('Entere an animal: ')
adjective2: str = input('Enter another adjective: ')
noun1: str = input('Entere a noun: ')
verb: str = input('Enter a verb: ')
noun2: str = input('Entere another noun: ')

story: str = f'''
Bob went to see the zoo today. He saw a(n) {adjective1} {animal} jumping up and down in its tree.
He turned his back for two seconds, and when he turned around again, the {adjective1} {animal} had transformed
into a(n) {adjective2} {noun1}! He couldn't believe his eyes, so he started to {verb} with his {noun2}. 
In the end, he woke up and realised it was all a dream.
''' 

print('Result:')
print(story)