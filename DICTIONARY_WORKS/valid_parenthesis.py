user_input="{[}]"
is_valid=False
bracket_pairs={
    "{":"}",
    "[":"]",
    "(":")",
    "<":">"
}
symbol_stack=[]
top=-1
for ch in user_input:
    if ch in bracket_pairs:
        top+=1
        symbol_stack.append(ch)
    else:
        if top==-1:
            is_valid=False
            break
        else:
            current_symbol_closing=bracket_pairs.get(symbol_stack[top])
        if current_symbol_closing==ch:
            symbol_stack.pop()
            top-=1
        else:
            is_valid=False
            break
else:
    if len(symbol_stack)==0:
        is_valid=True
    else:
        is_valid=False
print(is_valid)
