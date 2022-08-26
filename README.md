# 自用爬取小说

### 环境准备

**1.安装beautiful soup**
```shell
pip install bs4
pip install lxml
 ```

**2.安装requests**
```shell
 pip install requests
```

### 介绍

**1.网址 ：[笔趣阁](http://www.b520.cc/)**
![20220823155223](https://s2.loli.net/2022/08/23/zwmAiLIuBpkfeXE.png)


**2.使用方式**
+ 首先搜索你需要的书名，比如说[剑来]()
![20220823160044](https://s2.loli.net/2022/08/23/SBA8Xh4qYwfH1Jg.png)

+ 接着点击书名
![20220823160312](https://s2.loli.net/2022/08/23/rxdFAmik5SRCBgN.png)

+ 复制网址
![20220823160431](https://s2.loli.net/2022/08/23/Wp4NbkETLRVdZHj.png)

+ 运行main.py，根据提示输入网址
  
  ![20220823160548](https://s2.loli.net/2022/08/23/5DxYcy4hgGwXm1t.png)

### 后续
后续还会不断进行改进……
比如：
  -  **txt转pdf**，很多图书软件对于txt导入不是很友好
  -  代码规范，优化
  -  更加智能  

### 参考资料

+ [爬虫学习](https://github.com/wistbean/learn_python3_spider)
+ [字典的添加、创建、删除等](https://blog.csdn.net/cadi2011/article/details/85857917)
+ [Python判断字符串是否符合某一正则表达式](https://blog.csdn.net/diezhuzhen5707/article/details/101767552?spm=1001.2101.3001.6661.1&utm_medium=distribute.pc_relevant_t0.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-1-101767552-blog-107944677.pc_relevant_default&depth_1-utm_source=distribute.pc_relevant_t0.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-1-101767552-blog-107944677.pc_relevant_default&utm_relevant_index=1)
  

### 更新日志

### 2022-8-26
  
  #### 更新内容
  + 将书章节、网址以json文件格式保存
  + 根据json文件动态追加更新的文章

  #### 预期计划
  + 指定章节查看
           
