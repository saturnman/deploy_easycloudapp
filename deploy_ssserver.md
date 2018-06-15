# 部署shadowsocks 服务器
在部署好easycloudapp应用之后，在下载中添加一个下载项
**关于如何部署easycloudapp，请参照：**
https://github.com/saturnman/deploy_easycloudapp/blob/master/README.md

![image](https://user-images.githubusercontent.com/1621543/41453005-c00e66ec-70a6-11e8-9e71-2a15c49d9423.png)
大概几分钟之后就下载好了，可以在已安装的App里看到，点击运行
![image](https://user-images.githubusercontent.com/1621543/41453259-a699712e-70a7-11e8-8948-854dee521233.png)
应用默认内部开放的端口号是8388,可以点随机生成一个外部映射端口，之后点击运行
![image](https://user-images.githubusercontent.com/1621543/41453307-db32c278-70a7-11e8-9910-25ee236ac40b.png)
成功运行后在应用列表里就可以看到，点击详情就可以看到**连接密码**
![image](https://user-images.githubusercontent.com/1621543/41453340-f3b3d576-70a7-11e8-9f67-84261487d25e.png)
在shadowsocks客户端输入密码就可以连接了，网络流量都可以走这个代理了，如果是公共Wi-Fi的话使用这个可以提供一层保护，减少信息泄露风险。如果是服务器建设在境外，还可以浏览谷歌,youtube等境外网站科学上网:D
![image](https://user-images.githubusercontent.com/1621543/41453497-8b874428-70a8-11e8-86f1-b6468f263968.png)
**注意设置云服务器提供商的安全组，以阿里云为例**

在阿里云后台服务器列表里点击服务器之后在左边找到安全组选项，我自己一般把比较高的端口都开放了，如果端口被封还可以再启动一个新的App,简单方便
![image](https://user-images.githubusercontent.com/1621543/41453678-3b553ce8-70a9-11e8-858e-2d93ad5226ab.png)
