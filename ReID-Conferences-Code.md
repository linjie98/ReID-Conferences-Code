# ReID-Conferences-Code

## CVPR

### 2016

- 【ResNet】Deep Residual Learning for Image Recognition

	- 1、解决了网络退化问题，提出深度残差网络
2、引入了bottleneck结构，解决构建更深的ResNet，通道数过大导致计算复杂度过大的问题

### 2017

- Spindle Net: Person Re-identification with Human Body Region Guided Feature Decomposition and Fusion

	- 1、提出 Body Region Guided Spindle Net，有两个阶段：FEN：特征抽取网络、FFN：特征融合网络
2、构建了自有数据集：SenseReID

### 2019

- Bag of Tricks and A Strong Baseline for Deep Person Re-identification

	- 1、收集评估了一些train tricks，设计了一个强大而简单的ReID baseline
2、设计了BNNeck结构
3、实现center loss 来弥补聚类性能

### 2020

- High-Order Information Matters: Learning Relation and Topology for Occluded Person Re-Identification
1、提出了解决遮挡问题的三阶段模型
       - 关键点局部特征提取（提取人类关键点区域语义特征的单阶语义模块（S））
       - 图卷积融合关键点特征（建模不同语义（即不同关键点）局部特征之间的关系信息的高阶关系模块（R））
       - 图匹配方式计算相似度并训练模型（高阶人体拓扑模块 (T)，用于学习鲁棒对齐并预测两个图像之间的相似性）
2、在R阶段中提出方向自适应的图卷积层ADGC，利用局部特征和全局特征的差异性来评估权重，差异越小越重要。
3、在T阶段中提出跨图嵌入对齐（CGEA）

## IJCV

### 2021

- Intra-Camera Supervised Person Re-Identification

	- 提出了摄像机域内监督（ICS）行人重识别方法

## 中文期刊

