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

                with open(ns + '_' + p + '_containers.txt', "rt") as cont:
                    for c in cont:
                        c = c.strip("\n")
                        #cmd = 'kubectl logs pod/' + p + ' -n ' + ns + ' -c ' + c + r" | egrep --color=always -i 'username=|username =|user=|user =|id=|id ='"
                        #cmd = 'kubectl logs pod/' + p + ' -n ' + ns + ' -c ' + c + r" | egrep --color=always -i 'bearer'"
                        #cmd = 'kubectl logs pod/' + p + ' -n ' + ns + ' -c ' + c + r" | egrep --color=always -i 'password|passwd|pwd'"
                        #cmd = 'kubectl logs pod/' + p + ' -n ' + ns + ' -c ' + c + r" | egrep --color=always -i 'token=|tokens=|token =|tokens ='"
                        #cmd = 'kubectl logs pod/' + p + ' -n ' + ns + ' -c ' + c + r" | egrep --color=always -i 'key=|key =|key:|key :'"
                        #cmd = 'kubectl logs pod/' + p + ' -n ' + ns + ' -c ' + c + r" | egrep --color=always -i 'secret'"
                        #cmd = 'kubectl describe pod/' + p + ' -n ' + ns + r" | grep --color=always -i 'image:'"
                        cmd = 'kubectl describe pod/' + p + ' -n ' + ns + r" | grep --color=always -i 'psp:'"
                        print("root@tejas1: %s" %(cmd))
                        os.system(cmd)
                        print("\n")

print("DONE FULL TESTING")
