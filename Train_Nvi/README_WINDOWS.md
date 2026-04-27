# Clash Royale YOLO Training Package

这个文件夹可以整体复制到 Windows + NVIDIA 电脑上训练。

## 里面有什么

```text
Train_Nvi/
  Data/                 原始 KataCR 数据备份，保留 12 列标签和素材
  Data_Set/Yolo/        普通 Ultralytics YOLO 可直接训练的数据集
  train.py              开始训练
  val.py                训练后验证 best.pt
  predict.py            训练后批量预测验证集图片
  check_env.py          检查 CUDA、数据集、模型能否加载
  requirements.txt      Python 依赖
  setup_windows.bat     Windows 一键创建环境并检查
  train_windows.bat     Windows 一键训练
  val_windows.bat       Windows 一键验证
```

训练实际读取的是：

```text
Data_Set/Yolo/data.yaml
Data_Set/Yolo/images/train
Data_Set/Yolo/images/val
Data_Set/Yolo/labels/train
Data_Set/Yolo/labels/val
```

`Data/` 是原始数据备份，不是普通 YOLO 训练直接读取的目录。

## Windows 上怎么跑

打开 PowerShell 或 CMD，进入这个文件夹：

```bat
cd path\to\Train_Nvi
```

第一次运行：

```bat
setup_windows.bat
```

看到下面这些基本就对了：

```text
cuda available: True
nc: 155
names: 155
model load: OK
```

开始训练：

```bat
train_windows.bat
```

训练结束后验证：

```bat
val_windows.bat
```

## 训练结果

训练完成后，最重要的文件是：

```text
runs/cr_yolo26s/weights/best.pt
```

这个就是训练好的模型。

## 如果显存不够

打开 `train.py`，把：

```python
batch=8
```

改小：

```python
batch=4
```

还不够就改成：

```python
batch=2
```

## 如果 YOLO26 模型下载失败

先升级：

```bat
pip install -U ultralytics
```

如果你的环境仍然不支持 `yolo26s.pt`，可以把 `train.py` 里的：

```python
model = YOLO("yolo26s.pt")
name="cr_yolo26s"
```

改成：

```python
model = YOLO("yolo11s.pt")
name="cr_yolo11s"
```

同时把 `val.py` 和 `predict.py` 里的 `cr_yolo26s` 改成 `cr_yolo11s`。
