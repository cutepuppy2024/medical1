class Tv:
    channel = 0
    color = "black"
    size = 65
    volume = 0

    def up_volume(self,volume):
        self.volume += volume
    def down_volume(self,volume):
        self.volume -+ volume
        
    def up_channel(self,channel):
        self.channel += channel       
    def down_channel(self,channel):
        self.channel -= channel
        
        
t1 = Tv()    # 객체선언
t1.color = "화이트"
t1.channel = 0
t1.size = 65
t1.up_channel(2)
print(f"철수 tv:{t1.color},{t1.size},{t1.channel},{t1.volume}")


# 철수-화이트,채널 10번 변경, 2증가
# 영희-핑크,채널 7번 변경, 5 증가 
# 반장-실버,채널 1번 변경, 채널 3 증가



class Tv:
    channel = 0
    color = "black"
    size = 65
    volume = 0
    
    def __init__(self,color='',channel=0,size=0, volume=0):
        self.color = color
        self.size = size
        self.channel = channel
        self.volume = volume
        
        
    def up_volume(self,volume):
        self.volume += volume
    def down_volume(self,volume):
        self.volume -+ volume
        
    def up_channel(self,channel):
        self.channel += channel
        
    def down_channel(self,channel):
        self.channel -= channel
        
t2 = Tv("핑크",65,0,7)
print(f"영희 tv:{t2.color},{t2.size},{t2.channel},{t2.volume}")
t2.up_channel(5)
print(f"영희 tv:{t2.color},{t2.size},{t2.channel},{t2.volume}")


t3 = Tv("실버",65,0,1)
print(f"반장 tv:{t3.color},{t3.size},{t3.channel},{t3.volume}")
t3.up_channel(3)
print(f"반장 tv:{t3.color},{t3.size},{t3.channel},{t3.volume}")




# clear










      





