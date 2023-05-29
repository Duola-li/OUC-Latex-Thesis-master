# 中国海洋大学硕博士学位论文 LaTeX 模板
本模板是中国海洋大学硕博士学位论文 LaTeX 模板。

本项目以[高峰老师Latex模板](https://github.com/summitgao/OUC-LaTex-master)和 [ouc-ocean-group](https://github.com/ouc-ocean-group/oucthesis) 两个项目为基础进行部分改写。

## 使用环境
本项目在texStudio和Overleaf均可使用。首推Overleaf，但图片较多时Overleaf可能编译超时。

### OverLeaf
编译器为XeLaTex即可。

### TexStudio
本人使用环境：
1. TeXstudio ==4.3.1==
2. TeX Live ==2022==
3. Texstudio编译器：==xelatex==

## 修改说明
1. 修正参考文献、keyword、公式等格式问题。后续格式可自行修改oucthesis.cls文件
2. 增加附录章节选项
3. 增加注释工具，应对查重版本全文字论文。python脚本为 **./includes/removeTable_Pic.py**。
4. 增加编译时间统计，以及编译完成提示音。

## 使用说明
具体参见 main.tex

编译时间统计及编译完成提示音功能，编写工具**mytime.exe**，首次执行记录开始编译时间，再次执行记录编译完成时间，并播放提示音。可在TexStudio中配置使用。首先将两个不使用的命令配置为mytime.exe，如SVN和SVNADMIN。然后再编译器命令前后分别加上SVN和SVNADMIN即可。

![配置texstudio的两个命令为mytime.exe](https://github.com/Duola-li/OUC-Latex-Thesis-master/blob/main/Time_statistics/1.png)
![将mytime.exe添加到编译命令中](https://github.com/Duola-li/OUC-Latex-Thesis-master/blob/main/Time_statistics/2.png)


### cleanbib.py
去掉bib文件中多于项，找出重复引用，统计文献个数，近5年文献率。