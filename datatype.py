#int
a=2
print(a,type(a))

#float
a=2.3
print(a,type(a))

#complex
a=1+2j
print(a,type(a))


#string
s="hello@123"
print(s,type(s))

s='hello@123'
print(s,type(s))

s='''hello@123'''
print(s,type(s))

s='100'
print(s,type(s))

#list
l=[10,22,2.5,1+2j,'ravi']
print(l,type(l))

l=[10,22,2.5,1+2j,'ravi']
l[3]=33
print(l,type(l))

#tuple
t=(2,4.3,1+2j,'hello')
print(t,type(t))

#dictionary
d={
    'course_name':'python',
    'cource_duration':'2 month'
}
print(d)
print(d['course_name'])
print(d,type(d))

d={
    'myname':'ravi',
    'mycontactno':6299662337
}
print(d)
print(d['mycontactno'])
print(d,type(d))

#set
s={1,2,3}
print(s,type(s))

s={10,20,10}
print(s)
print(s,type(s))