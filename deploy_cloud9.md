#部署基于cloud9的webIDE开发环境
cloud9是基于浏览器接口的IDE开发环境，实际上并没有太多神秘的地方，和普通的IDE和编辑器一样是一个用来编辑源文件和执行浏览调试等功能的程序，不过它的交互接口做成了web界面，让用户方便的在浏览器中使用，这样非常适合一般远程开发和调试，也非常利于远程结对开发。

在部署好easycloudapp应用之后，在下载中添加一个下载项
**关于如何部署easycloudapp，请参照：**
https://github.com/saturnman/deploy_easycloudapp/blob/master/README.md

![image](https://user-images.githubusercontent.com/1621543/41632737-ebc40416-746d-11e8-9df4-235def84c62f.png)

下载完成后在已安装的程序中找到它并点击运行
![image](https://user-images.githubusercontent.com/1621543/41632740-f07fb626-746d-11e8-8317-41398c8cc2b3.png)
此App默认开放的端口是443,可以自行映射到一个端口。环境变量控制了访问服务器的账号和密码，
**格式是<用户名>:<密码>**
如果不填写默认的用户名和密码是administrator:mywebide，**请一定要设置账号和密码，否则会非常不安全，这个变量会保存在App的状态参数中，如果忘记密码可以在运行中的App中查看**，
运行起来就可以在浏览器中访问App了
![image](https://user-images.githubusercontent.com/1621543/41632741-f329ea90-746d-11e8-845e-3947b26478b2.png)
**注意:访问时一定要写全地址，比如https://<IP地址或域名>:<端口>，前面的https://**，一定要写全，否则会出错。访问时浏览器还会弹出类似警告
![image](https://user-images.githubusercontent.com/1621543/41632880-a4f41a02-746e-11e8-91ed-f2a77e7aaf7a.png)
**直接点击继续浏览即可**,出现这个是因为每次启动App时会自动生成一张自签名的SSL证书，证书不会被浏览器信任但是可以保护与服务器通讯的安全性，只是未签名的证书失去了验证服务器身份的作用。
本App镜像的制作引用了这个作者制作的镜像，我仅仅添加生成证书的功能和一些适配脚本
**https://github.com/xczh/c9**
