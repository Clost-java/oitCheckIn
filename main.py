from user import User
from index import UserApi





def main():
    
    
    dataset1= User(username="学号", password="身份证后六位",key="sendkey")
    # 例子 dataset1= User(username="202071100xx", password="123456",key="abcd")
    # dataset2= User(username="学号", password="身份证后六位",key="sendkey")

   
    
    
    #继续添加dataset3,dataset4......同时添加到下面的dataset中
    dataset = [dataset1]
    for x in range(0,len(dataset)):
        userAPI = UserApi(dataset[x])
        userAPI.login()
        userAPI.report()
        userAPI.push()
    
 
def main_handler(event, context):
    return main()
if __name__ == '__main__':
    main()
    
