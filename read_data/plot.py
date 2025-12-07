import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

def plot_csv_raw(csv_path):
    """ 
    读取一个csv文件地址,以第一列为x轴,第二到第九列(除第六列)为y绘制散点图
    即绘制传感器原始数据散点图
    """
    data = pd.read_csv(csv_path)
    time = data[data.columns[0]]
    columns_to_plot = list(data.columns[1:5]) + list(data.columns[6:9])
    colors = plt.cm.tab10(np.linspace(0, 1, len(columns_to_plot)))
    for i, col in enumerate(columns_to_plot):
        plt.scatter(time, data[col], label=col, color=colors[i])
    plt.xlabel('Time')
    plt.ylabel('Value')
    plt.title('Scatter Plot of 8 Data Series')
    plt.legend(title='Series', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.show()
    
def plot_csv_res(csv_path):
    """ 
    读取一个csv文件地址,以第一列为x轴,第二到第九列(除第六列)为y绘制散点图
    即绘制传感器相对基线的响应散点图
    """
    data = pd.read_csv(csv_path)
    time = data[data.columns[0]]
    columns_to_plot = list(data.columns[9:13]) + list(data.columns[14:17])
    colors = plt.cm.tab10(np.linspace(0, 1, len(columns_to_plot)))
    for i, col in enumerate(columns_to_plot):
        plt.scatter(time, data[col], label=col, color=colors[i])
    plt.xlabel('Time')
    plt.ylabel('Value')
    plt.title('Scatter Plot of 8 Data Series')
    plt.legend(title='Series', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.show()
    
    
if __name__ == '__main__':
    csv_path = r'dataset\dryer\251204135439_AlwhalesGDS_TestData_Resp.csv'
    print(plot_csv_res(csv_path))