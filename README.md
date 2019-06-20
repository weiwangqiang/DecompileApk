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