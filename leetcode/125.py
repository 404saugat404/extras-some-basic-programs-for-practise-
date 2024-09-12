class solutions:
    def valid_pal(string):
        new_str=""

        for s in string:
            if s.isalnum():
                new_str+=s

        return new_str[:]==new_str[::-1]
    


# abc=solutions

# value="race a car"
# print(abc.valid_pal(value))