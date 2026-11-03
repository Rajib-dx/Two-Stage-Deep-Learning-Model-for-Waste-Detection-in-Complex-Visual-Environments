import torch 
from torchvision.models import mobilenet_v3_small
from torchvision import transforms
from PIL import Image

model = mobilenet_v3_small(weights=None)
model.classifier[3]=torch.nn.Linear(1024,2)
MODEL_PATH ="models\classification_model.pt"
model.load_state_dict(torch.load(MODEL_PATH,map_location= torch.device("cpu")))

model.eval()


transform= transforms.Compose([
    transforms.Resize((256 , 256)),
    transforms.ToTensor()
])

def classifier(image):
    image = Image.open(image).convert("RGB")
    image_tensor = transform(image).unsqueeze(0)

    with torch.inference_mode():
        output= model(image_tensor)
        probs = torch.softmax(output,dim=1)
        confidence , pred= torch.max(probs ,dim=1)

        pred=pred.item()
        confidence=confidence.item()*100

    return pred , confidence        
