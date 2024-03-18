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

