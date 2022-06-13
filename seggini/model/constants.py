from pathlib import Path
import os

LABEL = "label"
CENTROID = "centroid"
FEATURES = "feat"
GNN_NODE_FEAT_IN = "gnn_node_feat_in"
GNN_NODE_FEAT_OUT = "gnn_node_feat_out"

NR_CLASSES = 2
BACKGROUND_CLASS = 2
VARIABLE_SIZE = True
WSI_FIX = True
THRESHOLD = 0.003
DISCARD_THRESHOLD = 5000
VALID_FOLDS = [-1, 1, 2, 3, 4]

MASK_VALUE_TO_TEXT = {
    0: "Benign",
    1: "Tangle",
    2: "unlabelled",
}
MASK_VALUE_TO_COLOR = {0: "green", 1: "red", 2: "white"}


class Constants:
    def __init__(self, base_path: Path, mode: str, fold: int, partial: int):
        self.BASE_PATH = base_path
        self.MODE = mode
        self.FOLD = fold
        self.PARTIAL = partial

        assert fold in VALID_FOLDS, f"Fold must be in {VALID_FOLDS} but is {self.FOLD}"
        self.set_constants()

    def set_constants(self):
        self.PREPROCESS_PATH = self.BASE_PATH / 'preprocess'
        self.IMAGES_DF = self.BASE_PATH / 'pickles'/ 'images.pickle'
        self.ANNOTATIONS_DF = self.BASE_PATH / 'pickles'/ Path('annotation_masks' + '.pickle')
        self.LABELS_DF = self.BASE_PATH / 'pickles'/ 'image_level_annotations.pickle'

        self.ID_PATHS = []
        if self.MODE == 'train':
            self.ID_PATHS.append(os.path.join(self.BASE_PATH, 'partition' , 'Train' , f"Val{self.FOLD}" , "Train.csv"))
        elif self.MODE == 'val':
            self.ID_PATHS.append(os.path.join(self.BASE_PATH, 'partition' , 'Train' , f"Val{self.FOLD}" , "Val.csv"))
        elif self.MODE == 'test':
            self.ID_PATHS.append(os.path.join(self.BASE_PATH, 'partition' , 'Test' , "Test.csv"))
