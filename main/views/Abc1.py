from main.helpers.commons import *
import falcon

class abc1():

    def on_get(self, req, resp):
        """Handles GET requests"""
        resp.status = falcon.HTTP_200  
        resp.content_type = falcon.MEDIA_JSON
        '''l=[]
        for y in User.objects:
            a = int(y.id)
            z=str(y.time)
            x={
            "name":y.name,
            "time":z,
            "id":a
            }
            l.append(x)'''
        z = process_ge()
        resp.media = z
    def on_post(self, req, resp):

         """Handles post requests"""
         resp.status = falcon.HTTP_200  
         resp.content_type = falcon.MEDIA_JSON
         a = req.media.get("name")
         #y = process_pos()
         #User(name =x ).save()
         y = process_pos(a)
         resp.media = {
             'result':'done'
         }

    def on_put(self, req, resp):
        resp.status = falcon.HTTP_200  
        resp.content_type = falcon.MEDIA_JSON
        p = int(req.media.get("id"))
        e = req.media.get("name")
        '''user = User.objects.get(user_id=p)
        user.update(name=str(e))'''
        n = process_upda(p,e)
        
        resp.media = {
            'result':'successfully update'
        }
        
        
    def on_delete(self, req, resp):
        resp.status = falcon.HTTP_200  
        resp.content_type = falcon.MEDIA_JSON
        t=int(req.media.get("id"))
        #User.objects.get(user_id=t).delete()
        t = process_del(t)
        resp.media = {
            'result':'deleted'
        }



