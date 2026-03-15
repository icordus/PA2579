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
        // Round to 2 decimals to avoid boundary drift (e.g., 24.999999 vs 25.0)
        double roundedBmi = Math.round(bmi * 100.0) / 100.0;

        if (roundedBmi < 18.5) {
            return "Underweight";
        } else if (roundedBmi < 25.0) {
            return "Normal weight";
        } else if (roundedBmi < 30.0) {
            return "Overweight";
        } else {
            return "Obese";
        }
    }
}