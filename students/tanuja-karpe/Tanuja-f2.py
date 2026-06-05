#problem1 
s={'a','b','c','d'}
s.update({'e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','y','z'})
print(s)
count=0
count=26
v={'a','e','i','o','u'}
for x in v:
         if x in s:
           count=count-1 
print(count)       

#problem2
s={'a','b','c','d'}
s.update({'e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','y','z'})
print(s)
count=0
v={'a','e','i','o','u'}
for x in v:
         if x in s:
           count=count+1 
print(count)       

