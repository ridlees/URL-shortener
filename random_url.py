import random as r

def generate_random_string(length):
    random_string = ''
    random_str_seq = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    for i in range(0,length):
        random_string += str(random_str_seq[r.randint(0, len(random_str_seq) - 1)])
    return random_string

if __name__ == '__main__':
    print(generate_random_string(8))
