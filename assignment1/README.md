# WeightHelper Assignment

This is a simple Java assignment demonstrating BMI (Body Mass Index) calculation and weight category determination.

## Overview

The `WeightHelper` class provides two main functionalities:
- Calculate BMI from height (in cm) and weight (in kg).
- Determine weight category based on BMI.

## Usage

### Prerequisites
- Java 11 or higher
- JUnit 5 console launcher JAR (1.9.2) in the project root:
  ```
  curl -LO https://repo1.maven.org/maven2/org/junit/platform/junit-platform-console-standalone/1.9.2/junit-platform-console-standalone-1.9.2.jar
  ```

### Build and Test
Use a dedicated `out` folder to avoid stale class files.

**Linux/macOS**
```bash
rm -rf out && mkdir out
javac -d out src/main/java/WeightHelper.java
javac -cp "out:junit-platform-console-standalone-1.9.2.jar" -d out src/test/java/TestWeightHelper.java
java -jar junit-platform-console-standalone-1.9.2.jar --class-path out --scan-class-path
```

**Windows (PowerShell)**
```powershell
Remove-Item -Recurse -Force out -ErrorAction Ignore
New-Item -ItemType Directory -Force -Path out | Out-Null
javac -d out src/main/java/WeightHelper.java
javac -cp "out;junit-platform-console-standalone-1.9.2.jar" -d out src/test/java/TestWeightHelper.java
java -jar junit-platform-console-standalone-1.9.2.jar --class-path out --scan-class-path
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