# WeightHelper Assignment

This is a simple Java assignment demonstrating BMI (Body Mass Index) calculation and weight category determination.

## Overview

The `WeightHelper` class provides two main functionalities:
- Calculate BMI from height (in cm) and weight (in kg).
- Determine weight category based on BMI.

## Usage

### Prerequisites
- Java 11 or higher
- JUnit 5 for testing

### Running the Code
1. Compile the classes:
   ```
   javac -cp . src/main/java/WeightHelper.java
   javac -cp .:junit-platform-console-standalone-1.9.2.jar src/test/java/TestWeightHelper.java
   ```

2. Run tests:
   ```
   java -cp .:junit-platform-console-standalone-1.9.2.jar org.junit.platform.console.ConsoleLauncher --class-path . --scan-classpath
   ```

### Example
```java
WeightHelper helper = new WeightHelper();
double bmi = helper.calculateBmi(180.0, 75.0); // ~23.15
String category = helper.getCategory(180.0, 75.0); // "Normal weight"
```

## BMI Categories
- Underweight: BMI < 18.5
- Normal weight: 18.5 ≤ BMI < 25
- Overweight: 25 ≤ BMI < 30
- Obese: BMI ≥ 30

## Validation
- Height must be > 0 cm
- Weight must be ≥ 0 kg
- Invalid inputs throw `IllegalArgumentException`