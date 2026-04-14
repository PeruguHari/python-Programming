def ip_address(ip):
    parts=ip.split(".")
    if len(parts)!=4:
        return False
    for i in parts:
        if not i.isdigit():
            return False
        n=int(i)
        if n<0 or n>225:
            return False
        if len(i)>1 and i[0]==0:
            return False
    return True
ip=input("Enter the ip address= ")
print("Valid Ip address"if ip_address(ip)else"Invalid Ip addess")