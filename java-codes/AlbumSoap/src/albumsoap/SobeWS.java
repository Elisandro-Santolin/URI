package albumsoap;


import javax.xml.ws.Endpoint;

public class SobeWS {

		public static void main(String[] args){
			
			Acervo acervo = new Acervo();
			acervo.addAlbum(new Album("Raul", "1972", "SomLivre"));
			acervo.addAlbum(new Album("Titas", "1987", "SomLivre"));
			acervo.addAlbum(new Album("Raimundos", "1997", "SomLivre"));
			
			AcervoWS ws = new AcervoWS(acervo);	
			
			String url ="http://192.168.0.104:8080/acervo";
			Endpoint.publish(url, ws);
			System.out.println("Rodando na porta 8080");
			System.out.println("WSDL: http://192.168.0.104:8080/acervo"+"?wsdl");


		}

		
}