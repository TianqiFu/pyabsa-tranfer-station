from sklearn.model_selection import train_test_split
import pandas as pd
import csv
# 创建一个示例DataFrame
# data = {'sentence': ['This is a sample sentence.', 'Another sentence with the term.', 'No term here.'],
#         'term': ['term', 'term', 'term'],
#         'sentiment': ['positive', 'negative', 'neutral']}
# df = pd.DataFrame(data)
# 从CSV文件读取DataFrame
file_path = './dataset/AWARE_Social_Networking.csv'  # 替换为你的文件路径
df = pd.read_csv(file_path)

# # 添加判断条件：如果term中元素为N/A，则删除该行
# # 经过统计N/A的行占总数量的0.005806451612903226
df = df[df['term'].notna()]

# 随机分割数据集，80%为训练集，20%为测试集
train_df, test_df = train_test_split(df, test_size=0.2, random_state=42)

# # 将包含term内容的sentence中的term替换为"$T$"
# df['temp'] = df.apply(lambda row: row['sentence'].replace(row['term'], '$T$'), axis=1)

# df['format'] = df.apply(lambda row: f"{row['temp']}\n{row['term']}\n{row['sentiment']}", axis=1)

# # 打印结果
# # print(df)
# # 如果需要保存到新的CSV文件
# df.to_csv('output_file.csv', index=False)
def FormatData(df, save_file): # save_file 保存后的名称
    with open(save_file, "a", encoding='utf-8') as f: #
        for index,row in df.iterrows():
            # print(index,type(row),row['code'],row['name'])
            # #对于每一行，通过列名访问对应的元素
            # print("-----")
            term=row['term']
            sentence = row['sentence']
            sentiment=row['sentiment']
            if len(term)<=0 or len(sentence)<=0 or len(sentiment)<=0:
                continue
            if term in sentence:
                sentence = sentence.replace(term, '$T$')  # 将包含term内容的sentence中的term替换为"$T$"

            sentence = sentence.replace('\n', '')  # 将句子中的换行移除
            print(sentence)

            f.writelines(sentence+'\n')
            f.writelines(term+'\n')
            f.writelines(sentiment+'\n')

    f.close()

test_df_path = 'AWARE_Social_Networking.test.txt'
train_df_path = 'AWARE_Social_Networking.train.txt'

FormatData(test_df, test_df_path)
FormatData(train_df, train_df_path)

























