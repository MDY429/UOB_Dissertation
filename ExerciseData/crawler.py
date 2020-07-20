import requests
import re
import csv
import pandas as pd
from bs4 import BeautifulSoup

def csvProccess():
    
    with open('test.csv', 'w', newline='') as csvfile:
        fieldnames = ['Body', 'muscle', 'exercise', 'equipment', 'resource']

        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

        mainPage(writer)

    csvfile.close()

    # Remove duplicated elements.
    file_name = "test.csv"
    file_name_output = "Exercise.csv"

    inFile = open('test.csv','r')

    outFile = open('Exercise.csv','w')

    listLines = []

    for line in inFile:

        if line in listLines:
            continue

        else:
            outFile.write(line)
            listLines.append(line)

    outFile.close()

    inFile.close()


def mainPage(writer):
    response = requests.get("https://exrx.net/Lists/Directory")

    soup = BeautifulSoup(response.text, "html.parser")

    # Find the part of body tag
    a_tags = soup.find_all('a')
    for tag in a_tags:
        linkID = str(tag.get('href'))
        a = linkID.find('ExList/')
        b = linkID.find('#')
        if a != -1 and b == -1:
            switch(linkID[a+7:], writer)


def switch(body, writer):
    '''
    Input the part of body then call the corresponding method.
    '''
    link = "https://exrx.net/Lists/ExList/" + body
    if body == 'NeckWt':
        neck(link, writer)
    elif body == 'ShouldWt':
        shoulder(link, writer)
    elif body == 'ArmWt':
        UpperArms(link, writer)
    elif body == 'ForeArmWt':
        ForeArms(link, writer)
    elif body == 'BackWt':
        back(link, writer)
    elif body == 'ChestWt':
        chest(link, writer)
    elif body == 'WaistWt':
        waist(link, writer)
    elif body == 'HipsWt':
        hips(link, writer)
    elif body == 'ThighWt':
        thighs(link, writer)
    elif body == 'CalfWt':
        calves(link, writer)
    else:
        print("Not such part of body")


def neck(link, writer):
    print(link)
    response = requests.get(link)
    soup = BeautifulSoup(response.text, "html.parser")
    titles = soup.find_all("h2")
    muscles = []
    for title in titles:
        muscles.append(title.getText())

    print(muscles)
    results = soup.find_all("a")
    for res in results:
        linker = str(res.get("href"))
        for m in muscles:
            a = linker.find('WeightExercises/' + m)
            muscleLen = len(m)
            if a != -1:
                newUrl = "https://exrx.net/" + linker[a:]
                subUrl = linker[a+muscleLen+17:]
                print(newUrl)
                getExercise(writer, 'neck', m, getEquipment(subUrl[0:2]), newUrl)


def shoulder(link, writer):
    response = requests.get(link)
    soup = BeautifulSoup(response.text, "html.parser")
    titles = soup.find_all("h2")
    muscles = ['DeltoidAnterior', 'DeltoidLateral',
               'DeltoidPosterior', 'Supraspinatus']

    print(muscles)
    results = soup.find_all("a")
    for res in results:
        linker = str(res.get("href"))
        for m in muscles:
            a = linker.find('WeightExercises/' + m)
            muscleLen = len(m)
            if a != -1:
                newUrl = "https://exrx.net/" + linker[a:]
                subUrl = linker[a+muscleLen+17:]
                print(newUrl)
                getExercise(writer, 'shoulder', m, getEquipment(subUrl[0:2]), newUrl)


def UpperArms(link, writer):
    response = requests.get(link)
    soup = BeautifulSoup(response.text, "html.parser")
    titles = soup.find_all("h2")
    muscles = ['Triceps', 'Biceps', 'Brachialis']

    print(muscles)
    results = soup.find_all("a")
    for res in results:
        linker = str(res.get("href"))
        for m in muscles:
            a = linker.find('WeightExercises/' + m)
            muscleLen = len(m)
            if a != -1:
                newUrl = "https://exrx.net/" + linker[a:]
                subUrl = linker[a+muscleLen+17:]
                print(newUrl)
                getExercise(writer, 'UpperArms', m, getEquipment(subUrl[0:2]), newUrl)


def ForeArms(link, writer):
    response = requests.get(link)
    soup = BeautifulSoup(response.text, "html.parser")
    titles = soup.find_all("h2")
    muscles = []
    for title in titles:
        s = title.getText().replace(" ", "")
        muscles.append(s)

    print(muscles)
    results = soup.find_all("a")
    for res in results:
        linker = str(res.get("href"))
        for m in muscles:
            a = linker.find('WeightExercises/' + m)
            muscleLen = len(m)
            if a != -1:
                newUrl = "https://exrx.net/" + linker[a:]
                subUrl = linker[a+muscleLen+17:]
                print(newUrl)
                getExercise(writer, 'ForeArms', m, getEquipment(subUrl[0:2]), newUrl)


