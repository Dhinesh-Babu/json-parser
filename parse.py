def tokenize(json_string:str) -> list[str]:
    token = []

    i = 0
    n = len(json_string)

    while i<n:
        char = json_string[i]
        # whitespace
        if char.isspace():
            i+=1
            continue

        # single-character / punctuations
        if char in '{}[],:':
            token.append(char)
            i+=1
            continue
        
        # strings
        if char == '"':
            #TODO I think we need some kind of loop.
            print("TBI")
            continue
        
        # numbers
        if char.isdigit():
            #TODO
            print("TBI")
        
        # literals
            #TODO i think if we get char done we can just use the same logic.
            
    return token