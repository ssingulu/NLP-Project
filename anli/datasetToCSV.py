# # import pandas as pd
# # df = pd.read_json('./anli/train.jsonl', lines = True)
# # df.rename(columns={'obs1': 'sentence1', 'obs2': 'sentence2'}, inplace=True)
# # labels = pd.read_json('./anli/train-labels.lst', lines = True)
# # df["label"] = labels
# # df.to_csv('./anli/train.csv')

# # df = pd.read_json('./anli/dev.jsonl', lines = True)
# # df.rename(columns={'obs1': 'sentence1', 'obs2': 'sentence2'}, inplace=True)
# # labels = pd.read_json('./anli/dev-labels.lst', lines = True)
# # df["label"] = labels
# # df.to_csv('./anli/dev.csv')

# # import torch
# # print(torch.cuda.device_count())

# import pandas as pd
# df = pd.read_json('./anli/train.jsonl', lines = True)
# df.rename(columns={'obs1': 'sentence1', 'obs2': 'sentence2'}, inplace=True)
# labels = pd.read_json('./anli/train-labels.lst', lines = True)
# df["label"] = labels
# # grouped = df.groupby(["label"])
# # s = False
# # for name, group in grouped:
# #   if not s:
# #     bdf = group.sample(n=100)
# #     s = True
# #   else:
# #     bdf = pd.concat([bdf, group.sample(n=100)])
# # # print(bdf.filter(items=["sentence1", "sentence2", "hyp1", "hyp2", "label"]))
# df["label"].replace({1: 0, 2: 1}, inplace=True)
# df.filter(items=["sentence1", "sentence2", "hyp1", "hyp2", "label"]).to_csv('./anli/train.csv')
# # print(df["label"].value_counts())

# df = pd.read_json('./anli/dev.jsonl', lines = True)
# df.rename(columns={'obs1': 'sentence1', 'obs2': 'sentence2'}, inplace=True)
# labels = pd.read_json('./anli/dev-labels.lst', lines = True)
# df["label"] = labels
# # grouped = df.groupby(["label"])
# # s = False
# # for name, group in grouped:
# #   if not s:
# #     bdf = group.sample(n=100)
# #     s = True
# #   else:
# #     bdf = pd.concat([bdf, group.sample(n=100)])
# # print(bdf.filter(items=["sentence1", "sentence2", "hyp1", "hyp2", "label"]))
# df["label"].replace({1: 0, 2: 1}, inplace=True)
# df.filter(items=["sentence1", "sentence2", "hyp1", "hyp2", "label"]).to_csv('./anli/dev.csv')

import torch
print(torch.cuda.device_count())
print(torch.__version__)