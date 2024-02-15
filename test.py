def remove_vowels(input_string):
    vowels = "aeiouAEIOU"
    result = ''.join(char for char in input_string if char not in vowels)
    return result

# Example usage:
user_input = input("Enter a string: ")
output_string = remove_vowels(user_input)
print("String with vowels removed:", output_string)
################################################################################
def disemvowel(string_):
    vowels = "aeiouAEIOU"
    result = ''.join(char for char in string_ if char not in vowels)
    return string_ 

# Example usage:
string_="This website is for losers LOL!"
output_string = disemvowel(string_)
print(output_string)
##########################################################
