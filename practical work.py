Python 3.10.5 (v3.10.5:f377153967, Jun  6 2022, 12:36:10) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
from faker import Faker
import json
output=open("data.JSON","w")
fake=FAKER()
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    fake=FAKER()
NameError: name 'FAKER' is not defined. Did you mean: 'Faker'?
fake=Faker()
alldata={}
alldata["records"]=[]
for x in range(1000):
    data={"name":fake.name(),"age":fake.random_int
 (min=18, max=80, step=1),
 "street":fake.street_address(),
 "city":fake.city(),"state":fake.state(),
 "zip":fake.zipcode(),
 "lng":float(fake.longitude()),
 "lat":float(fake.latitude())}
    alldata["records"].append(data)

    
json.dump(alldata,output)

