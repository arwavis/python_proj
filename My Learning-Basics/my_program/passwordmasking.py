import sys, readchar
import getpass

user_password = getpass.getpass('Password:')


# def passprompt(prompt: str, out=sys.stdout) -> str:
#     out.write(prompt);
#     out.flush()
#     password = ""
#     while True:
#         ch = str(readchar.readchar(), encoding='UTF-8')
#         if ch == '\r':
#             break
#         elif ch == '\b':
#             out.write('\b \b')
#             password = password[0:len(password) - 1]
#             out.flush()
#         else:
#             password += ch
#             out.write('*')
#             out.flush()
#     return password
#
#
# password_user = input(passprompt())


# https://stackoverflow.com/questions/27631629/masking-user-input-in-python-with-asterisks/69738764#69738764
