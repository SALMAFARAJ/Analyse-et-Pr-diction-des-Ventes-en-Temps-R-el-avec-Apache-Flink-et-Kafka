package flinkCom;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
public class ess {
	  private static final String jdbcUrl = "jdbc:postgresql://localhost:5432/postgres";
	    private static final String username = "postgres";
	    private static final String password = "root";


	public static void main(String[] args) {
		// TODO Auto-generated method stub

  
  
        Connection connection = null;
        try {
            // Charger le pilote JDBC
            Class.forName("org.postgresql.Driver");
            
            // Établir la connexion à la base de données
            System.out.println("Tentative de connexion à la base de données...");
            connection = DriverManager.getConnection(jdbcUrl, username, password);
            
            if (connection != null) {
                System.out.println("Connexion réussie à la base de données !");
            } else {
                System.out.println("Échec de la connexion à la base de données !");
            }
        } catch (ClassNotFoundException e) {
            System.out.println("Impossible de charger le pilote JDBC !");
            e.printStackTrace();
        } catch (SQLException e) {
            System.out.println("Erreur lors de la connexion à la base de données !");
            e.printStackTrace();
        } finally {
            // Fermer la connexion
            if (connection != null) {
                try {
                    connection.close();
                    System.out.println("Connexion à la base de données fermée avec succès !");
                } catch (SQLException e) {
                    System.out.println("Erreur lors de la fermeture de la connexion à la base de données !");
                    e.printStackTrace();
                }
            }
        }
    }
}

