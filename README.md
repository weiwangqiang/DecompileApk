# mac 平台反编译apk的工具


# How to use ?

在iterm中输入

```java
python DecompileApk.py /Volumes/G/xxxx.apk
```

即后面加apk的路径参数

等待执行完毕后，会在项目目录下生成一个 classes-dex2jar.jar文件，然后脚本自动打开JD-GUI，按照如下步骤打开项目目录下的classes-dex2jar.jar文件即可

![](https://github.com/weiwangqiang/ProjectIcn/blob/master/picture/csdn/1.jpg?raw=true)

如下，就可看到apk的源码了

![](https://github.com/weiwangqiang/ProjectIcn/blob/master/picture/csdn/2.jpg?raw=true)


# ApkTool

以上的方法只能用于反编译源码，但是不能获取到apk的资源文件，这里就需要使用apkTool了，方法如下：

到~DecompileApk/apkTool 路径下，执行

```java

 apktool d xxx/xxx.apk -o /test

```

其中 `d`的参数是apk的路径，`-o` 指需要把反编译后的资源放在哪里，可以不指定，默认在当前目录下。

获取到的结果如下，包含Androidmanifest，res,layout,asset等。

![](https://raw.githubusercontent.com/weiwangqiang/ProjectIcn/master/picture/csdn/decompileApk_res.jpg)


# 多Dex

目前暂时不支持多dex的apk，需要手动使用dex-tools-2.1-SNAPSHOT/d2j-dex2jar.sh 脚本

```sh

 d2j-dex2jar.sh apk路径

```

## 关于JD-GUI找不到Java版本的问题

可以参考如下文章

[Java反编译工具JD-GUI还是报错找不到java 1.8+](https://www.cnblogs.com/juhy/p/14193476.html)
