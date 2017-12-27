### 使用说明

- 该脚本在ubuntu14.04,python2.7上已经测试完成
- ansible版本为2.3.0.0
- etc目录为hosts,id_rsa私钥存放目录
- ansible.cfg为全局配置文件,运行错误并不成.retry文件
- 该脚本功能是在远程服务器上添加用户,并添加ssh公钥认证

roles/add_user/files目录下存放需要添加用户的公钥,公钥文件名称与需要添加的用户名称一致
默认执行hosts为dev29后续可添加接收用户输入,指定执行的hosts

`脚本执行无报错,会获取要添加的用户名称,以及添加的用户是否需要sudo权限,完成后脚本会到roles/add_user/files文件下寻找与用户一致的公钥文件,没找到脚本将无法继续运行`
