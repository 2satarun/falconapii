from main.models import *
from main.settings import *

def process_ge():
        #start = datetime.datetime.now()
        #if req.method == 'GET':
            l=[]
            for y in User.objects:
                a = int(y.id)
                z=str(y.time)
                x={
                "name":y.name,
                "time":z,
                "id":a
                 }
                l.append(x)
            return l
def process_pos(a):
        
           #if req.method =='POST':
           x=a
           #x = ('name')
           User(name =x ).save()
           return 
       
def process_upda(p,e):
          #if req.method =='PUT':
          
        #   x=p
        #   y=e
          user = User.objects.get(user_id=p)
          user.update(name=str(e))
          return 
      
def process_del(t):
          #if req.method =='DELETE':
        #   t=int(("id"))
          User.objects.get(user_id=t).delete()
          return 
        