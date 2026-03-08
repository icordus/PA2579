import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

/**
 * Test class for WeightHelper, covering BMI calculation and category determination.
 */
public class TestWeightHelper {

    private final WeightHelper helper = new WeightHelper();

    /**
     * Tests that calculateBmi returns the correct BMI for normal inputs.
     */
    @Test
    void calculateBmi_shouldReturnCorrectValue_forNormalInput() {
        double bmi = helper.calculateBmi(180.0, 81.0);
        assertEquals(25.0, bmi, 0.01);
    }

    /**
     * Tests that calculateBmi throws exception for negative height.
     */
    @Test
    void calculateBmi_shouldThrowException_forNegativeHeight() {
        assertThrows(IllegalArgumentException.class, () -> helper.calculateBmi(-1.0, 70.0));
    }

    /**
     * Tests that calculateBmi throws exception for negative weight.
     */
    @Test
    void calculateBmi_shouldThrowException_forNegativeWeight() {
        assertThrows(IllegalArgumentException.class, () -> helper.calculateBmi(170.0, -1.0));
    }

    /**
     * Tests that calculateBmi throws exception for zero height.
     */
    @Test
    void calculateBmi_shouldThrowException_forZeroHeight() {
        assertThrows(IllegalArgumentException.class, () -> helper.calculateBmi(0.0, 70.0));
    }

    /**
     * Tests that calculateBmi allows zero weight and returns zero BMI.
     */
    @Test
    void calculateBmi_shouldAllowZeroWeight() {
        double bmi = helper.calculateBmi(170.0, 0.0);
        assertEquals(0.0, bmi, 0.0001);
    }

    /**
     * Tests that getCategory returns "Underweight" for BMI below 18.5.
     */
    @Test
    void getCategory_shouldReturnUnderweight_whenBmiBelow18_5() {
        assertEquals("Underweight", helper.getCategory(170.0, 50.0));
    }

    /**
     * Tests that getCategory returns "Normal weight" for BMI exactly 18.5.
     */
    @Test
    void getCategory_shouldReturnNormalWeight_whenBmiIsExactly18_5() {
        double weight = 18.5 * Math.pow(1.70, 2);
        assertEquals("Normal weight", helper.getCategory(170.0, weight));
    }

    /**
     * Tests that getCategory returns "Normal weight" for BMI just below 25.
     */
    @Test
    void getCategory_shouldReturnNormalWeight_whenBmiJustBelow25() {
        double weight = 24.9 * Math.pow(1.70, 2);
        assertEquals("Normal weight", helper.getCategory(170.0, weight));
    }

    /**
     * Tests that getCategory returns "Overweight" for BMI exactly 25.
     */
    @Test
    void getCategory_shouldReturnOverweight_whenBmiIsExactly25() {
        double weight = 25.0 * Math.pow(1.70, 2);
        assertEquals("Overweight", helper.getCategory(170.0, weight));
    }

    /**
     * Tests that getCategory returns "Overweight" for BMI just below 30.
     */
    @Test
    void getCategory_shouldReturnOverweight_whenBmiJustBelow30() {
        double weight = 29.9 * Math.pow(1.70, 2);
        assertEquals("Overweight", helper.getCategory(170.0, weight));
    }

    /**
     * Tests that getCategory returns "Obese" for BMI exactly 30.
     */
    @Test
    void getCategory_shouldReturnObese_whenBmiIsExactly30() {
        double weight = 30.0 * Math.pow(1.70, 2);
        assertEquals("Obese", helper.getCategory(170.0, weight));
    }

    /**
     * Tests that getCategory returns "Obese" for BMI above 30.
     */
    @Test
    void getCategory_shouldReturnObese_whenBmiAbove30() {
        double weight = 35.0 * Math.pow(1.70, 2);
        assertEquals("Obese", helper.getCategory(170.0, weight));
    }
}