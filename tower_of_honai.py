i=1
def t_o_h(n,a,c,b):     #here a=initial rod , c=target rod , b=temporary rod
    global i
    if n==0:
        return "empty disk"
    else:
    
        t_o_h(n-1,a,b,c)
       
        print(f'step {i} : move disk {n} from {a} to {c}')
        i=i+1
        t_o_h(n-1,b,c,a)

    
    return f"total steps required to complete are {i-1}"


number=int(input('enter the number of disks: '))
total_steps=t_o_h(number,'A','C','B')    
print(total_steps)




