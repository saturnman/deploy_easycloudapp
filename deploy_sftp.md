# 部署sftp服务器
在部署好easycloudapp应用之后，在下载中添加一个下载项
**关于如何部署easycloudapp，请参照：**
https://github.com/saturnman/deploy_easycloudapp/blob/master/README.md

![image](https://user-images.githubusercontent.com/1621543/41556114-591f8056-736c-11e8-823c-b6a5de253831.png)

下载完成后运行，前映射好端口
![image](https://user-images.githubusercontent.com/1621543/41556142-7453325a-736c-11e8-93d3-576acf5f0216.png)
运行起来后在运行中的App找到，点击管理
![image](https://user-images.githubusercontent.com/1621543/41556169-83409316-736c-11e8-8234-14e5388e85b0.png)
![image]
添加一个用户![image](https://user-images.githubusercontent.com/1621543/41556313-f954b19a-736c-11e8-8569-12fe155c7938.png)
之后可以尝试用客户端连接，个人比较喜欢免费的fileZilla
![image](https://user-images.githubusercontent.com/1621543/41556395-39ee7e16-736d-11e8-9480-b8f13f3c5c9e.png)
连接后直接上传文件尝试，没有问题
![image](https://user-images.githubusercontent.com/1621543/41556441-55c2c99e-736d-11e8-8a76-f3af527ef310.png)
### 注意：如果连接不上请检查宿主机的防火墙设置，如果是阿里云的平台请设置安全组允许端口数据通过。本镜像使用rssh限制了用户的权限，只提供sftp服务，没有登陆交互shell。