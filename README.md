# Driver Drowsiness Detection System using Transfer Learning

## Project Overview
The Driver Drowsiness Detection System aims to enhance road safety by monitoring the driver’s state and alerting them when signs of drowsiness are detected. By leveraging transfer learning, this system utilizes pre-trained deep learning models to efficiently and accurately detect drowsiness in real time.

## Key Features
- **Pre-trained Model Utilization**: Employs a pre-trained Convolutional Neural Network (CNN) model, such as VGG16, ResNet50, or InceptionV3, for robust feature extraction.
- **Real-time Video Stream Analysis**: Captures live video feed from a camera focused on the driver’s face, processing frames in real-time to analyze facial features.
- **Facial Landmark Detection**: Identifies key points on the driver’s face to determine eye closure, yawning, and other indicators of drowsiness.
- **Drowsiness Detection Mechanism**: Classifies each frame to detect closed eyes or other signs of drowsiness using the fine-tuned pre-trained CNN model.
- **Alert System**: Triggers an alert upon detecting signs of drowsiness, including audible alarms, visual warnings, or haptic feedback.
- **Evidence Capture**: Captures a photo of the driver as evidence when drowsiness is detected.

## Implementation Steps
1. **Data Collection**: Collect images or video frames of drivers exhibiting various states (awake, drowsy, yawning, etc.).
   
      https://www.kaggle.com/datasets/serenaraju/yawn-eye-dataset-new/data 

3. **Data Preprocessing**: Resize images, normalize pixel values, and augment the dataset.
4. **Transfer Learning Setup**: Choose a pre-trained CNN model and replace the top layers with a new classifier for drowsiness detection. Fine-tune the model.
5. **Model Training**: Train the model on the dataset, adjusting hyperparameters to optimize performance.
6. **Integration with Real-time System**: Integrate the trained model into a real-time video processing pipeline using libraries like OpenCV.
7. **Facial Landmark Detection**: Implement facial landmark detection to extract key facial features.
8. **Alert Mechanism**: Develop an alert mechanism to activate upon detecting drowsiness.
9. **Testing and Deployment**: Test the system in various conditions and deploy it in a vehicle environment for real-world evaluation.

## Technologies Used
- **Deep Learning Frameworks**: TensorFlow, Keras, PyTorch
- **Pre-trained Models**: VGG16, ResNet50, InceptionV3
- **Computer Vision**: OpenCV
- **Programming Languages**: Python

## Potential Enhancements
- Integration with additional sensors (e.g., heart rate monitors) for improved accuracy.
- Incorporation of machine learning models for contextual analysis (e.g., road conditions, driving patterns).
- Development of a user-friendly interface for monitoring and configuring the system.

## Getting Started
To get started with this project, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/Bindhumanigar/Driver-Drowsiness-Detection-System-using-Transfer-Learning.git
   cd Driver-Drowsiness-Detection-System-using-Transfer-Learning