def back(link, writer):
    response = requests.get(link)
    soup = BeautifulSoup(response.text, "html.parser")
    titles = soup.find_all("h2")
    muscles = ['BackGeneral', 'LatissimusDorsi',
               'TrapeziusUpper', 'Infraspinatus', 'Subscapularis']

    print(muscles)
    results = soup.find_all("a")
    for res in results:
        linker = str(res.get("href"))
        for m in muscles:
            a = linker.find('WeightExercises/' + m)
            muscleLen = len(m)
            if a != -1:
                newUrl = "https://exrx.net/" + linker[a:]
                subUrl = linker[a+muscleLen+17:]
                print(newUrl)
                getExercise(writer, 'back', m, getEquipment(subUrl[0:2]), newUrl)


def chest(link, writer):
    response = requests.get(link)
    soup = BeautifulSoup(response.text, "html.parser")
    titles = soup.find_all("h2")
    muscles = ['PectoralSternal', 'PectoralClavicular', 'SerratusAnterior']

    print(muscles)
    results = soup.find_all("a")
    for res in results:
        linker = str(res.get("href"))
        for m in muscles:
            a = linker.find('WeightExercises/' + m)
            muscleLen = len(m)
            if a != -1:
                newUrl = "https://exrx.net/" + linker[a:]
                subUrl = linker[a+muscleLen+17:]
                print(newUrl)
                getExercise(writer, 'chest', m, getEquipment(subUrl[0:2]), newUrl)


def waist(link, writer):
    response = requests.get(link)
    soup = BeautifulSoup(response.text, "html.parser")
    titles = soup.find_all("h2")
    muscles = ['RectusAbdominis', 'Transverse', 'Obliques', 'ErectorSpinae']

    print(muscles)
    results = soup.find_all("a")
    for res in results:
        linker = str(res.get("href"))
        for m in muscles:
            a = linker.find('WeightExercises/' + m)
            muscleLen = len(m)
            if a != -1:
                newUrl = "https://exrx.net/" + linker[a:]
                subUrl = linker[a+muscleLen+17:]
                print(newUrl)
                getExercise(writer, 'waist', m, getEquipment(subUrl[0:2]), newUrl)


def hips(link, writer):
    response = requests.get(link)
    soup = BeautifulSoup(response.text, "html.parser")
    titles = soup.find_all("h2")
    muscles = ['GluteusMaximus', 'HipAbductor',
               'HipFlexors', 'HipExternalRotator']

    print(muscles)
    results = soup.find_all("a")
    for res in results:
        linker = str(res.get("href"))
        for m in muscles:
            a = linker.find('WeightExercises/' + m)
            muscleLen = len(m)
            if a != -1:
                newUrl = "https://exrx.net/" + linker[a:]
                subUrl = linker[a+muscleLen+17:]
                print(newUrl)
                getExercise(writer, 'hips', m, getEquipment(subUrl[0:2]), newUrl)


def thighs(link, writer):
    response = requests.get(link)
    soup = BeautifulSoup(response.text, "html.parser")
    titles = soup.find_all("h2")
    muscles = []
    for title in titles:
        s = title.getText().replace(" ", "")
        muscles.append(s)

    print(muscles)
    results = soup.find_all("a")
    for res in results:
        linker = str(res.get("href"))
        for m in muscles:
            a = linker.find('WeightExercises/' + m)
            muscleLen = len(m)
            if a != -1:
                newUrl = "https://exrx.net/" + linker[a:]
                subUrl = linker[a+muscleLen+17:]
                print(newUrl)
                getExercise(writer, 'thighs', m, getEquipment(subUrl[0:2]), newUrl)


def calves(link, writer):
    response = requests.get(link)
    soup = BeautifulSoup(response.text, "html.parser")
    titles = soup.find_all("h2")
    muscles = ['Gastrocnemius', 'TibialisAnterior', 'Soleus']

    print(muscles)
    results = soup.find_all("a")
    for res in results:
        linker = str(res.get("href"))
        for m in muscles:
            a = linker.find('WeightExercises/' + m)
            muscleLen = len(m)
            if a != -1:
                newUrl = "https://exrx.net/" + linker[a:]
                subUrl = linker[a+muscleLen+17:]
                print(newUrl)
                getExercise(writer, 'calves', m, getEquipment(subUrl[0:2]), newUrl)


def getExercise(writer, body, muscle, equipment, url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    titles = soup.find_all("h1")
    for title in titles:
        print(title.getText())
        writer.writerow({'Body': body,
                         'muscle': muscle,
                         'exercise': title.getText(),
                         'equipment': equipment,
                         'resource': url})


def getEquipment(equipment):
    switcher = {
        'BB': 'Barbell',
        'CB': 'Cable',
        'DB': 'Dumbbell',
        'SM': 'Smith',
        'LV': 'Lever',
        'ST': 'Suspended',
        'BW': 'BodyWeight',
        'SL': 'Sled',
        'Wt': 'Weight',
        'WT': 'Weight',
        'BR': 'Band Resistive',
        'AS': 'Assisted',
        'As': 'Assisted',
        'TB': 'TrapBar',
        'SB': 'SafetyBarbell',
        'MB': 'MedicineBall'
    }
    return switcher.get(equipment, 'None')


csvProccess()
