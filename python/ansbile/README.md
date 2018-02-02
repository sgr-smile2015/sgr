++++++ubuntu14.04安装ansible 2.2.1++++++
1.安装虚拟环境
sudo apt-get install python-pip
sudo pip install virtualenv

2.生成requirements.txt
pip freeze > requirements.txt

3.根据requirements.txt安装ansible
pip install -r requirements.txt

4.virtualenv使用
virtualenv env 创建虚拟环境env
退出虚拟环境  deactivate

5.重新激活
source ./bin/activate

18/1/21
通过apt下载最新ansible发布版本
sudo apt-get install software-properties-common
sudo apt-add-repository ppa:ansible/ansible
sudo apt-get update
sudo apt-get install ansible

++++++++++++++
