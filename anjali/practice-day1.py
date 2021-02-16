#dictionaries
myDict = {'book':'we read',
'school':'we go',
'pen':'we write',
'anotherdict':{'wreck it':'destroy it',
'venelope':'chracter',},
'prayer':'school'}
print(myDict)
print(myDict['school'])
print(myDict['pen'])
print(myDict['anotherdict']['wreck it'])
#dictionaries methods
print(myDict.keys())
print(myDict.values())
print(myDict.items())
updatedone={'cartoon':'animation'}
myDict.update(updatedone)
print(myDict)
print(myDict.get('school'))#it will not throw an error if word is not present in the dictionary
