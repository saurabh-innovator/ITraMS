from collections import namedtuple
from pprint import pprint as pp
import sys
from twilio.rest import Client

account_sid = "//twilio account ssid"
auth_token = "//twilio account auth token"

client = Client(account_sid, auth_token)

Pt = namedtuple('Pt', 'x, y')               # Point
Edge = namedtuple('Edge', 'a, b')           # Polygon edge from a to b
Poly = namedtuple('Poly', 'name, edges')    # Polygon
 
_eps = 0.00001
_huge = sys.float_info.max
_tiny = sys.float_info.min
 
def rayintersectseg(p, edge):
    ''' takes a point p=Pt() and an edge of two endpoints a,b=Pt() of a line segment returns boolean
    '''
    a,b = edge
    if a.y > b.y:
        a,b = b,a
    if p.y == a.y or p.y == b.y:
        p = Pt(p.x, p.y + _eps)
 
    intersect = False
 
    if (p.y > b.y or p.y < a.y) or (
        p.x > max(a.x, b.x)):
        return False
 
    if p.x < min(a.x, b.x):
        #print("You are inside the boundary limit, Happy Driving.")
        intersect = True
    else:
        if abs(a.x - b.x) > _tiny:
            m_red = (b.y - a.y) / float(b.x - a.x)
        else:
            m_red = _huge
        if abs(a.x - p.x) > _tiny:
            m_blue = (p.y - a.y) / float(p.x - a.x)
        else:
            m_blue = _huge
        intersect = m_blue >= m_red
    if intersect==True:
        client.api.account.messages.create(
            to="+918860851203",
            from_="+1 971-803-5931 ",
            body="You are inside the boundary limit, Happy Driving.")
        print("You are inside the boundary limit, Happy Driving.")
    else:
        client.api.account.messages.create(
            to="+91**********",
            from_="//your twilio no. ",
            body="You are outside the boundary limit, Get back.")
        print("You are outside the boundary limit, Get back.")
    return intersect
 
def _odd(x): return x%2 == 1
 
def ispointinside(p, poly):
    ln = len(poly)
    return _odd(sum(rayintersectseg(p, edge)
                    for edge in poly.edges ))
 
 
if __name__ == '__main__':
    polys = [
      Poly(name='strange', edges=(
        Edge(a=Pt(x=28.6784867, y=77.5005334), b=Pt(x=28.6336084, y=77.4538729)),
        Edge(a=Pt(x=28.6336084, y=77.4538729), b=Pt(x=28.6496778, y=77.4451184)),
        Edge(a=Pt(x=28.6496778, y=77.4451184), b=Pt(x=28.6756631, y=77.4379773)),
        Edge(a=Pt(x=28.6756631, y=77.4379773), b=Pt(x=28.6784867, y=77.5005334)),
        Edge(a=Pt(x=28.6784867, y=77.5005334), b=Pt(x=28.6228937, y=77.2783524))
        )),
      
      ]
    testpoints = (Pt(x=28.6758058, y=77.5000373),)
 
    for poly in polys:
        
        print ('   ', '\t'.join("%s: %s" % (p, ispointinside(p, poly))
                               for p in testpoints[:3]))
        print ('   ', '\t'.join("%s: %s" % (p, ispointinside(p, poly))
                               for p in testpoints[3:6]))
        print ('   ', '\t'.join("%s: %s" % (p, ispointinside(p, poly))
                               for p in testpoints[6:]))

