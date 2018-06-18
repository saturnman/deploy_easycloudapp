# 自动在基于debian的机器上部署easycloudapp映像的脚本
[关于背后机制，参考这里](https://zhuanlan.zhihu.com/p/38062002)

直接下载脚本
```bash
wget https://raw.githubusercontent.com/saturnman/deploy_easycloudapp/master/deploy_easycloudapp.sh
```

之后运行 
```bash
sh deploy_easycloudapp.sh
```
将会在机器上运行起来，默认端口是10080，可以自行修改脚本设置端口。
本机运行可以访问
### http://localhost:10080
默认登陆管理员用户名是administrator，密码是easycloudapp123。为了安全请在登陆后马上修改密码。

# 相关教程
###  [1. 部署shadowsocks服务](https://github.com/saturnman/deploy_easycloudapp/blob/master/deploy_ssserver.md)
### [2. 部署sftp服务](https://github.com/saturnman/deploy_easycloudapp/blob/master/deploy_sftp.md)
### [3. 部署jupyter notebook服务器](https://github.com/saturnman/deploy_easycloudapp/blob/master/deploy_anaconda3_notebook.md)
