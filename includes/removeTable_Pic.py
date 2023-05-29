#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2023-05-29 10:22:36
# @Author  : Octan3 (octan3@qq.com)
# @Link    : https://github.com/Duola-li/OUC-Latex-Thesis-master
# @Version : 1.1
# @Description : 毕业论文查重版工具，注释掉指定latex文件中的图表显示，生成新的latex文件，后缀为 xxx_noTP.tex。在main文件中引用即可。


def main():
	files = ["section_01.tex", "section_02.tex", "section_Conclusion.tex", ]

	#需要注释的标签类型
	tp_labels = ["figure", "table", "sidewaystable"]
	
	for f in files:
		results = []
		with open(f, "r", encoding='utf-8') as tex:
			print(f)
			while True:
				line = tex.readline()
				if line == "":
					break	#读完退出
				for kk in tp_labels:	#查找图表标签
					if line.lstrip().startswith(r"\begin{"+kk):
						line = "\\iffalse \n"+line
					elif line.lstrip().startswith(r"\end{"+kk):
						line = line + "\\fi\n"

				results.append(line)
		print(f, "修改完成，开始写入")
		with open(f[:-4]+"_noTP.tex", "w", encoding='utf-8') as tex:
			tex.writelines(results)
		print(f, "写入完毕，out: ", f[:-4]+"_noTP.tex")


if __name__ == '__main__':
	main()