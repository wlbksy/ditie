# 北京地铁站分析

1. 采用了[networkx](https://github.com/networkx/networkx)里[计算中心度的函数](https://networkx.org/documentation/stable/reference/algorithms/centrality.html)来衡量地铁站的重要性。
1. 使用的指标，除特殊标注外，均为数值越大越好
    1. Degree：相邻车站数目
    1. Eigenvector：
        1. eigenvector：根据邻居的中心度，迭代求解自己的中心度，直至收敛。中心度考虑是相邻车站数目
        1. katz：广义 eigenvector，有加权
    1. Closeness：到其它所有结点的平均站数的倒数
    1. (Shortest Path) Betweenness：任意两个车站之间的最短路，经过当前车站的占比
    1. Current Flow Closeness：两个车站之间有多种路线，每个路线都有流量，路越短流量越大，路越长流量越小。到其它所有结点的平均流量加权站数的倒数
    1. Current Flow Betweenness：任意两个车站之间的流量，经过当前结点的占比
    1. Communicability Betweenness：任意两个车站之间的最短路，经过当前车站的加权占比，长度越长的路，权重越小
    1. Load：类似 (Shortest Path) Betweenness，有加权
    1. Subgraph：该车站作为起终点的闭环长度的加权和，长度越长权重越小
    1. Harmonic：到其它所有结点的站数的倒数
    1. Second Order （数值越小越好）：在地铁内随机游走，回到该车站的次数的标准差

由于中心度的概念只是用来衡量网络中不同节点的重要性排名(ranking)，因此计算出来的具体数值不具有实际数值大小上的意义
