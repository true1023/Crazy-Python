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
        - [▶ A tic-tac-toe where X wins in the first attempt!](#▶-a-tic-tac-toe-where-x-wins-in-the-first-attempt)
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
### ▶ A tic-tac-toe where X wins in the first attempt!

```py
# Let's initialize a row
row = [""]*3 #row i['', '', '']
# Let's make a board
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

We didn't assign 3 "X"s or did we?

#### 💡 Explanation:

When we initialize `row` variable, this visualization explains what happens in the memory

![image](/images/tic-tac-toe/after_row_initialized.png)

And when the `board` is initialized by multiplying the `row`, this is what happens inside the memory (each of the elements `board[0]`, `board[1]` and `board[2]` is a reference to the same list referred by `row`)

![image](/images/tic-tac-toe/after_board_initialized.png)

We can avoid this scenario here by not using `row` variable to generate `board`. (Asked in [this](https://github.com/satwikkansal/wtfpython/issues/68) issue).

```py
>>> board = [['']*3 for _ in range(3)]
>>> board[0][0] = "X"
>>> board
[['X', '', ''], ['', '', ''], ['', '', '']]
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