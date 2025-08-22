tbl_list =["Products","Order","Customers"]

for i in tbl_list:
    print(i)
    if(i.lower()=="order"):
        break



for i in tbl_list:
    if(i.lower()=="order"):
        continue
    print(i)