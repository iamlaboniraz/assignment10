def readAllData(List_of_data):
    result=[]
    #file_n=open('short_data.txt',mode='r',encoding='cp1252')
    #outputFile = "{}".format('short_data.txt')
    with open(List_of_data,'r') as file_n:
        for i in file_n.readlines():
            if i[0]!='X':
                result.append(tuple(i.split()))
    return result
def computeAverageForClasses(List_of_data=None):
    find_all_yes_no=[]
    find_yes_no=[]
    avg={}
    for i in List_of_data:
        find_all_yes_no.append(i[1])
    #print(find_all_yes_no)
    for i in range(len(find_all_yes_no)):
        for j in range(len(find_all_yes_no)):
            if find_all_yes_no[i]==find_all_yes_no[j]:
                if find_all_yes_no[j] not in find_yes_no:
                    find_yes_no.append(find_all_yes_no[j])
    #print(find_yes_no)
    number_yes_no=list(i*0 for i in range(0,len(find_yes_no)))
    total_number=list(j*0 for j in range(0,len(find_yes_no)))
    #print(number_yes_no,total_number)
    for i in List_of_data:
        for j in range(0,len(find_yes_no)):
            if i[1]==find_yes_no[j]:
                number_yes_no[j]+=float(i[0])
                total_number[j]+=1
    #print(number_yes_no,total_number)
    for i in range(0,len(find_yes_no)):
        avg[find_yes_no[i]]=number_yes_no[i]/total_number[i]
        #print(avg)
    return avg
def misclassified(List_of_data=None):
    x=[]
    a=[]
    y=[]
    average_value=computeAverageForClasses(List_of_data)
    for i in average_value:
        a.append(average_value[i])
        y.append(i)
    #print(y)
    length=len(a)-1
    #print(length)
    for i in range(0,len(a)-1):
        #print(i)
        for j in List_of_data:
            if j[1]==y[i]:
                if abs(float(j[0])-float(a[i]))>abs(float(j[0])-float(a[i+1])):
                    x.append(j)
                    
            if j[1]==y[i+1]:
                if abs(float(j[0])-float(a[i+1]))>abs(float(j[0])-float(a[i])):
                    x.append(j)
                    

    return x
if __name__=='__main__':
    List_of_data=readAllData('short_data.txt')
    #print(List_of_data)
    average_value = computeAverageForClasses(List_of_data)
    #print(average_value)
    misclass=misclassified(List_of_data)
    print(misclass)       






