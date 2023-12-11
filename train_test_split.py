from sklearn.model_selection import train_test_split
import pandas as pd
import csv
# 从CSV文件读取DataFrame
file_path = 'output_file.csv'  # 替换为你的文件路径
df = pd.read_csv(file_path)

# 随机分割数据集，80%为训练集，20%为测试集
train_df, test_df = train_test_split(df, test_size=0.2, random_state=42)

# 打印训练集和测试集的长度
# print("训练集长度:", len(train_df))
# print("测试集长度:", len(test_df))

# 如果需要保存到新的CSV文件
# train_df.to_csv('./dataset/AWARE_Social_Networking_train.csv', index=False)
# test_df.to_csv('./dataset/AWARE_Social_Networking_test.csv', index=False)

# 如果需要保存到新的SEG文件 absa framework pyabsa要求这个格式
train_df['format'].to_csv('./dataset/AWARE_Social_Networking.train.txt', sep='\t', quoting=csv.QUOTE_NONE, escapechar='\t', index=False, header=False)# quoting=csv.QUOTE_NONE 除去引号
test_df['format'].to_csv('./dataset/AWARE_Social_Networking.test.txt', sep='\t', quoting=csv.QUOTE_NONE, escapechar='\t', index=False, header=False)