#opened file um-server-01.txt and assigned opend file to veriable log_file
log_file = open("um-server-01.txt")

#defined a function which loops though each line of the open file
def sales_reports(log_file):
    for line in log_file:
        #remove all the axtra space from the ends
        line = line.rstrip()
        #Assighn 3 first symbols to variable day
        day = line[0:3]
        #check condition and print the line if condition is met
        if day == "Mon":
            print(line)


sales_reports(log_file)
