import string
def rot13(msg):
    trans_table = message.maketrans(string.ascii_lowercase + string.ascii_uppercase,
                                    string.ascii_lowercase[13:] + string.ascii_lowercase[:13] +
                                    string.ascii_uppercase[13:] + string.ascii_uppercase[:13])
    enc_msg = msg.translate(trans_table)

    return enc_msg

def main():
    msg = input("Enter a message to encode: ")
    enc_msg = rot13(msg)
    print(encoded_message)

if __name__ == '__main__':
    main()
