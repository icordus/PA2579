/**
 * Utility class for calculating BMI and determining weight categories.
 */
public class WeightHelper {

    /**
     * Calculates the Body Mass Index (BMI) based on height in centimeters and weight in kilograms.
     *
     * @param heightCm the height in centimeters (must be > 0)
     * @param weightKg the weight in kilograms (must be >= 0)
     * @return the calculated BMI value
     * @throws IllegalArgumentException if height or weight is invalid
     */
    public double calculateBmi(double heightCm, double weightKg) {
        if (heightCm < 0 || weightKg < 0) {
            throw new IllegalArgumentException("Height and weight must be >= 0");
        }

        if (heightCm == 0) {
            throw new IllegalArgumentException("Height must be > 0");
        }

        double heightMeters = heightCm / 100.0;
        return weightKg / (heightMeters * heightMeters);
    }

    /**
     * Determines the weight category based on BMI calculation.
     *
     * @param heightCm the height in centimeters (must be > 0)
     * @param weightKg the weight in kilograms (must be >= 0)
     * @return the weight category as a string ("Underweight", "Normal weight", "Overweight", or "Obese")
     * @throws IllegalArgumentException if height or weight is invalid (via calculateBmi)
     */
    public String getCategory(double heightCm, double weightKg) {
        double bmi = calculateBmi(heightCm, weightKg);

        if (bmi < 18.5) {
            return "Underweight";
        } else if (bmi < 25.0) {
            return "Normal weight";
        } else if (bmi < 30.0) {
            return "Overweight";
        } else {
            return "Obese";
        }
    }
}