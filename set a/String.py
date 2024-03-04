def modification(str1):
    search=input("What You want to change : ")
    replace=input("What you want to insert : ")
    str1=str1.replace(search, replace)
    print("Modified String : ",str1)

string1=input()
string2=input()
con_str=string1+" "+string2
print("Concatenation          : ",con_str)
print("The length of String 1 : ",len(string1))
print("The length of String 2 : ",len(string2))
modification(string1)