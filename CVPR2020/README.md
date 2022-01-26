## CVPR 2020

#### Learning Relation and Topology for Occluded Person Re-Identification
- 论文链接：[https://arxiv.org/pdf/2003.08177.pdf](https://arxiv.org/pdf/2003.08177.pdf)
- 论文代码：[https://github.com/wangguanan/HOReID](https://github.com/wangguanan/HOReID)
- 论文主要贡献：
    - 提出了解决遮挡问题的三阶段模型
    
       1、关键点局部特征提取（提取人类关键点区域语义特征的单阶语义模块（S））
       
       2、图卷积融合关键点特征（建模不同语义（即不同关键点）局部特征之间的关系信息的高阶关系模块（R））
       
       3、图匹配方式计算相似度并训练模型（高阶人体拓扑模块 (T)，用于学习鲁棒对齐并预测两个图像之间的相似性）
    - 在2阶段中提出方向自适应的图卷积层ADGC，利用局部特征和全局特征的差异性来评估权重，差异越小越重要。
    - 在3阶段中提出跨图嵌入对齐（CGEA）
  
- 论文解读：[https://xulinjie.blog.csdn.net/article/details/122698052](https://xulinjie.blog.csdn.net/article/details/122698052)
