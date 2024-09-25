package Dto;

public class SalesPrediction {
    private int year;
    private double predictedSales;

    public SalesPrediction(int year, double predictedSales) {
        this.year = year;
        this.predictedSales = predictedSales;
    }

    public int getYear() {
        return year;
    }

    public void setYear(int year) {
        this.year = year;
    }

    public double getPredictedSales() {
        return predictedSales;
    }

    public void setPredictedSales(double predictedSales) {
        this.predictedSales = predictedSales;
    }
}
