

def take_pic():
    #return pic
    pass

def standerdise(pic):
    pass

def read_qr():
    pass

def update_DB():
    pass

def Cam_analysis(type):
    std_pic=standerdise(take_pic())
    if type == "qr":
        read_qr()
    else:
        pass
    update_DB()
    
