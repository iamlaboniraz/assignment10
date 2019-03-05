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
    x={}
    data_for_yes=0
    data_for_no=0
    data_for_ok=0
    
    count_number_for_yes=0
    count_number_for_no=0
    count_number_for_ok=0
    
    for i in List_of_data:
        if i[1]=='YES':
            data_for_yes=data_for_yes+float(i[0])
            count_number_for_yes=count_number_for_yes+1
            average_for_yes=(data_for_yes/count_number_for_yes)
            x[i[1]]=average_for_yes
        if i[1]=='NO':
            data_for_no = data_for_no+float(i[0])
            count_number_for_no = count_number_for_no+1
            average_for_no=(data_for_no/count_number_for_no)
            x[i[1]]=average_for_no
        if i[1]=='OK':
            data_for_ok = data_for_ok+float(i[0])
            count_number_for_ok = count_number_for_ok+1
            average_for_ok=(data_for_ok/count_number_for_ok)
            x[i[1]]=average_for_ok
    return x
def misclassified(List_of_data=None):
    x=[]
    a=[]
    average_value=computeAverageForClasses(List_of_data)
    for i in List_of_data:
        if i[1]=='YES':
            if average_value is not None and abs(float(i[0])-float(average_value['YES']))>abs(float(i[0])-float(average_value['NO'])):
                a.append(i)
        if i[1]=='NO':
            if average_value is not None and abs(float(i[0])-float(average_value['NO']))>abs(float(i[0])-float(average_value['YES'])):
                a.append(i)
        if i[1]=='OK':
            if average_value is not None and abs(float(i[0])-float(average_value['OK']))>abs(float(i[0])-float(average_value['NO'])):
                if average_value is not None and abs(float(i[0])-float(average_value['OK']))>abs(float(i[0])-float(average_value['YES'])):
                    a.append(i)        
    return a
if __name__=='__main__':
    List_of_data=readAllData('short_data.txt')
    #print(List_of_data)
    average_value = computeAverageForClasses(List_of_data)
    #print(average_value)
    misclass=misclassified(List_of_data)
    print(misclass)       


