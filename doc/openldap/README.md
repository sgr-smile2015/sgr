=====
ubuntu14.04配置openldap中memberOf选项
个人可是从属多个ou(组织)
使用root用户执行一下命令:
cd /etc/ldap/sldap.d/
ldapadd -Y EXTERNAL -H ldapi:/// -f memberof_config.ldif
ldapadd -Y EXTERNAL -H ldapi:/// -f member.ldif
/etc/init.d/sldap restart
