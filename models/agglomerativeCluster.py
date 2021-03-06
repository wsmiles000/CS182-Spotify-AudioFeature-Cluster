from sklearn.cluster import AgglomerativeClustering

class agglomerativeCluster():
    """
    https://scikit-learn.org/stable/modules/generated/sklearn.cluster.AgglomerativeClustering.html#sklearn.cluster.AgglomerativeClustering
    """
    def __init__(self, k):
        self.model = AgglomerativeClustering(n_clusters=k)
        self.name = "Agglomerative Clustering"
    
    def fit(self, data):
        self.model.fit(data)
    
    def predict(self, data):
        return self.model.fit_predict(data)