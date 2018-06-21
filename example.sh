#!/bin/bash

setup_server_userdata=$(cat <<'EOF'
#!/bin/bash

apt update
apt install -y apt-transport-https ca-certificates curl gnupg2 software-properties-common

curl -fsSL https://download.docker.com/linux/$(. /etc/os-release; echo "$ID")/gpg | sudo apt-key add -
# TODO verify fingerprint is equal to 9DC8 5822 9FC7 DD38 854A E2D8 8D81 803C 0EBF CD88
apt-key fingerprint 0EBFCD88
add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/$(. /etc/os-release; echo "$ID") $(lsb_release -cs) stable"

apt-get update
apt-get install docker-ce -y

usermod -aG docker debian
service docker restart
EOF
)

setup_server_userdata_str=$(echo "${setup_server_userdata}" | sed 's/\"/\\"/g' | awk 1 ORS='\\n')

echo "${setup_server_userdata_str}"

create_server_data=$(cat <<EOF
{
  "name": "test1",
  "image": "Debian 9",
  "flavor": "s1-2",
  "network": [
    "ae4fffbd-2cc5-4a34-965b-6b3920276ab3",
    "d807404c-817c-4b34-8910-ca3a4537d476"
  ],
  "key_name": "purple-paradise",
  "wait": true,
  "userdata": "${setup_server_userdata_str}"
}
EOF
)


curl -i \
  -H "Content-Type: application/json" \
  -X POST -d "${create_server_data}" \
  http://localhost:5000/servers
