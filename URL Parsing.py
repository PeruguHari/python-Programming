def website(url):
    protocol,rest=url.split("://")
    parts=rest.split("/",1)
    domain=parts[0]
    if len(parts)>1:
        path="/"+parts[1]
    else:
        path="/"
    print("Protocol: ",protocol)
    print("Domain: ",domain)
    print("Path: ",path)
    return protocol,domain,path
url=input("Enter the url= ")
print(website(url))