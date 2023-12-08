import pandas as pd

# 创建一个示例DataFrame
# data = {'sentence': ['This is a sample sentence.', 'Another sentence with the term.', 'No term here.'],
#         'term': ['term', 'term', 'term'],
#         'sentiment': ['positive', 'negative', 'neutral']}
# df = pd.DataFrame(data)
# 从CSV文件读取DataFrame
file_path = './dataset/AWARE_Social_Networking.csv'  # 替换为你的文件路径
df = pd.read_csv(file_path)

# 添加判断条件：如果term中元素为N/A，则删除该行
# 经过统计N/A的行占总数量的0.005806451612903226
df = df[df['term'].notna()]

# 将包含term内容的sentence中的term替换为"$T$"
df['temp'] = df.apply(lambda row: row['sentence'].replace(row['term'], '$T$'), axis=1)

df['format'] = df.apply(lambda row: f"{row['temp']}\n{row['term']}\n{row['sentiment']}", axis=1)

# 打印结果
# print(df)
# 如果需要保存到新的CSV文件
df.to_csv('output_file.csv', index=False)