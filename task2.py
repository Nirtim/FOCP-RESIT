import sys

def formattime(minutes):
    # Convert minutes to hours and minutes(in string)
    hours = minutes // 60
    minutes = minutes % 60
    return f"{hours} Hours, {minutes} Minutes"

def readlog(filename):
    try: #trying in case of error
        with open(filename, 'r') as file:
            lines = file.readlines()
        #initial reading
        catvisits = 0
        intruder = 0
        housetime = 0
        visit_lengths = []

        for line in lines: #line by line processing of log
            if line.strip() == "END":
                break  #end of log

            cat, entry_time, exit_time = line.strip().split(',')
            entry_time, exit_time = int(entry_time), int(exit_time)

            if cat == "OURS": #seperating our cats from intruders
                catvisits += 1
                housetime += exit_time - entry_time
                visit_lengths.append(exit_time - entry_time)
            else:
                intruder += 1

        if catvisits > 0:
            avg_visit_length = sum(visit_lengths) / catvisits #average
            longest_visit = max(visit_lengths) #shortest
            shortest_visit = min(visit_lengths) #longest
        else:
            avg_visit_length = longest_visit = shortest_visit = 0

        #results
        print("\nLog File Analysis")
        print("="*len("Log File Analysis"))
        print(f"Cat Visits: {catvisits}")
        print(f"Other Cats: {intruder}\n")
        print(f"Total Time in House: {formattime(housetime)}\n")
        print(f"Average Visit Length: {formattime(avg_visit_length)}")
        print(f"Longest Visit: {formattime(longest_visit)}")
        print(f"Shortest Visit: {formattime(shortest_visit)}")

    except FileNotFoundError: #error handling in case the file is not found or file name wrong
        print(f'Cannot open "{filename}"!')

if __name__ == "__main__":
    #if filename is givem in command line arguement
    if len(sys.argv) != 2:
        print("Missing command line argument!") #needs to omen in command prompt
    else:
        filename = sys.argv[1] #passing script since it is given in.log format
        readlog(filename)
