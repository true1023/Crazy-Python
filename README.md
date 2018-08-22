
<p align="center"><img src="/assets/logo.png" alt=""></p>
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


[Section: Strain your brainn!](#section-strain-yourbrain)


# Structure of the Examples

All the examples are structured like below:

> ### ▶ Some fancy Title *
> The asterisk at the end of the title indicates the example was not present in the first release and has been recently added.
>
> ```py
> # Setting up the code.
> # Preparation for the magic...
> ```
>
> **Output (Python version):**
> ```py
> >>> triggering_statement
> Probably unexpected output
> ```
> (Optional): One line describing the unexpected output.
>
>
> #### 💡 Explanation:
>
> * Brief explanation of what's happening and why is it happening.
>   ```py
>   Setting up examples for clarification (if necessary)
>   ```
>   **Output:**
>   ```py
>   >>> trigger # some example that makes it easy to unveil the magic
>   # some justified output
>   ```

**Note:** All the examples are tested on Python 3.5.2 interactive interpreter, and they should work for all the Python versions unless explicitly specified in the description.

# Usage

A nice way to get the most out of these examples, in my opinion, will be just to read the examples chronologically, and for every example:
- Carefully read the initial code for setting up the example. If you're an experienced Python programmer, most of the times you will successfully anticipate what's going to happen next.
- Read the output snippets and,
  + Check if the outputs are the same as you'd expect.
  + Make sure if you know the exact reason behind the output being the way it is.
    - If no, take a deep breath, and read the explanation (and if you still don't understand, shout out! and create an issue [here](https://github.com/satwikkansal/wtfPython)).
    - If yes, give a gentle pat on your back, and you may skip to the next example.

PS: You can also read WTFpython at the command line. There's a pypi package and an npm package (supports colored formatting) for the same.

To install the npm package [`wtfpython`](https://www.npmjs.com/package/wtfpython)
```sh
$ npm install -g wtfpython
```

Alternatively, to install the pypi package [`wtfpython`](https://pypi.python.org/pypi/wtfpython)
```sh
$ pip install wtfpython -U
```

Now, just run `wtfpython` at the command line which will open this collection in your selected `$PAGER`.

---

# 👀 Examples

<a name="section-strain-yourbrain"/>

## Section: Strain your brainsdfsdfsdf!
