import math
import catboost as cb

class emotion_detection:
    def __init__(self):
        self.ems = ['Neutral','Happy','Sad','Surprise','Fear','Disgust','Anger','Contempt']
        self.clf = cb.CatBoostClassifier()#set the parameter to multiclass and leave at default setting
        return
    
    def predict(self, val, aro):
        fet1 = val
        fet2 = aro
        fet3 = math.sqrt(val**2 + aro**2)
        fet4 = math.atan(aro/val)
        
        return self.ems[0],0
    
    def train(self, epochs=5):
        # need to call the NN here to get the output for val and aro and then predict
        for epoch in range(epochs):
            print(f'Epoch-{epoch}')
            train_batch(train_loader,modelReg,loss_plain,optimizer)
            validation(val_loader,modelReg,loss_plain)
        return