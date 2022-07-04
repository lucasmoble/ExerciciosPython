vt=int(input())
vm=int(input())
count=0
x = vt-vm
depois=x-vm

while x>=0:
        x-= vm
        depois-=vm
        count+=1
        print('pagamento ={} \nantes ={} \ndepois ={} \n----- \n'.format(count,depois,x))
        if x >=0 and depois ==0:
                break
    
        
   
