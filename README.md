# NMRIHPing
（Steam免费游戏地狱已满）向服务器发送UDP数据包获取服务器信息及玩家  
1、发送UDP协议数据包到（服务器、端口） 具体原理可往下看👇  
![buhuo](https://user-images.githubusercontent.com/42183711/202880158-470ecf05-8a76-41f9-a1cd-2b5f3acc7859.PNG)
# 发送原理
# 1、获取服务器信息
1、向服务器发送UDP数据包包含数据ffffffff54536f7572636520456e67696e6520517565727900  
2、服务器回应数据包例如ffffffff41b0ca0b76取ffffffff41后面的b0ca0b76拼接到ffffffff54536f7572636520456e67696e6520517565727900的后面  
变为ffffffff54536f7572636520456e67696e6520517565727900b0ca0b76发送服务器  
3、服务器回应服务器信息（目前可知服务器名称、地图名、服务器版本...）  
# 2、获取玩家信息
1、向服务器发送UDP数据包包含数据ffffffff5500000000  
2、服务器回应数据包例如ffffffff412ac8eed1取ffffffff41后面的2ac8eed1拼接到ffffffff55的后面  
变为ffffffff552ac8eed1发送服务器  
3、服务器回应服务器玩家字串  
  
  PS:目前技术有限不会把他们区分出来，看你们实力吧。  
  目前已知某些服务器可能会出现获取失败（例如X社区）隔一会再获取重复几次总会成功的。
