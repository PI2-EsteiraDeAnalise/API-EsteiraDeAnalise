import json
import torch
import torchvision
from torchvision import transforms, models
from PIL import Image
import numpy as np
from flask import make_response

transform = transforms.Compose([transforms.Resize((224,224)), transforms.ToTensor()])
models = {
    "CI": "modelos/CI.pt"
}

def predict(image, model):
  output = model(image)
  _, previsao = torch.max(output, dim = 1)
  return previsao, output


def predicao(jsonObject, img):
	Json = json.load(jsonObject)
	device = torch.device('cpu')

	for row in Json:
		cord = row["coordinates"]
		img_crop = img.crop((cord["x1"],cord["y1"],cord["x2"],cord["y2"]))
		img_crop = transform(img_crop).float()
		img_crop = img_crop.unsqueeze(0)
		img_crop = img_crop.to(device)

		model = torch.load(models[row["tag"]], map_location=torch.device('cpu'))
		model = model.to(device)
		resposta, probabilidades = predict(img_crop, model)   
		probabilidades = np.exp(probabilidades.tolist())*100 
		
		if(probabilidades[1] > probabilidades[0]):
			return make_response(self.serialize(records), 400)
	return make_response(self.serialize(records), 200)
