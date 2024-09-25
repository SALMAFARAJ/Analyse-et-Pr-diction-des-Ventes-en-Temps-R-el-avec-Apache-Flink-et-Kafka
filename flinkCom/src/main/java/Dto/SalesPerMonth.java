package Dto;

import lombok.AllArgsConstructor;
import lombok.Data;


public class SalesPerMonth {
    private int year;
    private int month;
    private double totalSales;
	public SalesPerMonth(int year2, int month2, double totalSales2) {
		this.month=month2;
		this.totalSales=totalSales2;
		this.month=month2;
	}
	public int getYear() {
		return year;
	}
	public void setYear(int year) {
		this.year = year;
	}
	public int getMonth() {
		return month;
	}
	public void setMonth(int month) {
		this.month = month;
	}
	public double getTotalSales() {
		return totalSales;
	}
	public void setTotalSales(double totalSales) {
		this.totalSales = totalSales;
	}
}