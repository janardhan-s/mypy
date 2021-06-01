import math
import csv
def employees_data_sheet(filename):
    data_list = []
    
    fd = open(filename, 'rt')
    fdata = csv.reader(fd)
    
    for row in fdata:
        print(row)
        data_list.append(row)
    print(len(data_list))

    n = (len(data_list))
    i = 1
    
    while(i < n):
        
        data_list[i][3] = int(data_list[i][2])/3600
        data_list[i][3] = math.ceil(data_list[i][3])
        #data_list[i][3] = round(data_list[i][3])round is one more function as like math.ceil and math.floor
        data_list[i][5] = int(data_list[i][4])/3600
        data_list[i][5] = math.ceil(data_list[i][5])
        
        data_list[i][6] = int(data_list[i][2]) - int(data_list[i][4])
       
        
        data_list[i][7] = data_list[i][3] - data_list[i][5]
        
        
        data_list[i][8] = data_list[i][5] / data_list[i][3] * 100
        data_list[i][8] = math.floor(data_list[i][8])

        
        i = i + 1
    #print(data_list)
    for r in data_list:
        print(r)
    return (data_list)
    
    
def main():
    filename = "02-data.csv"
    result = employees_data_sheet(filename)
    print(result)
    jdata = []
    for r in result:
        gfile = (['{},{},{},{},{},{},{},{},{}'.format(r[0],r[1],r[2],r[3],r[4],r[5],r[6],r[7],r[8])])
        #print(gfile)
        jdata.append(gfile)
    #print(jdata)
    with open("guser.csv", 'w') as csv_file:
        dd = csv.writer(csv_file, delimiter = '\t')
        for line in jdata:
            dd.writerow(line)

if (__name__=="__main__"):
	main()