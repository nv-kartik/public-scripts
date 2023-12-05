import argparse
import os

parser = argparse.ArgumentParser(prog="NowPrivacy UAT Setup Tool", description="Commandline tool that sets up a set of VMs for NowPrivacy UAT")

parser.add_argument(
    "--groupNumber",
    help="Group number of your set"
)

parser.add_argument(
    "--windowsVersion",
    help="Windows version of your set",
    choices=["2016", "2019"],
)

parser.add_argument(
    "--subnetRange",
    help="Range of the subnet for your VMs",
    default="172.99.99.0/24"
)

args = parser.parse_args()

if args.windowsVersion == '2016':
    vm_image_name = "win2016datacenter"
elif args.windowsVersion == '2019':
    vm_image_name = "MicrosoftWindowsServer:WindowsServer:2019-datacenter:latest"


subnet_name = "Windows" + args.windowsVersion + "-Group" + args.groupNumber 
subnet_range = args.subnetRange
dns_server = "10.0.1.4"

fc_vm_name = "Windows" + args.windowsVersion + "-Group" + args.groupNumber + "-FC"
mp_vm_name = "Windows" + args.windowsVersion + "-Group" + args.groupNumber + "-MP"
s1_vm_name = "Windows" + args.windowsVersion + "-Group" + args.groupNumber + "-S1"
s2_vm_name = "Windows" + args.windowsVersion + "-Group" + args.groupNumber + "-S2"

fc_comp_name = "W" + args.windowsVersion + "-G" + args.groupNumber + "-FC"
mp_comp_name = "W" + args.windowsVersion + "-G" + args.groupNumber + "-MP"
s1_comp_name = "W" + args.windowsVersion + "-G" + args.groupNumber + "-S1"
s2_comp_name = "W" + args.windowsVersion + "-G" + args.groupNumber + "-S2"

fc_nic_name = fc_vm_name + "VMNic"
mp_nic_name = mp_vm_name + "VMNic"
s1_nic_name = s1_vm_name + "VMNic"
s2_nic_name = s2_vm_name + "VMNic"

# print(fc_nic_name)
# print(mp_nic_name)
# print(s1_nic_name)
# print(s2_nic_name)


print("----------------------------------------------------------------------------------")
print("\t\t VMs with the below details will be created")
print("----------------------------------------------------------------------------------")


print(f"Subnet to be created                   = {subnet_name}")
print(f"Subnet's Address range                 = {subnet_range}")
print("----------------------------------------------------------------------------------")

print(f"FileCluster VM Name / Computer Name    = {fc_vm_name} / {fc_comp_name}") 
print(f"MediaProcessor VM Name / Computer Name = {mp_vm_name} / {mp_comp_name}") 
print(f"Solr1 VM Name / Computer Name          = {s1_vm_name} / {s1_comp_name}") 
print(f"Solr2 VM Name / Computer Name          = {s2_vm_name} / {s2_comp_name}") 

print("----------------------------------------------------------------------------------")

print(f"DNS to be set                          = {dns_server}")

print("----------------------------------------------------------------------------------")
# print(f"VM Image name = {vm_image_name}")
print("Confirm specifications (Yes/No)")

c = input()
if c == "Yes":
    print("----------------------------------------------------------------------------------")
    print("Process initiated..")
    step = os.system('cmd /c "az login"')

    if step == 0:
        print("Login successful !")
        print("Creating Subnet..")
        step1 = os.system(f'cmd /c "az network vnet subnet create --name {subnet_name} --resource-group NOWPrivacy-UAT --vnet-name NOWPrivacy-UAT-vnet --address-prefixes {subnet_range}"')
        # print(f'cmd /c "az network vnet subnet create --name {subnet_name} --resource-group NOWPrivacy-UAT --vnet-name NOWPrivacy-UAT-vnet --address-prefixes {subnet_range}"')
        # step1 = 0
        
        if step1 == 0:
            print("----------------------------------------------------------------------------------")
            print("Subnet created successfully !")
#####################################################################################################################################
            print("Creating FileCluster node..")
            step2 = os.system(f'cmd /c "az vm create --resource-group NOWPrivacy-UAT --name {fc_vm_name} --image {vm_image_name} --size Standard_B4ms --vnet-name NOWPrivacy-UAT-vnet --subnet {subnet_name} --computer-name {fc_comp_name} --public-ip-sku Standard --nic-delete-option Delete --os-disk-delete-option Delete --data-disk-delete-option Delete --admin-username admin-privacy --admin-password Welcome1234!!"')
            # print(f'cmd /c "az vm create --resource-group NOWPrivacy-UAT --name {fc_vm_name} --image {vm_image_name} --size Standard_B4ms --vnet-name NOWPrivacy-UAT-vnet --subnet {subnet_name} --computer-name {fc_comp_name} --public-ip-sku Standard --nic-delete-option Delete --os-disk-delete-option Delete --data-disk-delete-option Delete --admin-username admin-privacy --admin-password Welcome1234!!"')
            # step2 = 0

            if step2 == 0:
                print("----------------------------------------------------------------------------------")
                print("FC node created successfully!")
                print("Changing FC node's DNS server..")
                step3 = os.system(f'cmd /c "az network nic update --name {fc_nic_name} --resource-group NOWPrivacy-UAT --dns-servers {dns_server}"')
                # print(f'cmd /c "az network nic update --name {fc_nic_name} --resource-group NOWPrivacy-UAT --dns-servers {dns_server}"')
                # step3 = 0

                if step3 == 0:
                    print("----------------------------------------------------------------------------------")
                    print("FC node's DNS changed successfully !")
