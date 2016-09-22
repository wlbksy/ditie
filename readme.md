# 北京地铁站分析

1. 使用[python3](https://docs.python.org/3/)对北京地铁规划的地铁站进行计算。

2. 采用了[networkx](https://github.com/networkx/networkx)里[计算中心度的函数](http://networkx.github.io/documentation/development/reference/algorithms.centrality.html)来衡量地铁站的重要性。

3. 使用了[bokeh](https://github.com/bokeh/bokeh)来进行可视化。

4. 使用了Degree、Closeness、Betweenness、Eigenvector以及accessibility等几种评价指标

# 使用方法

1. 命令行下进入文件夹
    文件夹下有一个名为 ``beijing.py`` 的文件，
    里面有两个变量：
    ``all_lines`` ： 包含所有要计算的线路，格式为 list(list())
    ``cyclic_lines``: 包含环路，格式为 list(list())
    环路线路中的每一条线路，不需使得首尾地铁站重复一遍。

2. 运行
   ```bash
   python3 centrality.py
   ```
   会在当前目录生成一个 ``beijing.centrality.csv`` 的文件，其中包含了计算好的如下三个指标,
   并自动生成由这三个指标的[笛卡尔积](https://en.wikipedia.org/wiki/Cartesian_product)所构成的九个交互式图形

   数值|指标
   ----|----
   0|degree
   1|closeness
   2|betweenness
   3|eigenvector

3. 根据是否已经在本地生成了 ``acc_{loops}.csv`` 文件，来决定是否需要注释或反注释
  ``accessibility.py``中
  ```python
  main(G, total_loops)
  ```
  这一行，然后运行
  ```bash
  python3 accessibility.py
  ```
  会在当前目录生成一个 ``beijing.all.{loops}.csv`` 的文件，其中包含了计算好的可达性指标。

4. 第2、3步均会在当前目录生成一个 ``beijing.all.csv`` 的文件，其中包含了当前计算好的指标。
运行
```bash
python3 htmlplot.py
```
生成的网页文件在 ``./html/`` 文件夹下

# To Do List
1. 展示各地铁站随时间变化的中心度的变化
2. 其它城市


注：由于中心度的概念只是用来衡量网络中不同节点的重要性排名(ranking)，因此计算出来的具体数值不具有实际数值大小上的意义
