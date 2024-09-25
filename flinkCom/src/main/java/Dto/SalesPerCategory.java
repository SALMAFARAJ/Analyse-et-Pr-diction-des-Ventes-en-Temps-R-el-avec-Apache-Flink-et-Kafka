package Dto;

import lombok.AllArgsConstructor;
import lombok.Data;

import java.sql.Date;

@Data
@AllArgsConstructor
public class SalesPerCategory {
    private Date transactionDate;
    private String category;
    private Double totalSales;
	public SalesPerCategory(Date transactionDate2, String category2, double totalSales2) {
		this.category=category2;
		this.totalSales= totalSales2;
		this.transactionDate= transactionDate2;
	}
	public Date getTransactionDate() {
		return transactionDate;
	}
	public void setTransactionDate(Date transactionDate) {
		this.transactionDate = transactionDate;
	}
	public String getCategory() {
		return category;
	}
	public void setCategory(String category) {
		this.category = category;
	}
	public Double getTotalSales() {
		return totalSales;
	}
	public void setTotalSales(Double totalSales) {
		this.totalSales = totalSales;
	}
}