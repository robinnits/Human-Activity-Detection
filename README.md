## **Human Activity Detection Using Sensor Data**  
### **Neurathon AI/ML Hackathon**  

### **📌 Overview**  
This project focuses on **Human Activity Recognition (HAR) using smartphone sensor data**. The model classifies different human activities based on accelerometer and gyroscope data from mobile devices.  

### **🚀 Features**  
✔️ Classifies activities like Walking, Sitting, Standing, and Jogging  
✔️ Uses ML models to predict human actions based on sensor data  
✔️ Achieves **93% accuracy**  

---

## **📂 Dataset**  
The dataset used for this project is the **UCI HAR Dataset**. It contains motion sensor data collected from mobile devices while participants performed different activities.  

📌 **Dataset Files:**  
- `train.csv` - Training data  
- `test.csv` - Testing data  
- `features.txt` - Feature names  

---

## **🛠️ Tech Stack**  
🔹 **Programming Language:** Python  
🔹 **Libraries:** Pandas, NumPy, Scikit-Learn  
🔹 **Model Used:** Random Forest Classifier  

---

## **📊 Model Performance**  
| Metric  | Score  |  
|---------|--------|  
| Accuracy | 93% |  
| Precision | XX% |  
| Recall | XX% |  

---

## **📌 How to Run the Project**  
### **🔹 1. Clone the Repository**  
```sh
git clone https://github.com/robinnits/Human-Activity-Detection.git
cd Human-Activity-Detection
```
### **🔹 2. Create a Virtual Environment (Recommended)**  
```sh
python3 -m venv venv  
source venv/bin/activate  # (Mac/Linux)  
venv\Scripts\activate  # (Windows)  
```
### **🔹 3. Install Dependencies**  
```sh
pip install -r requirements.txt
```
### **🔹 4. Run the Model**  
```sh
python train_model.py
```

---

## **📚 Folder Structure**  
```
📂 Human-Activity-Detection
 ┣ 📂 data  
 ┃ ┣ 📜 train.csv  
 ┃ ┣ 📜 test.csv  
 ┣ 📂 models  
 ┃ ┣ 📜 trained_model.pkl  
 ┣ 📜 train_model.py  
 ┣ 📜 test_model.py  
 ┣ 📜 README.md  
 ┣ 📜 requirements.txt  
```

---

## **👨‍💻 Contributors**  
👤 **Robin Poddar**  
📌 NIT Silchar  

---

## **📌 Acknowledgments**  
- **UCI Machine Learning Repository** for providing the dataset.  
- **Scikit-Learn & Pandas** for ML implementation.  

---