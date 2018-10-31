import csv

#events file
events_file = open(r'data/events.csv','w',newline='\n')
writer = csv.writer(events_file,delimiter=',')

# first file:
with open(r'data/events1.csv','r') as f:
    reader = csv.reader(f)
    for row in reader:
        writer.writerow(row)
        
# seond file:    
with open(r'./data/events2.csv') as f:
    reader = csv.reader(f)
    next(reader) # skip header
    for row in reader:
        writer.writerow(row)
   
events_file.close()


#rides file
rides_file = open(r'data/rides.csv','w',newline='\n')
writer = csv.writer(rides_file,delimiter=',')

# first file:
with open(r'data/rides1.csv','r') as f:
    reader = csv.reader(f)
    for row in reader:
        writer.writerow(row)
        
# now the rest:
for num in range(2,11):
    file = open(r'./data/rides{}.csv'.format(num))   
    reader = csv.reader(file)
    next(reader) # skip header
    for row in reader:
        writer.writerow(row)
   
rides_file.close()