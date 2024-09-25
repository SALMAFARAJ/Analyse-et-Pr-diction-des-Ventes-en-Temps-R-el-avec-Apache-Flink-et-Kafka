package Dto;

import lombok.AllArgsConstructor;
import lombok.Data;

import java.sql.Date;

@Data
@AllArgsConstructor
public class SalesPerDay {
    public SalesPerDay(Date transactionDate2, double totalSales2) {
		this.totalSales=totalSales2;
		this.transactionDate=transactionDate2;
		
	}
	public Date getTransactionDate() {
		return transactionDate;
	}
	public void setTransactionDate(Date transactionDate) {
		this.transactionDate = transactionDate;
	}
	public Double getTotalSales() {
		return totalSales;
	}
	public void setTotalSales(Double totalSales) {
		this.totalSales = totalSales;
	}
	private Date transactionDate;
    private Double totalSales ;
}