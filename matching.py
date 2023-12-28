def matching_char(s : str , word_list : list):
    count  = 0
    for word in word_list:
        matching_character = True
        required_character = True
        for char in  word:
            if char not in s:
                matching_character = False
                break
        for char in s:
            if char not in  word:
                required_character = False
                break
        if matching_character and required_character:
            count +=1
    return count


print(matching_char('ab' , ['abbbb' , 'ad', 'acccc','bb','abaaba', 'ba','baad']))
