# test_fuseki
Для тестирования фусеки 

На удаленной машине создается ключ доступа с помощью комманды:

```bash
ssh-keygen -t rsa
```
отображение ключа производится с помощью команды:

```
cat ~/.ssh/id_rsa.pub
```

Далее создается виртуальная машина, выбираются необходимые параметры, копируется ключ, вставляется в необходимые настройки.
После создания у машины появляется публичный ключ, его необходимо вставить в код connect_test.py

```python
url = 'http://IP:3030/test/update'
```

Подключение к виртуальной машине осуществляется через ssh:

```
ssh user@IP
```

псле чего необходимо установить Docker согласно [инструкции по установке](https://docs.docker.com/engine/install/ubuntu/)

либо последовательно выполнив следующие операции (не обновлялось с 18.03.2024):

```bash
for pkg in docker.io docker-doc docker-compose docker-compose-v2 podman-docker containerd runc; do sudo apt-get remove $pkg; done
```

```bash
# Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
```

```bash
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

далее устанавливается образ fiseki:

```
sudo docker pull stain/jena-fuseki
```

в рабочей директории папка для хранения данных fuseki на диске

```
sudo mkdir fuseki
```
```
sudo chmod a+rwx fuseki
```
и запускается контейнер fuseki:

```
sudo docker run -p 3030:3030 -e ADMIN_PASSWORD=123 -e TDB=2 -e JVM_ARGS=-Xmx10g -v /home/user/fuseki:/fuseki stain/jena-fuseki
```

далее необходимо войти в fuseki с создать там базу данных с именем test

после чего можно запускать скрипт connection_test.py (объем тестирования определяется кодом)
