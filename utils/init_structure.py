
import os

if __name__ == '__main__':

    print(os.listdir(os.path.curdir))
    
    for i in range(1, 32):
        path = f"day{i}"
        if not os.path.exists(path): 
            os.mkdir(path)
            
            with open(path+"/input", mode="w") as fp:
                pass
            with open(path+"/test1", mode="w") as fp:
                pass

    