def isvalidparenthese( s):
    open = ('{', '[', '(')
    close = ('}',']',')')
    open_stack = []
    for character in s:
        if character in open:
            open_stack.append (character)
        print(open_stack)
        if character in close:
            if open[close.index(character)] != open_stack.pop():
                return False
        print(open_stack) #true then leave it , false leave and return
        print('\n')
    return not open_stack # return true when list=[]
print(isvalidparenthese('{[()(({}))]}'))
