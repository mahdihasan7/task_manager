# Study Helper

## [Video Demo](https://youtu.be/_UIyW3o8BJw)

### Description:
This project is a BMI (Body Mass Index) calculator, which allows users to easily calculate their BMI based on weight and height inputs. The web application not only computes the BMI but also provides additional insights into how much weight needs to be gained or lost to achieve a healthy BMI range. The project was created as part of CS50, Harvard University's Introduction to Computer Science course, and demonstrates fundamental skills in web development, HTML/CSS, JavaScript, and algorithm design.

### How the Program Works:
The web application interface consists of two input fields: one for the user's weight in kilograms and one for their height in meters. Once the user inputs their data and clicks the "Calculate" button, the program calculates the BMI using the formula: `bmi = kg / m^2`.

The program then displays the result and, if the BMI indicates underweight or overweight, provides an additional calculation showing how much weight the user should gain or lose to reach a normal BMI range.

### Project Files:
- `index.html`: Contains the structure of the web page and input fields for weight and height.
- `app.js`: Handles BMI calculation, user input validation, and provides weight adjustment feedback.
- `styles.css`: Contains the styling for the web page, ensuring a clean and user-friendly design.

### Design Choices:
I chose JavaScript for the BMI calculation due to its ability to efficiently handle user inputs and dynamically update the page. For styling, I kept the interface minimalistic to make the tool easy to use for all types of users.

### Features:
- Calculates BMI from user input.
- Provides suggestions for weight adjustments to achieve a normal BMI.
- Validates input to prevent errors or unrealistic entries.
- User-friendly interface with clear instructions and results display.

### Challenges:
The most challenging part of the project was creating accurate weight gain/loss suggestions based on BMI results. Through testing and research, I was able to refine the algorithm and improve user feedback.

### Installation:
After downloading the project repository, navigate to the folder using the terminal:

```
$ cd bmi_calculator
```
Open VScode in the directory:

```
$ code .
```

Use the Live Server extension to run the application locally. Click "Go Live" in the bottom right corner of VS Code, and the application will open in your browser.

### Usage:
Once the program is running, input your weight and height, and click "Calculate BMI" to see your results.

### Interface:
![Interface Image](https://github.com/mahdihasan7/bmi_calculator/blob/main/images/sample%20interface.png)

After providing inputs:
![Output Image](https://github.com/mahdihasan7/bmi_calculator/blob/main/images/sample%20output.png)

>[!IMPORTANT]
> The program only accepts kilograms for weight and meters for height.
