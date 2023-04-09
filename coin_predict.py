from sklearn.cluster import KMeans
import numpy as np


def predict_groups(radii: list):
    model = KMeans(n_clusters=2, n_init=10)
    data = np.array(radii).reshape(-1, 1)
    res = model.fit_predict(data)
    return res


def fix_groups_ids(radii, groups):
    res = groups.copy()
    if groups[np.argmax(radii)] != 1:
        res = np.where(res == 1, 0, 1)
    return res
