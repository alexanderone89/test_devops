Данное тестовое задание выполнилось в составе следующих составных частей:
<li>имитатор процесса для мониторинга на ЯП python - test.py</li>
<li>сам скрипт bash - monitor.sh </li>
<li>юнит для systemd - unit_for_monitor.service</li>
<li>локальный сервер для имитации "https://test.com/monitoring/test/api" на fastapi - main.py</li>

Работа monitor.sh и unit_for_monitor.service тестировалась на Ubuntu 24.04.1 



Для развертывания test.py и main.py необходим python версии 3.10 и Docker.

sudo docker build --no-cache -t fastapi1 .
<br>
sudo docker run -p 8000:80 fastapi1
