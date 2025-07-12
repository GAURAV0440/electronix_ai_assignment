import json
import random
import os
import argparse
import torch
import numpy as np
from transformers import AutoTokenizer, AutoModelForSequenceClassification, Trainer, TrainingArguments
from datasets import load_dataset, Dataset
from sklearn.preprocessing import LabelEncoder

SEED = 42
random.seed(SEED)
np.random.seed(SEED)
torch.manual_seed(SEED)

def load_data(jsonl_path):
    with open(jsonl_path, "r", encoding="utf-8") as f:
        data = [json.loads(line.strip()) for line in f]
    texts = [d["text"] for d in data]
    labels = [d["label"] for d in data]
    return texts, labels

def main(data_path, epochs, lr):
    texts, labels = load_data(data_path)
    label_encoder = LabelEncoder()
    labels_encoded = label_encoder.fit_transform(labels)
    label_mapping = dict(zip(label_encoder.classes_, label_encoder.transform(label_encoder.classes_)))
    print("Label mapping:", label_mapping)

    tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")
    encodings = tokenizer(texts, truncation=True, padding=True)

    dataset = Dataset.from_dict({
        "input_ids": encodings["input_ids"],
        "attention_mask": encodings["attention_mask"],
        "labels": labels_encoded
    })

    model = AutoModelForSequenceClassification.from_pretrained("distilbert-base-uncased", num_labels=len(set(labels_encoded)))

    args = TrainingArguments(
        output_dir="./results",
        num_train_epochs=epochs,
        per_device_train_batch_size=8,
        learning_rate=lr,
        logging_dir="./logs",
        save_strategy="epoch",
        seed=SEED
    )

    trainer = Trainer(
        model=model,
        args=args,
        train_dataset=dataset
    )

    trainer.train()

    if not os.path.exists("./backend/model"):
        os.makedirs("./backend/model")
    model.save_pretrained("./backend/model")
    tokenizer.save_pretrained("./backend/model")
    print("✅ Fine-tuned model saved to ./backend/model")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", required=True, help="Path to .jsonl data file")
    parser.add_argument("--epochs", type=int, default=3)
    parser.add_argument("--lr", type=float, default=3e-5)
    args = parser.parse_args()
    main(args.data, args.epochs, args.lr)
