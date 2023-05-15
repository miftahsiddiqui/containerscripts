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
        print("*** Testing NS: %s" %(ns))

        with open(ns + '_pods.txt', "rt") as pod:
            for p in pod:
                p = p.strip("\n")
                cmd = 'kubectl get pod' + r"/" + p + ' -n ' + ns + " -o json | jq '.spec.containers[].securityContext'"
                print("root@tejas1: %s" %(cmd))
                os.system(cmd)
                print("\n")
                #print("AT POD LEVEL:\n")
                #print("root@tejas1: %s" %(cmd1))
                cmd1 = 'kubectl get pod' + r"/" + p + ' -n ' + ns + " -o json | jq '.spec.securityContext'"
                print("root@tejas1: %s" %(cmd1))
                os.system(cmd1)
                print("\n")

print("DONE FULL TESTING")
