依赖环境
安装Python3环境（百度解决）
     安装两个依赖库
pip install web3==6.11.3 
pip install python-dotenv==1.0.0
具体步骤
1）.env文件

创建文件命名为 .env (注意env前面有个点)
文件内容为(换成自己地址)：
account_address = 0xdD870fA1b7C4700F2BD7f44238821C26f7392148”
account_private_key = ''0x71975fbf7fe448e004ac7ae54cad0a383c3906055a65468714156a07385e96ce”

2）mint.py文件

创建文件命名为 mint.py (和.env在同一个目录)
文件内容为本文档代码。

3）启动/停止
启动：python mint.py
停止：Ctrl + C
