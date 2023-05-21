import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)

timestamp = int(time.strftime('%H'))
print(timestamp)

if  (timestamp < 12) :
    print("good morning sir")

elif (timestamp > 12 & timestamp <18):
    print('good afternoon')

elif (timestamp > 18 & timestamp <20):
    print('good evening')

else:
    print('good night')
  
    

