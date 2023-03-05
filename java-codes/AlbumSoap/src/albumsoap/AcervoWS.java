package albumsoap;


import java.util.ArrayList;
import javax.jws.WebResult;
import javax.jws.WebService;


@WebService
public class AcervoWS {
	private Acervo acervo;
	
	public AcervoWS(Acervo a) {
		this.acervo = a;
	}

	@WebResult(name="album")
	public ArrayList<Album> verAlbuns(){
		
		for(Album a : acervo.todosOsAlbuns()) {
			System.out.println(a.getNome());		
		}
		return acervo.todosOsAlbuns();
	}
	
	@WebResult(name="album")
	public ArrayList<Album> albunsPorAno(String ano){
		ArrayList<Album> albunsAno = new ArrayList<Album>();
		System.out.println("Chamando albuns por ano");
	
		for(Album i: acervo.todosOsAlbuns()) {
			if(i.getAno().equals(ano)) {
				albunsAno.add(i);
			}
		}
		return albunsAno;	
	}
	
	@WebResult(name="album")
	public Album cadastrarAlbum(Album a) {
		acervo.addAlbum(a);
		System.out.println("Cadastrando album");
		return a;
	}

}