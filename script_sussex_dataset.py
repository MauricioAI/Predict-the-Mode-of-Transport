import pandas as pd

# Load data of 22 june
labels = pd.read_csv("./SHLDataset_preview_v1/User1/220617/Label.txt", delimiter=(" "), header=None).iloc[:, 0:2]
labels.columns = ["timestamp", "activity"]
labels.drop(labels[(labels.activity != 1) & (labels.activity != 2) & (labels.activity != 5)].index, inplace=True)
labels.loc[labels['activity'] == 1, 'activity'] = 'STILL'
labels.loc[labels['activity'] == 2, 'activity'] = 'WALK'
labels.loc[labels['activity'] == 5, 'activity'] = 'CAR'

bag_df = pd.read_csv("./SHLDataset_preview_v1/User1/220617/Bag_Motion.txt", delimiter=(" "), header=None).iloc[:, 0:4]
bag_df.columns = ["timestamp", "acc_X", "acc_Y", "acc_Z"]

torso_df = pd.read_csv("./SHLDataset_preview_v1/User1/220617/Torso_Motion.txt", delimiter=(" "), header=None).iloc[:, 0:4]
torso_df.columns = ["timestamp", "acc_X", "acc_Y", "acc_Z"]

hips_df = pd.read_csv("./SHLDataset_preview_v1/User1/220617/Hips_Motion.txt", delimiter=(" "), header=None).iloc[:, 0:4]
hips_df.columns = ["timestamp", "acc_X", "acc_Y", "acc_Z"]

hand_df = pd.read_csv("./SHLDataset_preview_v1/User1/220617/Hand_Motion.txt", delimiter=(" "), header=None).iloc[:, 0:4]
hand_df.columns = ["timestamp", "acc_X", "acc_Y", "acc_Z"]

#Load data of 26 june
labels1 = pd.read_csv("./SHLDataset_preview_v1/User1/260617/Label.txt", delimiter=(" "), header=None).iloc[:, 0:2]
labels1.columns = ["timestamp", "activity"]
labels1.drop(labels1[(labels1.activity != 1) & (labels1.activity != 2) & (labels1.activity != 5)].index, inplace=True)
labels1.loc[labels1['activity'] == 1, 'activity'] = 'STILL'
labels1.loc[labels1['activity'] == 2, 'activity'] = 'WALK'
labels1.loc[labels1['activity'] == 5, 'activity'] = 'CAR'

bag_df1 = pd.read_csv("./SHLDataset_preview_v1/User1/260617/Bag_Motion.txt", delimiter=(" "), header=None).iloc[:, 0:4]
bag_df1.columns = ["timestamp", "acc_X", "acc_Y", "acc_Z"]

torso_df1 = pd.read_csv("./SHLDataset_preview_v1/User1/260617/Torso_Motion.txt", delimiter=(" "), header=None).iloc[:, 0:4]
torso_df1.columns = ["timestamp", "acc_X", "acc_Y", "acc_Z"]

hips_df1 = pd.read_csv("./SHLDataset_preview_v1/User1/260617/Hips_Motion.txt", delimiter=(" "), header=None).iloc[:, 0:4]
hips_df1.columns = ["timestamp", "acc_X", "acc_Y", "acc_Z"]

hand_df1 = pd.read_csv("./SHLDataset_preview_v1/User1/260617/Hand_Motion.txt", delimiter=(" "), header=None).iloc[:, 0:4]
hand_df1.columns = ["timestamp", "acc_X", "acc_Y", "acc_Z"]

#Load data of 27 june
labels2 = pd.read_csv("./SHLDataset_preview_v1/User1/270617/Label.txt", delimiter=(" "), header=None).iloc[:, 0:2]
labels2.columns = ["timestamp", "activity"]
labels2.drop(labels2[(labels2.activity != 1) & (labels2.activity != 2) & (labels2.activity != 5)].index, inplace=True)
labels2.loc[labels2['activity'] == 1, 'activity'] = 'STILL'
labels2.loc[labels2['activity'] == 2, 'activity'] = 'WALK'
labels2.loc[labels2['activity'] == 5, 'activity'] = 'CAR'

bag_df2 = pd.read_csv("./SHLDataset_preview_v1/User1/270617/Bag_Motion.txt", delimiter=(" "), header=None).iloc[:, 0:4]
bag_df2.columns = ["timestamp", "acc_X", "acc_Y", "acc_Z"]

torso_df2 = pd.read_csv("./SHLDataset_preview_v1/User1/270617/Torso_Motion.txt", delimiter=(" "), header=None).iloc[:, 0:4]
torso_df2.columns = ["timestamp", "acc_X", "acc_Y", "acc_Z"]

hips_df2 = pd.read_csv("./SHLDataset_preview_v1/User1/270617/Hips_Motion.txt", delimiter=(" "), header=None).iloc[:, 0:4]
hips_df2.columns = ["timestamp", "acc_X", "acc_Y", "acc_Z"]

hand_df2 = pd.read_csv("./SHLDataset_preview_v1/User1/270617/Hand_Motion.txt", delimiter=(" "), header=None).iloc[:, 0:4]
hand_df2.columns = ["timestamp", "acc_X", "acc_Y", "acc_Z"]

pd.merge(labels, bag_df, on='timestamp', validate='1:1').to_csv("./220617_Bag.csv", index=False)
pd.merge(labels, torso_df, on='timestamp', validate='1:1').to_csv("./220617_Torso.csv", index=False)
pd.merge(labels, hips_df, on='timestamp', validate='1:1').to_csv("./220617_Hips.csv", index=False)
pd.merge(labels, hand_df, on='timestamp', validate='1:1').to_csv("./220617_Hand.csv", index=False)

pd.merge(labels1, bag_df1, on='timestamp', validate='1:1').to_csv("./260617_Bag.csv", index=False)
pd.merge(labels1, torso_df1, on='timestamp', validate='1:1').to_csv("./260617_Torso.csv", index=False)
pd.merge(labels1, hips_df1, on='timestamp', validate='1:1').to_csv("./260617_Hips.csv", index=False)
pd.merge(labels1, hand_df1, on='timestamp', validate='1:1').to_csv("./260617_Hand.csv", index=False)

pd.merge(labels2, bag_df2, on='timestamp', validate='1:1').to_csv("./270617_Bag.csv", index=False)
pd.merge(labels2, torso_df2, on='timestamp', validate='1:1').to_csv("./270617_Torso.csv", index=False)
pd.merge(labels2, hips_df2, on='timestamp', validate='1:1').to_csv("./270617_Hips.csv", index=False)
pd.merge(labels2, hand_df2, on='timestamp', validate='1:1').to_csv("./270617_Hand.csv", index=False)