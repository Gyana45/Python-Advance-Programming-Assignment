'''Given a list of words in the singular form, return a set of those words in the plural form if they appear more than once in the list.

Examples

pluralize(["cow", "pig", "cow", "cow"]) ➞ { "cows", "pig" }

pluralize(["table", "table", "table"]) ➞ { "tables" }
pluralize(["chair", "pencil", "arm"]) ➞ { "chair", "pencil", "arm" }


'''
def pluralize(l):
    l_new=[]
    for i in l:
        if l.count(i)>1:
            i=i+'s'
            if i not in l_new:
                l_new.append(i)
        else: 
            l_new.append(i)   

    print(set(l_new)  )

pluralize(["cow", "pig", "cow", "cow"])  
pluralize(["table", "table", "table"])  
pluralize(["chair", "pencil", "arm"]) 