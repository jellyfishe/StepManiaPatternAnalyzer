import re

patterns = []

def multiRegex(lst):
    return '(' + lst.join(')|(') + ')'

def analyze(filename, dance_type, difficulty):
    crossoverRegex = re.compile(r'1000\n0100\n0001') # Left crossover
    beatmapRegex = re.compile('(?s)(?:{0}[:\s]*{1}[:\s]*\d+[:\n\s]*)([^;]*)(?:;)'.format(dance_type, difficulty))

    with open(filename, 'r') as f:
        data = f.read()
        beatmap = beatmapRegex.search(data)
        if beatmap:
            crossovers = crossoverRegex.findall(beatmap.group(1))
            if crossovers:
                print('The number of crossovers is: ' + str(len(crossovers)))
            else:
                print('There are no crossovers in this beatmap.')
        else:
            print('Could not read beatmap for specified difficulty or dance type')

# Testing/Mainy
analyze('Schrodinger no neko.sm', 'dance-single', 'Hard')
