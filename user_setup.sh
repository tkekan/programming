#!/bin/bash

path="/usr/bin"
name=`whoami`
tenant=`whoami`
pass=Juniper1
tmpfile=`mktemp`
host=`hostname`

export OS_TENANT_NAME=admin
export OS_USERNAME=admin
export OS_PASSWORD=nova
export OS_AUTH_URL=http://$host:35357/v2.0

$path/keystone tenant-create --name $tenant --description "$tenant  Tenant" 2>/dev/null
$path/keystone user-create --name $name --pass $pass --email $name@juniper.net 2>/dev/null
if [ $? != 0 ]
then
	echo -e "\nCumulus user \"$name\" and tenant \"$tenant\" already present." 
	echo -e "\nHere is your Cumulus environment variables:\nexport OS_TENANT_NAME=$tenant\nexport OS_USERNAME=$name\nexport OS_PASSWORD=$pass\nexport OS_AUTH_URL=http://$host:5000/v2.0\n"
	exit 1
fi 
$path/keystone user-role-add --tenant $tenant --user $name --role _member_

# Create tenant network for internal IPs
export OS_TENANT_NAME=$name
export OS_USERNAME=$name
export OS_PASSWORD=$pass
export OS_AUTH_URL=http://$host:5000/v2.0

$path/neutron net-create $name-net
$path/neutron subnet-create $name-net --name $name-subnet --gateway 192.168.1.1 192.168.1.0/24
$path/neutron router-create $name-router
$path/neutron router-interface-add $name-router $name-subnet
$path/neutron router-gateway-set $name-router ext-net

# Create security group rules to allow TCP, ICMP and UDP traffic to VMs
$path/nova secgroup-add-rule default tcp 1 65535 0.0.0.0/0
$path/nova secgroup-add-rule default icmp -1 -1 0.0.0.0/0
$path/nova secgroup-add-rule default udp 1 65535 0.0.0.0/0

# Generate and send welcome email to user."

echo -e "\n===Welcome to cumulus pod($host)===\n" >> $tmpfile
echo -e "Here is your cumulus environment variables:" >> $tmpfile
echo -e "=================================================" >> $tmpfile
echo -e "export OS_TENANT_NAME=$name" >> $tmpfile
echo -e "export OS_USERNAME=$name" >> $tmpfile
echo -e "export OS_PASSWORD=$pass" >> $tmpfile
echo -e "export OS_AUTH_URL=http://$host:5000/v2.0" >> $tmpfile
echo -e "=================================================\n" >> $tmpfile

echo -e "Here is your horizon dashboard access info for this cumulus pod:\n" >> $tmpfile
echo -e "=================================================" >> $tmpfile
echo -e "Web URL: http://$host/horizon" >> $tmpfile
echo -e "Username: $name" >> $tmpfile
echo -e "Password: $pass" >> $tmpfile
echo -e "=================================================\n" >> $tmpfile
echo -e "Thanks!" >> $tmpfile
echo -e "cumulus-dev" >> $tmpfile

cat $tmpfile | mailx -s "Welcome $name!!!" $name@juniper.net 2>/dev/null;
rm -f $tmpfile
