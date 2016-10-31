# SQLDataGen
''' firstName	VARCHAR(12)	NOT NULL,
lastName	VARCHAR(12)	NOT NULL,
dateOfBirth	DATE		NOT NULL,
hoursFlown '''

import random
import string

def pilot():

    data = ''
    firstnameSample = ['adam','james','kyle', 'Terresa', 'Rosamaria', 'Glayds', 'Cameron', 'Sau', 'Francis', 'Jeri', 'Merideth' \
                   , 'Aja', 'Shanon', 'Kamilah', 'Rita', 'Elissa', 'Agatha', 'Glendora', 'Yulanda', 'Letha', 'Deeanna', 'Amina', 'Rocio']
    lastnameSample = ['Smith', 'Rawlin', 'Ellery', 'Tutty', 'Mason', 'Howlett', 'Courts', 'Kidd', 'King', 'Hunt', 'Morg', 'Boag', 'Higgins', 'Hugo', 'Stanton']

    for i in range (0,20):
        person = '(\''
        firstname = firstnameSample[random.randint (0, len(firstnameSample) -1)]
        lastname = lastnameSample[random.randint (0, len(lastnameSample) -1)]
        dateOfBirth = str(random.randint(1950,2000)) + '-' + str(random.randint(1,12)) + '-' + str(random.randint(1,28))
        hoursFlown = random.randint(0,2000)
        person += firstname + '\', \'' + lastname + '\', \''+ dateOfBirth + '\', ' + str(hoursFlown) + '),'
        print (person)

def plane():
    for i in range (0,20):
        rego = ''
        modelNumbers = ['dna0f0ez4mt9', '9o4x8evm74v6', 'v16hiprr2zbs', 'd53wq2hz99kv', 'ns2ecikvuz6r', 'agclnxs1lfb8', 'ep7xli41qofu']
        dateBuilt = str(random.randint(1980,2016)) + '-' + str(random.randint(1,12)) + '-' + str(random.randint(1,28))
        sampleSpace = string.ascii_lowercase + string.digits
        firstClassCap = random.randrange(50,300, 10)
        ecoClassCap = random.randrange(100,500, 10)
        modelNum = modelNumbers[random.randint(0, len (modelNumbers)-1)]
        for i in range (0,12):
            rego += sampleSpace[random.randint(0, len(sampleSpace) -1)]
        plane = '(\'' + rego + '\', \'' + dateBuilt + '\', ' + str(firstClassCap) + ', ' + str(ecoClassCap) + ', \'' + modelNum + '\'),'
        print (plane)

def model():
    for i in range (0,7):
        modNum = ''
        fuelRange = random.randrange(5000,7000000, 100)
        crusingSpeed = random.randrange(150, 400, 5)
        sampleSpace = string.ascii_lowercase + string.digits
        for i in range (0,12):
                modNum += sampleSpace[random.randint(0, len(sampleSpace) -1)]
        model = '(\'' + modNum + '\', \'modelName\', ' + str(fuelRange) + ' , ' + str(crusingSpeed) + '),'
        print (model)

def attendant():

    data = ''
    firstnameSample = ['adam','james','kyle', 'Terresa', 'Rosamaria', 'Glayds', 'Cameron', 'Sau', 'Francis', 'Jeri', 'Merideth' \
                   , 'Aja', 'Shanon', 'Kamilah', 'Rita', 'Elissa', 'Agatha', 'Glendora', 'Yulanda', 'Letha', 'Deeanna', 'Amina', 'Rocio']
    lastnameSample = ['Smith', 'Rawlin', 'Ellery', 'Tutty', 'Mason', 'Howlett', 'Courts', 'Kidd', 'King', 'Hunt', 'Morg', 'Boag', 'Higgins', 'Hugo', 'Stanton']

    for i in range (0,20):
        person = '(\''
        firstname = firstnameSample[random.randint (0, len(firstnameSample) -1)]
        lastname = lastnameSample[random.randint (0, len(lastnameSample) -1)]
        hireDate = str(random.randint(1950,2000)) + '-' + str(random.randint(1,12)) + '-' + str(random.randint(1,28))
        if random.randint(0,2) >= 1 and i != 0:
            FSM = random.randint(1,i)
            person += firstname + '\', \'' + lastname + '\', \''+ hireDate + '\', ' + str(FSM) + '),'
        else:
            FSM = ''
            person += firstname + '\', \'' + lastname + '\', \''+ hireDate + '\', NULL),'
        print (person)

def airport():
    for i in range (0,20):
        portNum = ''
        phNum = '0410'
        countryCodes = ['AUS', 'USA', 'CAN', 'CHI', 'DEN', 'EGY']
        sampleSpace = string.digits
        for i in range (0,6):
            phNum += sampleSpace[random.randint(0, len(sampleSpace) -1)]
        countryCode = countryCodes[random.randint(0, len(countryCodes) - 1)]
        lat = str(random.randint(-90, 90)) + '.' + str(random.randint(0, 255))
        long = str(random.randint(-180, 180)) + '.' + str(random.randint(0, 255))
        sampleSpace = string.ascii_lowercase + string.digits
        for i in range (0,12):
            portNum += sampleSpace[random.randint(0, len(sampleSpace) -1)]
        airport = '(\''+ portNum + '\', \'' + phNum + '\', \'' + lat + '\', \'' + long + '\', \'' + countryCode + '\'),'
        print (airport)
    


    

pilot()
plane()
model()
attendant()
airport()
