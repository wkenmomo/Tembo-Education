# Without changing the provided lists and dictionaries, create a script that cycles
# through all the parents and prints to the terminal the proper activities for
# their child's age group. When there are no more activities for that parent,
# print “curriculum complete!” and move on to the next parent.
#
# (Make sure your script accounts for any edge cases in the provided variables!)

parents = [
    {'parent': 'Henry', 'child': {'name': 'Calvin', 'age': 2}},
    {'parent': 'Ada', 'child': {'name': 'Lily', 'age': 3}},
    {'parent': 'Emilia', 'child': {'name': 'Petra', 'age': 1}},
    {'parent': 'Biff', 'child': {'name': 'Biff Jr', 'age': 4}},
    {'parent': 'Milo', 'child': {}},
    {'child': {'name': 'Biff', 'age': "0"}}
]

curriculum = [
    {
        'age': 1,
        'activity': [
            'Try singing a song together.',
            'Point and name objects.'
            ]
    },
    {
        'age': 2,
        'activity': [
            'Go outside and feel surfaces.',
            'Draw with crayons.',
            'Play with soundmaking toys or instruments.',
            'Look at family pictures together.'
            ]
    },
    {
        'age': 3,
        'activity': [
            'Build with blocks.',
            'Try a simple puzzle.',
            'Read a story together.'
            ]
    },
    {
        'age': 3,
        'activity': [
            'Pissing contest.'
            ]
    }
]

# Want to really shine and show us your chops?  Work in some of these stretch
# goals using any tools or libraries you see fit.
# - Personalize the message output to make it more friendly.
# - Allow users to input new activities & parents before executing the script.
# - Print one activity at a time per parent and continue cycling through until
#   all parents have recieved all their activities.

import sys
mapping = [-1]*201 #maps age to index in curriculum in case it's not sorted or gaps
for i in range(0, len(curriculum)):
    try:
        if mapping[curriculum[i]['age']] == -1:
            mapping[curriculum[i]['age']] = [i]
        else:
            mapping[curriculum[i]['age']] = mapping[curriculum[i]['age']]+[i]
    except IndexError as error:
        sys.stderr.write("Children older than 200 years which is considered impossible for a human in around 2018")
        continue

for i in parents:
    try:
        print("Hello "+i["parent"])
    except KeyError:
        pass
    try:
        print("And little " +i["child"]["name"])
    except KeyError:
        print("What's the baby's name?")
    try:
        for j in mapping[i["child"]["age"]]:
            for k in curriculum[j]['activity']:
                print(k)
    except KeyError:
        print("age not found/negative/older than 200")
    except TypeError:
        print("Activities for your kid haven't been in our database yet")
    print("curriculum complete!")
