
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
                        #cmd = 'kubectl exec ' + p + ' -n ' + ns + ' -c ' + c + r" -- nginx -v" 
                        #cmd = 'kubectl exec ' + p + ' -n ' + ns + ' -c ' + c + r" -- java -version"
                        #cmd = 'kubectl exec ' + p + ' -n ' + ns + ' -c ' + c + r" -- python3 -V"
                        #cmd = 'kubectl exec ' + p + ' -n ' + ns + ' -c ' + c + r" -- node -v"
                        #cmd = 'kubectl exec ' + p + ' -n ' + ns + ' -c ' + c + r" -- postgres -V"
                        #cmd = 'kubectl exec ' + p + ' -n ' + ns + ' -c ' + c + r" -- apache2 -v" #httpd -v"
                        #cmd = 'kubectl exec ' + p + ' -n ' + ns + ' -c ' + c + r" -- redis-server -v"
                        cmd = 'kubectl exec ' + p + ' -n ' + ns + ' -c ' + c + r" -- cat /etc/os-release"
                        print("root@tejas1: %s" %(cmd))
                        os.system(cmd)
                        print("\n")

print("DONE FULL TESTING")
