# openstackapi

use the [`openstacksdk`](https://docs.openstack.org/openstacksdk/latest/) as a microservice over HTTP.

useful when you want to use [`openstacksdk`](https://docs.openstack.org/openstacksdk/latest/) from a language that isn't Python.

__work in progress, has working proof of concept__

sponsored by [PeachCloud](http://peachcloud.org) :peach: :cloud:

## setup

```shell
pip install --user pipenv
# add ~/.local/bin to PATH
pipenv shell
```

---

create [OVH Public Cloud account[(https://ovh.com)

---

generate SSH key for OVH

```shell
ssh-keygen -t rsa -b 8192 -f ~/.ssh/ovh
```

---

create OpenStack user

download OpenStack rc file with environment variables

```shell
source config.sh
```

---

```
sudo apt install -y python-novaclient
```

get OpenStack credentials from provider

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

---

enable private networks

create vRack and private network

---

add ssh keypair

```shell
nova keypair-add --pub-key ~/.ssh/ovh.pub $(hostname)
```

---

run api server

```shell
python api.py
```

---

create cloud server with Docker auto-installed

```shell
bash example.sh
```
