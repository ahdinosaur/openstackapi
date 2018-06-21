# ovh

---

create [OVH Public Cloud account[(https://ovh.com)

---

generate SSH key for OVH

```shell
ssh-keygen -t rsa -b 8192 -f ~/.ssh/ovh
```

upload to OVH

```shell
cat ~/.ssh/ovh.pub
```

---

enable private networks

create vRack and private network

---

```
sudo apt install -y python-novaclient
```

get OpenStack credentials from provider

```shell
tee ~/rc.sh << EOF
export OS_AUTH_URL=https://auth.cloud.ovh.net/v2.0/
export OS_TENANT_ID=cca6608c1346428d9c0ea5748bf91272
export OS_TENANT_NAME="3526803835773644"
export OS_USERNAME="qrGGDwAZZKhC"
echo "Please enter your OpenStack Password: "
read -sr OS_PASSWORD_INPUT
export OS_PASSWORD=\$OS_PASSWORD_INPUT
export OS_REGION_NAME="WAW1"
EOF
```

source with `source ~/rc.sh`

> to find available flavors
> 
> ```shell
> nova flavor-list
> ```

> to find available images
> 
> ```shell
> nova image-list
> ```

> to find available networks
> 
> ```shell
> nova tenant-network-list
> ```
