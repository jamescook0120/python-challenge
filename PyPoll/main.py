import csv 
import os

file = os.path.join('Resources','election_data.csv')

with open(file) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')
    header=next(csvreader) 

    voterids=[]
    counties=[] 
    candidates=[] 
    candidatenames=[]
    totaleachcan=[]
    resultprintcan=[]
    totaleachcanperc=[]

   
    line_count=0
    winnervotes=0
    loservotes=0
    candidatenew=0
    counter=0
    analysis1=0
    x=0
    
   
    for row in csvreader:
        voterid=row[0]
        county=row[1] 
        candidate=row[2] 
        voterids.append(voterid)
        counties.append(county)
        candidates.append(candidate)
    
    line_count= len(voterids)


candidatenames.append(candidates[0])

for candidatenew in range (line_count-1):
    if candidates[candidatenew+1] != candidates[candidatenew] and candidates[candidatenew+1] not in candidatenames:
        candidatenames.append(candidates[candidatenew+1])

n=len(candidatenames)



for counter in range (n): 
    totaleachcan.append(candidates.count(candidatenames[counter]))

loservotes=line_count

for analysis1 in range(n): 
    totaleachcanperc.append(f'{round((totaleachcan[analysis1]/line_count*100), 4)}%')
    if totaleachcan[analysis1]>winnervotes: 
        winner=candidatenames[analysis1]
        winnervotes=totaleachcan[analysis1]
    if totaleachcan[analysis1]<loservotes:
        loser=candidatenames[analysis1]
        loservotes=totaleachcan[analysis1]

for x in range(n):
    resultprintcan.append(f'{candidatenames[x]}: {totaleachcanperc[x]} ({totaleachcan[x]})') #Format list resultprintcan

resultlines='\n'.join(resultprintcan) 

analysis=f'\
Election Results\n\
----------------------------\n\
Total Votes: {line_count}\n\
----------------------------\n\
{resultlines}\n\
----------------------------\n\
Winner: {winner} :)\n\
Last: {loser} :(\n\
----------------------------\n'

print(analysis) 
