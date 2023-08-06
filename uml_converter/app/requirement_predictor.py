import torch
from transformers import DistilBertTokenizer, DistilBertForSequenceClassification
import os

def predict_requirement(sentence):

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    # Load the tokenizer
    tokenizer = DistilBertTokenizer.from_pretrained("distilbert-base-uncased")


    # Tokenize the sentence and convert it into input tensors
    inputs = tokenizer(sentence, padding=True, truncation=True, return_tensors="pt")
    input_ids = inputs["input_ids"]
    attention_mask = inputs["attention_mask"]

    # Assuming you have loaded the trained model already
    model_loaded = DistilBertForSequenceClassification.from_pretrained("distilbert-base-uncased")
    model_path = os.path.join(os.path.dirname(__file__), r"C:\req_classifier\req_classifier.pth")
    model_loaded.load_state_dict(torch.load(model_path))
    # Set the model to evaluation mode
    model_loaded.eval()

    # Make a prediction on the individual sentence
    with torch.no_grad():
        # Move the input tensors to the same device as the model (CPU or GPU)
        input_ids, attention_mask = input_ids.to(device), attention_mask.to(device)

        # Forward pass
        outputs = model_loaded(input_ids=input_ids, attention_mask=attention_mask)

        # Get the predicted class (index with the highest probability)
        _, predicted_class = torch.max(outputs.logits, dim=1)

    # Convert the predicted class tensor to a Python scalar
    predicted_class = predicted_class.item()

    # return prediction
    return False if predicted_class == 1 else True


