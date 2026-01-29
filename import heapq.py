import heapq
def A(a,b,t):
 h=lambda s:min(abs(s[0]-t),abs(s[1]-t))
 pq=[(h((0,0)),0,(0,0),[])];v=set()
 while pq:
  _,g,(x,y),p=heapq.heappop(pq)
  if (x,y) in v:continue
  v.add((x,y));p+=[(x,y)]
  if t in (x,y):return p
  for n in {(a,y),(x,b),(0,y),(x,0),
            (x-min(x,b-y),y+min(x,b-y)),
            (x+min(y,a-x),y-min(y,a-x))}:
   heapq.heappush(pq,(g+1+h(n),g+1,n,p))
