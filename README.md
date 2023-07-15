# Poe-Bot
<a href="https://github.com/smallnew666/Poe-Bot/blob/main/README_en.md">English</a>

Poe-Bot 是一个利用 poe-api 使用 python gradio 框架开发的聊天机器人/Poe-Bot is a chatbot developed using the python gradio framework that leverages the poe-api.
<img width="1352" alt="截屏2023-07-15 12 34 54" src="https://github.com/smallnew666/Poe-Bot/assets/24582880/67d18969-29a4-4ba9-9e26-11e42ee2a2ca">

# 项目描述

这个仓库包含了 Poe-Bot 的代码,它是一个由逆向工程 poe-api 创建的的 poe 聊天机器人。这个机器人使用 Python 和 Gradio 库构建,用于用户界面。

## 主要功能

聊天界面: 机器人通过一个简单直观的聊天界面与用户交流。
多个模型: 用户可以通过单选按钮选择机器人的不同人格。
清除历史记录: 用户可以随时清除聊天记录。

## 安装

克隆仓库:


```
git clone https://github.com/smallnew666/Poe-Bot.git
```



进入项目目录:



```
cd Poe-Bot
```

安装需要的依赖:



```
pip install -r requirements.txt
```

设置 token

在任何桌面 Web 浏览器上登录 poe.com，然后打开浏览器的开发人员工具（也称为“检查”）并在以下菜单中查找 p-b cookie 的值：

Chromium: Devtools > Application > Cookies > poe.com

修改 app.py 中的 token 为你获取的值



```
bot = PoeChatBot('your token')#your poe token
```

安装项目依赖



```
pip install -r requirements.txt
```

运行


```
python app.py
```


应用程序将启动本地服务器。你可以通过浏览器访问 0.0.0.0:8000 访问聊天机器人。


**许可**

这个项目使用 MIT 许可证授权 - 详见 LICENSE 文件。

**联系**

如果你有任何问题,可以联系仓库所有者或提 issue。
