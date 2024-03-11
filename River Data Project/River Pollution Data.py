# Project 8 - Texas River Pollution Data
# CSC 110
# Evan Wallace

# This program generates reports on specific rivers in Texas, using data from the Texas Department of Ecology.

# Reads and writes data from a file, uses loop alogorithims including counters, accumulators, minimums and maximums.

def main():
    # UI:
    riverData =      input('Which river?: '    )
    monthData =      input('Which month?: '    )
    pollutantData =  int(input("Avaliable pollutants:\n"
                           '1. Arsenic\n'
                           '2. Lead\n'
                           '3. Fertilizer\n'
                           '4. Pesticides\n'
                           'Which Pollutant?:\n'))
    
    print('Processing of all rows is complete. See summary file for results.')

    riverFile = open('RiverPollutionData.txt', 'r')
    summaryFile = open('PollutionSummary.txt', 'w')

    # min/max reverse psychology
    maxLevel = -999
    minLevel =  999
    # count and accumulator variables
    totalReadings = 0
    countReadings = 0
    pollutantName = ''

    # loop through file, skip the first line:
    skipFirstLine = riverFile.readline()
    for riverLine in riverFile:
        riverFields = riverLine.strip().split('\t')
        riverIndex, monthIndex = riverFields[0], riverFields[1]
        pollutantNum = 0

        # set pollutant name
        if pollutantData == 1:
                pollutantName = 'Arsenic'
        elif pollutantData == 2:
                pollutantName = 'Lead'
        elif pollutantData == 3:
                pollutantName = 'Fertilizer'
        elif pollutantData == 4:
                pollutantName = 'Pesticides'
        else:
            pollutantName = 'This substance is not in our records'
        # calculates report based off user data entry 
        if riverIndex == riverData and monthIndex == monthData:
            if pollutantData == 1 or pollutantData == 2:
                pollutantNum = int(riverFields[pollutantData + 2])
                countReadings += 1

            elif pollutantData == 3 or pollutantData == 4:
                pollutantNum = float(riverFields[pollutantData + 2])
                countReadings += 1
            elif pollutantData > 4:
                 print('Out of range, please try again.')

            # update accumulator
            totalReadings += pollutantNum
            #min and max
            if pollutantNum >= maxLevel:
                maxLevel = pollutantNum
            if pollutantNum <= minLevel:
                minLevel = pollutantNum

    # average
    if countReadings > 0:
        averageReading = totalReadings /countReadings
    else:
        averageReading = 0

    # Write to text file:
    summaryFile.write('Data for river: '     + riverData                     + '\n'  )
    summaryFile.write('Data for month: '     + monthData                     + '\n'  )
    summaryFile.write('Data for pollutant: ' + pollutantName                 + '\n\n')
    summaryFile.write('Number of readings: ' + str(countReadings)            + '\n'  )
    summaryFile.write('Average of readings: '+ format(averageReading, ".3f") + '\n'  )
    summaryFile.write('Lowest reading: '     + format(minLevel, '.3f')       + '\n'  )
    summaryFile.write('Highest reading: '    + format(maxLevel, '.3f')       + '\n'  )
    

    riverFile.close()
    summaryFile.close()

main()






