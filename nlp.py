from transformers import AutoTokenizer, TFAutoModelForSequenceClassification

checkpoint = "amir7d0/distilbert-base-uncased-finetuned-amazon-reviews"
tokenizer = AutoTokenizer.from_pretrained(checkpoint)
model = TFAutoModelForSequenceClassification.from_pretrained(checkpoint)

text = "Fuck this bullshit ass broke piece of shit"

encoded_input = tokenizer(text, return_tensors='tf')
output = model(encoded_input)
logits = output.logits.numpy()
predicted_class = int(logits.argmax(axis=1).item())

# Print the raw logits and the predicted class label
'''print("Text: ", text)
predicted_class = int(logits.argmax(axis=1).item())
if predicted_class == 0:
    print("Predicted stars: 1\nSentiment: Negative")
elif predicted_class == 1:
    print("Predicted stars: 2\nSentiment: Negative")
elif predicted_class == 2:
    print("Predicted stars: 3\nSentiment: Neutral")
elif predicted_class == 3:
    print("Predicted stars: 4\nSentiment: Positive")
else:
    print("Predicted stars: 5\nSentiment: Positive")'''
    
print (encoded_input)