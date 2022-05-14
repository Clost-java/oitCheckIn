from time import time
from user import User
from index import UserApi
import time

def main():
    dataset1= User(username="202071100xx", password="123456",key="1")
    # 例子 dataset1= User(username="202071100xx", password="123456",key="abcd")
   

    #继续添加dataset3,dataset4......同时添加到下面的dataset中
    dataset = [dataset1]
    for x in range(0,len(dataset)):
        userAPI = UserApi(dataset[x])
        cookie = userAPI.login()
        userAPI.report(cookie)

        time.sleep(2)
        userAPI.push()
    
 
def main_handler(event, context):
    return main()
if __name__ == '__main__':
    main()
    
