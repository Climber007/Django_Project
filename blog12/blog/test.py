import bcrypt
import datetime

password = b'123456'
# 每次拿到盐都不一样
print(1, bcrypt.gensalt())
print(2, bcrypt.gensalt())
salt = bcrypt.gensalt()

# 拿到的盐相同，计算等到的密文相同
print('=========same salt ==========')
x = bcrypt.hashpw(password, salt)
print(3, x)
x = bcrypt.hashpw(password, salt)
print(4, x)

print('=========different salt ==========')
x = bcrypt.hashpw(password, bcrypt.gensalt())
print(5, x)
x = bcrypt.hashpw(password, bcrypt.gensalt())
print(6, x)

for hashedpw in ['$2b$12$3yyi.8cNq3ifBGzd5UulGuXU.Fsx9nuEVOfBnrYWNTWKrIp1PJl9u']:
    x = bcrypt.checkpw(password, hashedpw.encode())
    print(x)