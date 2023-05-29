## 去掉mendeley导出的bib文件中不必要的项
# 其中url必须去掉，否则会影响毕业论文引用
# 检查重复引用的文献

infile = "c_Mendeley_cite.bib"
outfile = "cite.bib"

# 要去除的标签
filters = ["abstract", "url", "urldate", "mendeley-groups", "file", "mendeley-tags", "doi"]
yearscount = {}
#url misc要有

#统计近5年文献
# MYCITENUM = 124    # 用实际引用计算
# MYCITENUM = 0   # 用cite文件计算

latex = True	# 输出所有引用代码
latexr = ""

results = []
citekeys = []
with open(infile, "r", encoding='utf-8') as file:
	while True:
		line = file.readline()
		if line == "":
			break
		line = line.lstrip()
		if line.startswith("@"):
			##
			loci = line.index("{")
			cite = line[loci+1:-2]
			if latex:
				latexr += "\\cite{%s} "%cite
			##
			WebType = False
			if line.startswith("@misc{on"):	#是网页类型
				WebType = True
		if line.startswith("year"):
			loci = line.index("{")
			year = line[loci+1:loci+5]
			if year in yearscount:
				yearscount[year] += 1
			else:
				yearscount[year] = 1
		if line.startswith("author"):
			line = line.replace(" & ", " and ")
		if line.startswith("title"):
			line = line.replace("{{", "{")
			line = line.replace("}}", "}")
			loci = line.index("{")
			bibkey = line[loci+1:-2]
			if bibkey in citekeys:
				print("\n ! Repeat bib entry: \n", bibkey)
			else:
				citekeys.append(bibkey)
		if line.startswith("//"):
			line = "\n"+line
			
		if line != "\n":
			find = False
			for key in filters:
				if line.startswith(key) and "}" in line[-5:]:
					if WebType and key == "url":
						find = False
						break
					else:
						find = True
						break
			if not find:
				results.append(line)
				# print("-", line)
print("清理完成，开始写入")

with open(outfile, "w", encoding='utf-8') as file:
	file.writelines(results)

print("共有 %d 个bib条目"%len(citekeys))

tempall = 0
for i in range(2023, 2015, -1):
	try:
		tempall += yearscount[str(i)]
	except Exception as e:
		print(i, "None")
	else:
		if MYCITENUM:
			alls = MYCITENUM
		else:
			alls = len(citekeys)
		print("%d: %2d/%d-%2.1f%%"%(i, tempall, alls, 100*tempall/alls) )

print("Done!")

if latex:
	print(latexr)


	