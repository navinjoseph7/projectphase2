def make_snippet(str1):
    
    li = str1.split()
    if len(li) <= 5:
        return str1
    else:
        first_five = li[:5]
        snippet = " ".join(first_five)
        return snippet + " ..."