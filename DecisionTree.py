class DecisionTree:
    def __init__(self, max_depth=None):
        self.max_depth = max_depth
    def fit(self, X, y, depth=0):
        if depth == self.max_depth or len(set(y)) == 1:
            return {'class': max(set(y), key=y.count)}
        num_features = len(X[0])
        best_gini = float('inf')
        best_split = None
        best_sets = None
        for feature in range(num_features):
            feature_values = set([data[feature] for data in X])
            for value in feature_values:
                set1_X, set1_y, set2_X, set2_y = self.split_data(X, y, feature, value)
                if len(set1_y) > 0 and len(set2_y) > 0:
                    gini = self.calculate_gini(set1_y, set2_y)
                    if gini < best_gini:
                        best_gini = gini
                        best_split = (feature, value)
                        best_sets = (set1_X, set1_y, set2_X, set2_y)
        if best_gini == float('inf'):
            return {'class': max(set(y), key=y.count)}
        left = self.fit(best_sets[0], best_sets[1], depth + 1)
        right = self.fit(best_sets[2], best_sets[3], depth + 1)
        return {'feature': best_split[0], 'value': best_split[1], 'left': left, 'right': right}
    def predict(self, tree, X):
        if 'class' in tree:
            return tree['class']
        feature, value = tree['feature'], tree['value']
        if X[feature] == value:
            return self.predict(tree['left'], X)
        else:
            return self.predict(tree['right'], X)
    def split_data(self, X, y, feature, value):
        set1_X, set1_y, set2_X, set2_y = [], [], [], []
        for i in range(len(X)):
            if X[i][feature] == value:
                set1_X.append(X[i])
                set1_y.append(y[i])
            else:
                set2_X.append(X[i])
                set2_y.append(y[i])
        return set1_X, set1_y, set2_X, set2_y
    def calculate_gini(self, set1_y, set2_y):
        total = len(set1_y) + len(set2_y)
        gini = (len(set1_y) / total) * self.calculate_gini_impurity(set1_y)
        gini += (len(set2_y) / total) * self.calculate_gini_impurity(set2_y)
        return gini
    def calculate_gini_impurity(self, y):
        classes = set(y)
        impurity = 1.0
        for c in classes:
            impurity -= (len([1 for val in y if val == c]) / len(y))**2
        return impurity
X = [
    [0, 1],
    [1, 0],
    [1, 1],
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1],
    [0, 0]
]
y = [1, 1, 0, 0, 1, 1, 0, 0]
tree = DecisionTree(max_depth=3)
model = tree.fit(X, y)
predictions = [tree.predict(model, x) for x in X]
print("Predictions:", predictions)
