# 使用共享文件夹功能
在部署好easycloudapp应用之后，在下载中添加一个下载项
**关于如何部署easycloudapp，请参照：**
https://github.com/saturnman/deploy_easycloudapp/blob/master/README.md

在共享目录管理中创建一个新的共享文件夹，之后在启动的任何应用中都可以使用共享目录来保存文件.
![image](https://user-images.githubusercontent.com/1621543/41815994-50c18e06-77ac-11e8-90e3-d6419cebacd5.png)
这里以启动两个cloud9的在线编辑器为例展示如何使用共享目录
![image](https://user-images.githubusercontent.com/1621543/41815995-511f96e0-77ac-11e8-9c68-60da01150b4a.png)
启动第一个cloud9的应用，把之前创建的共享目录映射到/workspace
![image](https://user-images.githubusercontent.com/1621543/41815996-517a4b58-77ac-11e8-8cd8-31be4883b84c.png)
再启动第二个cloud9应用，同样把之前创建的共享目录映射到/workspace
![image](https://user-images.githubusercontent.com/1621543/41815997-51d46066-77ac-11e8-8a48-6693147e3881.png)
这时在任何一个应用中创建和写入文件都会直接在另一个应用中显示。这非常方便远程合作编辑或是共享。目录映射时可以设置为只读，如果只是了为让对方以只读方式使用文件。
