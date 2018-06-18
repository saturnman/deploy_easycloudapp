# 部署python jupyter笔记本服务器
在部署好easycloudapp应用之后，在下载中添加一个下载项
**关于如何部署easycloudapp，请参照：**
https://github.com/saturnman/deploy_easycloudapp/blob/master/README.md

![image](https://user-images.githubusercontent.com/1621543/41562127-4e7b6e64-737e-11e8-80ba-58736d990fcf.png)
此应用是基于anaconda的python3工具包的，里面内置了丰富的工具包比直接使用python方便得多，注意这个镜像非常大，要下载大概几分钟到十几分钟不等，和网络带宽有关
![image](https://user-images.githubusercontent.com/1621543/41562206-8862ccda-737e-11e8-9857-7cbb4ccd0b45.png)
下载完成后在已安装的应用中可以看到它，点击运行，配置端口号。外部访问端口可以自己设置
![image](https://user-images.githubusercontent.com/1621543/41562290-bfbde35e-737e-11e8-9eef-47e1fd5b0c9d.png)
运行后可以在运行中的App中看到它，点击状态参数会弹出来连接服务器要使用的token令牌，直接复制token=xxx后面的xxx就可以
![image](https://user-images.githubusercontent.com/1621543/41562486-5ec09fdc-737f-11e8-8d74-a71d102a6cff.png)
访问服务器提示输入令牌，把刚才保存的令牌复制进去就可以
![image](https://user-images.githubusercontent.com/1621543/41562592-abfd83f0-737f-11e8-8bc8-753114c0c2ac.png)
![image](https://user-images.githubusercontent.com/1621543/41562744-1e7412aa-7380-11e8-85b8-afb9d080565b.png)
### 注意:应用在退出关闭后数据都会清空，所以在线应用不适合保存重要数据，对于重要笔记应该在线使用后保存到本地