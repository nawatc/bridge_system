import re


text = "He was carefully disguised but captured quickly by police."
print(re.findall(r"\w+ly\b", text))

#print(re.search("c", "abcdef")    ) 





"""if __name__ == '__main__':
    #main()
    pass"""