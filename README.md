<p align="center"><img src="./assets/logo.png" alt=""></p>

<h1 align="center">疯狂的Python! 🐍</h1>
<p align="center">一些有趣的鲜为人知的Python特性集合.</p>

<a href="http://www.wtfpl.net/"><img
       src="http://www.wtfpl.net/wp-content/uploads/2012/12/wtfpl-badge-4.png"
       width="80" height="15" alt="WTFPL" /></a>

[![Join the chat at https://gitter.im/Crazy-Python/Lobby](https://badges.gitter.im/Crazy-Python/Lobby.svg)](https://gitter.im/Crazy-Python/Lobby?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

*本文翻译自[What the f*ck Python!](https://github.com/satwikkansal/wtfpython)*

*本文全文为意译,若有错误,请联系作者*




Python作为一个设计优美的交互式脚本语言，提供了许多人性化的语法。但是也因为这个原因，有些Python的代码片段并不会按照用户想象的那样运行。

这篇文章就让我们总结一下那些Python里反直觉的代码片段，并且深入研究一下其中的运行原理。

下面的某些例子可能并不像是标题说的那样....嗯....疯狂(WTFs)，但是它们仍旧会揭示一些你从来没有意识到的Python的语言特性。

我发现这是一种很好的学习编程语言内部原理的方法，我相信你会对这些东西感兴趣的！

如果你已经写了很久的Python代码，你可以把下面的这些例子当做一个挑战，试一试自己能不能在第一次就做对。也许你会感觉某些例子很熟悉，希望这些例子会勾起你通过自己的努力填上这些坑时的成就感。:sweat_smile:

好了，那么我们开始吧！

<h1>Table of Contents</h1>
<!-- TOC depthFrom:1 depthTo:3 -->

- [示例结构说明](#示例结构说明)
- [使用方法](#使用方法)
- [:eyes: 例子](#eyes-例子)
    - [第一章: 撕裂大脑](#第一章-撕裂大脑)
        - [▶ 善变的字符串 *](#▶-善变的字符串-)
        - [▶ 不变的哈希值](#▶-不变的哈希值)
        - [▶ 说了要执行就一定会执行！](#▶-说了要执行就一定会执行)
        - [▶ 鸠占鹊巢 *](#▶-鸠占鹊巢-)
        - [▶ 神奇赋值法](#▶-神奇赋值法)
        - [▶ 时间的误会](#▶-时间的误会)
        - [▶ 特殊的数字们](#▶-特殊的数字们)
        - [▶ 三子棋之一步取胜法](#▶-三子棋之一步取胜法)
        - [▶ 没脑子的函数](#▶-没脑子的函数)
        - [▶ `is not ...` 并不是  `is (not ...)`](#▶-is-not--并不是--is-not-)
        - [▶ 尾部的逗号](#▶-尾部的逗号)
        - [▶ 最后一个反斜杠](#▶-最后一个反斜杠)
        - [▶ 纠结的not](#▶-纠结的not)
        - [▶ 只剩一半的三引号](#▶-只剩一半的三引号)
        - [▶ 消失的午夜零点](#▶-消失的午夜零点)
        - [▶ 站错队的布尔型](#▶-站错队的布尔型)
        - [▶ 类属性与类实例属性](#▶-类属性与类实例属性)
        - [▶ None的产生](#▶-none的产生)
        - [▶ 不可修改的元组](#▶-不可修改的元组)
        - [▶ 消失的变量e](#▶-消失的变量e)
        - [▶ 亦真还假](#▶-亦真还假)
        - [▶ 转瞬即空](#▶-转瞬即空)
        - [▶ 子类的关系 *](#▶-子类的关系-)
        - [▶ 神秘的键值转换 *](#▶-神秘的键值转换-)
        - [▶ 看你能不能猜到这个的结果？](#▶-看你能不能猜到这个的结果)
    - [第二章: 瞒天过海](#第二章-瞒天过海)
        - [▶ Skipping lines?](#▶-skipping-lines)
    - [第三章: 注意地雷](#第三章-注意地雷)
        - [▶ Modifying a dictionary while iterating over it](#▶-modifying-a-dictionary-while-iterating-over-it)
    - [第四章: 隐藏的宝藏](#第四章-隐藏的宝藏)
        - [▶ Okay Python, Can you make me fly? *](#▶-okay-python-can-you-make-me-fly-)
    - [第五章: 杂项](#第五章-杂项)
        - [▶ `+=` is faster](#▶--is-faster)
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
> **Output (Python version):**
> ```py
> >>> python语句，执行某个命令
> 一些神奇的输出
> ```
> (可选): 有可能会介绍一下输出的内容
>
>
> #### :bulb: 解释:
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

# :eyes: 例子

## 第一章: 撕裂大脑

### ▶ 善变的字符串 *

1\.
```py
>>> a = "crazy_python"
>>> id(a)
2387669241224
>>> id("crazy" + "_" + "python") # 注意这两个字符串的id号是一样的
2387669241224
```

2\.
```py
>>> a = "crazy"
>>> b = "crazy"
>>> a is b
True

>>> a = "crazy!"
>>> b = "crazy!"
>>> a is b
False

>>> a, b = "crazy!", "crazy!"
>>> a is b
True
```

3\.
```py
>>> 'a' * 20 is 'aaaaaaaaaaaaaaaaaaaa'
True
>>> 'a' * 21 is 'aaaaaaaaaaaaaaaaaaaaa'
False
```

很不可思议，对吧？

#### :bulb: 解释:
+ 上面这种特性是CPython的一种编译器优化技术（叫做字符串驻留技术）。就是如果将要创建的字符串在之前已经创建过并且驻留在了内存没有释放，那么CPython不会创建一个新的实例，而是会把指针指向已经存在于内存的老的字符串实例。
+ 如果一个字符串实例已经驻村在了内存中，那么后续所有跟它值一样的变量都可以将指针指向这个内存中的字符串实例（这样就会节省内存空间）
+ 在上面这几段程序代码中，有几段的字符串明显驻留在了内存中供多个变量引用。 决定一个字符串是否会驻留在内存中是由这个字符串的实现方法决定的。下面是一些判断字符串变量是否会驻留内存的方法：
  * 所有长度为1或者0的字符串，全部会驻留
  * 编译阶段（也就是把源代码编译成.pyc文件的阶段）的字符串被驻留在内存（`'crazy'`会驻留在内存，但是`''.join(['c','r','a','z','y'])`就不会）
  * 如果字符串包含除了ASCII字符，数字和下划线以外的字符，那么这个字符串就不会驻留内存。这就是为什么`'crazy!'`赋值给`a`,`b`的时候得到的结果是False，因为`!`感叹号。CPython中对这个特点的具体实现请参考[这里](https://github.com/python/cpython/blob/3.6/Objects/codeobject.c#L19)
  <img src="./assets/string-intern/string_intern.png" alt="">
+ 当变量`a`和`b`在同一行赋值`"crazy!"`的时候，Python的解释器会创建一个新的字符串实例，然后把这两个变量同时指向这一个实例。但是如果你用两行实现赋值的话，Python解释器就不会知道已经有一个`'crazy!'`的字符串实例存在了（因为根据上面的规则，`'crazy!'`实例不会进行内存驻留供后面的语句引用）。这是一种专门在交互环境下编译器的一种优化方法。
+ 常量折叠是Python实现的一种[窥孔优化(Peephole optimization)](https://baike.baidu.com/item/%E7%AA%A5%E5%AD%94%E4%BC%98%E5%8C%96)技术。意思就是`'a'*20`这个语句在编译的时候会自动替换成`'aaaaaaaaaaaaaaaaaaaa'`这个变量，用来减少运行时的运算时钟周期（`'a'*20`需要多执行20次乘法运算）。常量折叠只在字符串长度小于等于20的时候发生（至于为什么？想想如果有一个`'a*10**10'`这样的语句，折叠后需要多大一个`.pyc`才能存下折叠后的字符串啊）。[这里](https://github.com/python/cpython/blob/3.6/Python/peephole.c#L288)是实现这种技术的实现代码。

---


### ▶ 不变的哈希值

1\.
```py
some_dict = {}
some_dict[5.5] = "Ruby"
some_dict[5.0] = "JavaScript"
some_dict[5] = "Python"
```

**Output:**
```py
>>> some_dict[5.5]
"Ruby"
>>> some_dict[5.0]
"Python"
>>> some_dict[5]
"Python"
```
"Python" 把之前的 "JavaScript" 覆盖掉了吗?

#### :bulb: 解释

* Python的字典结构是根据key值的哈希值判断两个key值是否相等的
* 在Python中，不变对象（Immutable objects）的值如果一样，那么它们的哈希值肯定也一样
  ```py
  >>> 5 == 5.0
  True
  >>> hash(5) == hash(5.0)
  True
  ```
  **注意:** 有些对象有不同的值，但是它们的哈希值也有可能是一样的（所谓的哈希冲突）
* 当`some_dict[5] = "Python"`这句话执行的时候， "Python"这个字符串就会覆盖掉"JavaScript"这个值，因为在Python看来，`5`和`5.0`的哈希值是一样的，也就是说对于字典结构他们对应的是一个key值。
* 在 StackOverflow 上面有一个[回答](https://stackoverflow.com/a/32211042/4354153)对Python的这个特性解释的很棒。

---

### ▶ 说了要执行就一定会执行！

```py
def some_func():
    try:
        return 'from_try'
    finally:
        return 'from_finally'
```

**Output:**
```py
>>> some_func()
'from_finally'
```

#### 💡 解释:

- 当在`try`语句块中遇到`return`,`break`或者`continue`的时候，如果是"try...finlly"语句块，那么在执行完`try`语句块里的内容后，依然会执行`finally`语句块的内容。
- 当`return`语句返回一个值的时候，那么因为在`finally`语句块中的`return`语句是最后执行的，那么返回的值就永远都是`finally`语句块中`return`语句返回的值。

---

### ▶ 鸠占鹊巢 *

```py
class Crazy:
  pass
```

**Output:**
```py
>>> Crazy() == Crazy() # 两个类实例是不同的
False
>>> Crazy() is Crazy() # 它们的id号也是不一样的
False
>>> hash(Crazy()) == hash(Crazy()) # 它们的哈希值按说也应该不一样
True
>>> id(Crazy()) == id(Crazy())
True
```

#### :bulb: 解释:

* 当`id`函数被调用的时候，Python创建了一个`Crazy`类实例，然后把这个实例传给了`id`函数。然后`id`函数返回这个实例的"id"号（实际上就是这个实例在内存中的地址），接着这个实例就被丢弃并且销毁了。
* 当我们紧接着再做一遍上面的步骤的时候，Python会把同一块内存空间分配给第二次创建的`Crazy`实例。又因为在CPython中`id`函数使用的是内存地址作为返回值，所以就会出现两个对象实例的id号相同的情况了。
* 所以，"对象的id是唯一的"这句话有一个前提条件是"在这个对象的生命周期内"。当这个对象在内存被销毁以后，其他的对象就可以占用它之前所用的内存空间产生一样的id号。
* 但是为什么上面的例子里`is`操作符却产生了`False`? 我们再看一个例子。
  ```py
  class Crazy(object):
    def __init__(self): print("I ")
    def __del__(self): print("D ")
  ```

  **Output:**
  ```py
  >>> Crazy() is Crazy()
  I I D D
  >>> id(Crazy()) == id(Crazy())
  I D I D
  ```
  现在你可以发现, 不同的使用实例的方法会对实例销毁的时间产生影响。

---

### ▶ 神奇赋值法

```py
some_string = "crazy"
some_dict = {}
for i, some_dict[i] in enumerate(some_string):
    pass
```

**Output:**
```py
>>> some_dict # 一个带引索的字典被创建.
{0: 'c', 1: 'r', 2: 'a', 3: 'z', 4: 'y'}
```

####  :bulb: 解释:

* 一个 `for` 语句在[Python语法](https://docs.python.org/3/reference/grammar.html)中是这么定义的：
  ```
  for_stmt: 'for' exprlist 'in' testlist ':' suite ['else' ':' suite]
  ```
  `exprlist` 是一组被赋值的变量. 这就等于说这组变量在**每次迭代**开始的时候都会执行一次 `{exprlist} = {next_value}` 。
  下面这个例子很好的解释了上面想要表达的意思:
  ```py
  for i in range(4):
      print(i)
      i = 10
  ```

  **Output:**
  ```
  0
  1
  2
  3
  ```

  是不是以为上面的循环就会执行一次？

  **:bulb: 解释:**
  - 在上面这个循环中，`i=10`这个赋值语句不会整个迭代过程产生任何影响。因为在每次迭代开始前，迭代函数（在这里是`range(4)`）都会把下一次的值赋值给目标变量（在这里是`i`）。

* 再来看上面的例子，`enumerate(some_string)`这个函数会在每次迭代的时候产生两个值，分别是`i`(一个从0开始的索引值)和一个字符（来自`some_string`的值）。然后这两个值会分别赋值给`i`和`some_dict[i]`。把刚才的循环展开来看就像是下面这样：
  ```py
  >>> i, some_dict[i] = (0, 'c')
  >>> i, some_dict[i] = (1, 'r')
  >>> i, some_dict[i] = (2, 'a')
  >>> i, some_dict[i] = (3, 'z')
  >>> i, some_dict[i] = (4, 'y')
  >>> some_dict
  ```

---

### ▶ 时间的误会

1\.
```py
array = [1, 8, 15]
g = (x for x in array if array.count(x) > 0)
array = [2, 8, 22]
```

**Output:**
```py
>>> print(list(g))
[8]
```

2\.

```py
array_1 = [1,2,3,4]
g1 = (x for x in array_1)
array_1 = [1,2,3,4,5]

array_2 = [1,2,3,4]
g2 = (x for x in array_2)
array_2[:] = [1,2,3,4,5]
```

**Output:**
```py
>>> print(list(g1))
[1,2,3,4]

>>> print(list(g2))
[1,2,3,4,5]
```

#### :blub: 解释

- 在[生成器](https://wiki.python.org/moin/Generators)表达式中,`in`语句会在声明阶段求值，但是条件判断语句（在这里是`array.count(x) > 0`）会在真正的运行阶段(runtime)求值。
- 在生成器运行之前，`array`已经被重新赋值为`[2, 8, 22]`了，所以这个时候再用`count`函数判断`2`,`8`,`22`在原列表中的数量，只有`8`是数量大于`0`的，所以最后这个生成器只返回了一个`8`是符合条件的。
- 在第二部分中，`g1`,`g2`输出结果不同，是因为对`array_1`和`array_2`的赋值方法不同导致的。
- 在第一个例子中， `array_1`绑定了一个新的列表对象`[1,2,3,4,5]`（可以理解成`array_1`的指针指向了一个新的内存地址），而且在这之前，`in`语句已经在声明时就为`g1`绑定好了旧的列表对象`[1,2,3,4]`（这个就对象也没有随着新对象的赋值而销毁）。所以这时候`g1`和`array_1`是指向不同的对象地址的。
- 在第二个例子中，由于切片化的赋值，`array_2`并没有绑定（指向）新对象，而是将旧的对象`[1,2,3,4]`更新（也就是说旧对象的内存地址被新对象占用了）成了新的对象`[1,2,3,4,5]`。所以，`g2`和`array_2`依旧同时指向一个地址，所以都更新成了新对象`[1,2,3,4,5]`。

---

### ▶ 特殊的数字们

下面这个例子在网上非常的流行。

```py
>>> a = 256
>>> b = 256
>>> a is b
True

>>> a = 257
>>> b = 257
>>> a is b
False

>>> a = 257; b = 257
>>> a is b
True
```

#### :blub: 解释:

**`is`和`==`的区别**

* `is` 操作符会检查两边的操作数是否引用的是同一个对象（也就是说，会检查两个操作数的id号是否匹配）。
* `==` 操作符会比较两个操作数的值是否一样。
* 所以说`is`是比较引用地址是否相同，`==`是比较值是否相同。下面的例子解释的比较清楚，
  ```py
  >>> [] == []
  True
  >>> [] is [] # 这里的两个空list分配了不同的内存地址
  False
  ```

**`256` 是一个已经存在于内存的对象 但是 `257` 不是**

当你启动一个Python解释器的时候，数字`-5`到`256`就会自动加载进内存。 这些数字都是一些比较常用的数字，所以Python解释器会把他们提前准备好以备以后使用。

下面这段话摘抄自 https://docs.python.org/3/c-api/long.html （已经翻译为中文）
> The current implementation keeps an array of integer objects for all integers between -5 and 256, when you create an int in that range you just get back a reference to the existing object. So it should be possible to change the value of 1. I suspect the behavior of Python, in this case, is undefined.:-)
>
> 当前的实现方法是，维护一个从-5到256的整数数组，当你使用其中某一个数字的时候，系统会自动为你引用到已经存在的对象上去。我认为应该让它可以改变数字1的值。不过就现在来说，Python还没有这个功能。:-)

```py
>>> id(256)
10922528
>>> a = 256
>>> b = 256
>>> id(a)
10922528
>>> id(b)
10922528
>>> id(257)
140084850247312
>>> x = 257
>>> y = 257
>>> id(x)
140084850247440
>>> id(y)
140084850247344
```

Python解释器在执行`y = 257`的时候还不能意识到我们之前已经创建过了一个值为`257`的对象，所以它又在内存创建了一个新的对象。

**当`a`和`b`变量在同一行赋值并且所赋值相等时，它们会引用到同一个对象**

```py
>>> a, b = 257, 257
>>> id(a)
140640774013296
>>> id(b)
140640774013296
>>> a = 257
>>> b = 257
>>> id(a)
140640774013392
>>> id(b)
140640774013488
```

* 当a和b在同一行被赋值为`257`的时候, Python解释器会创建一个新的对象，然后把这两个变量同时引用到这个新的对象。如果你分开两行赋值两个变量，那么解释器不会“知道”之前自己已经创建过一个同样的`257`对象了。
* 这是一种专门针对交互式解释器环境的优化机制。 当你在控制面板中敲入两行命令的时候，这两行命令是分开编译的，所以他们也会单独进行优化。如果你准备把这个例子（两行分别赋值的例子）写进`.py`文件然后进行测试，那么你会发现结果跟写在一行是一样的，因为文件里的代码是一次性编译的。

---

### ▶ 三子棋之一步取胜法

```py
# 首先先来初始化一个1*3的一维数组
row = [""]*3 #row i['', '', '']
# 然后再用二维数组模拟一个3*3的棋盘
board = [row]*3
```

**Output:**
```py
>>> board
[['', '', ''], ['', '', ''], ['', '', '']]
>>> board[0]
['', '', '']
>>> board[0][0]
''
>>> board[0][0] = "X"
>>> board
[['X', '', ''], ['X', '', ''], ['X', '', '']]
```

我们只赋值了一个“X”为什么会出来三个呢？

#### :bulb: 解释:

当我们初始化`row`变量的时候，下图显示的是内存中的变化

![image](./assets/1=3/after_row_initialized.png)

接着当变量`board`通过`[row]*3`初始化后，下图显示了内存的变化（其实最终每一个变量`board[0]`,`board[1]`,`board[2]`都引用了同一个`row`对象的内存地址）

![image](./assets/1=3/after_board_initialized.png)

我们可以通过不使用`row`变量来阻止这种情况的发生

```py
>>> board = [['']*3 for _ in range(3)]
>>> board[0][0] = "X"
>>> board
[['X', '', ''], ['', '', ''], ['', '', '']]
```

---

### ▶ 没脑子的函数

```py
funcs = []
results = []
for x in range(7):
    def some_func():
        return x
    funcs.append(some_func)
    results.append(some_func())

funcs_results = [func() for func in funcs]
```

**Output:**
```py
>>> results
[0, 1, 2, 3, 4, 5, 6]
>>> funcs_results
[6, 6, 6, 6, 6, 6, 6]
```
虽然我们每次把`some_func`函数加入到`funcs`列表里的时候`x`都不一样，但是`funcs`列表里的所有函数都返回了6.

//下面这段代码也是这样

```py
>>> powers_of_x = [lambda x: x**i for i in range(10)]
>>> [f(2) for f in powers_of_x]
[512, 512, 512, 512, 512, 512, 512, 512, 512, 512]
```

#### :bulb: 解释

- 当我们在一个循环中定义一个函数，并且在函数体中用了循环中的变量时，这个函数只会绑定这个变量本身，并不会绑定当前变量循环到的值。所以最终所有在循环中定义的函数都会使用循环变量最后的值做计算。

- 如果你想实现心中想的那种效果，可以把循环变量当做一个参数传递进函数体。**为什么这样可以呢？**因为这样在函数作用域内会重新定义一个变量，不是循环里面的那个变量了。

    ```py
    funcs = []
    for x in range(7):
        def some_func(x=x):
            return x
        funcs.append(some_func)
    ```

    **Output:**
    ```py
    >>> funcs_results = [func() for func in funcs]
    >>> funcs_results
    [0, 1, 2, 3, 4, 5, 6]
    ```

---

### ▶ `is not ...` 并不是  `is (not ...)`

```py
>>> 'something' is not None
True
>>> 'something' is (not None)
False
```

#### :bulb: 解释

- `is not` 是一个单独的二元运算符, 和分开使用的`is`和`not`作用是不同的。
- `is not` 只有在两边的操作数相同时（id相同）结果才为`False`，否则为`True`

---

### ▶ 尾部的逗号

**Output:**
```py
>>> def f(x, y,):
...     print(x, y)
...
>>> def g(x=4, y=5,):
...     print(x, y)
...
>>> def h(x, **kwargs,):
  File "<stdin>", line 1
    def h(x, **kwargs,):
                     ^
SyntaxError: invalid syntax
>>> def h(*args,):
  File "<stdin>", line 1
    def h(*args,):
                ^
SyntaxError: invalid syntax
```

#### :bulb: 解释:

- 末尾的逗号在函数参数列表最后并不总是合法的
- 在Python中，参数列表里，有一部分使用前导逗号分隔的，有一部分是用后导逗号分隔的（比如`**kwargs`这种参数用前导逗号分隔，正常参数`x`用后导逗号分隔）。而这种情况就会导致有些参数列表里的逗号前后都没有用到，就会产生冲突导致编译失败。
- **注意** 这种尾部逗号的问题已经在Python 3.6中被[修复](https://bugs.python.org/issue9232)了。然后[这里](https://bugs.python.org/issue9232#msg248399)有对各种尾部逗号用法的讨论。

---

### ▶ 最后一个反斜杠

**Output:**
```
>>> print("\\ C:\\")
\ C:\
>>> print(r"\ C:")
\ C:
>>> print(r"\ C:\")

    File "<stdin>", line 1
      print(r"\ C:\")
                     ^
SyntaxError: EOL while scanning string literal
```

#### :bulb: 解释

- 如果字符串前面声明了`r`，说明后面紧跟着的是一个原始字符串，反斜杠在这种字符串中是没有特殊意义的
  ```py
  >>> print(repr(r"craz\"y"))
  'craz\\"y'
  ```
- 解释器实际上是怎么做的呢，虽然看起来仅仅是改变了反斜杠的转义特性，实际上，它（反斜杠）会把自己和紧跟着自己的下一个字符一起传入到解释器，用来供解释器做判断和转换。这也就是为什么当反斜杠在最后一个字符的时候会报错。

---

### ▶ 纠结的not

```py
x = True
y = False
```

**Output:**
```py
>>> not x == y
True
>>> x == not y
  File "<input>", line 1
    x == not y
           ^
SyntaxError: invalid syntax
```

#### :bulb: 解释:

* 操作符的优先级会影响表达式的计算顺序，并且在Python里，`==`操作符的优先级要高于`not`操作符。
* 所以`not x == y`等于 `not (x == y)`，又等于`not (True == False)`，最终计算结果就会是`True`。
* 但是`x == not y`会报错是因为这个表达式可以等价于`(x == not) y`，而不是我们第一眼认为的`x == (not y)`。

---

### ▶ 只剩一半的三引号

**Output:**
```py
>>> print('crazypython''')
wtfpython
>>> print("crazypython""")
wtfpython
>>> # 下面的语句将会产生语法错误
>>> # print('''crazypython')
>>> # print("""crazypython")
```

#### :bulb: 解释:
+ Python支持隐试的[字符串连接](https://docs.python.org/2/reference/lexical_analysis.html#string-literal-concatenation),比如下面这样，
  ```
  >>> print("crazy" "python")
  crazypython
  >>> print("crazy" "") # or "crazy"""
  crazy
  ```
+ 在Python中，`'''` 和 `"""` 也是一种字符串界定符，所以如果Python解释器发现了其中一个，那么就会一直在后面找对称的另一个界定符，这也就是为什么上面例子里注释掉的语句会有语法错误，因为解释器在后面找不到和前面`'''`或`"""`配对的界定符。

---

### ▶ 消失的午夜零点

```py
from datetime import datetime

midnight = datetime(2018, 1, 1, 0, 0)
midnight_time = midnight.time()

noon = datetime(2018, 1, 1, 12, 0)
noon_time = noon.time()

if midnight_time:
    print("Time at midnight is", midnight_time)

if noon_time:
    print("Time at noon is", noon_time)
```

**Output:**
```sh
('Time at noon is', datetime.time(12, 0))
```
午夜时间并没有被打印出来

#### :bulb: 解释:

在Python 3.5以前, 对于被赋值为UTC零点的`datetime.time`对象的布尔值，会被认为是`False`。这是一个在用`if obj:`这种语句的时候经常会忽略的特性，所以我们在写这种`if`语句的时候，要注意判断`obj`是否等于`null`或者空。

---

### ▶ 站错队的布尔型

1\.
```py
# 一个计算列表里布尔型和Int型数量的例子
mixed_list = [False, 1.0, "some_string", 3, True, [], False]
integers_found_so_far = 0
booleans_found_so_far = 0

for item in mixed_list:
    if isinstance(item, int):
        integers_found_so_far += 1
    elif isinstance(item, bool):
        booleans_found_so_far += 1
```

**Output:**
```py
>>> booleans_found_so_far
0
>>> integers_found_so_far
4
```

2\.
```py
another_dict = {}
another_dict[True] = "JavaScript"
another_dict[1] = "Ruby"
another_dict[1.0] = "Python"
```

**Output:**
```py
>>> another_dict[True]
"Python"
```

3\.
```py
>>> some_bool = True
>>> "crazy"*some_bool
'crazy'
>>> some_bool = False
>>> "crazy"*some_bool
''
```

#### :bulb: 解释:

* 布尔型(Booleans)是 `int`类型的一个子类型(bool is instance of int in Python)
  ```py
  >>> isinstance(True, int)
  True
  >>> isinstance(False, int)
  True
  ```

* `True`的整形值是`1`，`False`的整形值是`0`
  ```py
  >>> True == 1 == 1.0 and False == 0 == 0.0
  True
  ```

* StackOverFlow有针对这个问题背后原理的[解答](https://stackoverflow.com/a/8169049/4354153)。

---

### ▶ 类属性与类实例属性

1\.
```py
class A:
    x = 1

class B(A):
    pass

class C(A):
    pass
```

**Ouptut:**
```py
>>> A.x, B.x, C.x
(1, 1, 1)
>>> B.x = 2
>>> A.x, B.x, C.x
(1, 2, 1)
>>> A.x = 3
>>> A.x, B.x, C.x
(3, 2, 3)
>>> a = A()
>>> a.x, A.x
(3, 3)
>>> a.x += 1
>>> a.x, A.x
(4, 3)
```

2\.
```py
class SomeClass:
    some_var = 15
    some_list = [5]
    another_list = [5]
    def __init__(self, x):
        self.some_var = x + 1
        self.some_list = self.some_list + [x]
        self.another_list += [x]
```

**Output:**

```py
>>> some_obj = SomeClass(420)
>>> some_obj.some_list
[5, 420]
>>> some_obj.another_list
[5, 420]
>>> another_obj = SomeClass(111)
>>> another_obj.some_list
[5, 111]
>>> another_obj.another_list
[5, 420, 111]
>>> another_obj.another_list is SomeClass.another_list
True
>>> another_obj.another_list is some_obj.another_list
True
```

#### :bulb: 解释:

* 类里的属性和类实例中的属性是作为一个字典列表对象进行处理的。如果在当前类中没有找到需要调用的属性名，那么就会递归去父类中寻找。
* `+=`操作符会在原有易变类型对象的基础上做改变而不会重新创建一个新的对象。所以在一个类实例中修改属性值，会影响到所有调用这个属性的相关类实例和类。

---

### ▶ None的产生

```py
some_iterable = ('a', 'b')

def some_func(val):
    return "something"
```

**Output:**
```py
>>> [x for x in some_iterable]
['a', 'b']
>>> [(yield x) for x in some_iterable]
<generator object <listcomp> at 0x7f70b0a4ad58>
>>> list([(yield x) for x in some_iterable])
['a', 'b']
>>> list((yield x) for x in some_iterable)
['a', None, 'b', None]
>>> list(some_func((yield x)) for x in some_iterable)
['a', 'something', 'b', 'something']
```

#### :bulb: 解释:
- 这是一个CPython中`yield`关键字在列表构造和生成器表达式中使用的bug。已经在Python3.8中修复了。在Python3.7中也会警告过时。具体可以看Python的这篇[bug report](https://bugs.python.org/issue10544)
---

### ▶ 不可修改的元组

```py
some_tuple = ("A", "tuple", "with", "values")
another_tuple = ([1, 2], [3, 4], [5, 6])
```

**Output:**
```py
>>> some_tuple[2] = "change this"
TypeError: 'tuple' object does not support item assignment
>>> another_tuple[2].append(1000) #这里并没有报错
>>> another_tuple
([1, 2], [3, 4], [5, 6, 1000])
>>> another_tuple[2] += [99, 999]
TypeError: 'tuple' object does not support item assignment
>>> another_tuple
([1, 2], [3, 4], [5, 6, 1000, 99, 999])
```

我还以为元组是不可以修改的呢......

#### :bulb: 解释:

* 引用自 https://docs.python.org/2/reference/datamodel.html
    > 不可变序列
        一个不可变序列对象在第一次定义后就不再可以修改。（如果这个对象中包含有对其他对象的引用，这些其他对象有可能是可变的或者可修改的；总之，只有直接引用的对象是不可以修改的。）
* `+=`操作符会对左侧操作对象本身进行修改。但是元组是不允许修改的，所以会报错，但是实际上修改的是一个可变的列表（list），元组里保存的只是这个列表的地址，所以最终还是会修改成功。

---

### ▶ 消失的变量e

```py
e = 7
try:
    raise Exception()
except Exception as e:
    pass
```

**Output (Python 2.x):**
```py
>>> print(e)
# 什么都没有打印
```

**Output (Python 3.x):**
```py
>>> print(e)
NameError: name 'e' is not defined
```

#### :bulb: 解释:

* 参考自: https://docs.python.org/3/reference/compound_stmts.html#except
  
  当一个异常(exception)被用`as`赋值给一个变量后，这个变量将会在`except`语句块结束后清除。看下面这段

  ```py
  except E as N:
      foo
  ```

  相当于这样

  ```py
  except E as N:
      try:
          foo
      finally:
          del N
  ```
  
  这意味着你最好不要在外面定义一个和"N"重名的变量。这些被赋值的异常变量被清除是因为，Python会将这些变量加入一个异常回溯栈中（traceback，仔细观察每次程序出错控制台输出的错误信息就是从tranceback这个堆栈里面以此取出来的），记录这些异常的具体位置信息并且一直保持这个堆栈的信息直到下一次垃圾回收开始。

* 这些Python的子句并没有独立的作用域，上面所有的例子都在一个作用域里，所以当变量`e`在`except`子句里面被移除后，就相当于在整个作用域都消失了。但是在函数中情况就和上面不一样了，因为Python函数有自己的“内部”作用域。下面这个例子将说明这种情况：

     ```py
     def f(x):
         del(x)
         print(x)

     x = 5
     y = [5, 4, 3]
     ```

     **Output:**
     ```py
     >>>f(x)
     UnboundLocalError: local variable 'x' referenced before assignment
     >>>f(y)
     UnboundLocalError: local variable 'x' referenced before assignment
     >>> x
     5
     >>> y
     [5, 4, 3]
     ```

* 在 Python 2.x 版本里面, 变量`e`会被赋值`Exception()`实例，所以当打印的时候什么都不会打印出来。

    **Output (Python 2.x):**
    ```py
    >>> e
    Exception()
    >>> print e
    # 什么都没有打印出来
    ```

---

### ▶ 亦真还假

```py
True = False
if True == False:
    print("It's true of false?")
```

**Output:**
```
It's true of false?
```

#### :bulb: 解释:

- 一开始， Python是没有`bool`布尔类型的（人们用0代表假用非0代表真）。后来增加了`True`，`False`还有`bool`类型，但是为了向前兼容，所以并没有`True`和`False`的关键字常量，只不过作为一个内部变量出现。
- Python 3是不向前兼容的，所以终于修复了这个问题，同时也要注意上面的例子在Python 3.X版本下是运行不了的！

---

### ▶ 转瞬即空

```py
some_list = [1, 2, 3]
some_dict = {
  "key_1": 1,
  "key_2": 2,
  "key_3": 3
}

some_list = some_list.append(4)
some_dict = some_dict.update({"key_4": 4})
```

**Output:**
```py
>>> print(some_list)
None
>>> print(some_dict)
None
```

#### :bulb: 解释

大部分修改序列结构对象的方法，比如`list.append`，`dict.update`，`list.sort`等等。都会直接对序列对象本身进行操作，也就是所谓的“就地操作”（in-plcae）并且会返回`None`。这么做是为了提升程序的性能，避免还需要把原有对象拷贝一次。（参考[这里](http://docs.python.org/2/faq/design.html#why-doesn-t-list-sort-return-the-sorted-list)）。

```py
some_list = [1, 2, 3]
```

**Output:**
```py
>>>some_list2 = some_list.append(4)
>>>some_list2
None
>>>some_list
[1, 2, 3, 4]
```

---

### ▶ 子类的关系 *

**Output:**
```py
>>> from collections import Hashable
>>> issubclass(list, object)
True
>>> issubclass(object, Hashable)
True
>>> issubclass(list, Hashable)
False
```

是不是觉得类的继承关系应该是可传递的（transitive）？（比如，`A`是`B`的一个子类，`B`又是`C`的一个子类，那么`A`也"应该"是`C`的子类）

#### :bulb: 解释:

* 在Python中子类的继承关系不一定是传递的，任何人都可以自定义元类（metaclass）中的`__subclasscheck__`函数（`_subclasscheck__(subclass)`检查subclass是不是调用类的子类）。
* 当调用`issubclass(cls, Hashable)`的时候，函数只是简单的检查一下`cls`和它继承的类中有没有"`__hash__`"这个方法。
* 因为`object`是可以被哈希的(也就是说`object`有`__hash__`这个函数)，但是`list`是不能被哈希的，所以他们之间打破了传导关系。
* 如果想看更详尽的解释，[这里](https://www.naftaliharris.com/blog/python-subclass-intransitivity/)有关于Python子类关系传导的详细解释。

---

### ▶ 神秘的键值转换 *

```py
class SomeClass(str):
    pass

some_dict = {'s':42}
```

**Output:**
```py
>>> type(list(some_dict.keys())[0])
str
>>> s = SomeClass('s')
>>> some_dict[s] = 40
>>> some_dict # expected: Two different keys-value pairs
{'s': 40}
>>> type(list(some_dict.keys())[0])
str
```

#### :bulb: 解释:

* 类`s`和字符串`s`的哈希值是一样的，因为`SomeClass`继承了`str`类的`__hash__`方法。
* `SomeClass("s") == "s"` 等于`True`，因为`SomeClass`同样继承了`str`类的`__eq__`方法。
* 因为两个对象的哈希值(hash)和值(value)全都相等,所以他们在字典的关键字(key)里是被认为相同的。
* 如果想要打到预期的效果，我们可以重新定义`SomeClass`的`__eq__`方法
  ```py
  class SomeClass(str):
    def __eq__(self, other):
        return (
            type(self) is SomeClass
            and type(other) is SomeClass
            and super().__eq__(other)
        )

    # 当我们自定义 __eq__ 方法后， Python会停止
    # 自动继承 __hash__ 方法， 所以我们同样也需要定义它
    __hash__ = str.__hash__

  some_dict = {'s':42}
  ```

  **Output:**
  ```py
  >>> s = SomeClass('s')
  >>> some_dict[s] = 40
  >>> some_dict
  {'s': 40, 's': 42}
  >>> keys = list(some_dict.keys())
  >>> type(keys[0]), type(keys[1])
  (__main__.SomeClass, str)
  ```

---

### ▶ 看你能不能猜到这个的结果？

```py
a, b = a[b] = {}, 5
```

**Output:**
```py
>>> a
{5: ({...}, 5)}
```

#### :bulb: 解释:

* 根据Python的赋值语句的[文档](https://docs.python.org/3.7/reference/simple_stmts.html#assignment-statements),赋值语句有如下的格式
  ```
  (target_list "=")+ (expression_list | yield_expression)
  ```
  并且
  > 一个赋值语句会对表达式列表(expression_list)进行求值（这个可以只有一个表达式，也可以多个表达式用逗号分开组成表达式列表，后者最终会表现为元组的形式）并且会将单次的求值结果对象依次从左至右赋值给目标列表(target_list)。

* 在`(target_list "=")+`这个表达式中`+`意味着 **一个或者多个** 目标列表。这上面这个例子中，目标列表是`a,b`和`a[b]`（注意表达式列表永远只有一个，在我们这个例子里是`{}, 5`）。

* 当表达式计算出来后，它的值会被 **从左至右** 依次赋值给目标列表。所以，在上面的例子里，第一次赋值会把`{}, 5`这个元组赋值给`a, b`这个目标列表，这个时候`a = {}` 并且 `b = 5`。

* 现在`a`被赋值成了`{}`，一个可变对象(mutable object)。

* 第二个目标列表是`a[b]`（你可能会认为这种写法会报错，因为我们没有之前并没有定义`a`和`b`，但是没关系，我们刚刚已经给`a`和`b`分别赋值了`{}`和`5`）。

* 现在我们会把元组`({}, 5)`赋值给字典关键为`5`的字典对象（也就是`a[5]`），同时也因此创建了一个循环引用(circular reference)（`{...}`在输出中代表同一个对象`a`已经被引用了）。下面是一个关于引用循环简单点的例子

  ```py
  >>> some_list = some_list[0] = [0]
  >>> some_list
  [[...]]
  >>> some_list[0]
  [[...]]
  >>> some_list is some_list[0]
  True
  >>> some_list[0][0][0][0][0][0] == some_list
  True
  ```
  在我们的例子用也是同样的情况（`a[b][0]`和`a`是指向同一个对象）

* 所以总结一下，我们可以把上面的列子像如下这样拆分
  ```py
  a, b = {}, 5
  a[b] = a, b
  ```
  并且通过`a[b][0]`和`a`是同一个对象来证明确实存在引用循环
  ```py
  >>> a[b][0] is a
  True
  ```

---

## 第二章: 瞒天过海

### ▶ Skipping lines?


---

## 第三章: 注意地雷


### ▶ Modifying a dictionary while iterating over it

---


## 第四章: 隐藏的宝藏

This section contains few of the lesser-known interesting things about Python that most beginners like me are unaware of (well, not anymore).

### ▶ Okay Python, Can you make me fly? *

---

## 第五章: 杂项


### ▶ `+=` is faster


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