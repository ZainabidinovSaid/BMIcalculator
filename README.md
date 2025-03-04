
# BMI Calculator (PyQt6)  

## Overview  
The **BMI Calculator** is a GUI application built with PyQt6 that allows users to calculate their **Body Mass Index (BMI)** based on their weight and height. It categorizes the BMI and visually represents it with different background colors.  

## Features  
- Input fields for **weight (kg)** and **height (cm)**.  
- Button to **calculate BMI**.  
- Displays **BMI value and category** (Underweight, Normal, Overweight, or Obese).  
- Changes **background color** based on BMI category.  
- Handles **invalid inputs** gracefully.  

## How It Works  
1. The user enters **weight (kg)** and **height (cm)** in the input fields.  
2. Clicking the **calculate button** triggers the BMI computation.  
3. The BMI is displayed along with its **category**.  
4. The label background color changes based on the BMI range:  
   - **Yellow**: Underweight (BMI < 18.5)  
   - **Green**: Normal weight (BMI 18.5–24.9)  
   - **Orange**: Overweight (BMI 25–29.9)  
   - **Red**: Obese (BMI ≥ 30)  


## File Structure  
```
/bmi_calculator/
│-- bmicalculator.py  # Main application script  
│-- bmicalculator.ui  # UI file for PyQt6  
│-- README.md         # Documentation  
```  

## Error Handling  
- If the user enters **non-numeric** values, the program displays `"Invalid Input"` with a **gray background**.  


## Example inputs/outputs
- Here I entered 56 kg and 174 cm, which is underweight by BMI
  
![Снимок экрана (159)](https://github.com/user-attachments/assets/68a0bfba-0b17-4f6d-80f7-72d65c72de06)
- 66 kg and 167 cm
  
![Снимок экрана (157)](https://github.com/user-attachments/assets/5e8e8f32-5172-42e0-ab8e-5419eac68866)
- 80 kg and 170 cm
  
![Снимок экрана (158)](https://github.com/user-attachments/assets/3f6e3393-d9a7-41a4-badb-3b23f7627025)
- 85 kg and 188 cm
  
![Снимок экрана (160)](https://github.com/user-attachments/assets/9c8d35a9-43d6-4545-ae4d-ba83d322cd43)
- And also if the entered values are not numeric, it will give "Invalid Input"
  
![Снимок экрана (162)](https://github.com/user-attachments/assets/2997bb8d-fb94-4476-b2cc-16e2455e06d5)
