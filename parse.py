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
#_COMMENT             print("Found Special:\t",char)
            token.append(char)
            i+=1
            continue
        
        # strings
        if char == '"':

            string = '"'
            i+=1
            while i < n and json_string[i] !='"':
                string+= json_string[i]
                i+=1

            if i >= n:
                raise ValueError("Unterminated string",json_string)
            
            # ending '"' 
            string+= json_string[i]
            i+=1

            token.append(string)
#_COMMENT             print("Found String:\t",string)
            continue
        
        # numbers
        if char.isdigit() or char == "-":

            number = char
            i+=1
            # This is a tokenizer only. We should worry about the double '.' or '+' in the middle in the parser stage.
            while i<n and (json_string[i].isdigit() or json_string[i] in ".+-"):
                number+=json_string[i]
                i+=1
#_COMMENT             print("Found Number:\t",number)

            token.append(number)
            continue

        # literals

        if char.isalpha():

            literal = ''

            while i < n and json_string[i].isalpha():
                literal+= json_string[i]
                i+=1
            if literal in ["true","false","null"]:
#_COMMENT                 print("Found Literal:\t",literal)
                token.append(literal)
            else:
                raise ValueError("Invalid Literal")
            
            continue
            
    return token


# Simple Test
test_string = '{ "key" : "value", "nums" : [1, -2.5, true, null] }'
print(f"Tokenizing the string: {test_string}\n")
try:
    result_tokens = tokenize(test_string)
    print(f"Resulting tokens: {result_tokens}")
except ValueError as e:
    print(f"Error: {e}")