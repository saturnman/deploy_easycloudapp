# 自动在基于debian/ubuntu的机器上部署easycloudapp映像的脚本
### [关于背后机制,参考这里](https://zhuanlan.zhihu.com/p/38062002)

直接下载脚本
```bash
wget https://raw.githubusercontent.com/saturnman/deploy_easycloudapp/master/deploy_easycloudapp.sh
```

之后运行 
```bash
sh deploy_easycloudapp.sh
```
将会在机器上运行起来，默认端口是10080，可以自行修改脚本设置端口。
本机运行可以访问
### http://localhost:10080
默认登陆管理员用户名是administrator，密码是easycloudapp123。为了安全请在登陆后马上修改密码。
![image](https://user-images.githubusercontent.com/1621543/41822391-5792428c-7821-11e8-86e5-418beed0437c.png)
![image](https://user-images.githubusercontent.com/1621543/41822393-71e1b118-7821-11e8-8746-17ae1ee0e6ba.png)

# 相关教程
###  [1. 部署shadowsocks服务](https://github.com/saturnman/deploy_easycloudapp/blob/master/deploy_ssserver.md)
### [2. 部署sftp服务](https://github.com/saturnman/deploy_easycloudapp/blob/master/deploy_sftp.md)
### [3. 部署jupyter notebook服务器](https://github.com/saturnman/deploy_easycloudapp/blob/master/deploy_anaconda3_notebook.md)
### [4. 部署cloud9 webIDE开发环境](https://github.com/saturnman/deploy_easycloudapp/blob/master/deploy_cloud9.md)
### [5. 使用共享目录](https://github.com/saturnman/deploy_easycloudapp/blob/master/shared_folder.md)
