# just a dictionary to set default value of state
class Counter(dict):
    def __getitem__(self, idx):
        self.setdefault(idx, idx[1])
        return dict.__getitem__(self, idx)