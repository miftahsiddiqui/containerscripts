import os

proj_dir = "/root/container"
ns_list = proj_dir + "/ns_list.txt"

print("Project directory path: %s" %(proj_dir))

print("namespaces to scan are: ")
with open(ns_list,"rt") as f:
    print(f.read())

with open(ns_list,"rt") as file:
    for ns in file:
        ns = ns.strip("\n")
        #print("Testing NS: %s" %(ns))
        cmd = r"kubectl get pods -n " + ns 
        #cmd1 = ' | awk {print $1} '
        cmd = cmd #+ cmd1
        print("root@tejas1: %s" %(cmd))
        os.system(cmd)
print("DONE FULL TESTING")