#####################################################################################################################################
                    print("Creating MediaProcessor node..")
                    step4 = os.system(f'cmd /c "az vm create --resource-group NOWPrivacy-UAT --name {mp_vm_name} --image {vm_image_name} --size Standard_B2ms --vnet-name NOWPrivacy-UAT-vnet --subnet {subnet_name} --computer-name {mp_comp_name} --public-ip-sku Standard --nic-delete-option Delete --os-disk-delete-option Delete --data-disk-delete-option Delete --admin-username admin-privacy --admin-password Welcome1234!!"')
                    # print(f'cmd /c "az vm create --resource-group NOWPrivacy-UAT --name {mp_vm_name} --image {vm_image_name} --size Standard_B4ms --vnet-name NOWPrivacy-UAT-vnet --subnet {subnet_name} --computer-name {mp_comp_name} --public-ip-sku Standard --nic-delete-option Delete --os-disk-delete-option Delete --data-disk-delete-option Delete --admin-username admin-privacy --admin-password Welcome1234!!"')
                    # step4 = 0

                    if step4 == 0:
                        print("----------------------------------------------------------------------------------")
                        print("MP node created successfully!")
                        print("Changing MP node's DNS server..")
                        step5 = os.system(f'cmd /c "az network nic update --name {mp_nic_name} --resource-group NOWPrivacy-UAT --dns-servers {dns_server}"')
                        # print(f'cmd /c "az network nic update --name {mp_nic_name} --resource-group NOWPrivacy-UAT --dns-servers {dns_server}"')
                        # step5 = 0

                        if step5 == 0:
                            print("----------------------------------------------------------------------------------")
                            print("MP node's DNS changed successfully !")
#####################################################################################################################################
                            print("Creating 1st Solr node..")
                            step6 = os.system(f'cmd /c "az vm create --resource-group NOWPrivacy-UAT --name {s1_vm_name} --image {vm_image_name} --size Standard_B2s --vnet-name NOWPrivacy-UAT-vnet --subnet {subnet_name} --computer-name {s1_comp_name} --public-ip-sku Standard --nic-delete-option Delete --os-disk-delete-option Delete --data-disk-delete-option Delete --admin-username admin-privacy --admin-password Welcome1234!!"')
                            # print(f'cmd /c "az vm create --resource-group NOWPrivacy-UAT --name {s1_vm_name} --image {vm_image_name} --size Standard_B4ms --vnet-name NOWPrivacy-UAT-vnet --subnet {subnet_name} --computer-name {s1_comp_name} --public-ip-sku Standard --nic-delete-option Delete --os-disk-delete-option Delete --data-disk-delete-option Delete --admin-username admin-privacy --admin-password Welcome1234!!"')
                            # step6 = 0
                            
                            if step6 == 0:
                                print("----------------------------------------------------------------------------------")
                                print("S1 node created successfully!")
                                print("Changing S1 node's DNS server..")
                                step7 = os.system(f'cmd /c "az network nic update --name {s1_nic_name} --resource-group NOWPrivacy-UAT --dns-servers {dns_server}"')
                                # print(f'cmd /c "az network nic update --name {s1_nic_name} --resource-group NOWPrivacy-UAT --dns-servers {dns_server}"')
                                # step7 = 0

                                if step7 == 0:
                                    print("----------------------------------------------------------------------------------")
                                    print("S1 node's DNS changed successfully !")
#####################################################################################################################################
                                    print("Creating 2nd Solr node..")
                                    step8 = os.system(f'cmd /c "az vm create --resource-group NOWPrivacy-UAT --name {s2_vm_name} --image {vm_image_name} --size Standard_B2s --vnet-name NOWPrivacy-UAT-vnet --subnet {subnet_name} --computer-name {s2_comp_name} --public-ip-sku Standard --nic-delete-option Delete --os-disk-delete-option Delete --data-disk-delete-option Delete --admin-username admin-privacy --admin-password Welcome1234!!"')
                                    # print(f'cmd /c "az vm create --resource-group NOWPrivacy-UAT --name {s2_vm_name} --image {vm_image_name} --size Standard_B4ms --vnet-name NOWPrivacy-UAT-vnet --subnet {subnet_name} --computer-name {s2_comp_name} --public-ip-sku Standard --nic-delete-option Delete --os-disk-delete-option Delete --data-disk-delete-option Delete --admin-username admin-privacy --admin-password Welcome1234!!"')
                                    # step8 = 0

                                    if step8 == 0:
                                        print("----------------------------------------------------------------------------------")
                                        print("S2 node created successfully!")
                                        print("Changing S2 node's DNS server..")
                                        step9 = os.system(f'cmd /c "az network nic update --name {s2_nic_name} --resource-group NOWPrivacy-UAT --dns-servers {dns_server}"')
                                        # print(f'cmd /c "az network nic update --name {s2_nic_name} --resource-group NOWPrivacy-UAT --dns-servers {dns_server}"')
                                        # step9 = 0

                                        if step9 == 0:
                                            print("----------------------------------------------------------------------------------")
                                            print("S2 node's DNS changed successfully !")
#####################################################################################################################################
                                            print("----------------------------DONE---------------------------------------------------")
