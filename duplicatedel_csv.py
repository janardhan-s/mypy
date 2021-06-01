import csv

def delete_duplicates_from_csv_file(filename):
    data_list = []
    
    fd = open(filename, 'rt')
    fdata = csv.reader(fd)
    
    for row in fdata:
        #print(row)
        data_list.append(row)
    
    #print(len(data_list))
        
    n = len(data_list)
    i=1
    j=1
    while(i < n):
        j=i+1
        while(j<n):
            phone1 = "".join(data_list[i][4].split())
            phone2 = "".join(data_list[i][5].split())
            
            num1 = "".join(data_list[j][4].split())
            num2 = "".join(data_list[j][5].split())
            if (phone1 == num1 or phone1 == num2):
                del(data_list[j])
                n = n - 1
            if (phone2 == num2):
                del(data_list[j][5])
                
            j = j + 1
        i = i + 1
    fd.close()
    print("data_list:",data_list)
    for r in data_list:
        print(r[4], r[5])
    return (data_list)
	
def main():
    filename = "users-data.csv"
    unique=delete_duplicates_from_csv_file(filename)
    #for r in unique:
        #print(r)
if (__name__=="__main__"):
	main()