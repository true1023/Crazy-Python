<p align="center"><img src="./assets/logo.png" alt=""></p>

<h1 align="center">疯狂的Python! 🐍</h1>
<p align="center">一些有趣的鲜为人知的Python特性集合.</p>

<a href="http://www.wtfpl.net/"><img
       src="http://www.wtfpl.net/wp-content/uploads/2012/12/wtfpl-badge-4.png"
       width="80" height="15" alt="WTFPL" /></a>



*本文翻译自[What the f*ck Python!](https://github.com/satwikkansal/wtfpython)*

*本文全文为意译,若有错误,请联系作者*




Python作为一个设计优美的交互式脚本语言，提供了许多人性化的语法。但是也因为这个原因，有些Python的代码片段并不会按照用户想象的那样运行。

这篇文章就让我们总结一下那些Python里反直觉的代码片段，并且深入研究一下其中的运行原理。

下面的某些例子可能并不像是标题说的那样....嗯....疯狂(WTFs)，但是它们仍旧会揭示一些你从来没有意识到的Python的语言特性。

我发现这是一种很好的学习编程语言内部原理的方法，我相信你会对这些东西感兴趣的！

如果你已经写了很久的Python代码，你可以把下面的这些例子当做一个挑战，试一试自己能不能在第一次就做对。也许你会感觉某些例子很熟悉，希望这些例子会勾起你通过自己的努力填上这些坑时的成就感。:sweat_smile:

好了，那么我们开始吧！

<h1>Table of Contents</h1>
<!-- TOC -->

- [示例结构说明](#示例结构说明)
- [使用方法](#使用方法)
- [:eyes: Examples](#eyes-examples)
- [贡献](#贡献)
- [感谢](#感谢)
- [:mortar_board: 版权声明](#mortar_board-版权声明)

<!-- /TOC -->

# 示例结构说明

下面是例子里所使用的结构说明：

> ### ▶ 这是一个标题 *
> 首先是例子的标题，如果某个标题后面带有星号，说明这一段是最新的一个版本加上的。
> ```py
> # 介绍会在这里写一些初始化代码
> # 为下面的神奇时刻做准备...
> ```
>
> **输出 (Python version):**
> ```py
> >>> python语句，执行某个命令
> 一些神奇的输出
> ```
> (可选): 有可能会介绍一下输出的内容
>
>
> #### 💡 解释:
>
> * 简短的介绍发生了什么和为什么会产生这些输出。
>   ```py
>   写一些初始化代码
>   ```
>   **Output:**
>   ```py
>   >>> 触发相应代码 # 这些代码会揭示为何会有上方那些神奇的输出内容
>   ```

**注意：** 所有的例子都是在 Python 3.5.2 环境下测试通过，理论上如果没有特殊声明，可以在所有的Python版本下运行。

# 使用方法

在我看来，为了充分的利用这个仓库里的所有例子，最好的办法就是按照顺序把每个例子挨个看一遍：
- 仔细阅读每个例子的初始化代码。如果你是一个经验丰富的Python程序员，那么大部分时候你都可以知道初始化代码执行后具体会发生什么。
- 阅读输出结果并且，
    + 检查输出结果是否和你想的一样
    + 确认你是否知道产生这种结果背后的原理，
        - 如果不知道，那么请仔细阅读解释章节（如果你看完解释还是不懂的话，别犹豫，提交一个 [issue](https://github.com/true1023/Crazy-Python/issues) 吧）
        - 如果知道，那么给自己点个赞，继续看下一个例子

# :eyes: Examples



# 贡献

欢迎任何补丁和修正！详细信息请看 [CONTRIBUTING.md](./CONTRIBUTING.md)

如果想要参与讨论， 可以选择创建一个新的[issue](https://github.com/true1023/Crazy-Python/issues) 或者加我的 QQ752602742

# 感谢

这个仓库翻译自 [What the fu*k Python](https://github.com/satwikkansal/wtfpython)，迄今为止没谁需要感谢，感谢下原作者[Satwik Kansal](https://github.com/satwikkansal)吧。

# :mortar_board: 版权声明

<a href="http://www.wtfpl.net/"><img
       src="http://www.wtfpl.net/wp-content/uploads/2012/12/wtfpl-badge-4.png"
       width="80" height="15" alt="WTFPL" /></a>

:copyright: [True1023](https://github.com/true1023/)